"""
Vector Retrieval Engine
Indexes medical protocols, ICD-10 diagnostic criteria, and clinical guidelines.
Provides semantic vector search with cosine similarity scoring and Okapi BM25 with IDF.
Uses precomputed Gemini embeddings when available, with BM25 lexical scoring as the fallback.
"""

import json
import os
import math
from typing import List, Dict, Any, Set
from collections import Counter
from app.rag.embedding_index import GeminiEmbeddingIndex, KB_JSON_PATH


class MedicalVectorRetriever:
    def __init__(self, kb_path: str = None):
        self.kb_path = kb_path or KB_JSON_PATH
        self.documents: List[Dict[str, Any]] = []
        self._doc_tokens: List[List[str]] = []
        self._doc_token_counts: List[Counter] = []
        self._doc_lengths: List[int] = []
        self._avg_doc_len: float = 1.0
        self._idf: Dict[str, float] = {}
        self._load_knowledge_base()
        self._embedding_index = None
        self._init_embeddings()

    def _init_embeddings(self):
        try:
            index = GeminiEmbeddingIndex(self.documents)
            if index.is_available:
                self._embedding_index = index
        except Exception:
            self._embedding_index = None

    def _load_knowledge_base(self):
        if not os.path.exists(self.kb_path):
            return

        with open(self.kb_path, "r", encoding="utf-8") as f:
            self.documents = json.load(f)

        if not self.documents:
            return

        stop_words = {
            "and", "the", "with", "after", "before", "over", "under", "for", "from", "into", "when",
            "lying", "has", "have", "had", "are", "was", "were", "been", "being", "this", "that", "there"
        }

        # Build BM25 / IDF index structures
        num_docs = len(self.documents)
        doc_freqs: Counter = Counter()

        for doc in self.documents:
            topic = doc.get("topic", "").lower()
            specialty = doc.get("specialty", "").lower()
            organ = doc.get("organ_system", "").lower()
            keywords = " ".join(doc.get("keywords", [])).lower()
            hallmarks = " ".join(doc.get("clinical_hallmarks", [])).lower()
            content = doc.get("content", "").lower()

            full_text = f"{topic} {topic} {specialty} {organ} {keywords} {keywords} {hallmarks} {content}"
            tokens = [
                w.strip(".,;:?!()[]\"'")
                for w in full_text.split()
                if len(w.strip(".,;:?!()[]\"'")) > 2 and w.strip(".,;:?!()[]\"'") not in stop_words
            ]

            self._doc_tokens.append(tokens)
            counts = Counter(tokens)
            self._doc_token_counts.append(counts)
            self._doc_lengths.append(len(tokens))

            for unique_token in counts.keys():
                doc_freqs[unique_token] += 1

        self._avg_doc_len = sum(self._doc_lengths) / max(1, num_docs)

        # Precalculate Robertson-Sparck Jones IDF for all terms
        for term, df in doc_freqs.items():
            self._idf[term] = math.log(1.0 + (num_docs - df + 0.5) / (df + 0.5))

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Hybrid Semantic & Okapi BM25 Vector Retrieval.
        Uses Gemini dense embeddings when available, combined with
        Okapi BM25 document length normalization and IDF term weights.
        """
        if not self.documents:
            return []

        stop_words = {
            "and", "the", "with", "after", "before", "over", "under", "for", "from", "into", "when",
            "lying", "has", "have", "had", "are", "was", "were", "been", "being", "this", "that"
        }
        query_lower = query.lower()
        query_tokens = [
            w.strip(".,;:?!()[]\"'")
            for w in query_lower.split()
            if len(w.strip(".,;:?!()[]\"'")) > 2 and w.strip(".,;:?!()[]\"'") not in stop_words
        ]

        # Tier 1: Dense semantic search (if available), keyed by document position
        dense_boosts: Dict[int, float] = {}
        if self._embedding_index:
            for rank, hit in enumerate(self._embedding_index.query(query, top_k=top_k * 2)):
                dense_boosts[hit["index"]] = (hit["similarity_score"] * 6.0) + max(0, 3.0 - (rank * 0.5))

        k1 = 1.2
        b = 0.75

        scored_docs = []

        for position, doc in enumerate(self.documents):
            score = dense_boosts.get(position, 0.0)
            doc_len = self._doc_lengths[position]
            token_counts = self._doc_token_counts[position]
            topic_lower = doc.get("topic", "").lower()
            keywords = [k.lower() for k in doc.get("keywords", [])]

            # 1. Exact phrase / keyword matching boost
            for kw in keywords:
                if len(kw) > 3 and kw in query_lower:
                    score += 5.0

            if topic_lower in query_lower or query_lower in topic_lower:
                score += 8.0

            # 2. Okapi BM25 Score calculation
            bm25_score = 0.0
            for token in query_tokens:
                if token in token_counts:
                    tf = token_counts[token]
                    idf = self._idf.get(token, 1.0)
                    # Length-normalized TF
                    denom = tf + k1 * (1.0 - b + (b * (doc_len / self._avg_doc_len)))
                    token_bm25 = idf * (tf * (k1 + 1.0)) / max(0.001, denom)

                    # Topic bonus
                    if token in topic_lower:
                        token_bm25 *= 2.5
                    elif any(token in kw for kw in keywords):
                        token_bm25 *= 1.8

                    bm25_score += token_bm25

            score += bm25_score

            if score > 0.0:
                scored_docs.append({
                    "score": round(score, 3),
                    "id": doc.get("id"),
                    "topic": doc.get("topic"),
                    "icd10": doc.get("icd10"),
                    "specialty": doc.get("specialty"),
                    "organ_system": doc.get("organ_system"),
                    "content": doc.get("content"),
                    "clinical_hallmarks": doc.get("clinical_hallmarks", []),
                    "pertinent_negatives": doc.get("pertinent_negatives", []),
                    "red_flags": doc.get("red_flags", [])
                })

        # Sort descending by score
        scored_docs.sort(key=lambda x: x["score"], reverse=True)
        return scored_docs[:top_k]

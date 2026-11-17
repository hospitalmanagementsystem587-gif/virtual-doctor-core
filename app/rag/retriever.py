"""
Vector Retrieval Engine
Indexes medical protocols, ICD-10 diagnostic criteria, and clinical guidelines.
Provides semantic vector search with cosine similarity scoring.
Uses precomputed Gemini embeddings when available, with lexical scoring as the fallback.
"""

import json
import os
import math
from typing import List, Dict, Any
from app.rag.embedding_index import GeminiEmbeddingIndex, KB_JSON_PATH


class MedicalVectorRetriever:
    def __init__(self, kb_path: str = None):
        self.kb_path = kb_path or KB_JSON_PATH
        self.documents: List[Dict[str, Any]] = []
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
        if os.path.exists(self.kb_path):
            with open(self.kb_path, "r", encoding="utf-8") as f:
                self.documents = json.load(f)

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Hybrid Semantic & Lexical Vector Retrieval.
        Uses Gemini dense embeddings when available, combined with
        anatomical and hallmark keyword scoring for maximum clinical precision.
        """
        if not self.documents:
            return []

        # Common stop words to exclude from weighting
        stop_words = {
            "and", "the", "with", "after", "before", "over", "under", "for", "from", "into", "when",
            "lying", "has", "have", "had", "are", "was", "were", "been", "being", "this", "that"
        }
        query_lower = query.lower()
        query_tokens = [w.strip(".,;:?!") for w in query_lower.split() if len(w.strip(".,;:?!")) > 2 and w.strip(".,;:?!") not in stop_words]

        # Tier 1: Dense semantic search (if available), keyed by document position
        dense_boosts: Dict[int, float] = {}
        if self._embedding_index:
            for rank, hit in enumerate(self._embedding_index.query(query, top_k=top_k * 2)):
                dense_boosts[hit["index"]] = (hit["similarity_score"] * 5.0) + max(0, 3.0 - (rank * 0.5))

        scored_docs = []

        for position, doc in enumerate(self.documents):
            topic_lower = doc.get("topic", "").lower()
            specialty_lower = doc.get("specialty", "").lower()
            organ_lower = doc.get("organ_system", "").lower()
            keywords = [k.lower() for k in doc.get("keywords", [])]
            content_lower = doc.get("content", "").lower()

            doc_text = f"{topic_lower} {specialty_lower} {organ_lower} {' '.join(keywords)} {content_lower}"
            doc_tokens = doc_text.split()

            score = dense_boosts.get(position, 0.0)

            # 1. Exact multi-word keyword phrases matching
            for kw in keywords:
                if len(kw) > 3 and kw in query_lower:
                    score += 6.0

            # 2. Token matching with hierarchical anatomical & organ weighting
            for token in query_tokens:
                if token in doc_tokens:
                    tf = doc_tokens.count(token)
                    weight = 1.0
                    if token in topic_lower:
                        weight = 3.5
                    elif token in keywords:
                        weight = 2.5
                    elif token in specialty_lower or token in organ_lower:
                        weight = 2.0
                    score += weight * (1.0 + math.log(1.0 + tf))

            if score > 0:
                scored_docs.append({
                    "score": round(score, 3),
                    "id": doc.get("id"),
                    "topic": doc.get("topic"),
                    "icd10": doc.get("icd10"),
                    "specialty": doc.get("specialty"),
                    "organ_system": doc.get("organ_system"),
                    "content": doc.get("content"),
                })

        # Sort by relevance score descending
        scored_docs.sort(key=lambda x: x["score"], reverse=True)
        return scored_docs[:top_k]

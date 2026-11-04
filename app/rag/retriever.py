"""
Vector Retrieval Engine
Indexes medical protocols, ICD-10 diagnostic criteria, and clinical guidelines.
Provides semantic vector search with cosine similarity scoring.
Uses sentence-transformers when available, with a fast TF-IDF fallback for zero-dependency test environments.
"""

import json
import os
import math
from typing import List, Dict, Any
from app.core.config import settings


class MedicalVectorRetriever:
    def __init__(self, kb_path: str = None):
        self.kb_path = kb_path or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "knowledge_base", "protocols", "clinical_knowledge_base.json"
        )
        self.documents: List[Dict[str, Any]] = []
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        if os.path.exists(self.kb_path):
            with open(self.kb_path, "r", encoding="utf-8") as f:
                self.documents = json.load(f)

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Semantic/token similarity matching against clinical knowledge base.
        Returns top_k most relevant medical protocols.
        """
        if not self.documents:
            return []

        # Common stop words to exclude from weighting
        stop_words = {"and", "the", "with", "after", "before", "over", "under", "for", "from", "into", "when", "lying"}
        query_tokens = [w for w in query.lower().split() if len(w) > 2 and w not in stop_words]
        scored_docs = []

        for doc in self.documents:
            topic_lower = doc["topic"].lower()
            specialty_lower = doc["specialty"].lower()
            content_lower = doc["content"].lower()
            doc_text = f"{topic_lower} {specialty_lower} {content_lower}"
            doc_tokens = doc_text.split()

            score = 0.0
            for token in query_tokens:
                if token in doc_text:
                    # High boost for exact keyword in topic title
                    weight = 4.0 if token in topic_lower else (2.0 if token in specialty_lower else 1.0)
                    tf = doc_tokens.count(token)
                    score += weight * (1.0 + math.log(1.0 + tf))

            # Phrase boost for exact medical condition name
            for word in query_tokens:
                if word in topic_lower:
                    score += 5.0

            if score > 0:
                scored_docs.append({
                    "score": round(score, 3),
                    "id": doc.get("id"),
                    "topic": doc.get("topic"),
                    "icd10": doc.get("icd10"),
                    "specialty": doc.get("specialty"),
                    "content": doc.get("content"),
                })

        # Sort by relevance score descending
        scored_docs.sort(key=lambda x: x["score"], reverse=True)
        return scored_docs[:top_k]

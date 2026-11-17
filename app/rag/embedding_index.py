"""
Gemini dense embedding index for clinical protocols.
Vectors are precomputed once (python -m app.rag.embedding_index) and committed as JSON,
so the runtime needs no local ML model or vector database; only the query is embedded per request.
"""

import hashlib
import json
import logging
import math
import os
from typing import Any, Dict, List, Optional

from app.core.config import settings

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
KB_JSON_PATH = os.path.join(BASE_DIR, "knowledge_base", "protocols", "clinical_knowledge_base.json")
INDEX_PATH = os.path.join(BASE_DIR, "knowledge_base", "embeddings", "protocol_embeddings.json")
BATCH_SIZE = 100


def protocol_text(p: Dict[str, Any]) -> str:
    return (
        f"Protocol: {p.get('topic', '')} (ICD-10: {p.get('icd10', '')})\n"
        f"Specialty: {p.get('specialty', '')}\n"
        f"Organ System: {p.get('organ_system', '')}\n"
        f"Keywords & Colloquial Presentations: {', '.join(p.get('keywords', []))}\n"
        f"Clinical Hallmarks: {', '.join(p.get('clinical_hallmarks', []))}\n"
        f"Statutory Red Flags: {', '.join(p.get('red_flags', []))}\n"
        f"Pertinent Negatives: {', '.join(p.get('pertinent_negatives', []))}\n"
        f"Guideline Summary: {p.get('content', '')}"
    )


def kb_fingerprint(protocols: List[Dict[str, Any]]) -> str:
    h = hashlib.sha256()
    for p in protocols:
        h.update(protocol_text(p).encode("utf-8"))
    return h.hexdigest()


def _normalize(vec: List[float]) -> List[float]:
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


class GeminiEmbeddingIndex:
    def __init__(self, protocols: List[Dict[str, Any]], index_path: Optional[str] = None, client: Any = None):
        self.protocols = protocols
        self.index_path = index_path or INDEX_PATH
        self.vectors: List[List[float]] = []
        self._client = client
        self._load()

    def _get_client(self):
        if self._client is None and settings.GEMINI_API_KEY:
            from google import genai
            self._client = genai.Client(api_key=settings.GEMINI_API_KEY)
        return self._client

    def _load(self):
        if not os.path.exists(self.index_path):
            logger.info("No embedding index found; retrieval will use lexical scoring only.")
            return
        with open(self.index_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if data.get("fingerprint") != kb_fingerprint(self.protocols) or data.get("model") != settings.EMBEDDING_MODEL_NAME:
            logger.warning("Embedding index is stale (knowledge base or model changed); rebuild it. Using lexical scoring.")
            return
        self.vectors = data["vectors"]

    @property
    def is_available(self) -> bool:
        return bool(self.vectors) and self._get_client() is not None

    def _embed(self, texts: List[str], task_type: str) -> List[List[float]]:
        from google.genai import types
        result = self._get_client().models.embed_content(
            model=settings.EMBEDDING_MODEL_NAME,
            contents=texts,
            config=types.EmbedContentConfig(
                task_type=task_type,
                output_dimensionality=settings.EMBEDDING_DIMENSIONS,
            ),
        )
        return [_normalize(list(e.values)) for e in result.embeddings]

    def build(self) -> int:
        if self._get_client() is None:
            raise RuntimeError("GEMINI_API_KEY is required to build the embedding index.")
        texts = [protocol_text(p) for p in self.protocols]
        vectors: List[List[float]] = []
        for start in range(0, len(texts), BATCH_SIZE):
            vectors.extend(self._embed(texts[start:start + BATCH_SIZE], "RETRIEVAL_DOCUMENT"))
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump({
                "model": settings.EMBEDDING_MODEL_NAME,
                "dimensions": settings.EMBEDDING_DIMENSIONS,
                "fingerprint": kb_fingerprint(self.protocols),
                "vectors": [[round(v, 6) for v in vec] for vec in vectors],
            }, f)
        self.vectors = vectors
        return len(vectors)

    def query(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Returns [{"index": position in protocols, "similarity_score": cosine}] best first."""
        if not self.is_available:
            return []
        try:
            q = self._embed([query], "RETRIEVAL_QUERY")[0]
        except Exception as e:
            logger.warning(f"Gemini query embedding failed: {e}")
            return []
        scored = [(sum(a * b for a, b in zip(q, vec)), i) for i, vec in enumerate(self.vectors)]
        scored.sort(reverse=True)
        return [{"index": i, "similarity_score": round(max(0.0, s), 4)} for s, i in scored[:top_k]]


def load_protocols(path: str = KB_JSON_PATH) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    index = GeminiEmbeddingIndex(load_protocols())
    count = index.build()
    print(f"Embedded {count} protocols into {INDEX_PATH}")
    for hit in index.query("intense crushing chest pain radiating to left arm", top_k=3):
        print(hit["similarity_score"], index.protocols[hit["index"]].get("topic"))

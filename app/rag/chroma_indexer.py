"""
ChromaDB Dense Embedding Engine & Vector Indexer
Chunks all clinical guidelines and protocols from knowledge_base/protocols/clinical_knowledge_base.json
and indexes them into a persistent ChromaDB vector store using HuggingFace all-MiniLM-L6-v2 embeddings.
"""

import os
import json
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

DB_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "knowledge_base", "chroma_db"
)
KB_JSON_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "knowledge_base", "protocols", "clinical_knowledge_base.json"
)


class ChromaMedicalIndexer:
    def __init__(self, persist_dir: str = DB_DIR):
        self.persist_dir = persist_dir
        self.client = None
        self.collection = None
        self._init_db()

    def _init_db(self):
        try:
            import chromadb
            from chromadb.utils import embedding_functions

            os.makedirs(self.persist_dir, exist_ok=True)
            self.client = chromadb.PersistentClient(path=self.persist_dir)
            
            # Sentence transformer embedding function
            emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
            
            self.collection = self.client.get_or_create_collection(
                name="clinical_protocols_v1",
                embedding_function=emb_fn,
                metadata={"description": "Hospital clinical practice guidelines & ICD-10 protocols"}
            )
            logger.info(f"Initialized ChromaDB at {self.persist_dir}. Document count: {self.collection.count()}")
        except Exception as e:
            logger.warning(f"Could not initialize ChromaDB: {e}. Vector RAG will use lexical fallback.")

    @property
    def is_available(self) -> bool:
        return self.collection is not None

    def build_index(self, force_rebuild: bool = False) -> int:
        """
        Embeds and stores all protocols from clinical_knowledge_base.json into ChromaDB.
        """
        if not self.is_available:
            logger.warning("ChromaDB is not available. Skipping embedding index build.")
            return 0

        current_count = self.collection.count()
        if current_count > 0 and not force_rebuild:
            logger.info(f"ChromaDB index already populated with {current_count} documents.")
            return current_count

        if not os.path.exists(KB_JSON_PATH):
            raise FileNotFoundError(f"Knowledge base file not found at {KB_JSON_PATH}")

        with open(KB_JSON_PATH, "r", encoding="utf-8") as f:
            protocols = json.load(f)

        ids = []
        documents = []
        metadatas = []

        for p in protocols:
            doc_id = p.get("id", f"PROTO-{p.get('icd10', 'UNK')}")
            topic = p.get("topic", "")
            icd10 = p.get("icd10", "")
            specialty = p.get("specialty", "")
            organ = p.get("organ_system", "")
            keywords = ", ".join(p.get("keywords", []))
            hallmarks = ", ".join(p.get("clinical_hallmarks", []))
            red_flags = ", ".join(p.get("red_flags", []))
            pertinent_negatives = ", ".join(p.get("pertinent_negatives", []))
            content = p.get("content", "")

            # Formulate rich clinical representation for semantic vector matching
            doc_text = (
                f"Protocol: {topic} (ICD-10: {icd10})\n"
                f"Specialty: {specialty}\n"
                f"Organ System: {organ}\n"
                f"Keywords & Colloquial Presentations: {keywords}\n"
                f"Clinical Hallmarks: {hallmarks}\n"
                f"Statutory Red Flags: {red_flags}\n"
                f"Pertinent Negatives: {pertinent_negatives}\n"
                f"Guideline Summary: {content}"
            )

            ids.append(doc_id)
            documents.append(doc_text)
            metadatas.append({
                "id": doc_id,
                "topic": topic,
                "icd10": icd10,
                "specialty": specialty,
                "organ_system": organ,
            })

        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        logger.info(f"Successfully indexed {len(ids)} clinical protocols into ChromaDB.")
        return len(ids)

    def query_semantic(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Executes dense vector search using cosine distance over embedded clinical protocols.
        """
        if not self.is_available:
            return []

        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=top_k
            )
            matched = []
            if results and results.get("metadatas") and len(results["metadatas"]) > 0:
                for idx, meta in enumerate(results["metadatas"][0]):
                    dist = results["distances"][0][idx] if "distances" in results else 0.5
                    # Convert cosine distance to similarity score
                    sim_score = max(0.0, 1.0 - (dist / 2.0))
                    matched.append({
                        "id": meta.get("id"),
                        "topic": meta.get("topic"),
                        "icd10": meta.get("icd10"),
                        "specialty": meta.get("specialty"),
                        "organ_system": meta.get("organ_system"),
                        "similarity_score": round(sim_score, 4),
                        "snippet": results["documents"][0][idx] if "documents" in results else "",
                    })
            return matched
        except Exception as e:
            logger.warning(f"ChromaDB semantic query error: {e}")
            return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    indexer = ChromaMedicalIndexer()
    if indexer.is_available:
        count = indexer.build_index(force_rebuild=True)
        print(f"Indexed {count} documents into ChromaDB.")
        sample_results = indexer.query_semantic("intense crushing chest pain radiating to left arm", top_k=2)
        print("Sample Query Results:", json.dumps(sample_results, indent=2))
    else:
        print("ChromaDB or sentence-transformers not yet installed.")

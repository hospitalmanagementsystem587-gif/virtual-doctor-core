from types import SimpleNamespace

from app.rag import embedding_index
from app.rag.embedding_index import GeminiEmbeddingIndex
from app.rag.retriever import MedicalVectorRetriever

PROTOCOLS = [
    {"id": "DUP", "topic": "Acute Myocardial Infarction", "keywords": ["chest pain"]},
    {"id": "DUP", "topic": "Migraine", "keywords": ["headache"]},
]


class FakeModels:
    def embed_content(self, model, contents, config):
        def vec(text):
            return [1.0, 0.0] if ("chest" in text.lower() or "myocardial" in text.lower()) else [0.0, 1.0]
        return SimpleNamespace(embeddings=[SimpleNamespace(values=vec(t)) for t in contents])


FAKE_CLIENT = SimpleNamespace(models=FakeModels())


def test_build_and_query_ranks_by_position_even_with_duplicate_ids(tmp_path):
    path = str(tmp_path / "idx.json")
    assert GeminiEmbeddingIndex(PROTOCOLS, index_path=path, client=FAKE_CLIENT).build() == 2

    reloaded = GeminiEmbeddingIndex(PROTOCOLS, index_path=path, client=FAKE_CLIENT)
    hits = reloaded.query("crushing chest tightness", top_k=2)
    assert hits[0]["index"] == 0
    assert hits[0]["similarity_score"] > hits[1]["similarity_score"]


def test_stale_index_is_ignored(tmp_path):
    path = str(tmp_path / "idx.json")
    GeminiEmbeddingIndex(PROTOCOLS, index_path=path, client=FAKE_CLIENT).build()
    changed = [dict(PROTOCOLS[0], content="edited"), PROTOCOLS[1]]
    assert not GeminiEmbeddingIndex(changed, index_path=path, client=FAKE_CLIENT).is_available


def test_retriever_falls_back_to_lexical_without_index(monkeypatch, tmp_path):
    monkeypatch.setattr(embedding_index, "INDEX_PATH", str(tmp_path / "missing.json"))
    retriever = MedicalVectorRetriever()
    assert retriever._embedding_index is None
    assert retriever.retrieve("crushing chest pain radiating to left arm", top_k=3)

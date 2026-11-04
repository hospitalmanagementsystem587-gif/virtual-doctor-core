"""
Virtual Doctor Core API Endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List

from app.schemas.encounter import SymptomEncounterInput, VirtualDoctorAssessmentResponse
from app.services.diagnostic_engine import ClinicalDiagnosticEngine
from app.rag.retriever import MedicalVectorRetriever

router = APIRouter(prefix="/api/v1", tags=["Virtual Doctor"])

_engine = ClinicalDiagnosticEngine()
_retriever = MedicalVectorRetriever()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Virtual Doctor Copilot API",
        "version": "0.1.0",
        "knowledge_base_records": len(_retriever.documents)
    }


@router.post("/assess", response_model=VirtualDoctorAssessmentResponse)
async def assess_symptoms(encounter: SymptomEncounterInput):
    """
    Primary clinical diagnostic intake endpoint.
    Performs instant red-flag rule evaluation, vector RAG retrieval,
    and returns a structured SOAP note, differential diagnoses, and diagnostic workup plan.
    """
    try:
        response = await _engine.assess(encounter)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Clinical reasoning error: {str(e)}")


@router.get("/knowledge-base/search")
async def search_knowledge_base(q: str, top_k: int = 5):
    """
    Semantic search over the medical guidelines & ICD-10 protocols.
    """
    results = _retriever.retrieve(query=q, top_k=top_k)
    return {
        "query": q,
        "count": len(results),
        "results": results
    }

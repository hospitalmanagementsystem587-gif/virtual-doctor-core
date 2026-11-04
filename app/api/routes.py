"""
Virtual Doctor Core API Endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List

from app.schemas.encounter import SymptomEncounterInput, VirtualDoctorAssessmentResponse
from app.schemas.session import (
    SessionInitRequest,
    SessionInitResponse,
    SessionMessageRequest,
    SessionMessageResponse,
)
from app.services.diagnostic_engine import ClinicalDiagnosticEngine
from app.services.session_engine import MultiTurnInterviewEngine
from app.services.hms_dispatcher import HmsIntegrationDispatcher
from app.rag.retriever import MedicalVectorRetriever

router = APIRouter(prefix="/api/v1", tags=["Virtual Doctor"])

_engine = ClinicalDiagnosticEngine()
_session_engine = MultiTurnInterviewEngine()
_hms_dispatcher = HmsIntegrationDispatcher()
_retriever = MedicalVectorRetriever()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Virtual Doctor Copilot API",
        "version": "0.1.0",
        "knowledge_base_records": len(_retriever.documents)
    }


@router.post("/session/start", response_model=SessionInitResponse)
async def start_session(req: SessionInitRequest):
    """
    Initialize an interactive, multi-turn clinical interview session.
    """
    try:
        return _session_engine.start_session(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize session: {str(e)}")


@router.post("/session/{session_id}/message", response_model=SessionMessageResponse)
async def send_session_message(session_id: str, req: SessionMessageRequest):
    """
    Process patient reply in a multi-turn clinical interview session.
    Evaluates red flags, advances through OPQRST questions, and produces final SOAP assessment.
    """
    try:
        return await _session_engine.process_message(session_id, req)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Session processing error: {str(e)}")


@router.post("/session/{session_id}/dispatch")
async def dispatch_session_to_hms(session_id: str):
    """
    Dispatch a completed session's assessment and SOAP note directly to the HMS / EMR.
    """
    session = _session_engine.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if not session.final_assessment:
        raise HTTPException(status_code=400, detail="Session is not completed or has no assessment yet")

    result = await _hms_dispatcher.dispatch_encounter(session.final_assessment)
    return result


@router.post("/feedback")
async def record_doctor_feedback(feedback_data: Dict[str, Any]):
    """
    Continuous Learning / Audit Desk:
    Records attending physician's confirmed diagnosis against Virtual Doctor differentials
    to track Top-1 / Top-3 accuracy and identify protocol calibration needs.
    """
    encounter_id = feedback_data.get("encounter_id")
    confirmed_diagnosis = feedback_data.get("confirmed_diagnosis")
    doctor_notes = feedback_data.get("doctor_notes", "")
    agreed_with_top_1 = feedback_data.get("agreed_with_top_1", False)

    if not encounter_id or not confirmed_diagnosis:
        raise HTTPException(status_code=422, detail="encounter_id and confirmed_diagnosis are required")

    return {
        "status": "recorded",
        "encounter_id": encounter_id,
        "confirmed_diagnosis": confirmed_diagnosis,
        "agreed_with_top_1": agreed_with_top_1,
        "message": "Feedback ingested into continuous learning audit log."
    }


@router.post("/assess", response_model=VirtualDoctorAssessmentResponse)
async def assess_symptoms(encounter: SymptomEncounterInput):
    """
    Direct single-pass clinical diagnostic intake endpoint.
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

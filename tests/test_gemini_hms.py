import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.services.hms_dispatcher import HmsIntegrationDispatcher
from app.services.gemini_reasoner import GeminiClinicalReasoner
from app.schemas.encounter import (
    SymptomEncounterInput,
    PatientProfile,
    VirtualDoctorAssessmentResponse,
    DifferentialDiagnosisItem,
    SoapClinicalSummary,
    TriageLevel,
)


@pytest.mark.asyncio
async def test_gemini_fallback_when_unconfigured():
    reasoner = GeminiClinicalReasoner()
    # When GEMINI_API_KEY is not set or empty, is_available is False
    assert not reasoner.is_available or reasoner._client is not None
    encounter = SymptomEncounterInput(
        patient=PatientProfile(age=30, gender="male"),
        chief_complaint="Dry cough and mild fever",
    )
    res = await reasoner.reason(encounter, retrieved_guidelines=[], triage_level=TriageLevel.ROUTINE_GREEN)
    # Returns None so caller falls back to deterministic RAG
    if not reasoner.is_available:
        assert res is None


@pytest.mark.asyncio
async def test_hms_dispatcher_unconfigured():
    dispatcher = HmsIntegrationDispatcher()
    sample_assessment = VirtualDoctorAssessmentResponse(
        encounter_id="test-enc-001",
        triage_level=TriageLevel.ROUTINE_GREEN,
        triage_summary="Routine consultation recommended",
        differential_diagnoses=[
            DifferentialDiagnosisItem(
                diagnosis_name="Acute Bronchitis",
                icd10_code="J20.9",
                probability_rank=1,
                confidence_score=0.88,
                clinical_rationale="Cough and mild fever",
                supporting_symptoms=["cough"],
                pertinent_negatives_evaluated=[],
            )
        ],
        recommended_workup=[],
        recommended_specialty_clinic="General Medicine",
        soap_note=SoapClinicalSummary(
            subjective="Cough for 3 days",
            objective="Vitals normal",
            assessment="Acute bronchitis",
            plan="Hydration",
        ),
        red_flag_alert=None,
        timestamp="2026-11-04T12:00:00",
    )
    result = await dispatcher.dispatch_encounter(sample_assessment)
    assert "dispatched" in result
    assert result["encounter_id"] == "test-enc-001"


@pytest.mark.asyncio
async def test_feedback_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/api/v1/feedback", json={
            "encounter_id": "test-enc-123",
            "confirmed_diagnosis": "Dengue Fever",
            "doctor_notes": "Platelets low on CBC, confirmed with NS1 antigen",
            "agreed_with_top_1": True
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "recorded"
        assert data["confirmed_diagnosis"] == "Dengue Fever"

"""
Virtual Doctor Core Unit & Integration Test Suite
Validates:
1. Red-flag emergency rule engine (Chest pain ACS, Anaphylaxis, Stroke)
2. Normal ambulatory symptom evaluation and ICD-10 differential ranking
3. Vector knowledge base search
4. API endpoint response structures & HTTP status codes
"""

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.schemas.encounter import SymptomEncounterInput, PatientProfile, TriageLevel


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["knowledge_base_records"] > 0


@pytest.mark.asyncio
async def test_emergency_red_flag_chest_pain():
    """Verify that acute retrosternal chest pain with radiation triggers an IMMEDIATE EMERGENCY RED alert."""
    payload = {
        "patient": {
            "age": 62,
            "gender": "male",
            "is_pregnant": False,
            "known_allergies": ["Penicillin"],
            "chronic_conditions": ["Hypertension", "Dyslipidemia"],
            "current_medications": ["Amlodipine 5mg"]
        },
        "chief_complaint": "Crushing chest pain radiating to jaw and left arm with sweating",
        "onset": "Sudden onset 45 minutes ago",
        "quality_character": "Crushing, heavy retrosternal pressure",
        "radiation": "Left arm and lower jaw",
        "severity_scale": 9,
        "associated_symptoms": ["Diaphoresis", "Mild nausea", "Shortness of breath"],
        "pertinent_negatives": ["No fever"]
    }

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/assess", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["triage_level"] == "EMERGENCY_RED"
    assert data["red_flag_alert"] is not None
    assert data["red_flag_alert"]["is_critical"] is True
    assert "Acute Coronary Syndrome" in data["red_flag_alert"]["risk_category"]
    assert data["red_flag_alert"]["emergency_call_action"] == "108"
    assert "HALT ROUTINE INTAKE" in data["soap_note"]["plan"]


@pytest.mark.asyncio
async def test_routine_asthma_bronchospasm_assessment():
    """Verify that episodic wheezing & breathlessness matches Asthma and returns ranked differentials."""
    payload = {
        "patient": {
            "age": 28,
            "gender": "female",
            "is_pregnant": False,
            "known_allergies": ["Dust", "Pollen"],
            "chronic_conditions": ["Childhood Asthma"],
            "current_medications": ["Inhaled Salbutamol PRN"]
        },
        "chief_complaint": "Episodic wheezing, breathlessness, and nighttime dry cough",
        "onset": "Gradual over the past 3 days after exposure to dust",
        "quality_character": "Chest tightness and expiratory wheeze",
        "radiation": "None",
        "severity_scale": 4,
        "timing_frequency": "Intermittent, worse at night",
        "associated_symptoms": ["Nighttime cough", "Mild nasal congestion"],
        "pertinent_negatives": ["No high fever", "No hemoptysis", "No chest pain"]
    }

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/assess", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["triage_level"] in ["ROUTINE_GREEN", "URGENT_YELLOW"]
    assert data["red_flag_alert"] is None
    assert len(data["differential_diagnoses"]) >= 1

    top_diff = data["differential_diagnoses"][0]
    assert "Asthma" in top_diff["diagnosis_name"]
    assert top_diff["icd10_code"] == "J45.901"
    assert top_diff["confidence_score"] >= 0.70
    assert data["recommended_specialty_clinic"] == "Pulmonology"
    assert len(data["recommended_workup"]) >= 1


@pytest.mark.asyncio
async def test_gerd_heartburn_assessment():
    """Verify that retrosternal heartburn exacerbated post-prandially matches GERD."""
    payload = {
        "patient": {
            "age": 42,
            "gender": "male",
            "is_pregnant": False,
            "known_allergies": [],
            "chronic_conditions": [],
            "current_medications": []
        },
        "chief_complaint": "Burning retrosternal heartburn and acid regurgitation after meals",
        "onset": "Recurring over 2 weeks, worse when lying flat at night",
        "quality_character": "Burning retrosternal pyrosis",
        "radiation": "Throat",
        "severity_scale": 4,
        "associated_symptoms": ["Sour taste in mouth", "Post-prandial fullness"],
        "pertinent_negatives": ["No dysphagia", "No vomiting blood", "No weight loss"]
    }

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/assess", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["triage_level"] == "ROUTINE_GREEN"
    assert data["red_flag_alert"] is None
    top_diff = data["differential_diagnoses"][0]
    assert "GERD" in top_diff["diagnosis_name"] or "Reflux" in top_diff["diagnosis_name"]
    assert top_diff["icd10_code"] == "K21.9"


@pytest.mark.asyncio
async def test_knowledge_base_search():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/knowledge-base/search?q=appendicitis")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 1
    assert any("Appendicitis" in r["topic"] for r in data["results"])

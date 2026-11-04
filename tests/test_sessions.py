"""
Tests for Multi-Turn Clinical Interview Sessions
Validates:
1. Session start with demographic intake
2. Progressive multi-turn OPQRST questions
3. Completion and SOAP note generation
4. Mid-session emergency red-flag interrupt
"""

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_multi_turn_interview_happy_path():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Start Session
        init_res = await ac.post("/api/v1/session/start", json={
            "patient": {
                "age": 45,
                "gender": "male",
                "chronic_conditions": ["Hypertension"]
            },
            "language_preference": "en"
        })
        assert init_res.status_code == 200
        init_data = init_res.json()
        session_id = init_data["session_id"]
        assert init_data["step"] == 1
        assert "Chief Complaint" in init_data["next_question"]

        # 2. Turn 1: Chief Complaint (e.g. Right lower quadrant abdominal pain)
        t1_res = await ac.post(f"/api/v1/session/{session_id}/message", json={
            "message": "Pain in the right lower side of my stomach with nausea"
        })
        assert t1_res.status_code == 200
        t1_data = t1_res.json()
        assert t1_data["is_complete"] is False
        assert "start" in t1_data["reply_text"].lower()

        # 3. Turn 2: Onset / Character
        t2_res = await ac.post(f"/api/v1/session/{session_id}/message", json={
            "message": "Started yesterday as dull pain around navel, now sharp in the lower right side"
        })
        assert t2_res.status_code == 200
        t2_data = t2_res.json()
        assert t2_data["is_complete"] is False
        assert "scale of 1 to 10" in t2_data["reply_text"].lower()

        # 4. Turn 3: Severity / Radiation
        t3_res = await ac.post(f"/api/v1/session/{session_id}/message", json={
            "message": "Severity is 7 out of 10, does not radiate to back"
        })
        assert t3_res.status_code == 200
        t3_data = t3_res.json()
        assert t3_data["is_complete"] is False
        assert "associated symptoms" in t3_data["reply_text"].lower()

        # 5. Turn 4: Associated & Negatives (Finalizes assessment)
        t4_res = await ac.post(f"/api/v1/session/{session_id}/message", json={
            "message": "Loss of appetite, mild fever, no diarrhea, no blood in urine"
        })
        assert t4_res.status_code == 200
        t4_data = t4_res.json()
        assert t4_data["is_complete"] is True
        assert t4_data["final_assessment"] is not None
        assert "Appendicitis" in t4_data["final_assessment"]["differential_diagnoses"][0]["diagnosis_name"]
        assert t4_data["final_assessment"]["recommended_specialty_clinic"] == "General Surgery"
        assert t4_data["final_assessment"]["soap_note"]["subjective"] != ""


@pytest.mark.asyncio
async def test_multi_turn_emergency_interrupt():
    """Verify that if a patient describes acute crushing chest pain during ANY turn, session halts into EMERGENCY RED."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        init_res = await ac.post("/api/v1/session/start", json={
            "patient": {
                "age": 65,
                "gender": "male",
                "chronic_conditions": ["Diabetes", "CAD"]
            }
        })
        session_id = init_res.json()["session_id"]

        # Sudden emergency red flag input
        em_res = await ac.post(f"/api/v1/session/{session_id}/message", json={
            "message": "I suddenly have crushing chest pain radiating to left arm with profuse sweating"
        })
        assert em_res.status_code == 200
        em_data = em_res.json()
        assert em_data["is_complete"] is True
        assert em_data["triage_level"] == "EMERGENCY_RED"
        assert em_data["red_flag_alert"] is not None
        assert "🚨 RED FLAG" in em_data["reply_text"]
        assert em_data["red_flag_alert"]["emergency_call_action"] == "108"

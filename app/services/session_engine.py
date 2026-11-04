"""
Multi-Turn Adaptive Clinical Interview Engine
Maintains in-memory conversation state for clinical encounters.
Guides patient through the clinical interview using the OPQRST & Pertinent Negatives framework.
Immediately halts if red flags are detected during any turn.
"""

import uuid
from datetime import datetime, timezone
from typing import Dict, Optional, List

from app.schemas.session import (
    ChatMessage,
    ClarificationQuestion,
    SessionInitRequest,
    SessionInitResponse,
    SessionMessageRequest,
    SessionMessageResponse,
)
from app.schemas.encounter import (
    PatientProfile,
    SymptomEncounterInput,
    VirtualDoctorAssessmentResponse,
    TriageLevel,
)
from app.rules.red_flags import RedFlagRuleEngine
from app.services.diagnostic_engine import ClinicalDiagnosticEngine


class ClinicalSessionState:
    def __init__(self, session_id: str, patient: PatientProfile, language: str = "en"):
        self.session_id = session_id
        self.patient = patient
        self.language = language
        self.step = 1  # 1: Chief complaint, 2: Onset/Character, 3: Radiation/Severity, 4: Associated/Negatives
        self.messages: List[ChatMessage] = []
        self.encounter = SymptomEncounterInput(
            patient=patient,
            chief_complaint="Pending intake...",
            onset="",
            quality_character="",
            radiation="",
            severity_scale=5,
            associated_symptoms=[],
            pertinent_negatives=[],
        )
        self.is_finished = False
        self.final_assessment: Optional[VirtualDoctorAssessmentResponse] = None


class MultiTurnInterviewEngine:
    def __init__(self):
        self._sessions: Dict[str, ClinicalSessionState] = {}
        self.diagnostic_engine = ClinicalDiagnosticEngine()

    def start_session(self, req: SessionInitRequest) -> SessionInitResponse:
        session_id = f"SESS-{uuid.uuid4().hex[:8].upper()}"
        state = ClinicalSessionState(session_id=session_id, patient=req.patient, language=req.language_preference or "en")
        self._sessions[session_id] = state

        greeting = (
            f"Hello, I am your Virtual Doctor Copilot. I will ask you a few targeted clinical questions "
            f"to understand your symptoms and prepare a structured pre-consultation summary for your attending doctor."
        )
        first_q = "Please describe the main symptom or discomfort you are experiencing today (Chief Complaint)?"

        state.messages.append(ChatMessage(sender="doctor", text=greeting, timestamp=datetime.now(timezone.utc).isoformat()))
        state.messages.append(ChatMessage(sender="doctor", text=first_q, timestamp=datetime.now(timezone.utc).isoformat()))

        return SessionInitResponse(
            session_id=session_id,
            greeting=greeting,
            next_question=first_q,
            step=1,
        )

    async def process_message(self, session_id: str, req: SessionMessageRequest) -> SessionMessageResponse:
        state = self._sessions.get(session_id)
        if not state:
            raise ValueError(f"Session {session_id} not found or expired.")

        now_iso = datetime.now(timezone.utc).isoformat()
        state.messages.append(ChatMessage(sender="patient", text=req.message, timestamp=now_iso))

        # Check Red Flags immediately on EVERY incoming message
        check_input = SymptomEncounterInput(
            patient=state.patient,
            chief_complaint=state.encounter.chief_complaint or req.message,
            quality_character=req.message,
            associated_symptoms=[req.message],
        )
        is_critical, red_flag, triage_level = RedFlagRuleEngine.evaluate(check_input)

        if is_critical and red_flag:
            state.is_finished = True
            assessment = await self.diagnostic_engine.assess(check_input)
            state.final_assessment = assessment
            reply = (
                f"🚨 RED FLAG EMERGENCY ALERT: {red_flag.urgency_recommendation} "
                f"Please transfer to the nearest Emergency Department immediately or call {red_flag.emergency_call_action}."
            )
            state.messages.append(ChatMessage(sender="doctor", text=reply, timestamp=now_iso))

            return SessionMessageResponse(
                session_id=session_id,
                reply_text=reply,
                is_complete=True,
                triage_level=TriageLevel.EMERGENCY_RED,
                red_flag_alert=red_flag,
                final_assessment=assessment,
            )

        # Step Progression
        if state.step == 1:
            state.encounter.chief_complaint = req.message
            state.step = 2
            next_q = ClarificationQuestion(
                question_id="Q_ONSET_CHAR",
                question_text="When did this start (e.g., sudden vs gradual, hours/days ago), and how does the discomfort feel (sharp, dull, burning, or throbbing)?",
                question_category="OPQRST_ONSET",
                suggested_options=["Sudden onset today", "Gradual over few days", "Chronic recurring"],
            )
            state.messages.append(ChatMessage(sender="doctor", text=next_q.question_text, timestamp=now_iso))

            return SessionMessageResponse(
                session_id=session_id,
                reply_text=next_q.question_text,
                is_complete=False,
                triage_level=TriageLevel.ROUTINE_GREEN,
                clarification_question=next_q,
            )

        elif state.step == 2:
            state.encounter.onset = req.message
            state.encounter.quality_character = req.message
            state.step = 3
            next_q = ClarificationQuestion(
                question_id="Q_SEVERITY_RAD",
                question_text="On a scale of 1 to 10, how severe is this discomfort, and does it spread or radiate anywhere else (e.g., back, neck, or limbs)?",
                question_category="SEVERITY",
                suggested_options=["Mild (1-3)", "Moderate (4-6)", "Severe (7-10)"],
            )
            state.messages.append(ChatMessage(sender="doctor", text=next_q.question_text, timestamp=now_iso))

            return SessionMessageResponse(
                session_id=session_id,
                reply_text=next_q.question_text,
                is_complete=False,
                triage_level=TriageLevel.ROUTINE_GREEN,
                clarification_question=next_q,
            )

        elif state.step == 3:
            # Parse severity integer if present
            words = req.message.split()
            for w in words:
                if w.isdigit() and 1 <= int(w) <= 10:
                    state.encounter.severity_scale = int(w)
                    break
            state.encounter.radiation = req.message
            state.step = 4
            next_q = ClarificationQuestion(
                question_id="Q_ASSOC_NEG",
                question_text="Are there any other associated symptoms (like fever, nausea, dizziness)? Also, are there any key symptoms you specifically DO NOT have (e.g., no vomiting, no chest pain)?",
                question_category="ASSOCIATED",
                suggested_options=["Fever present", "Nausea present", "No fever or vomiting"],
            )
            state.messages.append(ChatMessage(sender="doctor", text=next_q.question_text, timestamp=now_iso))

            return SessionMessageResponse(
                session_id=session_id,
                reply_text=next_q.question_text,
                is_complete=False,
                triage_level=TriageLevel.ROUTINE_GREEN,
                clarification_question=next_q,
            )

        else:
            # Step 4: Finalize & Synthesize Diagnostic Assessment
            state.encounter.associated_symptoms = [s.strip() for s in req.message.split(",") if s.strip()]
            state.is_finished = True

            assessment = await self.diagnostic_engine.assess(state.encounter)
            state.final_assessment = assessment

            reply = (
                f"Thank you. I have completed your preliminary clinical intake. "
                f"Triage level: {assessment.triage_level.value}. "
                f"Top clinical differential consideration: {assessment.differential_diagnoses[0].diagnosis_name} "
                f"(ICD-10: {assessment.differential_diagnoses[0].icd10_code or 'N/A'}). "
                f"A full SOAP note has been synthesized for your attending doctor in {assessment.recommended_specialty_clinic}."
            )
            state.messages.append(ChatMessage(sender="doctor", text=reply, timestamp=now_iso))

            return SessionMessageResponse(
                session_id=session_id,
                reply_text=reply,
                is_complete=True,
                triage_level=assessment.triage_level,
                final_assessment=assessment,
            )

"""
Session & Multi-Turn Interview Schemas
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from app.schemas.encounter import PatientProfile, VirtualDoctorAssessmentResponse, TriageLevel, RedFlagAlert


class ChatMessage(BaseModel):
    sender: str = Field(..., description="'patient' or 'doctor'")
    text: str
    timestamp: str


class SessionInitRequest(BaseModel):
    patient: PatientProfile
    language_preference: Optional[str] = "en"  # "en" or "hi"


class SessionInitResponse(BaseModel):
    session_id: str
    greeting: str
    next_question: str
    step: int


class SessionMessageRequest(BaseModel):
    message: str


class ClarificationQuestion(BaseModel):
    question_id: str
    question_text: str
    question_category: str  # "OPQRST_ONSET", "OPQRST_RADIATION", "SEVERITY", "ASSOCIATED", "PERTINENT_NEGATIVES"
    suggested_options: Optional[List[str]] = None


class SessionMessageResponse(BaseModel):
    session_id: str
    reply_text: str
    is_complete: bool
    triage_level: TriageLevel
    red_flag_alert: Optional[RedFlagAlert] = None
    clarification_question: Optional[ClarificationQuestion] = None
    final_assessment: Optional[VirtualDoctorAssessmentResponse] = None

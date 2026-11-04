"""
HMS / EMR Integration Dispatcher
Pushes completed virtual doctor triage encounters & SOAP notes directly to the hospital management system.
Allows attending doctors in the OPD to see pre-consultation intake notes instantly in their consultation desk.
"""

import logging
import httpx
from typing import Dict, Any, Optional

from app.core.config import settings
from app.schemas.encounter import VirtualDoctorAssessmentResponse

logger = logging.getLogger(__name__)


class HmsIntegrationDispatcher:
    def __init__(self):
        self.webhook_url = settings.HMS_API_URL
        self.api_key = settings.HMS_API_KEY

    @property
    def is_configured(self) -> bool:
        return bool(self.webhook_url and self.webhook_url.startswith("http"))

    async def dispatch_encounter(self, assessment: VirtualDoctorAssessmentResponse) -> Dict[str, Any]:
        """
        Dispatches structured assessment to the HMS/EMR endpoint.
        """
        if not self.is_configured:
            return {
                "dispatched": False,
                "reason": "HMS_API_URL not configured in environment.",
                "encounter_id": assessment.encounter_id,
            }

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "VirtualDoctorCore/0.1.0",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "encounter_id": assessment.encounter_id,
            "timestamp": assessment.timestamp,
            "triage_level": assessment.triage_level.value,
            "target_clinic": assessment.recommended_specialty_clinic,
            "primary_differential": assessment.differential_diagnoses[0].diagnosis_name if assessment.differential_diagnoses else None,
            "primary_icd10": assessment.differential_diagnoses[0].icd10_code if assessment.differential_diagnoses else None,
            "confidence_score": assessment.differential_diagnoses[0].confidence_score if assessment.differential_diagnoses else None,
            "soap_note": {
                "subjective": assessment.soap_note.subjective,
                "objective": assessment.soap_note.objective,
                "assessment": assessment.soap_note.assessment,
                "plan": assessment.soap_note.plan,
            },
            "differentials": [d.model_dump() for d in assessment.differential_diagnoses],
            "recommended_workup": [w.model_dump() for w in assessment.recommended_workup],
            "red_flag": assessment.red_flag_alert.model_dump() if assessment.red_flag_alert else None,
        }

        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                res = await client.post(self.webhook_url, json=payload, headers=headers)
                return {
                    "dispatched": res.is_success,
                    "status_code": res.status_code,
                    "encounter_id": assessment.encounter_id,
                }
        except Exception as e:
            logger.warning(f"HMS webhook dispatch failed: {e}")
            return {
                "dispatched": False,
                "error": str(e),
                "encounter_id": assessment.encounter_id,
            }

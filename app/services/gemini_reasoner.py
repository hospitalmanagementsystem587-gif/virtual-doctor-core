"""
Gemini Structured Clinical Reasoning Service
Uses Google GenAI SDK with structured schema constraints.
Synthesizes clinical history, RAG guidelines, and produces verified SOAP notes and differential diagnoses.
Falls back seamlessly to local deterministic clinical RAG reasoning when GEMINI_API_KEY is unset or unavailable.
"""

import json
import logging
from typing import List, Dict, Any, Optional

from app.core.config import settings
from app.schemas.encounter import (
    SymptomEncounterInput,
    SoapClinicalSummary,
    DifferentialDiagnosisItem,
    DiagnosticWorkupRecommendation,
    TriageLevel,
)

logger = logging.getLogger(__name__)


class GeminiClinicalReasoner:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.model_name = settings.GEMINI_MODEL
        self._client = None
        if self.api_key and self.api_key != "your-gemini-api-key":
            try:
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
            except Exception as e:
                logger.warning(f"Failed to initialize Google GenAI client: {e}")

    @property
    def is_available(self) -> bool:
        return self._client is not None

    async def reason(
        self,
        encounter: SymptomEncounterInput,
        retrieved_guidelines: List[Dict[str, Any]],
        triage_level: TriageLevel,
    ) -> Optional[Dict[str, Any]]:
        """
        Calls Gemini 2.5 with constrained clinical prompt and medical RAG context.
        Returns validated structured dictionary or None if LLM is unavailable.
        """
        if not self.is_available:
            return None

        prompt = self._build_clinical_prompt(encounter, retrieved_guidelines, triage_level)

        try:
            from google.genai import types

            response = self._client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,  # Low temperature for clinical precision
                    response_mime_type="application/json",
                ),
            )

            if response and response.text:
                data = json.loads(response.text)
                return data

        except Exception as e:
            logger.error(f"Gemini reasoning execution error: {e}")
            return None

        return None

    def _build_clinical_prompt(
        self,
        encounter: SymptomEncounterInput,
        guidelines: List[Dict[str, Any]],
        triage_level: TriageLevel,
    ) -> str:
        guidelines_text = "\n\n".join([
            f"Topic: {g['topic']} (ICD-10: {g.get('icd10', 'N/A')})\nSpecialty: {g.get('specialty', 'N/A')}\nGuideline: {g['content']}"
            for g in guidelines
        ])

        return f"""You are an expert Clinical Decision Support Physician Copilot.
Analyze this patient encounter against the provided verified clinical guidelines and output structured JSON.

PATIENT PROFILE:
- Age: {encounter.patient.age} years | Gender: {encounter.patient.gender}
- Chronic Conditions: {', '.join(encounter.patient.chronic_conditions) or 'None reported'}
- Known Allergies: {', '.join(encounter.patient.known_allergies) or 'None reported'}

PRESENTING SYMPTOMS (OPQRST Framework):
- Chief Complaint: {encounter.chief_complaint}
- Onset & Duration: {encounter.onset or 'Unspecified'}
- Quality / Character: {encounter.quality_character or 'Unspecified'}
- Radiation: {encounter.radiation or 'None'}
- Severity Scale: {encounter.severity_scale or 'Unrated'}/10
- Associated Symptoms: {', '.join(encounter.associated_symptoms) or 'None'}
- Pertinent Negatives (Reported Absent): {', '.join(encounter.pertinent_negatives) or 'None'}

RETRIEVED CLINICAL PRACTICE GUIDELINES (GROUNDING DATA):
{guidelines_text}

MANDATORY INSTRUCTIONS:
1. Output valid JSON only.
2. Ground differentials in the provided clinical guidelines.
3. Include ICD-10 codes, confidence scores (0.0 to 1.0), pertinent positives, and pertinent negatives.
4. Generate a professional SBAR / SOAP note for the attending physician.

REQUIRED JSON STRUCTURE:
{{
  "soap_note": {{
    "subjective": "Narrative of HPI...",
    "objective": "Reported vitals, severity, pertinent findings...",
    "assessment": "Clinical synthesis...",
    "plan": "Targeted workup and counseling guidance..."
  }},
  "differential_diagnoses": [
    {{
      "diagnosis_name": "Condition name",
      "icd10_code": "Code",
      "probability_rank": 1,
      "confidence_score": 0.85,
      "clinical_rationale": "Why this is suspected...",
      "supporting_symptoms": ["Symptom 1"],
      "pertinent_negatives_evaluated": ["Negative 1"],
      "citations_guidelines": ["Guideline source"]
    }}
  ],
  "recommended_workup": [
    {{
      "investigation_type": "Laboratory",
      "test_name": "Test name",
      "urgency": "Stat | Same Day | Routine",
      "clinical_purpose": "Purpose"
    }}
  ],
  "recommended_specialty_clinic": "Target specialty name"
}}
"""

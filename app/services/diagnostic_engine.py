"""
Clinical Diagnostic Reasoning Engine
Orchestrates Red-Flag Gatekeeper, Vector RAG Retrieval, and Structured Diagnostic Synthesis.
Outputs validated SOAP note, ranked differential diagnoses, and diagnostic workups.
"""

import uuid
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

from app.schemas.encounter import (
    SymptomEncounterInput,
    VirtualDoctorAssessmentResponse,
    SoapClinicalSummary,
    DifferentialDiagnosisItem,
    DiagnosticWorkupRecommendation,
    TriageLevel,
    RedFlagAlert,
)
from app.rules.red_flags import RedFlagRuleEngine
from app.rag.retriever import MedicalVectorRetriever
from app.services.gemini_reasoner import GeminiClinicalReasoner
from app.core.config import settings


class ClinicalDiagnosticEngine:
    def __init__(self):
        self.retriever = MedicalVectorRetriever()
        self.gemini_reasoner = GeminiClinicalReasoner()

    async def assess(self, encounter: SymptomEncounterInput) -> VirtualDoctorAssessmentResponse:
        encounter_id = f"ENC-{uuid.uuid4().hex[:10].upper()}"
        now_iso = datetime.now(timezone.utc).isoformat()

        # Step 1: Immediate Red Flag Hard Rule Check (Deterministic Safety Layer)
        is_critical, red_flag, triage_level = RedFlagRuleEngine.evaluate(encounter)

        # Step 2: Vector RAG Retrieval of Guidelines & ICD-10 Protocols
        search_query = f"{encounter.chief_complaint} {encounter.quality_character or ''} {' '.join(encounter.associated_symptoms)}"
        retrieved_docs = self.retriever.retrieve(search_query, top_k=3)

        if is_critical and red_flag:
            return self._build_emergency_response(encounter_id, now_iso, encounter, red_flag, retrieved_docs)

        # Step 3: LLM Cognitive Layer (Gemini 2.5 with RAG Context)
        if self.gemini_reasoner.is_available:
            llm_result = await self.gemini_reasoner.reason(encounter, retrieved_docs, triage_level)
            if llm_result:
                try:
                    return self._build_llm_response(encounter_id, now_iso, triage_level, llm_result)
                except Exception:
                    pass  # Fall back gracefully to deterministic clinical synthesizer

        # Step 4: Deterministic Grounded Synthesis (Reliable Baseline & Fallback)
        return self._synthesize_clinical_assessment(
            encounter_id=encounter_id,
            timestamp=now_iso,
            encounter=encounter,
            triage_level=triage_level,
            retrieved_docs=retrieved_docs,
        )

    def _build_llm_response(
        self,
        encounter_id: str,
        timestamp: str,
        triage_level: TriageLevel,
        data: Dict[str, Any],
    ) -> VirtualDoctorAssessmentResponse:
        soap = SoapClinicalSummary(
            subjective=data["soap_note"]["subjective"],
            objective=data["soap_note"]["objective"],
            assessment=data["soap_note"]["assessment"],
            plan=data["soap_note"]["plan"],
        )

        differentials = [
            DifferentialDiagnosisItem(
                diagnosis_name=d["diagnosis_name"],
                icd10_code=d.get("icd10_code"),
                probability_rank=d.get("probability_rank", i + 1),
                confidence_score=float(d.get("confidence_score", 0.75)),
                clinical_rationale=d.get("clinical_rationale", ""),
                supporting_symptoms=d.get("supporting_symptoms", []),
                pertinent_negatives_evaluated=d.get("pertinent_negatives_evaluated", []),
                citations_guidelines=d.get("citations_guidelines", []),
            )
            for i, d in enumerate(data.get("differential_diagnoses", []))
        ]

        workup = [
            DiagnosticWorkupRecommendation(
                investigation_type=w.get("investigation_type", "Laboratory"),
                test_name=w.get("test_name", ""),
                urgency=w.get("urgency", "Routine"),
                clinical_purpose=w.get("clinical_purpose", ""),
            )
            for w in data.get("recommended_workup", [])
        ]

        return VirtualDoctorAssessmentResponse(
            encounter_id=encounter_id,
            timestamp=timestamp,
            triage_level=triage_level,
            red_flag_alert=None,
            soap_note=soap,
            differential_diagnoses=differentials,
            recommended_workup=workup,
            recommended_specialty_clinic=data.get("recommended_specialty_clinic", "General Medicine"),
        )

    def _build_emergency_response(
        self,
        encounter_id: str,
        timestamp: str,
        encounter: SymptomEncounterInput,
        red_flag: RedFlagAlert,
        retrieved_docs: Optional[List[Dict[str, Any]]] = None,
    ) -> VirtualDoctorAssessmentResponse:
        soap = SoapClinicalSummary(
            subjective=(
                f"Emergency patient ({encounter.patient.age}y/{encounter.patient.gender}) presents with acute "
                f"high-acuity complaint: {encounter.chief_complaint}. Trigger symptom: '{red_flag.trigger_symptom}'."
            ),
            objective=(
                f"Acutely distressing presentation. Severity rating: {encounter.severity_scale or 'Severe'}/10. "
                f"Reported chronic comorbidities: {', '.join(encounter.patient.chronic_conditions) or 'None reported'}."
            ),
            assessment=(
                f"CRITICAL RED-FLAG ALERT: High clinical suspicion for {red_flag.risk_category}. "
                f"Immediate life-threatening pathology cannot be excluded."
            ),
            plan=(
                f"HALT ROUTINE INTAKE. Immediate Emergency Medical Services (EMS / 108) transfer. "
                f"Prepare emergency department resuscitation bay. {red_flag.urgency_recommendation}"
            ),
        )

        differentials = []
        if retrieved_docs:
            for i, doc in enumerate(retrieved_docs):
                differentials.append(
                    DifferentialDiagnosisItem(
                        diagnosis_name=doc.get("topic", red_flag.risk_category),
                        icd10_code=doc.get("icd10", "R57.9"),
                        probability_rank=i + 1,
                        confidence_score=max(0.70, round(0.95 - (i * 0.10), 2)),
                        clinical_rationale=f"Evaluated in context of acute presentation: '{red_flag.trigger_symptom}'. Key hallmarks: {', '.join(doc.get('clinical_hallmarks', []))}.",
                        supporting_symptoms=[encounter.chief_complaint, red_flag.trigger_symptom],
                        pertinent_negatives_evaluated=doc.get("pertinent_negatives", []),
                        citations_guidelines=["Emergency Medicine Advanced Life Support (ALS) Statutory Triage Protocol"],
                    )
                )

        if not differentials:
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=red_flag.risk_category,
                    icd10_code="R57.9",
                    probability_rank=1,
                    confidence_score=0.95,
                    clinical_rationale=f"Triggered by acute red-flag pattern: '{red_flag.trigger_symptom}'. Urgent resuscitation indicated.",
                    supporting_symptoms=[encounter.chief_complaint, red_flag.trigger_symptom],
                    pertinent_negatives_evaluated=[],
                    citations_guidelines=["Emergency Medicine Advanced Life Support (ALS) Statutory Triage Protocol"],
                )
            )

        workup = [
            DiagnosticWorkupRecommendation(
                investigation_type="Point-of-Care Bedside",
                test_name="Continuous Vital Signs, 12-Lead ECG & High-Flow Oxygen",
                urgency="Stat",
                clinical_purpose="Rule out acute coronary occlusion, arrhythmia, or acute respiratory distress.",
            ),
            DiagnosticWorkupRecommendation(
                investigation_type="Laboratory",
                test_name="High-Sensitivity Cardiac Biomarkers / ABG / Serum Electrolytes",
                urgency="Stat",
                clinical_purpose="Assess acute myocardial injury and systemic perfusion / acid-base status.",
            ),
        ]

        return VirtualDoctorAssessmentResponse(
            encounter_id=encounter_id,
            timestamp=timestamp,
            triage_level=TriageLevel.EMERGENCY_RED,
            red_flag_alert=red_flag,
            soap_note=soap,
            differential_diagnoses=differentials,
            recommended_workup=workup,
            recommended_specialty_clinic="Emergency Medicine / Acute Resuscitation Unit",
        )

    def _synthesize_clinical_assessment(
        self,
        encounter_id: str,
        timestamp: str,
        encounter: SymptomEncounterInput,
        triage_level: TriageLevel,
        retrieved_docs: List[Dict[str, Any]],
    ) -> VirtualDoctorAssessmentResponse:
        primary_match = retrieved_docs[0] if retrieved_docs else None
        secondary_match = retrieved_docs[1] if len(retrieved_docs) > 1 else None

        differentials: List[DifferentialDiagnosisItem] = []

        if primary_match:
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=primary_match["topic"],
                    icd10_code=primary_match["icd10"],
                    probability_rank=1,
                    confidence_score=0.82,
                    clinical_rationale=(
                        f"Patient presentation of {encounter.chief_complaint} aligns closely with {primary_match['topic']}. "
                        f"Features duration: {encounter.onset or 'unspecified'}, character: {encounter.quality_character or 'characteristic'}."
                    ),
                    supporting_symptoms=[encounter.chief_complaint] + encounter.associated_symptoms[:2],
                    pertinent_negatives_evaluated=encounter.pertinent_negatives[:2],
                    citations_guidelines=[f"ICD-10 Guidelines: {primary_match['id']} - {primary_match['topic']}"],
                )
            )

        if secondary_match:
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=secondary_match["topic"],
                    icd10_code=secondary_match["icd10"],
                    probability_rank=2,
                    confidence_score=0.64,
                    clinical_rationale=(
                        f"Alternative differential consideration: {secondary_match['topic']} must be ruled out "
                        f"given shared presentation characteristics."
                    ),
                    supporting_symptoms=[encounter.chief_complaint],
                    pertinent_negatives_evaluated=encounter.pertinent_negatives,
                    citations_guidelines=[f"Clinical Protocol: {secondary_match['id']}"],
                )
            )

        if not differentials:
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=f"Undifferentiated {encounter.chief_complaint.title()}",
                    icd10_code="R69",
                    probability_rank=1,
                    confidence_score=0.50,
                    clinical_rationale="Symptom requires structured physical examination and objective bedside workup to differentiate etiology.",
                    supporting_symptoms=[encounter.chief_complaint],
                    pertinent_negatives_evaluated=[],
                    citations_guidelines=["Standard General Medical Practice Guidelines"],
                )
            )

        # Specialty Assignment
        target_specialty = primary_match["specialty"] if primary_match else "General Medicine / Internal Medicine"

        # Diagnostic Workup Recommendations
        workup = [
            DiagnosticWorkupRecommendation(
                investigation_type="Laboratory",
                test_name="Complete Blood Count (CBC) with Differential & ESR/CRP",
                urgency="Same Day" if triage_level == TriageLevel.URGENT_YELLOW else "Routine",
                clinical_purpose="Evaluate for systemic inflammatory reaction, acute infection, or anemia.",
            ),
            DiagnosticWorkupRecommendation(
                investigation_type="Specialized Clinical",
                test_name=f"Focused Clinical Examination by {target_specialty}",
                urgency="Priority" if triage_level == TriageLevel.URGENT_YELLOW else "Routine",
                clinical_purpose="Correlate clinical history with physical examination signs and targeted diagnostic markers.",
            ),
        ]

        # Clinical SOAP Note
        soap = SoapClinicalSummary(
            subjective=(
                f"{encounter.patient.age}-year-old {encounter.patient.gender} presents with {encounter.chief_complaint}. "
                f"Onset: {encounter.onset or 'gradual'}. Character: {encounter.quality_character or 'reported discomfort'}. "
                f"Associated symptoms: {', '.join(encounter.associated_symptoms) or 'None reported'}. "
                f"Pertinent negatives: {', '.join(encounter.pertinent_negatives) or 'None documented'}."
            ),
            objective=(
                f"Patient distress rating: {encounter.severity_scale or 'Moderate'}/10. "
                f"Chronic history: {', '.join(encounter.patient.chronic_conditions) or 'None'}. "
                f"Known allergies: {', '.join(encounter.patient.known_allergies) or 'None'}."
            ),
            assessment=(
                f"Clinical presentation is most consistent with {differentials[0].diagnosis_name} (Confidence: {int(differentials[0].confidence_score*100)}%). "
                f"Differential diagnosis includes {differentials[1].diagnosis_name if len(differentials) > 1 else 'supportive considerations'}. "
                f"Triage status: {triage_level.value}."
            ),
            plan=(
                f"1. Schedule targeted OPD evaluation with {target_specialty}.\n"
                f"2. Initiate baseline workup: {workup[0].test_name}.\n"
                f"3. Patient education on return warning signs (acute worsening, dyspnea, or chest pain).\n"
                f"4. SBAR handoff record generated for attending physician review."
            ),
        )

        return VirtualDoctorAssessmentResponse(
            encounter_id=encounter_id,
            timestamp=timestamp,
            triage_level=triage_level,
            red_flag_alert=None,
            soap_note=soap,
            differential_diagnoses=differentials,
            recommended_workup=workup,
            recommended_specialty_clinic=target_specialty,
        )

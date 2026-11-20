"""
Clinical Diagnostic Reasoning Engine
Orchestrates Red-Flag Gatekeeper, Bayesian Probabilistic Inference (4,920 cases),
Vector RAG Retrieval (535 protocols), and Structured Diagnostic Synthesis.
Outputs validated SOAP notes, ranked differential diagnoses, and diagnostic workups.
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
from app.services.bayesian_diagnostics import BayesianDiagnosticEngine
from app.services.gemini_reasoner import GeminiClinicalReasoner
from app.data.disease_precautions import get_precautions_for_condition
from app.services.severity_scorer import SymptomSeverityScorer
from app.core.config import settings


class ClinicalDiagnosticEngine:
    def __init__(self):
        self.retriever = MedicalVectorRetriever()
        self.bayesian_engine = BayesianDiagnosticEngine()
        self.gemini_reasoner = GeminiClinicalReasoner()

    async def assess(self, encounter: SymptomEncounterInput) -> VirtualDoctorAssessmentResponse:
        encounter_id = f"ENC-{uuid.uuid4().hex[:10].upper()}"
        now_iso = datetime.now(timezone.utc).isoformat()

        # Step 0: Objective Symptom Severity Scoring (Kaggle Weighting Matrix)
        text_corpus = f"{encounter.chief_complaint} {encounter.onset or ''} {encounter.quality_character or ''}"
        severity_info = SymptomSeverityScorer.evaluate(
            text_corpus,
            encounter.associated_symptoms
        )

        # Step 1: Immediate Red Flag Hard Rule Check (Deterministic Safety Layer)
        is_critical, red_flag, triage_level = RedFlagRuleEngine.evaluate(encounter)

        # Step 2: Bayesian Probabilistic Diagnostic Inference (Trained on 4,920 Kaggle cases)
        present_symptoms, negated_symptoms = self.bayesian_engine.extract_symptoms(
            text_corpus=f"{text_corpus} {' '.join(encounter.associated_symptoms)}",
            reported_symptoms=encounter.associated_symptoms,
            negatives_text=" ".join(encounter.pertinent_negatives) if encounter.pertinent_negatives else None
        )
        bayesian_differentials = self.bayesian_engine.diagnose(
            present_symptoms=present_symptoms,
            negated_symptoms=negated_symptoms,
            is_complete_profile=False,
            top_n=3
        )

        # Step 3: Okapi BM25 + Vector RAG Retrieval of Guidelines & ICD-10 Protocols
        search_terms = [encounter.chief_complaint, encounter.quality_character or ""]
        search_terms.extend(encounter.associated_symptoms)
        if bayesian_differentials:
            search_terms.append(bayesian_differentials[0]["diagnosis_name"])
            search_terms.append(bayesian_differentials[0]["icd10_code"])
        search_query = " ".join([t for t in search_terms if t])
        retrieved_docs = self.retriever.retrieve(search_query, top_k=3)

        if is_critical and red_flag:
            return self._build_emergency_response(
                encounter_id=encounter_id,
                timestamp=now_iso,
                encounter=encounter,
                red_flag=red_flag,
                retrieved_docs=retrieved_docs,
                bayesian_differentials=bayesian_differentials,
                severity_info=severity_info
            )

        # Step 4: LLM Cognitive Layer (Gemini with Bayesian Evidence and RAG Context)
        if self.gemini_reasoner.is_available:
            llm_result = await self.gemini_reasoner.reason(
                encounter=encounter,
                retrieved_guidelines=retrieved_docs,
                triage_level=triage_level,
                bayesian_differentials=bayesian_differentials
            )
            if llm_result:
                try:
                    return self._build_llm_response(
                        encounter_id=encounter_id,
                        timestamp=now_iso,
                        triage_level=triage_level,
                        data=llm_result,
                        severity_info=severity_info
                    )
                except Exception:
                    pass  # Fall back gracefully to deterministic clinical synthesizer

        # Step 5: Deterministic Grounded Synthesis (Reliable Baseline & Fallback)
        return self._synthesize_clinical_assessment(
            encounter_id=encounter_id,
            timestamp=now_iso,
            encounter=encounter,
            triage_level=triage_level,
            retrieved_docs=retrieved_docs,
            bayesian_differentials=bayesian_differentials,
            severity_info=severity_info,
        )

    def _build_llm_response(
        self,
        encounter_id: str,
        timestamp: str,
        triage_level: TriageLevel,
        data: Dict[str, Any],
        severity_info: Optional[Dict[str, Any]] = None,
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

        primary_dx = differentials[0].diagnosis_name if differentials else ""
        precautions = data.get("recommended_precautions")
        if not precautions or len(precautions) < 2:
            precautions = get_precautions_for_condition(primary_dx, triage_level.value)

        sev_score = severity_info.get("score", 5) if severity_info else None

        return VirtualDoctorAssessmentResponse(
            encounter_id=encounter_id,
            timestamp=timestamp,
            triage_level=triage_level,
            red_flag_alert=None,
            soap_note=soap,
            differential_diagnoses=differentials,
            recommended_workup=workup,
            recommended_specialty_clinic=data.get("recommended_specialty_clinic", "General Medicine"),
            recommended_precautions=precautions,
            severity_score=sev_score,
        )

    def _build_emergency_response(
        self,
        encounter_id: str,
        timestamp: str,
        encounter: SymptomEncounterInput,
        red_flag: RedFlagAlert,
        retrieved_docs: Optional[List[Dict[str, Any]]] = None,
        bayesian_differentials: Optional[List[Dict[str, Any]]] = None,
        severity_info: Optional[Dict[str, Any]] = None,
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
        emergency_terms = [w.lower() for w in red_flag.risk_category.split() if len(w) > 3]

        # 1. Identify primary emergency condition matching the critical alert
        matched_retrieved = None
        if retrieved_docs:
            for doc in retrieved_docs:
                doc_topic = doc.get("topic", "").lower()
                if any(t in doc_topic for t in emergency_terms):
                    matched_retrieved = doc
                    break

        matched_bayes = None
        if bayesian_differentials:
            for b in bayesian_differentials:
                b_topic = b.get("diagnosis_name", "").lower()
                if any(t in b_topic for t in emergency_terms):
                    matched_bayes = b
                    break

        if matched_retrieved:
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=matched_retrieved["topic"],
                    icd10_code=matched_retrieved.get("icd10", "R57.9"),
                    probability_rank=1,
                    confidence_score=0.95,
                    clinical_rationale=f"CRITICAL RED-FLAG ALERT: Acute presentation of '{red_flag.trigger_symptom}' correlates directly with life-threatening {matched_retrieved['topic']}.",
                    supporting_symptoms=[encounter.chief_complaint, red_flag.trigger_symptom],
                    pertinent_negatives_evaluated=matched_retrieved.get("pertinent_negatives", []),
                    citations_guidelines=[f"ICD-10 Emergency Protocol: {matched_retrieved.get('id', '')} - {matched_retrieved['topic']}"],
                )
            )
        elif matched_bayes:
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=matched_bayes["diagnosis_name"],
                    icd10_code=matched_bayes.get("icd10_code", "R57.9"),
                    probability_rank=1,
                    confidence_score=0.95,
                    clinical_rationale=f"CRITICAL RED-FLAG ALERT: Acute presentation of '{red_flag.trigger_symptom}' aligns with {matched_bayes['diagnosis_name']}.",
                    supporting_symptoms=[encounter.chief_complaint, red_flag.trigger_symptom],
                    pertinent_negatives_evaluated=matched_bayes.get("pertinent_negatives_evaluated", []),
                    citations_guidelines=[f"ICD-10 Emergency Protocol: {matched_bayes.get('icd10_code', '')} - {matched_bayes['diagnosis_name']}"],
                )
            )
        else:
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

        # 2. Append secondary and tertiary differential candidates
        candidate_docs = retrieved_docs or []
        for doc in candidate_docs:
            if len(differentials) >= 3:
                break
            if not any(d.diagnosis_name == doc["topic"] for d in differentials):
                differentials.append(
                    DifferentialDiagnosisItem(
                        diagnosis_name=doc["topic"],
                        icd10_code=doc.get("icd10", "R57.9"),
                        probability_rank=len(differentials) + 1,
                        confidence_score=max(0.60, round(0.85 - (len(differentials) * 0.10), 2)),
                        clinical_rationale=f"Considered as alternative / coexisting acute pathology in emergency differential.",
                        supporting_symptoms=[encounter.chief_complaint],
                        pertinent_negatives_evaluated=doc.get("pertinent_negatives", []),
                        citations_guidelines=[f"Clinical Protocol: {doc.get('id', '')}"],
                    )
                )

        if bayesian_differentials:
            for b in bayesian_differentials:
                if len(differentials) >= 3:
                    break
                if not any(d.diagnosis_name == b["diagnosis_name"] for d in differentials):
                    differentials.append(
                        DifferentialDiagnosisItem(
                            diagnosis_name=b["diagnosis_name"],
                            icd10_code=b["icd10_code"],
                            probability_rank=len(differentials) + 1,
                            confidence_score=max(0.50, b["confidence_score"]),
                            clinical_rationale=b.get("clinical_rationale", ""),
                            supporting_symptoms=b.get("supporting_symptoms", [encounter.chief_complaint]),
                            pertinent_negatives_evaluated=b.get("pertinent_negatives_evaluated", []),
                            citations_guidelines=[f"ICD-10 Protocol: {b['icd10_code']}"],
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

        precautions = get_precautions_for_condition(red_flag.risk_category, "EMERGENCY_RED")
        sev_score = max(8, severity_info.get("score", 9)) if severity_info else 9

        return VirtualDoctorAssessmentResponse(
            encounter_id=encounter_id,
            timestamp=timestamp,
            triage_level=TriageLevel.EMERGENCY_RED,
            red_flag_alert=red_flag,
            soap_note=soap,
            differential_diagnoses=differentials,
            recommended_workup=workup,
            recommended_specialty_clinic="Emergency Medicine / Acute Resuscitation Unit",
            recommended_precautions=precautions,
            severity_score=sev_score,
        )

    def _synthesize_clinical_assessment(
        self,
        encounter_id: str,
        timestamp: str,
        encounter: SymptomEncounterInput,
        triage_level: TriageLevel,
        retrieved_docs: List[Dict[str, Any]],
        bayesian_differentials: Optional[List[Dict[str, Any]]] = None,
        severity_info: Optional[Dict[str, Any]] = None,
    ) -> VirtualDoctorAssessmentResponse:
        differentials: List[DifferentialDiagnosisItem] = []
        workup: List[DiagnosticWorkupRecommendation] = []
        target_specialty = "General Medicine / Internal Medicine"
        precautions = []

        primary_retrieved = retrieved_docs[0] if retrieved_docs else None
        primary_bayes = bayesian_differentials[0] if bayesian_differentials else None

        # Determine whether retrieved protocol or Bayesian differential takes Rank 1:
        use_retrieved_top1 = False
        if primary_retrieved and primary_retrieved.get("score", 0) >= 38.0:
            if not primary_bayes or primary_bayes.get("confidence_score", 0) < 0.75:
                use_retrieved_top1 = True
            else:
                r_top = primary_retrieved.get("topic", "").lower()
                cardinal_surgical_or_acute = [
                    "appendicitis", "cholecystitis", "gastroenteritis", "nephrolithiasis",
                    "congestive heart failure", "anaphylaxis", "pulmonary embolism",
                    "sciatica", "radiculopathy", "asthma", "angina"
                ]
                if any(term in r_top for term in cardinal_surgical_or_acute):
                    use_retrieved_top1 = True

        if use_retrieved_top1 and primary_retrieved:
            target_specialty = primary_retrieved.get("specialty", "General Medicine / Internal Medicine")
            differentials.append(
                DifferentialDiagnosisItem(
                    diagnosis_name=primary_retrieved["topic"],
                    icd10_code=primary_retrieved.get("icd10", "R69"),
                    probability_rank=1,
                    confidence_score=min(0.95, round(0.70 + (primary_retrieved.get("score", 0) / 300.0), 2)),
                    clinical_rationale=f"Patient presentation of {encounter.chief_complaint} correlates with clinical hallmarks of {primary_retrieved['topic']}.",
                    supporting_symptoms=[encounter.chief_complaint] + encounter.associated_symptoms[:2],
                    pertinent_negatives_evaluated=encounter.pertinent_negatives[:2],
                    citations_guidelines=[f"ICD-10 Protocol: {primary_retrieved.get('id', '')} - {primary_retrieved['topic']}"],
                )
            )
            if len(retrieved_docs) > 1 and retrieved_docs[1].get("score", 0) >= 30.0:
                d2 = retrieved_docs[1]
                differentials.append(
                    DifferentialDiagnosisItem(
                        diagnosis_name=d2["topic"],
                        icd10_code=d2.get("icd10", "R69"),
                        probability_rank=2,
                        confidence_score=max(0.50, round(0.70 - (1 * 0.15), 2)),
                        clinical_rationale=f"Alternative differential consideration: {d2['topic']}.",
                        supporting_symptoms=[encounter.chief_complaint],
                        pertinent_negatives_evaluated=encounter.pertinent_negatives[:2],
                        citations_guidelines=[f"Clinical Protocol: {d2.get('id', '')}"],
                    )
                )
            if primary_bayes and not any(d.diagnosis_name == primary_bayes["diagnosis_name"] for d in differentials):
                differentials.append(
                    DifferentialDiagnosisItem(
                        diagnosis_name=primary_bayes["diagnosis_name"],
                        icd10_code=primary_bayes["icd10_code"],
                        probability_rank=len(differentials) + 1,
                        confidence_score=max(0.40, primary_bayes["confidence_score"]),
                        clinical_rationale=primary_bayes["clinical_rationale"],
                        supporting_symptoms=primary_bayes["supporting_symptoms"],
                        pertinent_negatives_evaluated=primary_bayes["pertinent_negatives_evaluated"],
                        citations_guidelines=[f"Bayesian Evidence: {primary_bayes['icd10_code']}"],
                    )
                )
            # Include disease-specific workup from primary retrieved doc if available
            workup = [
                DiagnosticWorkupRecommendation(
                    investigation_type="Specialized Clinical",
                    test_name=f"Focused Clinical Examination by {target_specialty}",
                    urgency="Priority" if triage_level == TriageLevel.URGENT_YELLOW else "Routine",
                    clinical_purpose=f"Correlate clinical presentation with physical signs of {primary_retrieved['topic']}.",
                ),
                DiagnosticWorkupRecommendation(
                    investigation_type="Laboratory",
                    test_name="Complete Blood Count (CBC) with Differential & Inflammatory Markers",
                    urgency="Priority" if triage_level == TriageLevel.URGENT_YELLOW else "Routine",
                    clinical_purpose="Assess leukocytosis and systemic inflammatory kinetics.",
                )
            ]
        elif bayesian_differentials:
            top_b = bayesian_differentials[0]
            target_specialty = top_b["specialty"]
            for b in bayesian_differentials[:3]:
                differentials.append(
                    DifferentialDiagnosisItem(
                        diagnosis_name=b["diagnosis_name"],
                        icd10_code=b["icd10_code"],
                        probability_rank=b["probability_rank"],
                        confidence_score=b["confidence_score"],
                        clinical_rationale=b["clinical_rationale"],
                        supporting_symptoms=b["supporting_symptoms"],
                        pertinent_negatives_evaluated=b["pertinent_negatives_evaluated"],
                        citations_guidelines=[f"ICD-10 Protocol: {b['icd10_code']} - {b['diagnosis_name']}"],
                    )
                )
            for w in top_b.get("recommended_workup", []):
                workup.append(
                    DiagnosticWorkupRecommendation(
                        investigation_type=w.get("investigation_type", "Laboratory"),
                        test_name=w.get("test_name", ""),
                        urgency=w.get("urgency", "Routine"),
                        clinical_purpose=w.get("clinical_purpose", ""),
                    )
                )
            precautions = top_b.get("recommended_precautions", [])

        elif retrieved_docs:
            primary_match = retrieved_docs[0]
            target_specialty = primary_match.get("specialty", "General Medicine / Internal Medicine")

            for i, doc in enumerate(retrieved_docs[:2]):
                differentials.append(
                    DifferentialDiagnosisItem(
                        diagnosis_name=doc["topic"],
                        icd10_code=doc.get("icd10", "R69"),
                        probability_rank=i + 1,
                        confidence_score=max(0.50, round(0.85 - (i * 0.20), 2)),
                        clinical_rationale=f"Patient presentation of {encounter.chief_complaint} correlates with {doc['topic']}.",
                        supporting_symptoms=[encounter.chief_complaint] + encounter.associated_symptoms[:2],
                        pertinent_negatives_evaluated=encounter.pertinent_negatives[:2],
                        citations_guidelines=[f"Clinical Protocol: {doc['id']}"],
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

        if not workup:
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

        if not precautions:
            primary_name = differentials[0].diagnosis_name if differentials else ""
            precautions = get_precautions_for_condition(primary_name, triage_level.value)

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

        sev_score = severity_info.get("score", 5) if severity_info else None

        return VirtualDoctorAssessmentResponse(
            encounter_id=encounter_id,
            timestamp=timestamp,
            triage_level=triage_level,
            red_flag_alert=None,
            soap_note=soap,
            differential_diagnoses=differentials,
            recommended_workup=workup,
            recommended_specialty_clinic=target_specialty,
            recommended_precautions=precautions,
            severity_score=sev_score,
        )

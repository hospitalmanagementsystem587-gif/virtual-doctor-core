"""
Instant Red-Flag Hard Rule Engine
Zero-LLM latency clinical rulebook for immediate emergency identification.
Evaluates high-acuity keywords and symptom patterns that require statutory emergency triage (Call 108 / ER).
"""

import re
from typing import Optional, Tuple
from app.schemas.encounter import RedFlagAlert, SymptomEncounterInput, TriageLevel


RED_FLAG_PATTERNS = [
    {
        "category": "Acute Coronary Syndrome / Myocardial Infarction",
        "pattern": r"\b(crushing chest pain|chest pressure|substernal|radiat(ing|es) to (jaw|left arm|shoulder)|sweating and chest pain)\b",
        "recommendation": "High risk of Acute Coronary Syndrome. Transfer immediately to emergency department. Obtain 12-lead ECG STAT.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Acute Stroke / Cerebrovascular Event (FAST Criteria)",
        "pattern": r"\b(facial droop|slurred speech|arm weakness|hemiparesis|sudden loss of vision|thunderclap headache|worst headache of my life)\b",
        "recommendation": "Suspected Acute Stroke or Subarachnoid Hemorrhage. Immediate emergency code FAST triage. Time-critical window for thrombolysis/imaging.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Severe Respiratory Distress / Airway Compromise",
        "pattern": r"\b(stridor|gasping|severe shortness of breath|unable to speak in full sentences|blue lips|cyanosis)\b",
        "recommendation": "Impaired airway or acute respiratory failure. Immediate oxygen therapy and emergency airway evaluation.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Severe Anaphylaxis",
        "pattern": r"\b(swelling of lips|swelling of tongue|throat tightness|throat closing|anaphylaxis|hives and breathing difficulty)\b",
        "recommendation": "Impending airway closure / Anaphylaxis. Intramuscular Epinephrine STAT required. Call 108 immediately.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Massive Hemorrhage or Shock",
        "pattern": r"\b(coughing up cup of blood|massive hemoptysis|vomiting blood|black tarry stool with dizziness|collapsed|unresponsive)\b",
        "recommendation": "Hemodynamic instability / severe gastrointestinal or pulmonary hemorrhage. Urgent resuscitation required.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Severe Acute Abdomen",
        "pattern": r"\b(rigid abdomen|board-like abdomen|rebound tenderness|sudden tearing abdominal pain)\b",
        "recommendation": "Suspected peritonitis, visceral perforation, or aortic dissection. Urgent surgical evaluation and IV access.",
        "level": TriageLevel.EMERGENCY_RED,
    },
]


class RedFlagRuleEngine:
    @staticmethod
    def evaluate(encounter: SymptomEncounterInput) -> Tuple[bool, Optional[RedFlagAlert], TriageLevel]:
        """
        Scans chief complaint, quality, radiation, and associated symptoms against verified red-flag patterns.
        Returns: (is_critical, alert_object, triage_level)
        """
        text_corpus = " ".join([
            encounter.chief_complaint or "",
            encounter.quality_character or "",
            encounter.radiation or "",
            " ".join(encounter.associated_symptoms or []),
        ]).lower()

        # Age and special risk modifier: elderly or known CAD with acute chest/epigastric distress
        is_elderly = encounter.patient.age >= 60
        has_cad = any("cad" in c.lower() or "heart" in c.lower() for c in encounter.patient.chronic_conditions)

        for rule in RED_FLAG_PATTERNS:
            match = re.search(rule["pattern"], text_corpus, re.IGNORECASE)
            if match:
                trigger = match.group(0)
                alert = RedFlagAlert(
                    is_critical=True,
                    trigger_symptom=trigger,
                    risk_category=rule["category"],
                    urgency_recommendation=rule["recommendation"],
                    emergency_call_action="108",
                )
                return True, alert, rule["level"]

        # Secondary rule: Severe pain (>= 9/10) with unexplained acute onset
        if encounter.severity_scale and encounter.severity_scale >= 9 and encounter.onset and "sudden" in encounter.onset.lower():
            alert = RedFlagAlert(
                is_critical=True,
                trigger_symptom="Severe sudden distress (Pain 9+/10)",
                risk_category="Hyperacute Severe Pain Protocol",
                urgency_recommendation="Acute high-grade pain requires prompt emergency triage to rule out ischemic or perforative etiology.",
                emergency_call_action="108",
            )
            return True, alert, TriageLevel.EMERGENCY_RED

        # Default: Ambulatory / Yellow / Green
        if encounter.severity_scale and encounter.severity_scale >= 6:
            return False, None, TriageLevel.URGENT_YELLOW

        return False, None, TriageLevel.ROUTINE_GREEN

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
        "pattern": r"(crushing chest pain|chest pressure|substernal|radiat(ing|es) to (jaw|left arm|shoulder)|sweating and chest pain|(seene|chhati|chaati)\s+me(n)?\s+.*?(dard|bhari|dabav)|(सीने|छाती)\s+में\s+.*?(दर्द|भारीपन|दबाव))",
        "recommendation": "High risk of Acute Coronary Syndrome. Transfer immediately to emergency department. Obtain 12-lead ECG STAT.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Acute Stroke / Cerebrovascular Event (FAST Criteria)",
        "pattern": r"(facial droop|slurred speech|arm weakness|hemiparesis|sudden loss of vision|thunderclap headache|worst headache of my life|muh tedha|bolne me(n)? dikkat|ek taraf ka hath|ek taraf kamzori|lakwa|achanak andha-?pan|मुंह टेढ़ा|बोलने में दिक्कत|लकवा|एक तरफ कमज़ोरी|अचानक नज़र जाना)",
        "recommendation": "Suspected Acute Stroke or Subarachnoid Hemorrhage. Immediate emergency code FAST triage. Time-critical window for thrombolysis/imaging.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Severe Respiratory Distress / Airway Compromise",
        "pattern": r"(stridor|gasping|severe shortness of breath|unable to speak in full sentences|blue lips|cyanosis|sans lene me(n)? bahut takleef|saans phool|dam ghut|saans ruk|सांस लेने में बहुत तकलीफ|सांस फूलना|दम घुटना|सांस रुकना)",
        "recommendation": "Impaired airway or acute respiratory failure. Immediate oxygen therapy and emergency airway evaluation.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Severe Anaphylaxis",
        "pattern": r"(swelling of lips|swelling of tongue|throat tightness|throat closing|anaphylaxis|hives and breathing difficulty|gala band ho raha|hoth sooj|jeebh sooj|गला बंद होना|होठों में सूजन|जीभ में सूजन)",
        "recommendation": "Impending airway closure / Anaphylaxis. Intramuscular Epinephrine STAT required. Call 108 immediately.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Diabetic Ketoacidosis / Severe Metabolic Crisis",
        "pattern": r"(kussmaul|fruity breath|sweet breath odor|sweet odor breath|severe dehydration with vomiting)",
        "recommendation": "Impending Diabetic Ketoacidosis (DKA) or hyperosmolar crisis. Immediate STAT intravenous fluids, blood glucose & blood gas evaluation.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Massive Hemorrhage or Shock",
        "pattern": r"(coughing up cup of blood|massive hemoptysis|vomiting blood|black tarry stool with dizziness|collapsed|unresponsive|khoon ki ulti|ulti me(n)? khoon|khansi me(n)? khoon|behosh|खून की उल्टी|उल्टी में खून|खांसी में खून|बेहोश)",
        "recommendation": "Hemodynamic instability / severe gastrointestinal or pulmonary hemorrhage. Urgent resuscitation required.",
        "level": TriageLevel.EMERGENCY_RED,
    },
    {
        "category": "Severe Acute Abdomen",
        "pattern": r"(rigid abdomen|board-like abdomen|sudden tearing abdominal pain|pet bilkul pathar jaisa|pet me(n)? achanak phatne jaisa dard|पेट बिल्कुल पत्थर जैसा|पेट में अचानक फटने जैसा दर्द)",
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

        # Secondary rule: Severe pain (>= 10/10) with unexplained sudden collapse or vascular tearing
        if encounter.severity_scale and encounter.severity_scale >= 10 and encounter.onset and "sudden" in encounter.onset.lower():
            # Exclude renal colic patterns from statutory red flag 108 transfer
            is_renal = any(k in text_corpus for k in ["flank", "groin", "urine", "kidney", "nephro"])
            if not is_renal:
                alert = RedFlagAlert(
                    is_critical=True,
                    trigger_symptom="Severe sudden distress (Pain 10/10)",
                    risk_category="Hyperacute Severe Pain Protocol",
                    urgency_recommendation="Acute high-grade pain requires prompt emergency triage to rule out ischemic or perforative etiology.",
                    emergency_call_action="108",
                )
                return True, alert, TriageLevel.EMERGENCY_RED

        # Default: Ambulatory / Yellow / Green
        if encounter.severity_scale and encounter.severity_scale >= 6:
            return False, None, TriageLevel.URGENT_YELLOW

        return False, None, TriageLevel.ROUTINE_GREEN

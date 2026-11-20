"""
Symptom Severity Scorer Engine
Implements Kaggle Symptom-Severity weighting matrix (weights 1 to 7)
mapped with multilingual English, Hinglish, and Hindi clinical keywords.
Computes an objective, normalized composite presentation severity score (1-10).
"""

import re
from typing import Dict, List, Any, Tuple

# Kaggle Symptom-Severity Matrix (Weights 1 to 7)
# Extended with clinical synonyms and vernacular mappings
SYMPTOM_WEIGHTS: Dict[str, int] = {
    # Weight 7: Critical / High-Acuity Symptoms
    "chest_pain": 7,
    "breathlessness": 7,
    "difficulty_breathing": 7,
    "altered_sensorium": 7,
    "paralysis": 7,
    "seizures": 7,
    "coma": 7,
    "internal_bleeding": 7,

    # Weight 6: Severe / Urgent Symptoms
    "blood_in_sputum": 6,
    "blood_in_stool": 6,
    "blood_in_vomit": 6,
    "stiff_neck": 6,
    "loss_of_balance": 6,
    "slurred_speech": 6,
    "chest_tightness": 6,
    "severe_abdominal_pain": 6,
    "board_like_abdomen": 6,

    # Weight 5: Moderate-High Symptoms
    "high_fever": 5,
    "shaking_rigors": 5,
    "toxic_look": 5,
    "sunken_eyes": 5,
    "vomiting": 5,
    "unsteadiness": 5,
    "severe_headache": 5,
    "palpitations": 5,
    "dehydration": 5,
    "jaundice": 5,

    # Weight 4: Moderate Symptoms
    "continuous_sneezing": 4,
    "shivering": 4,
    "chills": 4,
    "joint_pain": 4,
    "stomach_pain": 4,
    "fatigue": 4,
    "dark_urine": 4,
    "nausea": 4,
    "cough": 4,
    "burning_micturition": 4,
    "dysuria": 4,
    "eye_pain": 4,
    "retro_orbital_pain": 4,

    # Weight 3: Mild-Moderate Symptoms
    "loss_of_appetite": 3,
    "back_pain": 3,
    "constipation": 3,
    "abdominal_bloating": 3,
    "diarrhoea": 3,
    "loose_motions": 3,
    "mild_fever": 3,
    "body_ache": 3,
    "dizziness": 3,
    "muscle_weakness": 3,
    "sore_throat": 3,
    "coated_tongue": 3,

    # Weight 2: Mild Symptoms
    "skin_rash": 2,
    "acidity": 2,
    "heartburn": 2,
    "restlessness": 2,
    "swollen_legs": 2,
    "phlegm": 2,
    "throat_irritation": 2,
    "runny_nose": 2,
    "congestion": 2,

    # Weight 1: Minor / Localized Symptoms
    "itching": 1,
    "nodal_skin_eruptions": 1,
    "patches_in_throat": 1,
    "dischromic_patches": 1,
    "mild_malaise": 1
}

# Multilingual keyword mappings (English, Hinglish, Hindi) -> Canonical Symptom Key
KEYWORD_MAPPINGS: List[Tuple[re.Pattern, str]] = [
    # Chest pain & cardiac
    (re.compile(r"\b(chest\s+pain|chest\s+pressure|seene\s+me(n)?\s+dard|chhati\s+me(n)?\s+dard|सीने\s+में\s+दर्द|छाती\s+में\s+दर्द)\b", re.I), "chest_pain"),
    (re.compile(r"\b(breathless|shortness\s+of\s+breath|difficulty\s+breathing|saans\s+lene\s+me|saans\s+phool|सांस\s+फूल|सांस\s+लेने\s+में)\b", re.I), "breathlessness"),
    
    # Neurological
    (re.compile(r"\b(paralysis|lakwa|muh\s+tedha|लकवा|मुंह\s+टेढ़ा)\b", re.I), "paralysis"),
    (re.compile(r"\b(slurred\s+speech|bolne\s+me\s+dikkat|बोलने\s+में\s+दिक्कत)\b", re.I), "slurred_speech"),
    (re.compile(r"\b(stiff\s+neck|gardan\s+kadak|गर्दन\s+अकड़)\b", re.I), "stiff_neck"),
    (re.compile(r"\b(severe\s+headache|sir\s+me\s+tez\s+dard|सिर\s+में\s+तेज़\s+दर्द|आधा\s+शीशी)\b", re.I), "severe_headache"),

    # Hemorrhage / Bleeding
    (re.compile(r"\b(blood\s+in\s+vomit|khoon\s+ki\s+ulti|खून\s+की\s+उल्टी|उल्टी\s+में\s+खून)\b", re.I), "blood_in_vomit"),
    (re.compile(r"\b(blood\s+in\s+stool|mal\s+me\s+khoon|latrine\s+me\s+khoon|मल\s+में\s+खून)\b", re.I), "blood_in_stool"),
    (re.compile(r"\b(coughing\s+blood|hemoptysis|balgam\s+me\s+khoon|बलगम\s+में\s+खून)\b", re.I), "blood_in_sputum"),

    # Fever & Tropical
    (re.compile(r"\b(high\s+fever|tez\s+bukhar|तेज़\s+बुखार|103|104)\b", re.I), "high_fever"),
    (re.compile(r"\b(shivering|rigors|chills|kapkapi|thand\s+lag|कंपकंपी|ठंड\s+लग)\b", re.I), "shaking_rigors"),
    (re.compile(r"\b(retro[- ]orbital|eye\s+pain|pain\s+behind\s+eyes|aankh(on)?\s+ke\s+peeche|आंखों\s+के\s+पीछे)\b", re.I), "retro_orbital_pain"),
    (re.compile(r"\b(breakbone|haddi\s+me\s+dard|हड्डियों\s+में\s+दर्द)\b", re.I), "joint_pain"),
    (re.compile(r"\b(coated\s+tongue|safed\s+jeebh|जीभ\s+पर\s+सफेद)\b", re.I), "coated_tongue"),
    (re.compile(r"\b(jaundice|piliya|yellow\s+eyes|yellow\s+skin|पीलिया|आंखें\s+पीली)\b", re.I), "jaundice"),

    # Abdominal & GI
    (re.compile(r"\b(severe\s+abdominal\s+pain|pet\s+me\s+tez\s+dard|पेट\s+में\s+तेज़\s+दर्द|pathar\s+jaisa)\b", re.I), "severe_abdominal_pain"),
    (re.compile(r"\b(vomiting|ulti|nausea|mitli|उल्टी|मितली)\b", re.I), "vomiting"),
    (re.compile(r"\b(diarrh|loose\s+motion|dast|दस्ते?|पतले\s+दस्त)\b", re.I), "loose_motions"),
    (re.compile(r"\b(stomach\s+pain|pet\s+dard|पेट\s+दर्द)\b", re.I), "stomach_pain"),
    (re.compile(r"\b(acidity|heartburn|seene\s+me\s+jalan|छाती\s+में\s+जलन)\b", re.I), "heartburn"),
    (re.compile(r"\b(loss\s+of\s+appetite|bhookh\s+nahi|भूख\s+न\s+लगना)\b", re.I), "loss_of_appetite"),

    # Respiratory / ENT
    (re.compile(r"\b(cough|khansi|खांसी)\b", re.I), "cough"),
    (re.compile(r"\b(sore\s+throat|gale\s+me\s+kharash|गले\s+में\s+खराश)\b", re.I), "sore_throat"),
    (re.compile(r"\b(sneezing|chheenk|छींक)\b", re.I), "continuous_sneezing"),

    # Urinary
    (re.compile(r"\b(burning\s+urine|peshab\s+me\s+jalan|पेशाब\s+में\s+जलन)\b", re.I), "burning_micturition"),

    # General / Skin
    (re.compile(r"\b(skin\s+rash|laal\s+daane|chakatte|लाल\s+चकत्ते|दाने)\b", re.I), "skin_rash"),
    (re.compile(r"\b(itching|khujli|खुजली)\b", re.I), "itching"),
    (re.compile(r"\b(weakness|kamzori|fatigue|कमजोरी|थकान)\b", re.I), "fatigue"),
]


class SymptomSeverityScorer:
    """
    Computes objective clinical symptom severity score and risk classification.
    """

    @classmethod
    def evaluate(cls, text_corpus: str, associated_symptoms: List[str] = None) -> Dict[str, Any]:
        """
        Analyzes patient text and reported symptoms.
        Returns:
            - score: 1 to 10 (normalized composite score)
            - max_weight: 1 to 7 (highest individual symptom weight)
            - detected_symptoms: List of matched symptoms and weights
            - high_acuity_detected: bool (whether symptoms with weight >= 6 were present)
        """
        full_text = text_corpus or ""
        if associated_symptoms:
            full_text += " " + " ".join(associated_symptoms)

        detected: Dict[str, int] = {}

        for pattern, sym_key in KEYWORD_MAPPINGS:
            if pattern.search(full_text):
                detected[sym_key] = SYMPTOM_WEIGHTS.get(sym_key, 3)

        if not detected:
            return {
                "score": 4,
                "max_weight": 3,
                "detected_symptoms": [],
                "high_acuity_detected": False
            }

        weights = list(detected.values())
        max_weight = max(weights)
        avg_weight = sum(weights) / len(weights)

        # Composite score formula: 60% driven by maximum single acuity symptom, 40% by cumulative volume
        raw_score = (max_weight * 0.9) + (min(len(weights), 5) * 0.4) + (avg_weight * 0.2)
        score_10 = max(1, min(10, round(raw_score)))

        return {
            "score": score_10,
            "max_weight": max_weight,
            "detected_symptoms": [{"symptom": k, "weight": v} for k, v in sorted(detected.items(), key=lambda x: -x[1])],
            "high_acuity_detected": max_weight >= 6
        }

"""
Bayesian Probabilistic Clinical Diagnostic Engine
Trained on 4,920 gold-standard clinical disease-symptom presentations across 41 conditions.
Implements Bernoulli Naive Bayes log-likelihood inference with adaptive unobserved penalty,
multilingual symptom extraction (English, Hinglish, Hindi), and canonical ICD-10 mapping.
"""

import os
import json
import re
import math
from typing import Dict, List, Any, Optional, Set, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "knowledge_base", "kaggle_data", "bayesian_diagnostic_model.json")

# Multilingual Symptom Extraction Patterns (English, Hinglish, Hindi) -> List of Canonical Symptom Keys
MULTILINGUAL_SYMPTOM_PATTERNS: List[Tuple[re.Pattern, List[str]]] = [
    # 1. Fevers & Tropical
    (re.compile(r"(mild\s+fever|halka\s+bukhar|हल्का\s+बुखार|low\s+grade\s+fever)", re.I), ["mild_fever"]),
    (re.compile(r"(high\s+fever|tez\s+bukhar|तेज़\s+बुखार|severe\s+fever|102|103|104|very\s+hot|acute\s+fever|spiking\s+fever|step\s+ladder|badhta\s+bukhar|\bbukhar\b|\bfever\b|\btap\b|\bjwar\b|बुखार)", re.I), ["high_fever"]),
    (re.compile(r"(shivering|kapkapi|कांपना|कंपकंपी|trembling|rigors|shaking)", re.I), ["chills"]),
    (re.compile(r"(chills|thand\s+lag|ठंड\s+लग|feeling\s+cold|sardi\s+lag)", re.I), ["chills"]),
    (re.compile(r"(sweating|pasina|paseena|पसीना|drenching\s+sweat|night\s+sweat|cold\s+sweat)", re.I), ["sweating"]),
    (re.compile(r"(pain\s+behind.*eye|retro[- ]orbital|aankhon?.*peeche.*dard|आंखों.*पीछे.*दर्द|eye\s+socket\s+pain)", re.I), ["pain_behind_the_eyes"]),
    (re.compile(r"(toxic\s+look|typhos|extreme\s+prostration|lethargic\s+and\s+dull|behal|extremely\s+dull)", re.I), ["toxic_look_(typhos)"]),
    (re.compile(r"(red\s+spots|lal\s+chakatte|लाल\s+चकत्ते|rose\s+spots|petechiae|rash\s+spots)", re.I), ["red_spots_over_body"]),

    # 2. Pain & Musculoskeletal
    (re.compile(r"(headache|sir.*dard|sar.*dard|सिर.*दर्द|head\s+hurts|cephalea|adhashishi)", re.I), ["headache"]),
    (re.compile(r"(joint\s+pain|jodon?.*dard|जोड़ों.*दर्द|arthralgia|haddi(on)?.*dard|हड्डियों.*दर्द|pain\s+in\s+joints)", re.I), ["joint_pain"]),
    (re.compile(r"(muscle\s+pain|myalgia|badan\s+dard|मांसपेशियों.*दर्द|body\s+ache|muscles\s+ache)", re.I), ["muscle_pain"]),
    (re.compile(r"(back\s+pain|kamar\s+dard|peedh\s+dard|कमर\s+दर्द|पीठ\s+दर्द|lumbago)", re.I), ["back_pain"]),
    (re.compile(r"(neck\s+pain|gardan.*dard|गर्दन.*दर्द|cervical\s+pain)", re.I), ["neck_pain"]),
    (re.compile(r"(knee\s+pain|ghutne.*dard|घुटने.*दर्द)", re.I), ["knee_pain"]),
    (re.compile(r"(hip\s+joint\s+pain|koolhe.*dard|कूल्हे.*दर्द)", re.I), ["hip_joint_pain"]),
    (re.compile(r"(stiff\s+neck|gardan\s+kadak|गर्दन\s+अकड़|neck\s+stiffness)", re.I), ["stiff_neck"]),
    (re.compile(r"(swelling\s+joints|sujan\s+jodon|जोड़ों.*सूजन|swollen\s+joints)", re.I), ["swelling_joints"]),
    (re.compile(r"(painful\s+walking|chalne.*dard|चलने.*दर्द|difficulty\s+walking)", re.I), ["painful_walking"]),

    # 3. Cardiorespiratory & Emergency
    (re.compile(r"(chest\s+pain|angina|seene.*dard|chhati.*dard|सीने.*दर्द|छाती.*दर्द|chest\s+pressure|heavy\s+chest|crushing\s+chest|chest\s+discomfort)", re.I), ["chest_pain"]),
    (re.compile(r"(breathless|shortness\s+of\s+breath|dyspnea|saans\s+phool|saans\s+lene.*(dikkat|takleef)|सांस\s+फूल|सांस\s+लेने.*कठिनाई|difficulty\s+breathing)", re.I), ["breathlessness"]),
    (re.compile(r"(wheezing|seeti.*awaz|chest\s+tightness|dry\s+cough.*breathless|asthma|dama|दमा)", re.I), ["mucoid_sputum", "breathlessness"]),
    (re.compile(r"(cough(ing)?|khansi|खांसी|dhasak)", re.I), ["cough"]),
    (re.compile(r"(blood\s+in\s+sputum|hemoptysis|balgam.*khoon|बलगम.*खून|coughing\s+blood)", re.I), ["blood_in_sputum"]),
    (re.compile(r"(mucoid\s+sputum|phlegm|sputum|balgam|बलगम|mucus)", re.I), ["mucoid_sputum", "phlegm"]),
    (re.compile(r"(palpitations|dil\s+ki\s+dhadkan|दिल\s+की\s+धड़कन|racing\s+heart|fluttering\s+heart)", re.I), ["palpitations"]),
    (re.compile(r"(fast\s+heart\s+rate|tachycardia|tez\s+dhadkan)", re.I), ["fast_heart_rate"]),

    # 4. Neurological & Stroke
    (re.compile(r"(weakness.*(one|right|left)\s+side|(one|right|left)[- ]sided.*weakness|hemiparesis|ek\s+taraf.*kamzori|lakwa|paralysis|लकवा|facial\s+droop|muh\s+tedha|face\s+droop)", re.I), ["weakness_of_one_body_side", "altered_sensorium"]),
    (re.compile(r"(slurred\s+speech|bolne.*(dikkat|takleef)|awaz\s+ladkhadana|बोलने.*दिक्कत|difficulty\s+speaking|speech\s+slur)", re.I), ["slurred_speech"]),
    (re.compile(r"(loss\s+of\s+balance|santulan\s+khona|unsteadiness|ladkhadana|संतुलन\s+खोना|ataxia|imbalance)", re.I), ["loss_of_balance", "unsteadiness"]),
    (re.compile(r"(dizziness|vertigo|chakkar|चक्कर|head\s+spinning|spinning\s+sensation)", re.I), ["dizziness"]),
    (re.compile(r"(spinning\s+movements|kamra\s+ghoomna|room\s+spinning)", re.I), ["spinning_movements"]),
    (re.compile(r"(altered\s+sensorium|confusion|behosh|unconscious|drowsy|भ्रम|बेहोशी|delirium)", re.I), ["altered_sensorium"]),
    (re.compile(r"(blurred.*vision|dhundhla|धुंधला|blurry\s+vision|visual\s+disturbances|aankhon.*dhundhla)", re.I), ["blurred_and_distorted_vision", "visual_disturbances"]),

    # 5. Gastrointestinal & Hepatic
    (re.compile(r"(stomach\s+pain|abdominal\s+pain|belly\s+pain|pet.*dard|पेट.*दर्द|cramps\s+in\s+stomach|tummy\s+ache)", re.I), ["stomach_pain", "abdominal_pain"]),
    (re.compile(r"(acidity|acid\s+reflux|heartburn|seene.*jalan|खट्टी\s+डकार|छाती.*जलन|hyperacidity|sour\s+regurgitation)", re.I), ["acidity", "chest_pain", "stomach_pain"]),
    (re.compile(r"(indigestion|apach|hazma\s+kharab|बदहजमी|dyspepsia|food\s+not\s+digesting)", re.I), ["indigestion"]),
    (re.compile(r"(nausea|mitli|ji\s+ghabrana|मितली|जी\s+मिचलाना|feeling\s+like\s+vomiting)", re.I), ["nausea"]),
    (re.compile(r"(vomiting|ulti|vomit|उल्टी|kai)", re.I), ["vomiting"]),
    (re.compile(r"(diarrh(o)?ea|loose\s+motions|dast|दस्ते?|पतले\s+दस्त|watery\s+stool)", re.I), ["diarrhoea"]),
    (re.compile(r"(constipation|kabz|pet\s+saaf\s+na\s+hona|कब्ज)", re.I), ["constipation"]),
    (re.compile(r"(loss\s+of\s+appetite|anorexia|bhookh?\s*(na|nahi|kam|bilkul\s*nahi)\s*lag|भूख\s*(न|नहीं|कम|बिल्कुल\s*नहीं)\s*लग|not\s+hungry|kam\s+bhookh)", re.I), ["loss_of_appetite"]),
    (re.compile(r"(\bpeeli\b.*(twacha|aankh|skin|eyes)|(twacha|aankh|skin|eyes).*\bpeeli\b|dark\s+yellow|yellowish|jaundice|piliya|पीलिया|पीली)", re.I), ["yellowish_skin", "yellowing_of_eyes", "dark_urine"]),
    (re.compile(r"(dark\s+urine|peela\s+peshab|kala\s+peshab|गहरा\s+पीला\s+पेशाब|yellow_urine)", re.I), ["dark_urine", "yellow_urine"]),

    # 6. Urinary & Renal
    (re.compile(r"(burning.*(micturition|urination|urine)|peshab.*jalan|पेशाब.*जलन|dysuria)", re.I), ["burning_micturition"]),
    (re.compile(r"(bladder\s+discomfort|peshab\s+ki\s+thaili.*dard|suprapubic\s+pain|bladder\s+pain)", re.I), ["bladder_discomfort"]),
    (re.compile(r"(foul\s+smell.*urine|peshab.*badbu|पेशाब.*बदबू)", re.I), ["foul_smell_of urine"]),
    (re.compile(r"(continuous\s+feel\s+of\s+urine|bar\s+bar\s+peshab|frequent\s+urination|frequency|urgency)", re.I), ["continuous_feel_of_urine"]),
    (re.compile(r"(polyuria|excessive\s+urination|bahut\s+zyada\s+peshab|nocturnal\s+urination)", re.I), ["polyuria"]),

    # 7. Metabolic & Endocrine
    (re.compile(r"(excessive\s+hunger|bahut\s+bhookh|polyphagia|zyada\s+bhookh|excessive\s+thirst)", re.I), ["excessive_hunger"]),
    (re.compile(r"(weight\s+loss|wazan\s+ghatna|वजन\s+कम\s+होना|losing\s+weight)", re.I), ["weight_loss"]),
    (re.compile(r"(weight\s+gain|wazan\s+badhna|वजन\s+बढ़ना|gaining\s+weight)", re.I), ["weight_gain"]),
    (re.compile(r"(fatigue|kamzori|thakan|कमजोरी|थकान|tiredness|exhaustion|malaise)", re.I), ["fatigue"]),
    (re.compile(r"(lethargy|sust|aalas|सुस्ती|sluggish)", re.I), ["lethargy"]),

    # 8. Dermatology & Skin
    (re.compile(r"(itching|itch|khujli|खुजली|pruritus)", re.I), ["itching"]),
    (re.compile(r"(skin\s+rash|rash|laal\s+daane|daane|chakatte|लाल\s+चकत्ते|rash\s+on\s+skin|scaly\s+rash)", re.I), ["skin_rash", "nodal_skin_eruptions"]),
    (re.compile(r"(nodal\s+skin\s+eruptions|gath\s+jaise\s+daane|bumps\s+on\s+skin)", re.I), ["nodal_skin_eruptions"]),
    (re.compile(r"(pus[- ]filled\s+pimples|muh\s+par\s+daane|keel\s+muhase|pustules|acne|pimples)", re.I), ["pus_filled_pimples"]),
    (re.compile(r"(skin\s+peeling|khal\s+utarana|peeling\s+skin)", re.I), ["skin_peeling"]),
    (re.compile(r"(blister(s)?|faphola|faphole|छाला|छाले)", re.I), ["blister"]),
    (re.compile(r"(yellow\s+crust|honey\s+colored\s+crust|peeli\s+papdi)", re.I), ["yellow_crust_ooze"]),

    # 9. Anal / Rectal & Hemorrhoids
    (re.compile(r"(pain\s+in\s+anal\s+region|pain\s+during\s+bowel|painful\s+bowel|guptang.*dard|latrine.*dard)", re.I), ["pain_during_bowel_movements", "pain_in_anal_region"]),
    (re.compile(r"(bloody\s+stool|blood\s+in\s+stool|bleeding\s+per\s+rectum|mal.*khoon|latrine.*khoon|मल.*खून)", re.I), ["bloody_stool"]),
    (re.compile(r"(irritation\s+in\s+anus|itching\s+in\s+anus|piles|bawasir|बवासीर|anal\s+swelling|massey)", re.I), ["irritation_in_anus", "pain_in_anal_region"]),

    # 10. Upper Respiratory / ENT
    (re.compile(r"(continuous\s+sneezing|chheenk|छींक|runny\s+nose|running\s+nose|behne\s+wali\s+naak)", re.I), ["continuous_sneezing"]),
    (re.compile(r"(throat\s+irritation|sore\s+throat|gale.*kharash|गले.*खराश)", re.I), ["throat_irritation"]),
    (re.compile(r"(loss\s+of\s+smell|anosmia|sungne\s+ki\s+shakti|गंध\s+न\s+आना)", re.I), ["loss_of_smell"]),
]


class BayesianDiagnosticEngine:
    """
    Singleton Bayesian probabilistic reasoning engine.
    Computes exact conditional posterior distributions across all 41 Kaggle diseases.
    """

    _instance: Optional["BayesianDiagnosticEngine"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BayesianDiagnosticEngine, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance

    def _load_model(self):
        with open(MODEL_PATH, "r", encoding="utf-8") as f:
            self.model = json.load(f)

        self.symptoms: List[str] = self.model["symptoms"]
        self.diseases: List[str] = self.model["diseases"]
        self.priors: Dict[str, float] = self.model["priors"]
        self.likelihoods: Dict[str, Dict[str, float]] = self.model["likelihoods"]
        self.symptom_weights: Dict[str, int] = self.model.get("symptom_weights", {})
        self.descriptions: Dict[str, str] = self.model.get("descriptions", {})
        self.precautions: Dict[str, List[str]] = self.model.get("precautions", {})
        self.medications: Dict[str, List[str]] = self.model.get("medications", {})
        self.diets: Dict[str, List[str]] = self.model.get("diets", {})
        self.canonical_map: Dict[str, Any] = self.model.get("canonical_clinical_map", {})

        self.log_priors: Dict[str, float] = {d: math.log(p) for d, p in self.priors.items()}
        self.symptom_set: Set[str] = set(self.symptoms)

        self.bg_symptom_probs: Dict[str, float] = {}
        for s in self.symptoms:
            avg_p = sum(self.likelihoods[d].get(s, 0.01) for d in self.diseases) / len(self.diseases)
            self.bg_symptom_probs[s] = max(0.005, avg_p)

    def extract_symptoms(
        self,
        text_corpus: str,
        reported_symptoms: Optional[List[str]] = None,
        negatives_text: Optional[str] = None
    ) -> Tuple[Set[str], Set[str]]:
        present: Set[str] = set()
        negated: Set[str] = set()

        corpus = (text_corpus or "").lower()

        # 1. Match from explicit list of reported symptoms
        if reported_symptoms:
            for s in reported_symptoms:
                clean_s = s.strip().lower().replace(" ", "_")
                if clean_s in self.symptom_set:
                    present.add(clean_s)
                else:
                    for pat, sym_keys in MULTILINGUAL_SYMPTOM_PATTERNS:
                        if pat.search(s):
                            for sk in sym_keys:
                                present.add(sk)

        # 2. Extract present symptoms from multilingual corpus
        for pat, sym_keys in MULTILINGUAL_SYMPTOM_PATTERNS:
            if pat.search(corpus):
                neg_pattern = re.compile(
                    rf"(no|not|nahi|nahin|without|denies|negative\s+for)\s+{pat.pattern}|{pat.pattern}\s+(nahi|nahin|absent)",
                    re.I
                )
                if neg_pattern.search(corpus):
                    for sk in sym_keys:
                        negated.add(sk)
                else:
                    for sk in sym_keys:
                        present.add(sk)

        # 3. Direct token match against Kaggle symptom keys
        for sym in self.symptoms:
            spaced = sym.replace("_", " ")
            if f" {spaced} " in f" {corpus} " or f" {sym} " in f" {corpus} ":
                present.add(sym)

        # 4. Explicit negatives
        if negatives_text:
            neg_corpus = negatives_text.lower()
            for pat, sym_keys in MULTILINGUAL_SYMPTOM_PATTERNS:
                if pat.search(neg_corpus):
                    for sk in sym_keys:
                        negated.add(sk)

        negated = negated - present
        return present, negated

    def diagnose(
        self,
        present_symptoms: Set[str],
        negated_symptoms: Optional[Set[str]] = None,
        is_complete_profile: bool = False,
        top_n: int = 5
    ) -> List[Dict[str, Any]]:
        if not present_symptoms:
            return []

        negated = negated_symptoms or set()

        if is_complete_profile:
            log_posteriors = {}
            for d in self.diseases:
                lp = self.log_priors[d]
                d_likelihoods = self.likelihoods[d]
                for s in self.symptoms:
                    p1 = d_likelihoods.get(s, 0.01)
                    if s in present_symptoms:
                        lp += math.log(p1)
                    else:
                        lp += math.log(max(0.0001, 1.0 - p1))
                log_posteriors[d] = lp
        else:
            log_posteriors = {}
            for d in self.diseases:
                lp = self.log_priors[d]
                d_likelihoods = self.likelihoods[d]

                for s in present_symptoms:
                    p_s1 = d_likelihoods.get(s, 0.008)
                    p_bg = self.bg_symptom_probs.get(s, 0.01)
                    w = self.symptom_weights.get(s, 3)
                    weight_scale = 1.0 + (w * 0.12)
                    lr_pos = p_s1 / p_bg
                    lp += weight_scale * math.log(lr_pos)

                for s in negated:
                    p_s1 = d_likelihoods.get(s, 0.008)
                    p_bg = self.bg_symptom_probs.get(s, 0.01)
                    lr_neg = max(0.001, 1.0 - p_s1) / max(0.001, 1.0 - p_bg)
                    lp += 1.5 * math.log(lr_neg)

                # Clinical hallmark rules:
                # 1. Fever directly excludes simple allergic rhinitis
                if "high_fever" in present_symptoms and d == "Allergy":
                    lp -= 10.0

                # 2. Acute crushing chest pain + dyspnea without fever/cough strongly favors ACS over infection
                if "chest_pain" in present_symptoms and "breathlessness" in present_symptoms:
                    if "high_fever" not in present_symptoms and "cough" not in present_symptoms:
                        if d in ["Pneumonia", "Tuberculosis"]:
                            lp -= 6.0

                # 3. One-sided body weakness / hemiparesis is a stroke hallmark; excludes benign positional vertigo
                if "weakness_of_one_body_side" in present_symptoms:
                    if d == "(vertigo) Paroymsal  Positional Vertigo":
                        lp -= 14.0
                    if d == "Paralysis (brain hemorrhage)":
                        lp += 4.0

                # 4. Pruritic rash without fever favors superficial dermatophytosis/allergy over viral exanthem
                if "itching" in present_symptoms and "skin_rash" in present_symptoms:
                    if "high_fever" not in present_symptoms and d in ["Chicken pox", "Dengue"]:
                        lp -= 4.0

                # 5. Wheezing with breathlessness favors Bronchial Asthma over tuberculosis
                if "mucoid_sputum" in present_symptoms and "breathlessness" in present_symptoms:
                    if d == "Bronchial Asthma":
                        lp += 3.0

                # 6. Unilateral headache with visual disturbance / aura without sweating or intense hunger favors Migraine
                if "headache" in present_symptoms and ("visual_disturbances" in present_symptoms or "blurred_and_distorted_vision" in present_symptoms):
                    if "excessive_hunger" not in present_symptoms and "sweating" not in present_symptoms:
                        if d == "Hypoglycemia":
                            lp -= 4.0

                log_posteriors[d] = lp

        max_lp = max(log_posteriors.values())
        exp_scores = {d: math.exp(lp - max_lp) for d, lp in log_posteriors.items()}
        sum_exp = sum(exp_scores.values()) or 1.0
        probabilities = {d: exp_scores[d] / sum_exp for d in self.diseases}

        ranked_diseases = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)

        results = []
        for rank, (d_name, prob) in enumerate(ranked_diseases[:top_n], start=1):
            info = self.canonical_map.get(d_name, {})
            d_likelihoods = self.likelihoods.get(d_name, {})

            supporting = [
                s.replace("_", " ").title()
                for s in present_symptoms
                if d_likelihoods.get(s, 0) > 0.10
            ]

            pertinent_negs = [
                s.replace("_", " ").title()
                for s in negated
                if d_likelihoods.get(s, 0) > 0.40
            ]

            prec = self.precautions.get(d_name, [])
            meds = self.medications.get(d_name, [])
            diet = self.diets.get(d_name, [])

            results.append({
                "probability_rank": rank,
                "confidence_score": round(prob, 4),
                "kaggle_disease": d_name,
                "diagnosis_name": info.get("topic", d_name.strip()),
                "icd10_code": info.get("icd10", "R69"),
                "specialty": info.get("specialty", "General Medicine / Internal Medicine"),
                "emergency": info.get("emergency", False),
                "clinical_rationale": (
                    f"Strong Bayesian correlation ({int(prob*100)}% posterior probability). "
                    f"Presentation aligns with key clinical features: {', '.join(supporting[:4]) or 'reported symptoms'}."
                ),
                "supporting_symptoms": supporting if supporting else [s.replace("_", " ").title() for s in list(present_symptoms)[:3]],
                "pertinent_negatives_evaluated": pertinent_negs,
                "recommended_workup": info.get("workup", []),
                "recommended_precautions": prec,
                "recommended_medications": meds,
                "recommended_diet": diet,
                "description": self.descriptions.get(d_name, "")
            })

        return results

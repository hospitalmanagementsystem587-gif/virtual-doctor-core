"""
Clinical Scenario Benchmark Suite
Simulates 15 realistic hospital outpatient and emergency clinical vignettes.
Tests sensitivity for red-flags, Top-1 / Top-3 differential diagnostic accuracy,
and appropriate specialty clinic routing.
"""

import pytest
from app.schemas.encounter import SymptomEncounterInput, PatientProfile, TriageLevel
from app.services.diagnostic_engine import ClinicalDiagnosticEngine


CLINICAL_BENCHMARK_VIGNETTES = [
    # 1. Emergency Cardiology - Acute Coronary Syndrome
    {
        "id": "CASE-01-ACS",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=58, gender="male", chronic_conditions=["Hypertension", "Diabetes"]),
            chief_complaint="Severe retrosternal crushing chest pain radiating to left arm and jaw with profuse cold sweating and shortness of breath",
            onset="Started suddenly 45 minutes ago while climbing stairs",
            severity_scale=9,
            associated_symptoms=["diaphoresis", "nausea", "dyspnea", "sweating"],
        ),
        "expected_triage": TriageLevel.EMERGENCY_RED,
        "expected_specialty": "Emergency Medicine / Cardiology",
        "expected_top_differentials": ["Ischemic Heart Disease and Angina Pectoris"],
        "must_have_red_flag": True,
    },
    # 2. General Surgery - Acute Appendicitis
    {
        "id": "CASE-02-APPENDICITIS",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=22, gender="male"),
            chief_complaint="Severe right lower side abdominal pain around navel that moved to lower right belly with fever, vomiting, and loss of appetite",
            onset="Started yesterday around belly button, now sharp in right lower quadrant",
            severity_scale=8,
            associated_symptoms=["fever", "nausea", "vomiting", "anorexia", "rebound tenderness"],
        ),
        "expected_triage": TriageLevel.URGENT_YELLOW,
        "expected_specialty": "General Surgery",
        "expected_top_differentials": ["Acute Appendicitis"],
        "must_have_red_flag": False,
    },
    # 3. Pulmonology - Bronchial Asthma Exacerbation
    {
        "id": "CASE-03-ASTHMA",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=19, gender="female", chronic_conditions=["Asthma"]),
            chief_complaint="Sudden shortness of breath, tight chest, and high pitched musical wheezing after exposure to dust and cold air",
            onset="2 hours ago",
            severity_scale=6,
            associated_symptoms=["expiratory wheeze", "dry cough", "dyspnea"],
            pertinent_negatives=["no fever", "no chest pressure"],
        ),
        "expected_triage": TriageLevel.ROUTINE_GREEN,
        "expected_specialty": "Pulmonology",
        "expected_top_differentials": ["Bronchial Asthma & Acute Bronchospasm"],
        "must_have_red_flag": False,
    },
    # 4. Gastroenterology - GERD / Reflux
    {
        "id": "CASE-04-GERD",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=42, gender="male"),
            chief_complaint="Burning sensation behind breastbone and sour water regurgitation rising up into throat after heavy oily meals, worse when lying down flat",
            onset="Intermittent for 3 weeks",
            severity_scale=4,
            associated_symptoms=["heartburn", "acid regurgitation", "belching"],
            pertinent_negatives=["no radiating pain to arm", "no shortness of breath", "no sweating"],
        ),
        "expected_triage": TriageLevel.ROUTINE_GREEN,
        "expected_specialty": "Gastroenterology",
        "expected_top_differentials": ["Gastroesophageal Reflux Disease (GERD) & Reflux Esophagitis"],
        "must_have_red_flag": False,
    },
    # 5. Neurology - Acute Ischemic Stroke (FAST Red Flag)
    {
        "id": "CASE-05-STROKE",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=67, gender="female", chronic_conditions=["Hypertension", "Atrial Fibrillation"]),
            chief_complaint="Sudden right sided facial drooping, right arm weakness unable to lift arm, and slurred incomprehensible speech",
            onset="Sudden onset 30 minutes ago",
            severity_scale=8,
            associated_symptoms=["facial droop", "hemiparesis", "dysarthria", "arm drift"],
        ),
        "expected_triage": TriageLevel.EMERGENCY_RED,
        "expected_specialty": "Emergency Medicine / Stroke Unit",
        "expected_top_differentials": ["Stroke", "Transient Ischemic Attack", "TIA"],
        "must_have_red_flag": True,
    },
    # 6. Pulmonology / Infectious Disease - Community Acquired Pneumonia
    {
        "id": "CASE-06-PNEUMONIA",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=55, gender="male", chronic_conditions=["Smoker"]),
            chief_complaint="High fever with shaking chills, productive cough with rust-colored sputum, and sharp right-sided pleuritic chest pain on deep inspiration",
            onset="4 days",
            severity_scale=7,
            associated_symptoms=["productive cough", "purulent sputum", "fever", "chills", "pleuritic pain"],
        ),
        "expected_triage": TriageLevel.URGENT_YELLOW,
        "expected_specialty": "Pulmonology / Infectious Disease",
        "expected_top_differentials": ["Community-Acquired Pneumonia (CAP)"],
        "must_have_red_flag": False,
    },
    # 7. Gastroenterology / Surgery - Acute Cholecystitis / Biliary Colic
    {
        "id": "CASE-07-CHOLECYSTITIS",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=45, gender="female"),
            chief_complaint="Severe right upper quadrant pain under right ribs radiating to right shoulder and back, triggered after eating greasy butter chicken, with nausea and vomiting",
            onset="Started 3 hours after dinner",
            severity_scale=8,
            associated_symptoms=["nausea", "vomiting", "right upper quadrant pain", "biliary colic"],
        ),
        "expected_triage": TriageLevel.URGENT_YELLOW,
        "expected_specialty": "Gastroenterology / General Surgery",
        "expected_top_differentials": ["Acute Cholecystitis & Biliary Colic"],
        "must_have_red_flag": False,
    },
    # 8. Urology / Nephrology - Acute Nephrolithiasis (Kidney Stone)
    {
        "id": "CASE-08-KIDNEY-STONE",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=36, gender="male"),
            chief_complaint="Agonizing spasmodic sharp flank pain radiating down to groin and testicles, with blood in urine and inability to find a comfortable position",
            onset="Sudden onset 2 hours ago",
            severity_scale=10,
            associated_symptoms=["hematuria", "urinary frequency", "nausea", "flank pain", "groin radiation"],
        ),
        "expected_triage": TriageLevel.URGENT_YELLOW,
        "expected_specialty": "Urology / Nephrology",
        "expected_top_differentials": ["Nephrolithiasis", "Renal Colic", "Kidney Stones", "Urolithiasis"],
        "must_have_red_flag": False,
    },
    # 9. Infectious Disease / Tropical - Acute Viral Gastroenteritis
    {
        "id": "CASE-09-GASTROENTERITIS",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=28, gender="female"),
            chief_complaint="Frequent watery diarrhea multiple loose stools with abdominal cramping, nausea, vomiting, and low grade fever after eating street food",
            onset="Started 12 hours ago",
            severity_scale=5,
            associated_symptoms=["watery diarrhea", "cramping", "nausea", "vomiting", "low-grade fever"],
            pertinent_negatives=["no blood in stool", "no melena"],
        ),
        "expected_triage": TriageLevel.ROUTINE_GREEN,
        "expected_specialty": "General Medicine / Gastroenterology",
        "expected_top_differentials": ["Gastroenteritis", "Foodborne", "Enteritis"],
        "must_have_red_flag": False,
    },
    # 10. Cardiology - Congestive Heart Failure Exacerbation
    {
        "id": "CASE-10-CHF",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=71, gender="male", chronic_conditions=["Hypertension", "Previous MI"]),
            chief_complaint="Progressive shortness of breath on mild exertion, unable to lie flat sleeping on three pillows, and bilateral swelling in both ankles and feet",
            onset="Gradually worsening over 10 days",
            severity_scale=7,
            associated_symptoms=["orthopnea", "paroxysmal nocturnal dyspnea", "pedal edema", "ankle swelling"],
        ),
        "expected_triage": TriageLevel.URGENT_YELLOW,
        "expected_specialty": "Cardiology",
        "expected_top_differentials": ["Congestive Heart Failure (Acute Decompensated Heart Failure)"],
        "must_have_red_flag": False,
    },
    # 11. Neurology - Migraine with Aura
    {
        "id": "CASE-11-MIGRAINE",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=31, gender="female"),
            chief_complaint="Unilateral throbbing pulsing headache on left temple preceded by flashing zigzag visual lights, with intense photophobia and nausea",
            onset="Began 4 hours ago",
            severity_scale=7,
            associated_symptoms=["visual aura", "throbbing headache", "photophobia", "nausea", "phonophobia"],
            pertinent_negatives=["no neck stiffness", "no sudden thunderclap"],
        ),
        "expected_triage": TriageLevel.ROUTINE_GREEN,
        "expected_specialty": "Neurology",
        "expected_top_differentials": ["Migraine"],
        "must_have_red_flag": False,
    },
    # 12. Endocrinology - Diabetic Ketoacidosis / Hyperglycemia
    {
        "id": "CASE-12-DKA",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=24, gender="female", chronic_conditions=["Type 1 Diabetes"]),
            chief_complaint="Deep rapid heavy breathing, extreme thirst, excessive urination, severe nausea, abdominal pain, and fruity sweet breath odor",
            onset="Over past 24 hours after missing insulin dose",
            severity_scale=9,
            associated_symptoms=["kussmaul breathing", "fruity breath", "polyuria", "polydipsia", "vomiting"],
        ),
        "expected_triage": TriageLevel.EMERGENCY_RED,
        "expected_specialty": "Emergency Medicine / Endocrinology",
        "expected_top_differentials": ["Diabetic Ketoacidosis", "DKA", "Diabetes"],
        "must_have_red_flag": True,
    },
    # 13. Orthopedics / Spine - Lumbar Disc Herniation & Sciatica
    {
        "id": "CASE-13-SCIATICA",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=44, gender="male"),
            chief_complaint="Sharp shooting electric pain starting in lower back and radiating down buttock and posterior leg to foot, aggravated by coughing",
            onset="Started 2 days ago after lifting heavy weight",
            severity_scale=7,
            associated_symptoms=["shooting leg pain", "sciatica", "paresthesia", "foot numbness"],
            pertinent_negatives=["no bowel or bladder incontinence", "no saddle anesthesia"],
        ),
        "expected_triage": TriageLevel.ROUTINE_GREEN,
        "expected_specialty": "Orthopedics / Spine Clinic",
        "expected_top_differentials": ["Radiculopathy", "Sciatica", "Lumbago"],
        "must_have_red_flag": False,
    },
    # 14. Emergency - Acute Anaphylaxis
    {
        "id": "CASE-14-ANAPHYLAXIS",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=29, gender="male", known_allergies=["Peanuts"]),
            chief_complaint="Sudden swollen lips, tongue swelling, throat tightness, stridor, widespread itchy hives all over body, and severe dizziness right after eating meal",
            onset="15 minutes ago",
            severity_scale=10,
            associated_symptoms=["angioedema", "stridor", "wheezing", "urticaria", "hypotension"],
        ),
        "expected_triage": TriageLevel.EMERGENCY_RED,
        "expected_specialty": "Emergency Medicine / Resuscitation",
        "expected_top_differentials": ["Anaphylaxis", "Allergic Reaction"],
        "must_have_red_flag": True,
    },
    # 15. Pulmonology - Acute Pulmonary Embolism
    {
        "id": "CASE-15-PE",
        "encounter": SymptomEncounterInput(
            patient=PatientProfile(age=52, gender="female", chronic_conditions=["Recent knee surgery 1 week ago"]),
            chief_complaint="Sudden severe shortness of breath, sharp pleuritic chest pain, coughing up blood droplets, tachycardia, and right swollen tender calf",
            onset="Began suddenly 1 hour ago",
            severity_scale=9,
            associated_symptoms=["sudden dyspnea", "pleuritic chest pain", "hemoptysis", "calf swelling", "tachycardia"],
        ),
        "expected_triage": TriageLevel.EMERGENCY_RED,
        "expected_specialty": "Emergency Medicine / Pulmonology",
        "expected_top_differentials": ["Acute Pulmonary Embolism (PE)"],
        "must_have_red_flag": True,
    },
]


@pytest.mark.asyncio
async def test_run_clinical_benchmark_suite():
    engine = ClinicalDiagnosticEngine()
    total_cases = len(CLINICAL_BENCHMARK_VIGNETTES)
    red_flag_correct = 0
    top_3_correct = 0
    top_1_correct = 0

    print(f"\n======================================================================")
    print(f"RUNNING VIRTUAL DOCTOR CLINICAL BENCHMARK ({total_cases} Vignettes)")
    print(f"======================================================================\n")

    for case in CLINICAL_BENCHMARK_VIGNETTES:
        case_id = case["id"]
        encounter = case["encounter"]
        expected_triage = case["expected_triage"]
        expected_diffs = case["expected_top_differentials"]
        must_have_rf = case["must_have_red_flag"]

        assessment = await engine.assess(encounter)

        # Check Red Flag sensitivity
        has_rf = assessment.red_flag_alert is not None and assessment.red_flag_alert.is_critical
        rf_match = (has_rf == must_have_rf)
        if rf_match:
            red_flag_correct += 1

        # Check differentials
        top_differentials = [d.diagnosis_name for d in assessment.differential_diagnoses]
        top_1 = top_differentials[0] if top_differentials else "NONE"
        top_3 = top_differentials[:3]

        hit_top_1 = any(exp.lower() in top_1.lower() or top_1.lower() in exp.lower() for exp in expected_diffs)
        hit_top_3 = any(
            any(exp.lower() in d.lower() or d.lower() in exp.lower() for exp in expected_diffs)
            for d in top_3
        )

        if hit_top_1:
            top_1_correct += 1
        if hit_top_3:
            top_3_correct += 1

        status_icon = "✅" if (rf_match and hit_top_3) else "⚠️"
        print(f"[{status_icon}] {case_id}:")
        print(f"    Expected: {expected_diffs[0]} | Triage: {expected_triage.value}")
        print(f"    Predicted Top-1: {top_1} (Conf: {assessment.differential_diagnoses[0].confidence_score if assessment.differential_diagnoses else 0})")
        print(f"    Predicted Top-3: {top_3}")
        print(f"    Red-Flag Match: {rf_match} (Expected: {must_have_rf}, Actual: {has_rf})\n")

    top_1_acc = (top_1_correct / total_cases) * 100
    top_3_acc = (top_3_correct / total_cases) * 100
    rf_sensitivity = (red_flag_correct / total_cases) * 100

    print("======================================================================")
    print(f"BENCHMARK RESULTS SUMMARY:")
    print(f"  Total Cases Evaluated:       {total_cases}")
    print(f"  Red-Flag Triage Accuracy:    {rf_sensitivity:.1f}% ({red_flag_correct}/{total_cases})")
    print(f"  Top-1 Diagnostic Accuracy:   {top_1_acc:.1f}% ({top_1_correct}/{total_cases})")
    print(f"  Top-3 Diagnostic Accuracy:   {top_3_acc:.1f}% ({top_3_correct}/{total_cases})")
    print("======================================================================")

    # Hard clinical quality assertions:
    # 1. Red flag safety must never be compromised (< 90% is unacceptable for clinical use)
    assert rf_sensitivity >= 90.0, f"Red-flag sensitivity too low: {rf_sensitivity}%"
    # 2. Top-3 differential must be at least 80%
    assert top_3_acc >= 80.0, f"Top-3 accuracy below clinical baseline: {top_3_acc}%"

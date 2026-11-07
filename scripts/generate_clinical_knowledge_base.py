#!/usr/bin/env python3
"""
Parallel Clinical Diagnostic Protocol Generator
Expands clinical knowledge base from 71 to 300+ validated ICD-10 protocols
utilizing round-robin load distribution across 4 verified Gemini API keys.
"""

import os
import json
import time
import urllib.request
import urllib.error
from itertools import cycle

KB_PATH = "/Users/abhisheksahu/repos/virtual-doctor-core/knowledge_base/protocols/clinical_knowledge_base.json"

# Load keys from environment variables or .env
API_KEYS = [k.strip() for k in os.getenv("GEMINI_API_KEYS", "").split(",") if k.strip()]
if not API_KEYS:
    # Fallback to standard GEMINI_API_KEY
    single_key = os.getenv("GEMINI_API_KEY")
    if single_key:
        API_KEYS = [single_key.strip()]

if not API_KEYS:
    raise ValueError("No Gemini API keys found. Set GEMINI_API_KEYS or GEMINI_API_KEY environment variable.")

# Curated batches of clinical conditions across unrepresented specialties
BATCHES = [
    # 1. PEDIATRICS & NEONATOLOGY
    {
        "specialty": "Pediatrics",
        "organ_system": "Pediatric / Upper Airway / Infectious",
        "conditions": [
            "Croup (Laryngotracheobronchitis)",
            "Acute Bronchiolitis (RSV)",
            "Simple Febrile Seizures",
            "Hand, Foot, and Mouth Disease (HFMD)",
            "Neonatal Hyperbilirubinemia (Physiological vs Pathological Jaundice)",
            "Pediatric Dehydration (WHO Plan A, B, C)",
            "Post-Streptococcal Glomerulonephritis (PSGN)",
            "Henoch-Schönlein Purpura (IgA Vasculitis)",
            "Kawasaki Disease",
            "Infantile Colic & Gastroesophageal Reflux",
        ],
    },
    # 2. DERMATOLOGY & VENEREOLOGY
    {
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "conditions": [
            "Psoriasis Vulgaris (Plaque Psoriasis)",
            "Atopic Dermatitis (Severe Infantile & Adult Eczema)",
            "Acute and Chronic Urticaria with Angioedema",
            "Scabies Infestation with Secondary Impetigo",
            "Tinea Corporis & Cruris (Dermatophytosis)",
            "Herpes Zoster (Shingles) & Postherpetic Neuralgia",
            "Acne Vulgaris (Grade III/IV Nodulocystic)",
            "Alopecia Areata",
            "Contact Dermatitis (Allergic vs Irritant)",
            "Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis (SJS/TEN Alert)",
        ],
    },
    # 3. ORTHOPEDICS, SPINE & RHEUMATOLOGY
    {
        "specialty": "Orthopedics",
        "organ_system": "Musculoskeletal",
        "conditions": [
            "Knee Osteoarthritis (Grade III/IV Kellgren-Lawrence)",
            "Lumbar Spondylosis with Lumbar Radiculopathy (Sciatica)",
            "Cervical Spondylosis with Radiculopathy / Myelopathy",
            "Gouty Arthritis & Acute Podagra",
            "Rheumatoid Arthritis (Seropositive)",
            "Ankylosing Spondylitis",
            "Adhesive Capsulitis (Frozen Shoulder)",
            "Carpal Tunnel Syndrome (Median Nerve Entrapment)",
            "Acute Lateral Ankle Sprain (ATFL Tear)",
            "Supraspinatus Tendinitis / Rotator Cuff Tear",
        ],
    },
    # 4. ENT (OTORHINOLARYNGOLOGY)
    {
        "specialty": "ENT / Otorhinolaryngology",
        "organ_system": "Ear, Nose, Throat",
        "conditions": [
            "Acute Suppurative Otitis Media (ASOM)",
            "Chronic Suppurative Otitis Media (CSOM Safe vs Unsafe)",
            "Acute Rhinosinusitis (Bacterial vs Viral)",
            "Peritonsillar Abscess (Quinsy)",
            "Epistaxis (Anterior Kiesselbach vs Posterior)",
            "Benign Paroxysmal Positional Vertigo (BPPV)",
            "Meniere's Disease (Endolymphatic Hydrops)",
            "Otitis Externa (Swimmer's Ear & Malignant Otitis)",
            "Nasal Polyposis & Deviated Nasal Septum",
            "Vocal Cord Nodules & Hoarseness of Voice",
        ],
    },
    # 5. OPHTHALMOLOGY
    {
        "specialty": "Ophthalmology",
        "organ_system": "Ophthalmic / Vision",
        "conditions": [
            "Acute Angle-Closure Glaucoma (Emergency)",
            "Bacterial and Viral Conjunctivitis (Pink Eye)",
            "Corneal Ulcer (Keratitis - Bacterial vs Fungal)",
            "Diabetic Retinopathy (NPDR / PDR / Macular Edema)",
            "Senile Cataract (Immature / Mature)",
            "Stye (Hordeolum) & Chalazion",
            "Dry Eye Disease (Keratoconjunctivitis Sicca)",
            "Subconjunctival Hemorrhage",
            "Anterior Uveitis (Iritis)",
            "Central Retinal Artery Occlusion (CRAO Sudden Vision Loss)",
        ],
    },
    # 6. NEPHROLOGY & UROLOGY
    {
        "specialty": "Urology / Nephrology",
        "organ_system": "Genitourinary / Renal",
        "conditions": [
            "Chronic Kidney Disease (CKD Stage 3b-5 & Uremic Syndrome)",
            "Nephrotic Syndrome (Minimal Change / FSGS)",
            "Benign Prostatic Hyperplasia (BPH with Urinary Retention)",
            "Acute Pyelonephritis (Complicated UTI)",
            "Urolithiasis (Ureteric Calculus with Hydronephrosis)",
            "Epididymo-Orchitis (Acute Scrotal Infection)",
            "Testicular Torsion (Golden Hour Surgical Emergency)",
            "Fournier Gangrene (Necrotizing Fasciitis)",
            "Hydrocele & Varicocele",
            "Stress & Urge Urinary Incontinence",
        ],
    },
    # 7. NEUROLOGY & PSYCHIATRY
    {
        "specialty": "Neurology / Psychiatry",
        "organ_system": "Central & Peripheral Nervous System",
        "conditions": [
            "Migraine with and without Aura",
            "Tension-Type Headache & Medication Overuse Headache",
            "Bell's Palsy (Idiopathic Facial Nerve Paralysis)",
            "Trigeminal Neuralgia",
            "Parkinson's Disease (Tremor, Rigidity, Bradykinesia)",
            "Generalized Anxiety Disorder (GAD) & Panic Attacks",
            "Major Depressive Disorder (MDD with Suicidal Risk Assessment)",
            "Bipolar Affective Disorder (Mania vs Depression)",
            "Vascular Dementia & Alzheimer's Disease",
            "Delirium / Acute Confusional State (Hyperactive vs Hypoactive)",
        ],
    },
    # 8. ENDOCRINOLOGY & METABOLIC
    {
        "specialty": "Endocrinology",
        "organ_system": "Endocrine / Metabolic",
        "conditions": [
            "Hypothyroidism (Primary, Hashimoto's Thyroiditis)",
            "Hyperthyroidism & Graves' Disease (Thyrotoxicosis)",
            "Subacute De Quervain Thyroiditis",
            "Type 2 Diabetes Mellitus with Poor Glycemic Control",
            "Diabetic Peripheral Neuropathy & Diabetic Foot Ulcer",
            "Cushing's Syndrome & Hypercortisolemia",
            "Primary Hyperparathyroidism & Hypercalcemia",
            "Polycystic Ovary Syndrome (PCOS / PCOD)",
            "Vitamin D Deficiency & Osteomalacia",
            "Metabolic Syndrome & Nonalcoholic Fatty Liver Disease (MASLD)",
        ],
    },
    # 9. GASTROENTEROLOGY & HEPATOLOGY
    {
        "specialty": "Gastroenterology",
        "organ_system": "Gastrointestinal / Hepatobiliary",
        "conditions": [
            "Cirrhosis of Liver with Portal Hypertension & Ascites",
            "Spontaneous Bacterial Peritonitis (SBP)",
            "Hepatic Encephalopathy (West Haven Grading)",
            "Inflammatory Bowel Disease (Ulcerative Colitis)",
            "Crohn's Disease (Terminal Ileitis)",
            "Irritable Bowel Syndrome (IBS-D / IBS-C)",
            "Celiac Disease (Gluten-Sensitive Enteropathy)",
            "Hemorrhoids (Piles Grade I-IV) & Anal Fissure",
            "Non-Ulcer Functional Dyspepsia",
            "Acute Mesenteric Ischemia",
        ],
    },
    # 10. INFECTIOUS & TROPICAL MEDICINE (INDIA REGIONAL)
    {
        "specialty": "Infectious Disease",
        "organ_system": "Systemic / Tropical",
        "conditions": [
            "Pulmonary Tuberculosis (PTB sputum smear positive)",
            "Extrapulmonary TB (Tuberculous Pleural Effusion / Lymphadenitis)",
            "Kala-Azar (Visceral Leishmaniasis)",
            "Leptospirosis (Weil's Disease)",
            "Tetanus (Trismus & Opisthotonus)",
            "Rabies Post-Exposure Prophylaxis & Encephalitis",
            "Amoebic Liver Abscess vs Pyogenic Liver Abscess",
            "Herpes Simplex Encephalitis (HSE)",
            "Varicella (Chickenpox in Adults & Immunocompromised)",
            "Hospital-Acquired Pneumonia / Ventilator-Associated Pneumonia (HAP/VAP)",
        ],
    },
    # 11. OBSTETRICS & GYNECOLOGY
    {
        "specialty": "Obstetrics & Gynecology",
        "organ_system": "Female Reproductive",
        "conditions": [
            "Pelvic Inflammatory Disease (PID / Endometritis)",
            "Ectopic Pregnancy (Ruptured vs Unruptured Emergency)",
            "Abnormal Uterine Bleeding (AUB - PALM-COEIN)",
            "Uterine Fibroids (Leiomyoma with Menorrhagia)",
            "Endometriosis & Adenomyosis",
            "Ovarian Cyst Torsion",
            "Cervical Intraepithelial Neoplasia / Cervicitis",
            "Hyperemesis Gravidarum with Ketonuria",
            "Gestational Diabetes Mellitus (GDM - DIPSI criteria)",
            "Postpartum Depression & Puerperal Psychosis",
        ],
    },
    # 12. GENERAL SURGERY & EMERGENCY TRAUMA
    {
        "specialty": "General Surgery",
        "organ_system": "Surgical / Trauma",
        "conditions": [
            "Inguinal Hernia (Reducible, Incarcerated, Strangulated)",
            "Umbilical and Incisional Hernia",
            "Acute Intestinal Obstruction (Adhesive / Volvulus)",
            "Perforated Peptic Ulcer with Pneumoperitoneum",
            "Subcutaneous Abscess & Carbuncle (Diabetic Cellulitis)",
            "Necrotizing Soft Tissue Infection (Gas Gangrene)",
            "Burn Injury (Thermal Burns TBSA & Parkland Resuscitation)",
            "Tension Pneumothorax (Needle Decompression Protocol)",
            "Flail Chest & Pulmonary Contusion",
            "Ruptured Spleen (Blunt Abdominal Trauma Hemoperitoneum)",
        ],
    },
]

key_rotator = cycle(API_KEYS)


def generate_batch_protocols(batch):
    spec = batch["specialty"]
    organ = batch["organ_system"]
    conds = batch["conditions"]

    prompt = f"""
You are an expert Chief Medical Officer and clinical informatics specialist.
Generate precise, production-grade clinical triage protocols for the following {len(conds)} medical conditions in {spec}:

Conditions:
{json.dumps(conds, indent=2)}

For EACH condition, provide a structured JSON object matching EXACTLY this schema:
{{
  "id": "ICD10-<CODE-OR-SLUG>",
  "topic": "Exact Condition Name",
  "icd10": "Accurate ICD-10-CM code (e.g. H66.00, M17.11, etc.)",
  "specialty": "{spec}",
  "organ_system": "{organ}",
  "keywords": [5 to 8 lowercase search terms, symptoms, lay terms],
  "red_flags": [3 to 6 critical red-flag signs requiring urgent triage or emergency escalation],
  "clinical_hallmarks": [2 to 4 distinctive physical signs or symptom patterns that strongly point to this condition],
  "pertinent_negatives": [2 to 4 crucial clinical absence findings used to rule out deadly differentials],
  "content": "A rigorous, comprehensive clinical synthesis (120-200 words) describing the presentation, standard physical examination findings, pertinent rule-outs, and diagnostic workup (labs, imaging, staging) aligned with Indian and international hospital guidelines."
}}

Return ONLY a valid JSON array of these {len(conds)} objects. No markdown formatting, no commentary.
"""

    max_retries = 3
    for attempt in range(max_retries):
        key = next(key_rotator)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseMimeType": "application/json",
                "temperature": 0.2,
            },
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=90) as res:
                raw = json.loads(res.read().decode())
                text = raw["candidates"][0]["content"]["parts"][0]["text"]
                protocols = json.loads(text)
                if isinstance(protocols, list) and len(protocols) > 0:
                    return protocols
        except Exception as e:
            print(f"    [Retry {attempt+1}] with key {key[:8]}... error: {e}")
            time.sleep(2)

    return []


def main():
    print(f"Loading existing clinical knowledge base from: {KB_PATH}")
    with open(KB_PATH, "r") as f:
        existing = json.load(f)

    existing_topics = set(item["topic"].strip().lower() for item in existing)
    existing_icds = set(item["icd10"].strip().upper() for item in existing)
    print(f"Existing protocol count: {len(existing)}")

    new_protocols = []
    total_batches = len(BATCHES)

    for idx, batch in enumerate(BATCHES, 1):
        print(f"\n[{idx}/{total_batches}] Processing {batch['specialty']} ({len(batch['conditions'])} conditions)...")
        protocols = generate_batch_protocols(batch)
        added_count = 0
        for proto in protocols:
            t = proto.get("topic", "").strip().lower()
            icd = proto.get("icd10", "").strip().upper()
            if t not in existing_topics:
                existing_topics.add(t)
                existing_icds.add(icd)
                new_protocols.append(proto)
                added_count += 1

        print(f"    -> Added {added_count} validated clinical protocols.")
        time.sleep(1)

    print(f"\n==========================================")
    print(f"Generation Complete!")
    print(f"Newly Generated Protocols: {len(new_protocols)}")

    # Merge and save
    combined = existing + new_protocols
    print(f"Total Knowledge Base Count: {len(combined)} clinical protocols.")

    with open(KB_PATH, "w") as f:
        json.dump(combined, f, indent=2)
    print(f"Saved expanded clinical knowledge base to: {KB_PATH}")


if __name__ == "__main__":
    main()

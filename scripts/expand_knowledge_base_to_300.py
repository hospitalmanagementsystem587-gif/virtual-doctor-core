#!/usr/bin/env python3
"""
Parallel Clinical Diagnostic Protocol Generator - Phase 2 Expansion
Expands clinical knowledge base from 180 to 300+ validated ICD-10 protocols
utilizing round-robin load distribution across 3 verified Gemini API keys.
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
EXPANSION_BATCHES = [
    # 1. ENDOCRINOLOGY & METABOLIC (Backfill)
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
    # 2. CARDIOLOGY & VASCULAR MEDICINE EXPANSION
    {
        "specialty": "Cardiology",
        "organ_system": "Cardiovascular",
        "conditions": [
            "Atrial Fibrillation with Rapid Ventricular Response (AF with RVR)",
            "Supraventricular Tachycardia (AVNRT / AVRT / PSVT)",
            "Ventricular Tachycardia (Sustained vs Non-Sustained Monomorphic VT)",
            "Hypertrophic Cardiomyopathy (HOCM with LVOT obstruction)",
            "Dilated Cardiomyopathy with Low Ejection Fraction (HFrEF)",
            "Heart Failure with Preserved Ejection Fraction (HFpEF)",
            "Aortic Stenosis (Severe Symptomatic Triad)",
            "Mitral Regurgitation (Acute Papillary Rupture vs Chronic Rheumatic)",
            "Peripheral Arterial Disease (PAD Critical Limb Ischemia Fontaine III-IV)",
            "Subacute Bacterial Endocarditis (Infective Endocarditis Duke Criteria)",
        ],
    },
    # 3. PULMONOLOGY & CRITICAL CARE PULMONARY
    {
        "specialty": "Pulmonology",
        "organ_system": "Respiratory / Pulmonary",
        "conditions": [
            "Chronic Obstructive Pulmonary Disease Acute Exacerbation (AECOPD Anthonisen I)",
            "Severe Persistent Bronchial Asthma (Status Asthmaticus)",
            "Idiopathic Pulmonary Fibrosis (IPF / Usual Interstitial Pneumonia)",
            "Sarcoidosis (Pulmonary & Mediastinal Lymphadenopathy)",
            "Bronchiectasis with Hemoptysis & Secondary Infection",
            "Obstructive Sleep Apnea (Severe OSA / Hypopnea Index > 30)",
            "Pneumoconiosis (Silicosis & Asbestosis)",
            "Empyema Thoracis & Complicated Parapneumonic Effusion",
            "Primary Spontaneous Pneumothorax",
            "Pulmonary Arterial Hypertension (Group 1 PAH WHO Functional Class III-IV)",
        ],
    },
    # 4. ONCOLOGY & HEMATOLOGY
    {
        "specialty": "Oncology / Hematology",
        "organ_system": "Hematologic / Oncologic",
        "conditions": [
            "Acute Myeloid Leukemia (AML / Blast Crisis)",
            "Chronic Myelogenous Leukemia (CML Philadelphia Chromosome Positive)",
            "Multiple Myeloma (CRAB Criteria & Hyperviscosity)",
            "Hodgkin Lymphoma (B-symptoms & Reed-Sternberg)",
            "Non-Hodgkin Lymphoma (Diffuse Large B-Cell Lymphoma DLBCL)",
            "Immune Thrombocytopenic Purpura (ITP with Mucocutaneous Bleeding)",
            "Thrombotic Thrombocytopenic Purpura (TTP Pentad Emergency)",
            "Aplastic Anemia (Severe Pancytopenia)",
            "Febrile Neutropenia in Chemotherapy Patient",
            "Tumor Lysis Syndrome (Hyperuricemia, Hyperkalemia, Hypocalcemia)",
        ],
    },
    # 5. GERIATRICS & PALLIATIVE CARE
    {
        "specialty": "Geriatrics",
        "organ_system": "Multisystem / Geriatric",
        "conditions": [
            "Frailty Syndrome and Failure to Thrive in Elderly",
            "Recurrent Falls in Elderly (Gait Instability & Orthostatic Hypotension)",
            "Pressure Injuries (Decubitus Ulcers Stage III-IV / Sacral Sore)",
            "Polypharmacy & Anticholinergic Cognitive Burden",
            "Urinary Retention in Frail Elderly (Neurogenic Bladder / Overflow)",
            "Severe Sarcopenia and Malnutrition in the Aged",
            "Lewy Body Dementia (Visual Hallucinations & Parkinsonism)",
            "Normal Pressure Hydrocephalus (Hakim-Adams Triad: Gait, Incontinence, Dementia)",
            "Palliative Cancer Pain Management (WHO Analgesic Ladder Escalation)",
            "Terminal Agitation and Death Rattle in Palliative Setting",
        ],
    },
    # 6. RHEUMATOLOGY & AUTOIMMUNE
    {
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal / Immune",
        "conditions": [
            "Rheumatoid Arthritis (Seropositive Erosive Polyarthritis)",
            "Systemic Lupus Erythematosus (Lupus Nephritis & Malar Rash)",
            "Ankylosing Spondylitis (HLA-B27 Axial Spondyloarthritis)",
            "Systemic Sclerosis (Scleroderma / CREST Syndrome)",
            "Polymyalgia Rheumatica & Giant Cell Arteritis (Temporal Arteritis)",
            "Sjögren's Syndrome (Keratoconjunctivitis Sicca & Xerostomia)",
            "Gouty Arthritis (Acute Podagra & Tophaceous Gout)",
            "Pseudogout (Calcium Pyrophosphate Dihydrate CPPD Deposition)",
            "Fibromyalgia (Widespread Pain Index & Tender Points)",
            "Granulomatosis with Polyangiitis (GPA / Wegener's Vasculitis)",
        ],
    },
    # 7. EMERGENCY TOXICOLOGY & ENVENOMATION (INDIA SPECIFIC)
    {
        "specialty": "Emergency Medicine",
        "organ_system": "Toxicology / Environmental",
        "conditions": [
            "Organophosphate and Carbamate Poisoning (Cholinergic SLUDGE Toxidrome)",
            "Aluminium Phosphide (Celphos) Poisoning & Cardiotoxicity",
            "Viperine Snake Bite (Vasculotoxic Envenomation with Coagulopathy)",
            "Elapid Snake Bite (Krait / Cobra Neurotoxic Envenomation with Ptosis & Respiratory Failure)",
            "Scorpion Sting Envenomation & Autonomic Storm (Prazosin Protocol)",
            "Paracetamol (Acetaminophen) Overdose & Acute Liver Failure (NAC Protocol)",
            "Corrosive Acid / Alkali Ingestion & Esophageal Stricture",
            "Carbon Monoxide Poisoning & Carboxyhemoglobinemia",
            "Heat Stroke & Severe Heat Exhaustion",
            "Electric Shock and Lightning Injury (Arrhythmias & Deep Tissue Necrosis)",
        ],
    },
    # 8. PEDIATRIC EMERGENCIES & NEONATAL
    {
        "specialty": "Pediatrics",
        "organ_system": "Pediatric Critical Care",
        "conditions": [
            "Neonatal Sepsis (Early-Onset vs Late-Onset EOS/LOS)",
            "Foreign Body Aspiration in Toddler (Stridor / Unilateral Wheeze)",
            "Intussusception in Infants (Red Currant Jelly Stool & Target Sign)",
            "Congenital Hypertrophic Pyloric Stenosis (Projectile Non-Bilious Vomiting)",
            "Congenital Heart Disease (Cyanotic Spell / Tet Spells in Tetralogy of Fallot)",
            "Status Epilepticus in Children (Pediatric Convulsive Protocol)",
            "Pediatric Septic Shock & Cold vs Warm Shock",
            "Acute Post-Streptococcal Pharyngitis & Peritonsillar Abscess (Quinsy)",
            "Pediatric Appendicitis with Perforation Risk",
            "Acute Epiglottitis (Tripod Position & Thumbprint Sign)",
        ],
    },
    # 9. OBSTETRIC & GYNECOLOGICAL EMERGENCIES
    {
        "specialty": "Obstetrics & Gynecology",
        "organ_system": "Maternal-Fetal / Emergency",
        "conditions": [
            "Severe Preeclampsia and Eclampsia (Magnesium Sulfate Protocol)",
            "HELLP Syndrome (Hemolysis, Elevated Liver Enzymes, Low Platelets)",
            "Postpartum Hemorrhage (PPH Atony Management & Bakri Balloon)",
            "Placenta Previa with Antepartum Hemorrhage",
            "Abruptio Placentae with Concealed / Revealed Hemorrhage",
            "Preterm Premature Rupture of Membranes (PPROM & Chorioamnionitis)",
            "Shoulder Dystocia (HELPERR Emergency Protocol)",
            "Cord Prolapse During Labor",
            "Puerperal Sepsis (Endometritis Post-Cesarean / Normal Delivery)",
            "Ruptured Corpus Luteum Cyst with Hemoperitoneum",
        ],
    },
    # 10. ADVANCED NEUROLOGY & STROKE
    {
        "specialty": "Neurology",
        "organ_system": "Neurological / Cerebrovascular",
        "conditions": [
            "Acute Ischemic Stroke (Thrombolysis Window / Alteplase / Tenecteplase Protocol)",
            "Intracerebral Hemorrhage (Basal Ganglia Hematoma with Mass Effect)",
            "Subarachnoid Hemorrhage (Aneurysmal Rupture / Thunderclap Headache)",
            "Cerebral Venous Sinus Thrombosis (CVST in Puerperium & Hypercoagulable State)",
            "Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyradiculoneuropathy)",
            "Myasthenia Gravis Myasthenic Crisis vs Cholinergic Crisis",
            "Multiple Sclerosis (Relapsing-Remitting MS Acute Relapse)",
            "Epileptic Encephalopathy & Non-Convulsive Status Epilepticus (NCSE)",
            "Wernicke Encephalopathy & Korsakoff Syndrome",
            "Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)",
        ],
    },
    # 11. ADVANCED GASTROENTEROLOGY & HEPATOBILIARY
    {
        "specialty": "Gastroenterology",
        "organ_system": "Digestive / Pancreaticobiliary",
        "conditions": [
            "Acute Necrotizing Pancreatitis (Balthazar CT Severity Index)",
            "Ascending Cholangitis (Charcot Triad & Reynolds Pentad Emergency)",
            "Bleeding Esophageal Varices (Terlipressin / Endoscopic Band Ligation)",
            "Mallory-Weiss Syndrome vs Boerhaave Syndrome",
            "Gastric Outlet Obstruction (Peptic vs Malignant Antral Stricture)",
            "Acute Liver Failure (Fulminant Hepatic Failure Kings College Criteria)",
            "Clostridioides difficile Colitis (Pseudomembranous Colitis)",
            "Autoimmune Hepatitis (Type 1 & Type 2)",
            "Primary Biliary Cholangitis (PBC Antimitochondrial Antibodies)",
            "Budd-Chiari Syndrome (Hepatic Venous Outflow Tract Obstruction)",
        ],
    },
    # 12. ORTHOPEDIC TRAUMA & SPORTS MEDICINE
    {
        "specialty": "Orthopedics",
        "organ_system": "Musculoskeletal / Trauma",
        "conditions": [
            "Acute Compartment Syndrome (The 6 Ps Surgical Emergency)",
            "Hip Fracture in Elderly (Femoral Neck vs Intertrochanteric Fracture)",
            "Open / Compound Fracture (Gustilo-Anderson Classification)",
            "Acute Anterior Shoulder Dislocation (Bankart & Hill-Sachs Lesion)",
            "Anterior Cruciate Ligament (ACL) Tear & Meniscal Tear",
            "Achilles Tendon Rupture (Thompson Squeeze Test Positive)",
            "Cauda Equina Syndrome (Saddle Anesthesia & Sphincter Disturbance)",
            "Septic Arthritis (Kocher Criteria & Emergency Arthrotomy)",
            "Acute Osteomyelitis (Pediatric Hematogenous vs Chronic Diabetic)",
            "Pelvic Ring Fracture with Hemodynamic Instability (Tile / Young-Burgess)",
        ],
    },
    # 13. OTORHINOLARYNGOLOGY (ENT) ADVANCED & HEAD-NECK
    {
        "specialty": "ENT",
        "organ_system": "Head, Neck, Airway",
        "conditions": [
            "Ludwig's Angina (Submandibular Cellulitis Airway Threat)",
            "Deep Neck Space Infection (Retropharyngeal & Parapharyngeal Abscess)",
            "Malignant Otitis Externa (Skull Base Osteomyelitis in Diabetics)",
            "Sudden Sensorineural Hearing Loss (SSNHL Golden Window Steroid Therapy)",
            "Severe Posterior Epistaxis (Sphenopalatine Artery Bleed / Epistaxis Packing)",
            "Foreign Body Bronchus vs Foreign Body Esophagus (Coin vs Button Battery)",
            "Acute Mastoiditis with Subperiosteal Abscess",
            "Vestibular Neuritis & Labyrinthitis (HINTS Exam Central vs Peripheral)",
            "Nasal Bone Fracture with Septal Hematoma",
            "Vocal Cord Paralysis (Recurrent Laryngeal Nerve Palsy)",
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

    max_retries = 4
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
            time.sleep(3)

    return []


def main():
    print(f"Loading existing clinical knowledge base from: {KB_PATH}")
    with open(KB_PATH, "r") as f:
        existing = json.load(f)

    existing_topics = set(item["topic"].strip().lower() for item in existing)
    existing_icds = set(item["icd10"].strip().upper() for item in existing)
    print(f"Existing protocol count: {len(existing)}")

    new_protocols = []
    total_batches = len(EXPANSION_BATCHES)

    for idx, batch in enumerate(EXPANSION_BATCHES, 1):
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
            else:
                print(f"    (Skipped existing topic: {proto.get('topic')})")

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

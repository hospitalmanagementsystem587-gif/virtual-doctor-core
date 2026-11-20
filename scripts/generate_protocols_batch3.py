#!/usr/bin/env python3
"""
Batch 3: Endocrinology, Hematology/Oncology, Rheumatology, Infectious Diseases.
"""

import json
import os

KB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "knowledge_base",
    "protocols",
    "clinical_knowledge_base.json"
)

PROTOCOLS_TO_ADD = [
    # --- 6. ENDOCRINOLOGY & METABOLISM (12) ---
    {
        "id": "ICD10-C74.10",
        "topic": "Pheochromocytoma (Catecholamine Paroxysms & 10% Rule)",
        "icd10": "C74.10",
        "specialty": "Endocrinology / Endocrine Surgery / Cardiology",
        "organ_system": "Endocrine / Adrenal Neoplasm",
        "keywords": ["pheochromocytoma", "paroxysmal hypertension", "triad headache sweating tachycardia", "plasma free metanephrines", "rule of 10 pheochromocytoma", "phenoxybenzamine"],
        "red_flags": ["malignant hypertensive crisis (sbp > 220 mmHg, encephalopathy)", "catecholamine cardiomyopathy / acute pulmonary edema", "perioperative hemodynamic collapse if beta-blocked alone"],
        "clinical_hallmarks": ["the classic symptom triad during paroxysms: 1. Pounding, severe headache; 2. Profuse diaphoresis (drenching sweats); 3. Palpitations with marked tachycardia", "severe, paroxysmal or sustained refractory hypertension", "attacks last minutes to hours, accompanied by severe pallor, tremulousness, and impending doom sensation", "precipitated by postural change, abdominal palpation, urination (bladder paraganglioma), or drugs (beta-blockers, metoclopramide)", "the famous '10% Rule': 10% bilateral, 10% extra-adrenal (paragangliomas), 10% malignant, 10% familial (MEN-2A/2B, VHL, NF-1)"],
        "pertinent_negatives": ["CARDINAL RULE: NEVER ADMINISTER BETA-BLOCKERS BEFORE ADEQUATE ALPHA-BLOCKADE (avoids unopposed alpha-adrenergic vasoconstriction and fatal hypertensive crisis)"],
        "content": "Catecholamine-secreting tumor arising from chromaffin cells of the adrenal medulla (or sympathetic paraganglia). Diagnostic gold standard: Fractionated Plasma Free Metanephrines (high sensitivity > 97%) or 24-hour urinary fractionated metanephrines and catecholamines; Localization: Contrast CT/MRI abdomen, 123I-MIBG scan or 68Ga-DOTATATE PET-CT. Preoperative Medical Optimization (MANDATORY): Non-competitive alpha-blockade (Phenoxybenzamine 10 mg BID titrated for 10-14 days) PLUS high-salt diet and hydration; Beta-blocker (Propranolol) added ONLY AFTER full alpha-blockade achieved. Definitive cure: Laparoscopic adrenalectomy."
    },
    {
        "id": "ICD10-E10.10",
        "topic": "Diabetic Ketoacidosis (DKA - High Anion Gap Ketosis)",
        "icd10": "E10.10",
        "specialty": "Endocrinology / Emergency Medicine / Critical Care",
        "organ_system": "Metabolic Emergency",
        "keywords": ["diabetic ketoacidosis", "dka", "kussmaul breathing", "fruity acetone breath", "high anion gap acidosis ketones", "potassium in dka", "iv insulin fluid resuscitation"],
        "red_flags": ["cerebral edema (especially in pediatric patients receiving rapid fluids)", "fatal hypokalemic cardiac arrest during insulin infusion", "severe hypovolemic shock"],
        "clinical_hallmarks": ["classic diagnostic triad: 1. Hyperglycemia (blood glucose > 250 mg/dL, though euglycemic DKA can occur with SGLT2 inhibitors); 2. High anion gap metabolic acidosis (arterial/venous pH < 7.30, serum bicarbonate < 18 mEq/L, anion gap > 10-12); 3. Positive serum and urine ketones (beta-hydroxybutyrate > 3.0 mmol/L)", "clinical signs: rapid, deep sighing Kussmaul respirations (respiratory compensation blowing off CO2), sweet fruity acetone breath odor, diffuse abdominal pain mimicking surgical abdomen, nausea, vomiting, and profound dehydration (sunken eyes, dry mucous membranes, tachycardia, hypotension)"],
        "pertinent_negatives": ["anion gap is elevated (distinguishes from non-anion gap metabolic acidosis)"],
        "content": "Life-threatening acute metabolic complication of diabetes (predominantly Type 1, but occurs in Type 2 under severe stress/infection) characterized by absolute insulin deficiency and counter-regulatory hormone excess. Protocol (Order of Operations): 1. Aggressive IV Fluid Resuscitation (0.9% Normal Saline 1-1.5 L in 1st hour, switch to 0.45% NaCl based on corrected sodium); 2. POTASSIUM MANAGEMENT FIRST: If serum K+ < 3.3 mEq/L, HOLD INSULIN and give IV KCl until K+ > 3.3; if K+ 3.3-5.2, add 20-30 mEq KCl per liter of IV fluid; 3. IV Regular Insulin infusion (0.1 units/kg/hr); 4. Add 5% Dextrose when glucose reaches 200-250 mg/dL to prevent hypoglycemia while clearing ketoacidosis (continue insulin until anion gap closes and bicarbonate > 18)."
    },
    {
        "id": "ICD10-E11.00",
        "topic": "Hyperosmolar Hyperglycemic State (HHS - Extreme Osmolality)",
        "icd10": "E11.00",
        "specialty": "Endocrinology / Emergency Medicine / Critical Care",
        "organ_system": "Metabolic Emergency",
        "keywords": ["hyperosmolar hyperglycemic state", "hhs", "honk", "extreme hyperglycemia > 600", "effective serum osmolality > 320", "profound dehydration elderly diabetic", "altered mental status hhs"],
        "red_flags": ["arterial / venous thromboembolism from extreme hyperviscosity", "hypovolemic cardiovascular collapse", "septic shock trigger (pneumonia, uti)"],
        "clinical_hallmarks": ["predominantly occurs in elderly Type 2 diabetic patients, evolving insidiously over days to weeks", "diagnostic triad: 1. Extreme, profound hyperglycemia (plasma glucose > 600 mg/dL, often 800-1200 mg/dL); 2. High effective serum osmolality (> 320 mOsm/kg); 3. Absence of significant ketoacidosis (arterial pH > 7.30, serum bicarbonate > 18 mEq/L, negative or trace ketones)", "massive fluid deficit (typically 8 to 12 Liters / 100-200 mL/kg): severe hypotension, skin turgor loss, dry axillae, tachycardia", "prominent neurological impairment directly correlating with osmolality: lethargy, confusion, hemichorea, focal seizures, and deep coma"],
        "pertinent_negatives": ["absence of significant ketoacidosis (endogenous basal insulin is sufficient to suppress lipolysis and ketogenesis but insufficient for glucose uptake)"],
        "content": "Acute metabolic crisis of Type 2 diabetes with severe hyperglycemia, hyperosmolality, and profound dehydration without substantial ketosis. Mortality is 10-20% (significantly higher than DKA). Emergency Management: 1. MASSIVE, CAREFUL FLUID REHYDRATION is the single most critical intervention (0.9% Normal Saline initially, switching to 0.45% Saline based on corrected sodium, replacing estimated 9L deficit over 24-48 hours); 2. Low-dose IV Regular Insulin (0.05-0.1 units/kg/hr) initiated only AFTER aggressive fluid resuscitation has started; 3. Vigorous potassium replacement; 4. Prophylactic LMWH anticoagulation (hyperosmolality induces extreme thrombophilia)."
    },
    {
        "id": "ICD10-E05.00",
        "topic": "Graves' Disease & Thyroid Eye Disease (TSHR Antibodies)",
        "icd10": "E05.00",
        "specialty": "Endocrinology / Ophthalmology",
        "organ_system": "Endocrine Autoimmune",
        "keywords": ["graves disease", "thyrotoxicosis", "thyroid eye disease", "exophthalmos proptosis", "pretibial myxedema", "trab antibodies", "thyroid bruit"],
        "red_flags": ["thyroid storm (hyperpyrexia, atrial fibrillation, delirium)", "dysthyroid optic neuropathy (compressive blindness)", "malignant arrhythmias"],
        "clinical_hallmarks": ["signs of hyperthyroidism: heat intolerance, unexplained weight loss despite ravenous appetite, fine resting hand tremor, hyperdefecation, palpitations, emotional lability", "diffusely enlarged, smooth, non-tender goiter with an AUDIBLE SYSTOLIC BRUIT AND PALPABLE THRILL over the superior thyroid poles", "Graves' Orbitopathy / Exophthalmos (pathognomonic): bilateral proptosis, eyelid retraction (Dalrymple sign), lid lag on downgaze (von Graefe sign), periorbital edema, and diplopia from extraocular muscle enlargement", "Pretibial Myxedema (thyroid dermopathy): non-pitting, orange-peel, violaceous indurated plaques over the anterior shins", "laboratory hallmark: completely suppressed TSH (< 0.01 mIU/L), elevated Free T4 and Free T3, and positive Thyroid-Stimulating Immunoglobulin (TSI / TRAb in > 98%)"],
        "pertinent_negatives": ["radioactive iodine uptake (RAIU) shows diffuse, homogeneous high uptake (distinguishes from thyroiditis or toxic adenoma)"],
        "content": "Autoimmune disorder caused by circulating autoantibodies (TRAb/TSI) directed against the thyroid follicular TSH receptor, stimulating autonomous thyroid hormone hypersecretion and follicular hyperplasia. Treatment: 1. Beta-blockers (Propranolol 20-40 mg TID) for immediate adrenergic symptom relief; 2. Thionamides (Antithyroid drugs): Methimazole (10-30 mg daily) or Propylthiouracil (PTU - preferred in first trimester of pregnancy and thyroid storm); 3. Radioactive Iodine (RAI - 131I) ablation; 4. Total or near-total Thyroidectomy; Active moderate-to-severe orbitopathy: IV Methylprednisolone or Teprotumumab (IGF-1R inhibitor)."
    },
    {
        "id": "ICD10-E03.9",
        "topic": "Hashimoto's Thyroiditis & Myxedema Coma",
        "icd10": "E03.9",
        "specialty": "Endocrinology / Critical Care / Primary Care",
        "organ_system": "Endocrine Autoimmune",
        "keywords": ["hashimotos thyroiditis", "hypothyroidism", "myxedema coma", "anti tpo antibodies", "cold intolerance weight gain", "delayed deep tendon reflexes", "levothyroxine"],
        "red_flags": ["myxedema coma (hypothermia, bradycardia, hypoventilation, coma)", "pericardial effusion", "severe hyponatremia"],
        "clinical_hallmarks": ["clinical hypothyroidism: extreme cold intolerance, generalized lethargy, constipation, unexplained weight gain, coarse dry skin, thinning hair (loss of outer third of eyebrows / Hertoghe sign), and hoarse voice", "pathognomonic reflex sign: DELAYED RELAXATION PHASE OF DEEP TENDON REFLEXES ('hung-up' ankle jerk / Woltman sign)", "physical exam: firm, painless, rubbery, lobulated goiter or completely atrophic thyroid gland", "Myxedema Coma (medical emergency): profound hypothermia (< 35C / 95F), bradycardia, hypoventilation with hypercapnia, severe non-pitting periorbital and facial myxedematous edema, and progressive stupor/coma", "laboratory hallmarks: elevated serum TSH, low Free T4, and high titers of Anti-Thyroperoxidase (Anti-TPO in > 95%) and Anti-Thyroglobulin (Anti-Tg) antibodies"],
        "pertinent_negatives": ["no thyroid pain or tenderness (distinguishes from subacute de Quervain's thyroiditis)"],
        "content": "Chronic autoimmune thyroiditis mediated by cytotoxic T-cells and autoantibodies causing autoimmune destruction of thyroid follicular cells and progressive fibrotic atrophy. Most common cause of hypothyroidism in iodine-sufficient areas. Treatment: Standard Hypothyroidism: Oral Levothyroxine (T4: 1.6 mcg/kg/day, lower starting dose 25-50 mcg in elderly/coronary disease) taken fasting 30-60 min before breakfast; Myxedema Coma (ICU emergency): STAT IV Hydrocortisone (100 mg IV q8h to cover concomitant adrenal insufficiency BEFORE thyroid hormone), followed by IV Levothyroxine (200-400 mcg IV loading dose) +/- IV Liothyronine (T3), passive rewarming, and mechanical ventilation."
    },
    {
        "id": "ICD10-E22.0",
        "topic": "Acromegaly & Pituitary Growth Hormone Adenoma",
        "icd10": "E22.0",
        "specialty": "Endocrinology / Neurosurgery",
        "organ_system": "Pituitary / Neuroendocrine",
        "keywords": ["acromegaly", "growth hormone adenoma", "increased shoe hat ring size", "prognathism coarse facies", "igf 1 elevated", "bitemporal hemianopsia pituitary", "glucose suppression test"],
        "red_flags": ["bitemporal hemianopsia from optic chiasm compression", "cardiomyopathy / congestive heart failure", "obstructive sleep apnea with respiratory failure"],
        "clinical_hallmarks": ["insidious, progressive soft tissue and acral overgrowth: widening of hands and feet requiring increasing ring, shoe, and glove sizes ('spade-like hands')", "characteristic craniofacial changes: coarse facial features, frontal bossing, enlarged nose and lips, macroglossia (enlarged tongue with teeth indentations), and mandibular prognathism with dental malocclusion and widened teeth spacing", "deep, hollow, resonant voice and excessive oily skin (hyperhidrosis and seborrhea)", "mass effect from pituitary macroadenoma: bitemporal hemianopsia (compression of optic chiasm) and dull frontal headache", "comorbidities: secondary hypertension, diabetes mellitus, severe OSA, and colonic polyps/adenocarcinomas"],
        "pertinent_negatives": ["normal age-adjusted IGF-1 completely excludes acromegaly"],
        "content": "Syndrome of chronic autonomous Growth Hormone (GH) hypersecretion, > 95% caused by a benign pituitary somatotroph macroadenoma. Elevated GH stimulates excessive hepatic synthesis of Insulin-like Growth Factor 1 (IGF-1), which mediates peripheral tissue overgrowth. Diagnostic workup: 1. Serum IGF-1 (single best screening test; elevated confirms excess); 2. Oral Glucose Tolerance Test (OGTT: 75g glucose fails to suppress GH < 1.0 ng/mL); 3. Contrast MRI pituitary sella. Treatment: First-line definitive therapy: Endoscopic Transsphenoidal Pituitary Adenoma Resection; Medical therapy for residual disease: Long-acting Somatostatin receptor ligands (Octreotide LAR, Lanreotide), GH-receptor antagonist (Pegvisomant), or Dopamine agonist (Cabergoline)."
    },
    {
        "id": "ICD10-E23.2",
        "topic": "Diabetes Insipidus (Central vs Nephrogenic & Water Deprivation)",
        "icd10": "E23.2",
        "specialty": "Endocrinology / Nephrology",
        "organ_system": "Endocrine / Water Metabolism",
        "keywords": ["diabetes insipidus", "central diabetes insipidus", "nephrogenic diabetes insipidus", "polyuria polydipsia clear urine", "low urine osmolality dilute", "desmopressin test", "water deprivation test"],
        "red_flags": ["severe hypernatremic dehydration (serum Na+ > 160 mEq/L)", "hypovolemic shock / coma if water access restricted"],
        "clinical_hallmarks": ["massive, relentless polyuria (> 3 Liters/24 hours, often 8-15 L/day) of clear, pale, dilute water-like urine", "intense, unquenchable polydipsia with a striking preference for ice-cold water", "nocturia occurring multiple times each night", "laboratory hallmark: low urine osmolality (< 300 mOsm/kg) and low urine specific gravity (< 1.005) in the presence of elevated or high-normal serum osmolality (> 295 mOsm/kg) and hypernatremia", "Water Deprivation Test followed by Desmopressin (DDAVP) Challenge: Central DI shows marked rise in urine osmolality (> 50-100% increase after DDAVP); Nephrogenic DI shows NO or minimal (< 50%) response to DDAVP"],
        "pertinent_negatives": ["urine glucose is negative (distinguishes from osmotic diuresis of diabetes mellitus)"],
        "content": "Disorder of water homeostasis characterized by the excretion of abnormally large volumes of dilute urine, resulting from either deficient pituitary Antidiuretic Hormone (ADH / Vasopressin) synthesis/release (Central DI: head trauma, pituitary surgery, craniopharyngioma) or renal tubular insensitivity to ADH (Nephrogenic DI: Lithium toxicity, hypercalcemia, hereditary AVPR2 mutation). Diagnostic test of choice: Water Deprivation Test followed by DDAVP challenge, or plasma Copeptin measurement. Treatment: Central DI: Desmopressin (DDAVP: oral 0.1-0.2 mg BID/TID or intranasal spray 10-20 mcg); Nephrogenic DI: Discontinue Lithium, low-sodium/low-protein diet, Thiazide diuretics (paradoxical antidiuresis) + Amiloride / Indomethacin."
    },
    {
        "id": "ICD10-E20.9",
        "topic": "Hypoparathyroidism & Hypocalcemia (Chvostek & Trousseau Signs)",
        "icd10": "E20.9",
        "specialty": "Endocrinology / Emergency Medicine / General Surgery",
        "organ_system": "Endocrine / Mineral Metabolism",
        "keywords": ["hypoparathyroidism", "hypocalcemia", "chvostek sign", "trousseau sign", "carpopedal spasm", "tetany tingling lips", "prolonged qt interval", "calcium gluconate"],
        "red_flags": ["laryngospasm with acute asphyxiation", "generalized tonic seizures", "cardiac arrhythmias from prolonged QT"],
        "clinical_hallmarks": ["neuromuscular excitability: circumoral paresthesias (tingling/numbness around mouth), numbness in fingertips and toes, and painful muscle cramps", "pathognomonic latent tetany signs: 1. TROUSSEAU SIGN (carpopedal spasm: flexion of wrist and MCP joints with extension of IP joints and adduction of thumb ['main d'accoucheur'] provoked by inflating a BP cuff > 20 mmHg above systolic BP for 3 minutes); 2. CHVOSTEK SIGN (twitching of ipsilateral facial muscles provoked by tapping Cranial Nerve VII anterior to the ear)", "ECG hallmark: PROLONGED QT INTERVAL (ST segment prolongation) predisposing to polymorphic ventricular arrhythmias", "most common etiology: accidental damage, devascularization, or excision of parathyroid glands during total thyroidectomy or neck dissection", "laboratory triad: Low serum ionized and total calcium, Low or inappropriately normal intact PTH, and HIGH serum phosphate"],
        "pertinent_negatives": ["absence of elevated PTH (elevated PTH with low calcium indicates Vitamin D deficiency or pseudohypoparathyroidism)"],
        "content": "Deficiency of parathyroid hormone (PTH) causing impaired renal calcium reabsorption, decreased renal 1-alpha-hydroxylase activation of Vitamin D, and reduced bone resorption. Emergency Protocol for Acute Symptomatic Hypocalcemia: 1. STAT IV Calcium Gluconate (1-2 ampules of 10% Calcium Gluconate in 50-100 mL 5% Dextrose infused over 10-20 minutes with continuous ECG monitoring); 2. Correct concurrent Hypomagnesemia (low Mg impairs PTH secretion and induces end-organ resistance); 3. Chronic Maintenance: Oral Calcium carbonate/citrate (1-3 g elemental calcium daily) + Active Vitamin D (Calcitriol 0.25-1.0 mcg daily); Recombinant human PTH (Natpara) for refractory cases."
    },
    {
        "id": "ICD10-M10.00",
        "topic": "Acute Gouty Arthritis (Podagra & Monosodium Urate Crystals)",
        "icd10": "M10.00",
        "specialty": "Rheumatology / Orthopedics / Primary Care",
        "organ_system": "Musculoskeletal Metabolic",
        "keywords": ["gout", "podagra", "monosodium urate crystals", "negatively birefringent needle crystals", "acute big toe joint pain", "colchicine for gout", "allopurinol uric acid"],
        "red_flags": ["concomitant septic arthritis (requires urgent arthrocentesis)", "chronic tophaceous destruction of joints", "urate nephropathy and renal calculi"],
        "clinical_hallmarks": ["abrupt onset (reaching peak intensity in < 12-24 hours) of excruciating, agonizing monarticular joint pain, swelling, erythema, and warmth, often awakening patient in the middle of the night", "classic site (in > 50-70% of first attacks): First Metatarsophalangeal (MTP) joint (PODAGRA)", "joint is so exquisitely tender that even the light touch of a bedsheet is intolerable", "precipitating triggers: red meat, seafood, alcohol (especially beer), trauma, dehydration, or initiation of thiazide/loop diuretics", "arthrocentesis and polarized light microscopy (DIAGNOSTIC GOLD STANDARD): INTENSELY NEGATIVELY BIREFRINGENT, NEEDLE-SHAPED MONOSODIUM URATE (MSU) CRYSTALS phagocytosed within neutrophils (crystals appear bright yellow when parallel to compensator axis)"],
        "pertinent_negatives": ["absence of positively birefringent rhomboid crystals (distinguishes from pseudogout)"],
        "content": "Inflammatory arthritis triggered by the precipitation of monosodium urate microcrystals in synovial fluid and articular tissues when serum urate exceeds physiological solubility (> 6.8 mg/dL), activating the NLRP3 inflammasome. Treatment: 1. Acute Flares: NSAIDs (Indomethacin, Naproxen) OR oral Colchicine (1.2 mg STAT followed by 0.6 mg 1 hour later) OR oral Prednisone (30-40 mg daily tapered over 7-10 days); 2. Long-term Urate-Lowering Therapy (ULT): Xanthine Oxidase Inhibitors (Allopurinol 100-800 mg daily or Febuxostat) targeting serum uric acid < 6.0 mg/dL (< 5.0 mg/dL if tophi present); MANDATORY Flare Prophylaxis with low-dose Colchicine (0.6 mg daily) for 3-6 months when initiating ULT."
    },
    {
        "id": "ICD10-M11.20",
        "topic": "Pseudogout (Calcium Pyrophosphate Dihydrate - CPPD & Chondrocalcinosis)",
        "icd10": "M11.20",
        "specialty": "Rheumatology / Geriatrics",
        "organ_system": "Musculoskeletal Metabolic",
        "keywords": ["pseudogout", "cppd", "chondrocalcinosis", "calcium pyrophosphate crystals", "positively birefringent rhomboid crystals", "acute knee swelling elderly"],
        "red_flags": ["concomitant bacterial joint infection", "severe destructive neuropathic-like arthropathy"],
        "clinical_hallmarks": ["acute onset of intense monoarthritis or oligoarthritis mimicking true gout, characteristically occurring in elderly individuals (> 65-70 years)", "predominant joint site: THE KNEE (> 50% of attacks), followed by wrist, shoulder, ankle, and elbow", "frequently triggered by acute intercurrent medical illness, surgery (especially joint replacement), or joint trauma", "plain joint radiographs: pathognomonic CHONDROCALCINOSIS (linear, punctate radiodense calcifications within hyaline or fibrocartilage, most notably the triangular fibrocartilage of wrist and menisci of knee)", "synovial fluid analysis under polarized light microscopy: WEAKLY POSITIVELY BIREFRINGENT, RHOMBOID-SHAPED or rod-shaped Calcium Pyrophosphate Dihydrate (CPPD) crystals (crystals appear blue when parallel to compensator)"],
        "pertinent_negatives": ["rhomboid shape and positive birefringence distinguishes decisively from needle-like negative urate crystals of gout"],
        "content": "Metabolic arthropathy characterized by intra-articular deposition of calcium pyrophosphate dihydrate (CPPD) crystals. Associated metabolic conditions: Hemochromatosis ('bronze diabetes'), Hyperparathyroidism, Hypomagnesemia, and Hypophosphatasia. Treatment: Acute attacks: Intra-articular corticosteroid injection (highly effective for single large joints like knee); Oral NSAIDs or low-dose oral Colchicine (0.6 mg BID); Systemic oral corticosteroids; Long-term prophylaxis: low-dose daily Colchicine for frequent recurrent flares. There is no therapy that removes cartilage CPPD deposits."
    },
    {
        "id": "ICD10-M83.9",
        "topic": "Osteomalacia & Rickets (Severe Vitamin D Deficiency & Looser Zones)",
        "icd10": "M83.9",
        "specialty": "Endocrinology / Rheumatology / Pediatrics",
        "organ_system": "Metabolic Bone Disease",
        "keywords": ["osteomalacia", "rickets", "vitamin d deficiency severe", "looser zones", "waddling gait bone pain", "rachitic rosary", "craniotabes", "elevated alkaline phosphatase bone"],
        "red_flags": ["pathological fractures (femoral neck, ribs)", "hypocalcemic tetany or seizures in infants"],
        "clinical_hallmarks": ["Osteomalacia (Adults): diffuse, dull, aching bone pain and exquisite bone tenderness (especially over spine, pelvis, ribs, and anterior tibiae); proximal muscle weakness causing a characteristic 'waddling gait' and difficulty climbing stairs or standing from chair", "Rickets (Children): delayed fontanelle closure, craniotabes (ping-pong ball skull softness), 'rachitic rosary' (beading of costochondral junctions), Harrison groove, and progressive bowing of weight-bearing long bones (genu varum or genu valgum)", "radiographic hallmarks: generalized osteopenia, cortical thinning, and pathognomonic LOOSER'S ZONES (pseudofractures: narrow, radiolucent bands perpendicular to bone cortex, typically at pubic rami, femoral neck, and scapula)", "laboratory tetrad: Markedly low serum 25-hydroxyvitamin D (< 10-12 ng/mL), low or low-normal serum calcium, low serum phosphate, and ELEVATED BONE ALKALINE PHOSPHATASE (ALP) with secondary hyperparathyroidism"],
        "pertinent_negatives": ["bone pain and proximal myopathy are absent in pure uncomplicated osteoporosis"],
        "content": "Defective mineralization of newly formed osteoid matrix in cortical and trabecular bone (osteomalacia) and cartilaginous growth plates (rickets), overwhelmingly caused by severe, prolonged Vitamin D deficiency, dietary calcium lack, or chronic renal phosphate wasting. Diagnostic workup: Serum 25(OH)D, calcium, phosphate, ALP, intact PTH, skeletal radiographs. Treatment: High-dose Ergocalciferol (Vitamin D2: 50,000 IU orally once weekly for 8-12 weeks) or Cholecalciferol (Vitamin D3: 60,000 IU weekly) followed by maintenance (1,000-2,000 IU daily); Concurrent oral elemental Calcium supplementation (1,000-1,500 mg daily) to prevent 'hungry bone' hypocalcemia during rapid remineralization."
    },
    {
        "id": "ICD10-E29.1",
        "topic": "Male Hypogonadism (Klinefelter Syndrome 47,XXY & Testosterone Deficiency)",
        "icd10": "E29.1",
        "specialty": "Endocrinology / Medical Genetics / Urology",
        "organ_system": "Endocrine / Reproductive",
        "keywords": ["hypogonadism", "klinefelter syndrome", "47 xxy", "small firm testes", "gynecomastia eunuchoid proportions", "low testosterone high lh fsh", "azoospermia"],
        "red_flags": ["severe osteoporotic vertebral compression fractures", "metabolic syndrome and cardiovascular disease"],
        "clinical_hallmarks": ["Primary Hypogonadism / Klinefelter Syndrome (47,XXY - most common congenital form, 1 in 600 live male births): tall stature with eunuchoid body proportions (long limbs, arm span exceeding height by > 5 cm), bilateral painless gynecomastia, sparse facial and body hair with female pubic hair distribution, small, firm, fibrotic testes (< 4 mL volume), and azoospermia/infertility", "Adult-onset secondary hypogonadism: progressive loss of libido, erectile dysfunction, decreased spontaneous morning erections, chronic fatigue, muscle mass loss, and depressed mood", "laboratory hallmarks: Primary (Hypergonadotropic) shows Low morning total/free testosterone with HIGH LH and FSH; Secondary (Hypogonadotropic) shows Low testosterone with LOW or inappropriately normal LH/FSH", "karyotype analysis confirms 47,XXY in Klinefelter syndrome"],
        "pertinent_negatives": ["elevated gonadotropins distinguish primary testicular failure from pituitary failure"],
        "content": "Failure of the testes to produce physiological levels of testosterone and/or normal numbers of spermatozoa. Diagnostic workup: Morning (8-10 AM) fasting total testosterone on two separate mornings (diagnostic if < 300 ng/dL), LH, FSH, prolactin, karyotype analysis, semen analysis, bone mineral density (DEXA scan). Treatment: Klinefelter and primary hypogonadism: Lifelong Testosterone Replacement Therapy (TRT: transdermal gels, injectable testosterone cypionate/enanthate 100-200 mg q2 weeks, or testosterone undecanoate 1000 mg q10-14 weeks) to restore secondary sexual characteristics, muscle mass, bone density, and mood; TRT is contraindicated in active prostate or breast cancer."
    },

    # --- 7. HEMATOLOGY & ONCOLOGY (14) ---
    {
        "id": "ICD10-C92.00",
        "topic": "Acute Myeloid Leukemia (AML & Auer Rods)",
        "icd10": "C92.00",
        "specialty": "Hematology / Oncology",
        "organ_system": "Hematological Malignancy Emergency",
        "keywords": ["acute myeloid leukemia", "aml", "auer rods", "myeloblasts on smear", "bone marrow failure anemia bleeding", "gingival hyperplasia aml", "induction chemotherapy 7+3"],
        "red_flags": ["acute promyelocytic leukemia (apl / pml-rara) with catastrophic dic", "hyperleukocytosis / leukostasis syndrome (pulmonary distress, stroke)", "tumor lysis syndrome"],
        "clinical_hallmarks": ["abrupt onset (over days to weeks) of bone marrow failure symptoms: 1. Profound fatigue, pallor, and exertional dyspnea (severe anemia); 2. Petechiae, purpura, epistaxis, and gingival hemorrhage (thrombocytopenia); 3. Recurrent refractory bacterial infections or neutropenic fever", "pathognomonic morphological hallmark on peripheral smear or bone marrow aspirate: AUER RODS (crystalline cytoplasmic inclusions of fused lysosomal peroxidase granules inside myeloblasts)", "gingival hypertrophy, bleeding gums, and leukemia cutis (in monocytic subtypes - FAB M4/M5)", "bone marrow biopsy: hypercellular marrow with >= 20% MYELOBLASTS (WHO diagnostic criteria), expressing CD13, CD33, CD117, and Myeloperoxidase (MPO)"],
        "pertinent_negatives": ["Auer rods confirm myeloid lineage (completely absent in acute lymphoblastic leukemia)"],
        "content": "Clonal malignant disorder of hematopoietic progenitor cells characterized by accumulation of immature blast cells in bone marrow and peripheral blood, leading to marrow failure. In APL (t(15;17) PML-RARA), immediate All-Trans Retinoic Acid (ATRA) + Arsenic Trioxide (ATO) is curative and prevents fatal DIC. Standard AML Treatment: '7 + 3' Induction Chemotherapy (7 days continuous IV Cytarabine + 3 days IV Daunorubicin); Targeted therapies: FLT3 inhibitors (Midostaurin), IDH inhibitors (Ivosidenib); Allogeneic Hematopoietic Stem Cell Transplantation (Allo-HSCT) for intermediate/adverse cytogenetic risk."
    },
    {
        "id": "ICD10-C92.10",
        "topic": "Chronic Myeloid Leukemia (CML & Philadelphia Chromosome t(9;22))",
        "icd10": "C92.10",
        "specialty": "Hematology / Oncology",
        "organ_system": "Hematological Malignancy",
        "keywords": ["chronic myeloid leukemia", "cml", "philadelphia chromosome", "bcr abl1", "massive splenomegaly", "imatinib tyrosine kinase inhibitor", "leukocytosis full granulocyte spectrum"],
        "red_flags": ["blast crisis (acute leukemia transformation with > 20% blasts)", "splenic infarction", "leukostasis"],
        "clinical_hallmarks": ["insidious onset of fatigue, anorexia, night sweats, low-grade fever, and marked weight loss", "MASSIVE, FIRM, NON-TENDER SPLENOMEGALY extending into left lower quadrant or across umbilicus (causing early satiety and dragging abdominal sensation)", "peripheral blood smear hallmark: striking leukocytosis (WBC often 50,000 - 300,000 /mcL) showing the FULL SPECTRUM OF MYELOID DIFFERENTIATION (from myeloblasts to mature segmented neutrophils: myeloblasts, promyelocytes, myelocytes, metamyelocytes, bands, neutrophils) with marked BASOPHILIA and eosinophilia", "severely depressed Leukocyte Alkaline Phosphatase (LAP score < 20 distinguishes CML from leukemoid reaction)", "cytogenetic and molecular hallmark: PHILADELPHIA CHROMOSOME t(9;22)(q34;q11.2) creating the oncogenic BCR-ABL1 fusion gene"],
        "pertinent_negatives": ["LAP score is low (in leukemoid reactions to severe infection, LAP score is markedly elevated)"],
        "content": "Myeloproliferative neoplasm characterized by the unregulated clonal proliferation of the granulocytic lineage, driven by the constitutively active BCR-ABL1 tyrosine kinase. Clinical phases: Chronic Phase (85%), Accelerated Phase, and Blast Crisis. Diagnostic workup: Bone marrow biopsy, Cytogenetics for t(9;22), Quantitative RT-PCR for BCR-ABL1 transcripts. First-line Targeted Therapy: Oral BCR-ABL Tyrosine Kinase Inhibitors (TKIs: Imatinib 400 mg daily; second-generation: Dasatinib, Nilotinib) which induce deep molecular remission (MMR) and normal life expectancy; Allogeneic stem cell transplant for TKI-refractory or blast phase disease."
    },
    {
        "id": "ICD10-C81.90",
        "topic": "Hodgkin Lymphoma (Reed-Sternberg Cells & B-Symptoms)",
        "icd10": "C81.90",
        "specialty": "Hematology / Oncology",
        "organ_system": "Lymphoid Malignancy",
        "keywords": ["hodgkin lymphoma", "reed sternberg cells", "painless cervical lymphadenopathy", "pel ebstein fever", "alcohol induced pain in lymph node", "b symptoms lymphoma", "abvd chemotherapy"],
        "red_flags": ["superior vena cava (svc) syndrome from bulky mediastinal mass", "tracheal compression and airway compromise", "spinal cord compression"],
        "clinical_hallmarks": ["painless, firm, rubbery, non-tender, asymmetric enlargement of superficial lymph nodes, characteristically in the CERVICAL (60-70%) and supraclavicular regions, spreading in a predictable contiguous fashion", "bulky anterior mediastinal mass discovered on routine chest radiograph in young adults", "systemic 'B-symptoms' (carries prognostic significance): 1. Unexplained fever > 38C; 2. Drenching night sweats; 3. Unintentional weight loss > 10% of body weight over 6 months", "pathognomonic phenomenon: ALCOHOL-INDUCED LYMPH NODE PAIN (severe aching in enlarged lymph nodes immediately after drinking alcohol - occurs in 5% of patients with high specificity)", "Pel-Ebstein fever: cyclical, alternating bouts of several days of high fever followed by afebrile intervals", "excisional lymph node biopsy (pathognomonic): REED-STERNBERG CELLS (giant binucleated or multinucleated B-cells with prominent inclusion-like nucleoli resembling 'owl's eyes') positive for CD15 and CD30"],
        "pertinent_negatives": ["needle aspiration (FNAC) is INSUFFICIENT; excisional biopsy is mandatory to evaluate nodal architecture"],
        "content": "Malignant neoplasm of B-cell origin characterized by the presence of giant neoplastic Reed-Sternberg cells residing within a prominent non-neoplastic reactive inflammatory and fibrotic cellular background. Bimodal age incidence (peaks at 15-35 years and > 55 years). Ann Arbor Staging (Stage I-IV, with A/B designation). Staging workup: Excisional lymph node biopsy, Whole-body PET-CT (Deauville criteria). Treatment: Highly curable (> 80-90% cure rate); First-line chemotherapy: ABVD protocol (Doxorubicin [Adriamycin], Bleomycin, Vinblastine, Dacarbazine) or escalated BEACOPP +/- Involved-Site Radiation Therapy (ISRT); Brentuximab vedotin (anti-CD30) or Nivolumab for relapsed disease."
    },
    {
        "id": "ICD10-D69.3",
        "topic": "Immune Thrombocytopenic Purpura (ITP - Isolated Thrombocytopenia)",
        "icd10": "D69.3",
        "specialty": "Hematology / Pediatrics / Internal Medicine",
        "organ_system": "Hematological Autoimmune",
        "keywords": ["immune thrombocytopenic purpura", "itp", "isolated thrombocytopenia", "petechiae purpura wet purpura", "normal bone marrow megakaryocytes", "ivig for itp", "thrombopoietin receptor agonists"],
        "red_flags": ["intracranial hemorrhage (highest risk if platelets < 10,000 /mcL)", "wet purpura (hemorrhagic bullae on oral mucosa)", "massive gastrointestinal bleeding"],
        "clinical_hallmarks": ["mucocutaneous bleeding in an otherwise entirely well-appearing patient: petechiae (pinpoint non-blanching red/purple macules on lower extremities), ecchymoses (easy bruising), epistaxis, and menorrhagia", "'Wet purpura': blood blisters and hemorrhagic bullae on the buccal mucosa and palate, indicating high risk of severe bleeding", "LABORATORY HALLMARK: ISOLATED THROMBOCYTOPENIA (platelet count < 100,000 /mcL, often < 10,000-20,000 /mcL) with completely NORMAL red blood cell count, normal hemoglobin, and normal white blood cell count", "peripheral blood smear confirms true thrombocytopenia with normal to large platelets (rules out EDTA-induced pseudothrombocytopenia) and ABSENCE OF SCHISTOCYTES", "physical exam: ABSENCE OF SPLENOMEGALY, lymphadenopathy, or stigmata of chronic liver disease"],
        "pertinent_negatives": ["normal RBCs, WBCs, and absence of splenomegaly distinguishes ITP from leukemia, aplastic anemia, or hypersplenism"],
        "content": "Acquired autoimmune disorder characterized by pathogenic anti-platelet autoantibodies (predominantly IgG directed against platelet surface glycoproteins GPIIb/IIIa or GPIb/IX) leading to Fc-receptor-mediated phagocytosis and destruction of platelets in the spleen and liver. Treatment: Platelets > 30,000 /mcL without bleeding: watchful observation; Platelets < 30,000 /mcL or active bleeding: 1. First-line: Oral Corticosteroids (Prednisone 1 mg/kg/day for 2-4 weeks or high-dose Dexamethasone 40 mg daily for 4 days); 2. STAT IVIG (1 g/kg for 1-2 days) provides rapid platelet rise within 24-48 hours for emergency bleeding; 3. Second-line: Thrombopoietin receptor agonists (Romiplostim, Eltrombopag), Rituximab (anti-CD20), or Splenectomy."
    },
    {
        "id": "ICD10-M31.1",
        "topic": "Thrombotic Thrombocytopenic Purpura (TTP - ADAMTS13 Deficiency)",
        "icd10": "M31.1",
        "specialty": "Hematology / Critical Care / Emergency Medicine",
        "organ_system": "Microangiopathic Hemolytic Emergency",
        "keywords": ["thrombotic thrombocytopenic purpura", "ttp", "adamts13 deficiency", "schistocytes peripheral smear", "pentad fever thrombocytopenia maha", "plasma exchange ttp", "caplacizumab"],
        "red_flags": ["catastrophic stroke / coma", "acute myocardial infarction from microthrombi", "cardiac arrest if platelet transfusion given"],
        "clinical_hallmarks": ["classic diagnostic PENTAD (present simultaneously in < 40%, but the 'FAT RN' triad of MAHA + Thrombocytopenia + Neurologic signs warrants STAT presumptive diagnosis): 1. Fever; 2. Anemia (Microangiopathic Hemolytic Anemia - MAHA); 3. Thrombocytopenia; 4. Renal insufficiency (mild); 5. Neurological deficits (fluctuating confusion, headache, focal deficits, seizures, coma)", "peripheral blood smear: prominent SCHISTOCYTES (helmet cells, fragmented red cells, > 1% on oil immersion field) with profound thrombocytopenia", "laboratory markers of brisk intravascular hemolysis: markedly elevated LDH, unconjugated hyperbilirubinemia, and absent haptoglobin", "NORMAL COAGULATION PROFILE: PT/INR and aPTT are COMPLETELY NORMAL (crucial distinction from DIC)"],
        "pertinent_negatives": ["PLATELET TRANSFUSIONS ARE STRICTLY CONTRAINDICATED (act as 'fuel to the fire', precipitating widespread microvascular thrombosis and death)"],
        "content": "Life-threatening thrombotic microangiopathy caused by severe deficiency (< 10% activity) of the metalloprotease ADAMTS13, overwhelmingly due to an acquired IgG autoantibody. Uncleaved ultra-large Von Willebrand factor (ULVWF) multimers cause spontaneous platelet aggregation and microvascular platelet-rich thrombi. Statutory emergency with 90% mortality if untreated. Diagnostic test: ADAMTS13 activity and inhibitor titre. Immediate Protocol: 1. STAT Emergency Therapeutic Plasma Exchange (TPE / Plasmapheresis: 1.0-1.5 plasma volumes daily with fresh frozen plasma) initiated immediately; 2. High-dose IV Corticosteroids (Methylprednisolone 1 g daily for 3 days); 3. Caplacizumab (anti-vWF nanobody); 4. Rituximab (anti-CD20)."
    },
    {
        "id": "ICD10-D65",
        "topic": "Disseminated Intravascular Coagulation (DIC - Consumptive Coagulopathy)",
        "icd10": "D65",
        "specialty": "Hematology / Critical Care / Emergency Medicine",
        "organ_system": "Coagulation Emergency",
        "keywords": ["disseminated intravascular coagulation", "dic", "consumptive coagulopathy", "elevated d-dimer low fibrinogen", "oozing from iv lines", "sepsis induced dic", "prolonged pt and aptt"],
        "red_flags": ["exsanguinating multiorgan hemorrhage", "gangrene of digits (purpura fulminans)", "multiorgan failure (ards, aki, shock)"],
        "clinical_hallmarks": ["the clinical paradox: SIMULTANEOUS WIDESPREAD SYSTEMIC MICROVASCULAR THROMBOSIS (causing multiorgan failure) AND PROFUSE BLEEDING (due to consumption of platelets and clotting factors)", "spontaneous, persistent, continuous oozing of blood from IV venipuncture sites, surgical wounds, mucosal membranes, and catheter insertion points", "petechiae, widespread ecchymoses, and Purpura Fulminans (cutaneous microvascular thrombosis and hemorrhagic skin necrosis)", "triggered by a catastrophic underlying condition: severe sepsis / septic shock (Gram-negative endotoxemia), obstetric catastrophes (abruptio placentae, amniotic fluid embolism), massive trauma, or malignancy (APL)", "diagnostic laboratory tetrad: 1. Markedly elevated D-Dimer / Fibrin Degradation Products (FDPs); 2. Prolonged Prothrombin Time (PT/INR) and prolonged aPTT; 3. Progressive thrombocytopenia; 4. Severely depressed serum Fibrinogen level (< 100-150 mg/dL)"],
        "pertinent_negatives": ["prolonged PT and aPTT distinguish DIC decisively from TTP (where PT/aPTT are normal)"],
        "content": "Systemic thrombohemorrhagic syndrome characterized by uncontrolled systemic activation of the extrinsic coagulation cascade (tissue factor release), resulting in widespread microvascular fibrin deposition and consumptive depletion of platelets and coagulation factors. Management: 1. TREAT THE UNDERLYING PRIMARY TRIGGER IMMEDIATELY (antibiotics for sepsis, emergent delivery for placental abruption, chemotherapy); 2. Supportive replacement therapy guided by active bleeding: Platelet transfusion (target > 50,000 /mcL if bleeding); Fresh Frozen Plasma (FFP: 15-30 mL/kg for prolonged PT/aPTT); Cryoprecipitate (target fibrinogen > 150 mg/dL); 3. Heparin infusion considered only in predominant thrombotic phenotype (purpura fulminans, solid tumor)."
    },
    {
        "id": "ICD10-D57.00",
        "topic": "Sickle Cell Disease & Acute Vaso-Occlusive Bone Crisis",
        "icd10": "D57.00",
        "specialty": "Hematology / Pediatrics / Emergency Medicine",
        "organ_system": "Hemoglobinopathy Emergency",
        "keywords": ["sickle cell disease", "vaso occlusive crisis", "sickle cell bone pain", "acute chest syndrome", "dactylitis infant hand foot", "hemoglobin s electrophoresis", "hydroxyurea sickle cell"],
        "red_flags": ["acute chest syndrome (fever, chest pain, new lung infiltrate, hypoxemia)", "splenic sequestration crisis in young child (hypovolemic shock, massive spleen)", "ischemic stroke in pediatric sickle patient"],
        "clinical_hallmarks": ["recurrent, unpredictable episodes of severe, agonizing, deep bone or joint pain (commonly affecting back, ribs, femora, and tibiae) triggered by cold, hypoxia, dehydration, stress, or infection", "Dactylitis ('hand-foot syndrome'): symmetrical, exquisitely painful, warm, non-erythematous swelling of dorsal hands and feet in infants (6-18 months) - frequently the first clinical manifestation of sickle cell disease", "chronic hemolytic anemia: jaundice, scleral icterus, pigmented gallstones, and non-healing malleolar skin ulcers", "functional asplenia: early autosplenectomy by age 5 due to repeated splenic micro-infarctions, predisposing to fatal encapsulated bacterial infections (Streptococcus pneumoniae)", "diagnostic confirmation: Hemoglobin Electrophoresis or High-Performance Liquid Chromatography (HPLC) showing predominant Hemoglobin S (HbS > 80-90%) with absence of normal HbA in homozygous HbSS"],
        "pertinent_negatives": ["presence of sickled, crescent-shaped erythrocytes and Howell-Jolly bodies on peripheral blood smear"],
        "content": "Autosomal recessive hemoglobinopathy caused by a point mutation in the beta-globin gene (GAG to GTG, replacing glutamic acid with valine at codon 6 of beta-globin chain). Deoxygenation causes HbS polymerization into rigid, insoluble fibers that distort RBCs into sickle shapes, causing microvascular occlusion and hemolysis. Protocol for Acute Vaso-Occlusive Crisis: 1. Prompt, aggressive opioid analgesia (IV Morphine or Hydromorphone administered within 30-60 minutes); 2. Aggressive oral or IV hydration with hypotonic fluids (D5W or 0.45% Saline); 3. Supplemental oxygen ONLY IF SpO2 < 95%; 4. Preventative disease-modifying therapy: Hydroxyurea (induces fetal hemoglobin HbF synthesis, reducing crises by > 50%); L-glutamine, Voxelotor, Crizanlizumab."
    },
    {
        "id": "ICD10-D56.1",
        "topic": "Beta-Thalassemia Major (Cooley's Anemia & Iron Overload)",
        "icd10": "D56.1",
        "specialty": "Hematology / Pediatrics / Medical Genetics",
        "organ_system": "Hemoglobinopathy Genetic",
        "keywords": ["beta thalassemia major", "cooleys anemia", "chipmunk facies", "hair on end appearance skull", "microcytic hypochromic severe anemia", "transfusion dependent iron overload", "deferasirox"],
        "red_flags": ["severe high-output cardiac failure in infancy", "secondary iron overload endocrinopathies / cirrhosis", "severe transfusion reactions"],
        "clinical_hallmarks": ["infant presents between 6 and 24 months of age (as fetal hemoglobin HbF production wanes) with severe, progressive, life-threatening pallor, failure to thrive, feeding difficulties, and irritability", "profound microcytic, hypochromic anemia (hemoglobin typically 2-6 g/dL) with target cells, anisopoikilocytosis, basophilic stippling, and nucleated RBCs on blood smear", "MASSIVE EXTRAMEDULLARY HEMATOPOIESIS signs: 1. Striking 'chipmunk facies' (prominent frontal bossing, maxillary hypertrophy, depressed nasal bridge); 2. Skeletal X-ray showing widening of diploic space with classic 'hair-on-end' skull appearance; 3. Massive hepatosplenomegaly causing huge protuberant abdomen", "hemoglobin electrophoresis: profound deficiency or COMPLETE ABSENCE OF HbA, with compensatory elevation of HbF (> 90-95%) and variable HbA2"],
        "pertinent_negatives": ["normal or elevated serum ferritin and iron levels (decisively excludes iron deficiency anemia)"],
        "content": "Severe autosomal recessive hemoglobinopathy characterized by absent (beta-0) or severely reduced (beta-plus) synthesis of beta-globin chains, leading to an excess of unpaired alpha-globin chains that precipitate in erythroid precursors, causing profound ineffective erythropoiesis and severe peripheral hemolysis. Management: 1. Lifelong, regular, Transfusion-Dependent protocol: packed RBC transfusions every 2-4 weeks to maintain pre-transfusion Hb 9.5-10.5 g/dL; 2. MANDATORY Iron Chelation Therapy (oral Deferasirox, Deferiprone, or subcutaneous Deferoxamine) initiated after 10-20 transfusions or when serum ferritin exceeds 1000 ng/mL to prevent fatal hemochromatotic heart failure; 3. Definitive cure: Allogeneic Hematopoietic Stem Cell Transplantation (Allo-HSCT) or gene therapy."
    },
    {
        "id": "ICD10-D45",
        "topic": "Polycythemia Vera (JAK2 V617F Mutation & Aquagenic Pruritus)",
        "icd10": "D45",
        "specialty": "Hematology / Oncology",
        "organ_system": "Myeloproliferative Neoplasm",
        "keywords": ["polycythemia vera", "jak2 v617f", "aquagenic pruritus itching warm bath", "ruddy cyanosis plethora", "erythromelalgia burning red feet", "low erythropoietin epo", "therapeutic phlebotomy"],
        "red_flags": ["major arterial or venous thrombosis (stroke, mi, budd-chiari, dvt)", "transformation to myelofibrosis or aml"],
        "clinical_hallmarks": ["pathognomonic symptom: AQUAGENIC PRURITUS (intense, intractable, excruciating itching, burning, or stinging sensation triggered by warm water, showers, or baths, without any visible cutaneous rash)", "plethoric appearance: ruddy cyanosis ('red face'), engorged conjunctival vessels, and dusky redness of palms and soles", "Erythromelalgia: episodic, intense burning pain and erythema in the distal hands and feet, relieved by aspirin or cold application", "symptoms of hyperviscosity: dull throbbing headache, dizziness, visual scotomas, tinnitus, and epistaxis", "moderate splenomegaly on palpation (70%)", "laboratory hallmarks: Markedly elevated Hemoglobin (> 16.5 g/dL in men, > 16.0 g/dL in women) and Hematocrit (> 49% in men, > 48% in women), associated leukocytosis and thrombocytosis, SUPPRESSED SERUM ERYTHROPOIETIN (EPO < normal), and positive JAK2 V617F mutation in > 95% of patients"],
        "pertinent_negatives": ["suppressed serum EPO distinguishes primary PV from secondary polycythemia (where EPO is elevated)"],
        "content": "Clonal myeloproliferative neoplasm characterized by autonomous, erythropoietin-independent trilineage hematopoietic hyperplasia, driven by the somatic gain-of-function JAK2 V617F mutation (valine-to-phenylalanine substitution at codon 617) in exon 14. WHO diagnostic criteria (3 major, or 2 major + 1 minor). Treatment: 1. Therapeutic Phlebotomy (removal of 450-500 mL blood regularly) to STRICTLY MAINTAIN HEMATOCRIT < 45% (demonstrated to reduce cardiovascular death and major thrombotic events by fourfold); 2. Low-dose Aspirin (75-100 mg daily); 3. Cytoreductive therapy (Hydroxyurea) for high-risk patients (age > 60 or prior thrombosis); 4. JAK1/2 inhibitor (Ruxolitinib) for hydroxyurea-resistant cases."
    },
    {
        "id": "ICD10-C16.9",
        "topic": "Gastric Adenocarcinoma (Virchow Node & Krukenberg Tumor)",
        "icd10": "C16.9",
        "specialty": "Gastroenterology / Surgical Oncology",
        "organ_system": "Gastrointestinal Oncology",
        "keywords": ["gastric cancer", "gastric adenocarcinoma", "virchow node", "sister mary joseph nodule", "krukenberg tumor", "linitis plastica leather bottle", "signet ring cell"],
        "red_flags": ["gastric outlet obstruction (projectile vomiting)", "massive upper gi hemorrhage / hematemesis", "peritoneal carcinomatosis with malignant ascites"],
        "clinical_hallmarks": ["insidious, progressive early symptoms: persistent, vague postprandial epigastric fullness, early satiety, anorexia, and unintentional marked weight loss", "unexplained iron deficiency anemia and occult GI blood loss in an adult > 50 years", "pathognomonic metastatic lymph node and peritoneal stigmata: 1. VIRCHOW'S NODE (hard, non-tender enlargement of the LEFT SUPRACLAVICULAR lymph node / Troisier sign); 2. SISTER MARY JOSEPH NODULE (palpable metastatic nodule in the umbilicus); 3. BLUMER'S SHELF (metastatic ridge palpable on digital rectal exam in the rectovesical or rectouterine pouch); 4. KRUKENBERG TUMOR (bilateral metastatic ovarian enlargement with mucin-rich signet ring cells)", "Linitis Plastica: diffuse infiltrative adenocarcinoma causing a rigid, non-distensible, thickened 'leather bottle' stomach on barium swallow/CT"],
        "pertinent_negatives": ["symptoms refractory to empirical PPI courses warrant immediate endoscopy"],
        "content": "Malignant epithelial tumor of the stomach, categorized by Lauren classification into Intestinal type (associated with chronic H. pylori atrophic gastritis, smoking, dietary nitrosamines) and Diffuse type (infiltrative, E-cadherin/CDH1 gene mutation, signet-ring cells). Diagnostic gold standard: Upper GI Endoscopy (EGD) with multiple oriented biopsies (minimum 6-8 biopsies for high diagnostic yield); Endoscopic ultrasound (EUS) and Contrast CT chest/abdomen/pelvis for TNM staging. Treatment: Resectable disease: Radical Subtotal or Total Gastrectomy with D2 Lymphadenectomy + Perioperative FLOT Chemotherapy; Targeted Trastuzumab for HER2-positive metastatic disease; Nivolumab for PD-L1 positive tumors."
    },
    {
        "id": "ICD10-C25.9",
        "topic": "Pancreatic Adenocarcinoma (Painless Jaundice & Courvoisier Sign)",
        "icd10": "C25.9",
        "specialty": "Gastroenterology / Surgical Oncology",
        "organ_system": "Hepatobiliary-Pancreatic Oncology",
        "keywords": ["pancreatic cancer", "pancreatic adenocarcinoma", "painless jaundice", "courvoisier sign", "double duct sign", "ca 19 9 elevated", "whipple procedure"],
        "red_flags": ["trousseau syndrome of malignancy (migratory superficial thrombophlebitis)", "unresectable superior mesenteric artery encasement", "severe cachexia"],
        "clinical_hallmarks": ["cardinal clinical presentation: PROGRESSIVE, INSIDIOUS, PAINLESS OBSTRUCTIVE JAUNDICE (yellow sclerae, deep dark tea-colored urine, pale clay-colored acholic stools, and generalized pruritus)", "epigastric ache radiating through to the mid-back, characteristically partially relieved by sitting upright and leaning forward", "rapid, marked, unintentional weight loss and profound anorexia", "COURVOISIER'S SIGN (pathognomonic): A PALPABLE, ENLARGED, NON-TENDER GALLBLADDER in the presence of obstructive jaundice (indicates malignant distal common bile duct obstruction, as chronic gallstone disease causes a fibrotic shrunken non-distensible gallbladder)", "Trousseau syndrome: migratory, superficial thrombophlebitis presenting as recurrent tender inflammatory cords in superficial veins", "sudden, new-onset diabetes mellitus in an elderly patient without risk factors"],
        "pertinent_negatives": ["absence of biliary colic and absence of fever (distinguishes from acute gallstone cholangitis)"],
        "content": "Highly lethal malignancy arising from the ductal epithelium of the exocrine pancreas (70% located in the head of the pancreas). Diagnostic workup: Multiphase Thin-Cut Pancreatic Protocol CT of abdomen (shows hypoattenuating pancreatic mass, loss of peripancreatic fat planes, and pathognomonic 'DOUBLE DUCT SIGN' [simultaneous dilation of both the common bile duct and the main pancreatic duct]); Serum CA 19-9 tumor marker (useful for monitoring, sensitivity 80%); EUS with fine-needle biopsy. Treatment: Resectable head tumors: Pancreaticoduodenectomy (Whipple Procedure) followed by adjuvant modified FOLFIRINOX chemotherapy; Endoscopic biliary stenting (metal stent) for jaundice palliation."
    },
    {
        "id": "ICD10-C22.0",
        "topic": "Hepatocellular Carcinoma (HCC - Cirrhosis Surveillance & AFP)",
        "icd10": "C22.0",
        "specialty": "Gastroenterology / Hepatology / Surgical Oncology",
        "organ_system": "Hepatic Malignancy",
        "keywords": ["hepatocellular carcinoma", "hcc", "cirrhosis liver mass", "alpha fetoprotein elevated", "arterial phase hyperenhancement washout", "portal vein tumor thrombus", "bclc staging"],
        "red_flags": ["spontaneous tumor rupture with catastrophic hemoperitoneum", "portal vein tumor thrombosis with variceal hemorrhage", "rapid hepatic decompensation"],
        "clinical_hallmarks": ["develops almost exclusively (> 85-90%) in patients with underlying CHRONIC CIRRHOSIS (chronic Hepatitis B, chronic Hepatitis C, alcoholic cirrhosis, or NASH/MASH)", "clinical presentation is often subtle: rapid, unexplained decompensation of previously stable cirrhosis (new-onset refractory ascites, worsening encephalopathy, or variceal bleed)", "unintentional weight loss, anorexia, and dull right upper quadrant dragging pain", "physical examination: hard, nodular, enlarged liver; an audible hepatic arterial bruit over the tumor", "laboratory hallmark: Markedly elevated serum Alpha-Fetoprotein (AFP > 400-500 ng/mL is strongly suggestive in high-risk cirrhotic patient)", "pathognomonic dynamic multiphasic imaging criteria (CT/MRI): ARTERIAL PHASE HYPERENHANCEMENT (intense enhancement in late arterial phase) FOLLOWED BY 'WASHOUT' in the venous or delayed phase with an enhancing pseudocapsule (LI-RADS 5)"],
        "pertinent_negatives": ["biopsy is NOT required for diagnosis in cirrhotic patients if dynamic CT/MRI meets definitive non-invasive LI-RADS 5 criteria"],
        "content": "Primary malignant neoplasm of hepatocytes. Surveillance standard: Biannual (every 6 months) liver ultrasound + serum AFP in all cirrhotic patients. Staged using the Barcelona Clinic Liver Cancer (BCLC) system. Treatment options: Very early / Early stage (BCLC 0/A): Surgical Resection (for non-cirrhotic or preserved Child-Pugh A), Orthotopic Liver Transplantation (Milan criteria: 1 lesion <= 5 cm or up to 3 lesions <= 3 cm), or Radiofrequency / Microwave Ablation (RFA/MWA); Intermediate stage (BCLC B): Transarterial Chemoembolization (TACE); Advanced stage (BCLC C): Systemic immunotherapy combination (Atezolizumab + Bevacizumab is first-line)."
    }
]

def run():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        existing = json.load(f)
    
    existing_ids = {p["id"] for p in existing}
    existing_topics = {p["topic"].lower() for p in existing}
    
    added = 0
    for p in PROTOCOLS_TO_ADD:
        if p["id"] not in existing_ids and p["topic"].lower() not in existing_topics:
            existing.append(p)
            existing_ids.add(p["id"])
            existing_topics.add(p["topic"].lower())
            added += 1
            
    print(f"Batch 3 added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

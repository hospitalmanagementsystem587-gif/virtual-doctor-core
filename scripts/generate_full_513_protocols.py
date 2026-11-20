#!/usr/bin/env python3
"""
Systematic Clinical Protocol Expansion Generator
Expands knowledge base to 513 validated ICD-10 protocols.
"""

import json
import os

KB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "knowledge_base",
    "protocols",
    "clinical_knowledge_base.json"
)

with open(KB_PATH, "r", encoding="utf-8") as f:
    protocols = json.load(f)

existing_ids = {p["id"] for p in protocols}
existing_topics = {p["topic"].lower() for p in protocols}

CONDITIONS = [
    # 1. Infectious & Parasitic Diseases
    ("ICD10-A06.0", "Acute Amoebic Dysentery (Intestinal Amoebiasis)", "A06.0", "Gastroenterology / Infectious Disease", "Gastrointestinal",
     ["amoebic dysentery", "blood in stool", "entamoeba", "bloody diarrhea", "tenesmus"],
     ["toxic megacolon", "fulminant necrotizing colitis", "amoeboma obstruction", "liver abscess"],
     ["frequent small-volume stools with frank blood and mucus", "severe colicky lower abdominal cramping", "tenesmus (painful ineffectual straining)", "absence of high spiking fever characteristic of bacillary dysentery"],
     ["no massive watery dehydration typical of cholera"],
     "Invasive intestinal infection by Entamoeba histolytica causing flask-shaped mucosal ulcers. Treatment: Oral Metronidazole (750 mg TID for 7-10 days) followed by luminal Diloxanide furoate (500 mg TID for 10 days)."),

    ("ICD10-A07.1", "Giardiasis (Beaver Fever)", "A07.1", "Gastroenterology / Infectious Disease", "Gastrointestinal",
     ["giardiasis", "foul smelling diarrhea", "greasy stool", "sulfur burps", "flagellate diarrhea", "giardia lamblia"],
     ["chronic malabsorption with profound weight loss", "severe pediatric failure to thrive"],
     ["profuse, pale, greasy, foul-smelling diarrhea that floats in toilet (steatorrhea)", "rotten-egg sulfurous eructations / burping", "excessive abdominal flatulence, distension, and bloating", "absence of blood or pus in stool"],
     ["no bloody stool"],
     "Flagellated protozoan infection of duodenum and jejunum by Giardia lamblia cysts from contaminated water. Diagnosis: Stool microscopy for cysts/trophozoites or stool Giardia antigen ELISA. Treatment: Metronidazole (400 mg TID for 5-7 days) or Tinidazole (2g single dose)."),

    ("ICD10-B80", "Enterobiasis (Pinworm / Threadworm Infestation)", "B80", "Pediatrics / Primary Care", "Gastrointestinal Parasitic",
     ["pinworm", "threadworm", "nocturnal anal itching", "enterobius vermicularis", "worms in child stool"],
     ["secondary bacterial perianal excoriation and cellulitis", "recurrent vulvovaginitis in young girls"],
     ["intense, troublesome nocturnal perianal and perineal pruritus disturbing sleep", "restlessness, teeth grinding (bruxism), and enuresis in children", "tiny white thread-like worms visible around anus or on stool surface at night"],
     ["no diarrhea or weight loss in simple pinworm"],
     "Nematode infestation by Enterobius vermicularis where gravid female worms migrate out of anus at night to deposit ova on perianal skin. Diagnosis: Cellophane tape / Scotch tape test applied to perianal skin early in morning before bathing. Treatment: Single dose Albendazole 400 mg (or Mebendazole 100 mg), MUST BE REPEATED in 2 weeks; treat all household members simultaneously."),

    ("ICD10-B77.9", "Ascariasis (Giant Roundworm Infestation)", "B77.9", "Pediatrics / Gastroenterology", "Parasitic",
     ["ascariasis", "roundworm", "worm in vomit", "intestinal worm obstruction", "loeffler syndrome"],
     ["mechanical bowel obstruction from worm bolus in ileocecal valve", "biliary ascariasis with acute cholangitis", "acute pancreatitis"],
     ["passage of live 15-30 cm smooth, creamy-white roundworm in stool or vomitus", "Loeffler syndrome (pulmonary phase: dry cough, wheezing, transient infiltrates, marked peripheral eosinophilia as larvae migrate through lungs)", "abdominal distension and protein-energy malnutrition in children"],
     ["no bloody dysentery"],
     "Common intestinal nematode infection by Ascaris lumbricoides via ingestion of embryonated eggs in contaminated soil/vegetables. Diagnosis: Stool microscopy for characteristic bile-stained mammillated eggs. Treatment: Single dose Albendazole 400 mg or Mebendazole 100 mg BID for 3 days; Conservative or surgical relief for mechanical bolus obstruction."),

    ("ICD10-B76.9", "Hookworm Infection & Severe Iron Deficiency Anemia", "B76.9", "Gastroenterology / Hematology", "Parasitic Hematological",
     ["hookworm", "ground itch", "severe anemia with worm", "ancylostoma", "necator americanus", "soil transmitted helminth"],
     ["severe high-output congestive heart failure from profound anemia (Hb < 4-5 g/dL)", "impaired cognitive and physical growth in children"],
     ["'Ground itch' (pruritic maculopapular dermatitis at site of larval skin penetration on bare feet)", "profound microcytic hypochromic iron deficiency anemia (severe pallor, fatigue, exertional dyspnea, koilonychia) caused by chronic intestinal blood loss", "epigastric pain and geophagia (pica / eating dirt)"],
     ["no fever or acute abdomen"],
     "Intestinal nematode infection by Ancylostoma duodenale or Necator americanus whose adult worms attach to small bowel mucosa and consume 0.2 mL blood/worm/day. Diagnosis: Stool microscopy for hookworm ova, CBC showing severe microcytic anemia and eosinophilia. Treatment: Albendazole 400 mg single dose PLUS oral iron therapy (Ferrous sulfate 200 mg TID) for 3-6 months to replenish marrow iron stores."),

    ("ICD10-B67.9", "Echinococcosis / Hydatid Cyst Disease", "B67.9", "General Surgery / Hepatology / Pulmonology", "Parasitic Zoonosis",
     ["hydatid cyst", "echinococcus", "dog tapeworm cyst", "liver cyst with water lily sign", "cyst in lung"],
     ["anaphylactic shock and acute peritonitis secondary to hydatid cyst rupture", "biliary tract obstruction / cholangitis from daughter cyst rupture", "tension pneumothorax from pulmonary cyst rupture"],
     ["large, painless, slowly expanding cystic mass in right hepatic lobe (> 70%) or lung", "dull right upper quadrant heaviness or chronic cough with hemoptysis", "pathognomonic 'water lily sign' (floating collapsed endocyst membranes) or daughter cysts on ultrasound/CT"],
     ["asymptomatic for years due to slow growth (1-5 cm/year)"],
     "Zoonotic larval cestode infection caused by Echinococcus granulosus tapeworms whose definitive hosts are canines. Man is an accidental intermediate host. Diagnostic workup: Ultrasound / CT abdomen showing multilocular cystic lesion with calcified rim (Gharbi classification), Echinococcus IgG ELISA serology. Treatment: PAIR technique (Puncture, Aspiration, Injection of scolicidal agent [hypertonic saline], Re-aspiration) for selected cysts, radical surgical pericystectomy, combined with Albendazole (400 mg BID for 1-6 months)."),

    ("ICD10-A30.9", "Leprosy (Hansen's Disease - Tuberculoid vs Lepromatous)", "A30.9", "Dermatology / Neurology / Infectious Disease", "Infectious Neuropathy",
     ["leprosy", "hansens disease", "hypopigmented patch with no feeling", "thickened nerve", "claw hand", "leonine facies"],
     ["Type 1 reversal reaction (acute neuritis with rapid motor loss / foot drop)", "Type 2 erythema nodosum leprosum (ENL: painful red subcutaneous nodules, fever, uveitis)", "corneal ulceration and blindness from lagophthalmos"],
     ["hypopigmented or erythematous cutaneous macules / plaques with DEFINITE LOSS OF SENSATION (to light touch, pinprick, or temperature)", "thickened, enlarged, tender peripheral nerves (great auricular, ulnar, common peroneal)", "motor deformities: claw hand, wrist drop, trophic non-healing plantar ulcers", "lepromatous signs: diffuse cutaneous infiltration, leonine facies, madarosis (loss of eyebrows)"],
     ["sensory loss distinguishes from vitiligo or fungal tinea"],
     "Chronic granulomatous mycobacterial infection caused by Mycobacterium leprae, primarily targeting cooler tissues: skin, peripheral nerves, and upper respiratory mucosa. Classified by WHO into Paucibacillary (PB: 1-5 skin lesions) and Multibacillary (MB: > 5 lesions). Diagnosis: Slit-skin smear for acid-fast bacilli, nerve biopsy. Treatment: WHO Multi-Drug Therapy (MDT): Rifampicin + Dapsone (+ Clofazimine for MB) for 6-12 months."),

    ("ICD10-A35", "Tetanus (Clostridium Tetani - Lockjaw & Opisthotonus)", "A35", "Emergency Medicine / Critical Care", "Infectious Neurological Emergency",
     ["tetanus", "lockjaw", "trismus with muscle spasm", "opisthotonus", "risus sardonicus", "rusty nail injury"],
     ["laryngeal spasm / respiratory arrest from diaphragmatic spasm", "autonomic instability (labile BP, tachycardia, profuse diaphoresis)", "rhabdomyolysis and hyperpyrexia"],
     ["trismus / lockjaw (painful tonic contraction of masseter muscles preventing mouth opening)", "risus sardonicus (fixed sneering grin from sustained facial muscle contraction)", "opisthotonus (severe backward arching of spine, neck, and heels during paroxysms triggered by noise, light, or touch)", "clear sensorium throughout agonizing spasms (patient remains fully conscious)"],
     ["absence of fever distinguishes early tetanus from meningitis"],
     "Life-threatening neurotoxin-mediated disease caused by tetanospasmin produced by Clostridium tetani spores contaminating puncture wounds, burns, or unsterile umbilical cord cutting. Tetanospasmin retrogradely travels to spinal cord inhibiting GABA and glycine release. Protocol: 1. Human Tetanus Immunoglobulin (HTIG 3,000-6,000 units IM STAT); 2. Tetanus Toxoid vaccine; 3. Wound debridement; 4. IV Metronidazole (500 mg q6h); 5. Muscle spasm control (IV Diazepam / Midazolam infusions, IV Magnesium Sulfate); 6. Early elective tracheostomy and mechanical ventilation in quiet dark room."),

    ("ICD10-A36.9", "Diphtheria (Corynebacterium Diphtheriae - Bull-Neck Diphtheria)", "A36.9", "Pediatrics / ENT / Infectious Disease", "Infectious Airway Emergency",
     ["diphtheria", "pseudomembrane in throat", "bull neck", "stridor child throat membrane", "corynebacterium diphtheriae"],
     ["airway obstruction from membrane detachment causing sudden asphyxiation", "diphtheritic myocarditis (arrhythmias, heart failure on day 7-14)", "neuropathy (palatal paralysis with nasal regurgitation, polyneuritis)"],
     ["dense, dirty-grey, adherent fibrinous pseudomembrane firmly attached to tonsils, uvula, and pharynx that BLEEDS PROFUSELY when dislodged", "massive tender bilateral cervical lymphadenopathy and soft tissue edema producing pathognomonic 'bull-neck' appearance", "brassy barking cough, inspiratory stridor, and low-grade fever with disproportionate toxic prostration"],
     ["firm adherence of membrane distinguishes from easily scrapable candida thrush"],
     "Acute toxin-mediated infection by Corynebacterium diphtheriae producing diphtheria exotoxin which inhibits cellular protein synthesis. Statutory emergency. Treatment: Immediate Diphtheria Antitoxin (DAT: 20,000 - 100,000 units IV depending on extent) STAT without waiting for lab confirmation; IV Aqueous Penicillin G or oral Erythromycin for 14 days; Strict droplet isolation; Close monitoring for airway compromise and ECG monitoring for myocarditis."),

    ("ICD10-B27.9", "Infectious Mononucleosis (Epstein-Barr Virus - Glandular Fever)", "B27.9", "Infectious Disease / Pediatrics / ENT", "Infectious",
     ["infectious mononucleosis", "mono", "glandular fever", "ebv", "kissing disease", "atypical lymphocytes", "splenomegaly with sore throat"],
     ["traumatic or spontaneous splenic rupture (sudden severe LUQ pain and hemorrhagic shock)", "airway compromise from massive tonsillar enlargement", "autoimmune hemolytic anemia"],
     ["classic triad: 1. High fever; 2. Severe exudative pharyngitis with enlarged tonsils; 3. Symmetrical posterior cervical and generalized lymphadenopathy", "splenomegaly (present in > 50%) and hepatomegaly with mild transaminase elevation", "pathognomonic maculopapular rash appearing 5-7 days after taking Ampicillin or Amoxicillin"],
     ["negative rapid strep test", "absence of bacterial response to beta-lactams"],
     "Acute viral illness caused by Epstein-Barr Virus (EBV / Human Herpesvirus 4) spread by saliva ('kissing disease') infecting B-lymphocytes. Diagnostic workup: Heterophile antibody test (Monospot test), CBC showing absolute lymphocytosis with > 10% atypical reactive lymphocytes (Downey cells), EBV viral capsid antigen (VCA) IgM. Treatment: Supportive care (hydration, analgesia); STRICT AVOIDANCE of contact sports and heavy lifting for minimum 3-4 weeks to prevent catastrophic splenic rupture; Systemic steroids indicated only for airway obstruction or severe thrombocytopenia."),

    # 2. Neoplasms & Oncology Presentations
    ("ICD10-C34.9", "Bronchogenic Carcinoma & Pancoast Tumor Syndrome", "C34.9", "Pulmonology / Oncology", "Thoracic Oncology",
     ["lung cancer", "bronchogenic carcinoma", "coughing blood smoker", "pancoast tumor", "horner syndrome", "hemoptysis weight loss"],
     ["superior vena cava (SVC) syndrome (facial edema, neck vein distension, upper extremity plethora)", "malignant spinal cord compression from vertebral metastasis", "hypercalcemia of malignancy (confusion, polyuria, qt shortening)"],
     ["new-onset persistent cough or change in character of chronic smoker cough lasting > 3 weeks", "recurrent hemoptysis (coughing blood) and progressive exertional dyspnea", "unexplained rapid weight loss, anorexia, and digital clubbing", "Pancoast tumor (apical sulcus): shoulder/arm pain (C8-T1 distribution) PLUS Horner syndrome (unilateral ptosis, miosis, anhidrosis, enophthalmos)"],
     ["absence of acute infective fever or sputum response to antibiotics"],
     "Malignant epithelial tumor of the bronchopulmonary tree (Non-Small Cell [NSCLC 85%] vs Small Cell [SCLC 15%]), strongly correlated with tobacco smoking. Diagnostic workup: Contrast CT thorax/upper abdomen, bronchoscopy with transbronchial biopsy or CT-guided core biopsy, PET-CT staging, molecular profiling (EGFR, ALK, ROS1, PD-L1). Treatment: Surgical resection (lobectomy) for early stage NSCLC; Chemoradiotherapy, targeted Tyrosine Kinase Inhibitors (Osimertinib), or Immunotherapy (Pembrolizumab)."),

    ("ICD10-C18.9", "Colorectal Carcinoma (Left vs Right Sided)", "C18.9", "Gastroenterology / Surgical Oncology", "Gastrointestinal Oncology",
     ["colorectal cancer", "colon cancer", "rectal bleeding in elderly", "change in bowel habits", "pencil stools", "iron deficiency anemia male"],
     ["acute complete large bowel obstruction (vomiting, distension, obstipation)", "colonic perforation with acute fecal peritonitis", "massive lower GI hemorrhage"],
     ["Right-sided (caecal/ascending): insidious occult bleeding producing profound microcytic iron deficiency anemia, unexplained fatigue, and palpable right iliac fossa mass", "Left-sided (descending/sigmoid): progressive change in bowel habits (alternating constipation and diarrhea), narrowing of stool caliber ('pencil stools'), and visible hematochezia / red blood mixed with stool", "unintentional weight loss and tenesmus in rectal cancer"],
     ["absence of painful external anal pathology (differentiates from hemorrhoids/fissure)"],
     "Adenocarcinoma arising from epithelial lining of colon or rectum, predominantly progressing through adenoma-carcinoma sequence (APC, KRAS, p53 mutations) or Lynch syndrome (MSI-H). Diagnostic workup: Complete colonoscopy with biopsy (gold standard), CEA tumor marker, Contrast CT chest/abdomen/pelvis staging, MRI pelvis for rectal cancer. Treatment: Oncological resection (hemicolectomy / low anterior resection) with regional lymphadenectomy + adjuvant FOLFOX chemotherapy."),

    ("ICD10-C50.9", "Invasive Breast Carcinoma & Paget Disease", "C50.9", "Surgical Oncology / Breast Surgery", "Oncology",
     ["breast cancer", "breast lump", "peau d orange breast", "nipple retraction", "paget disease of nipple", "hard fixed breast lump"],
     ["inflammatory breast carcinoma (rapid fiery erythema, edema, peau d'orange mimicking mastitis but refractory to antibiotics)", "pathological fracture or spinal cord compression from bone metastasis"],
     ["painless, hard, irregular, solitary breast mass that is fixed to underlying pectoralis muscle or overlying skin", "skin tethering, dimpling, or nipple retraction / inversion", "peau d'orange (coarse orange-peel pitting of breast skin from dermal lymphatic invasion)", "unilateral spontaneous bloody or serous nipple discharge", "hard matted non-tender axillary lymphadenopathy", "Paget disease: persistent eczema-like, crusting, scaling lesion of the nipple-areolar complex"],
     ["distinct from cyclic bilateral tender nodularity of fibrocystic disease"],
     "Malignant neoplasm of breast epithelial tissue (Invasive Ductal Carcinoma 80%, Invasive Lobular 10-15%). Triple Assessment (The Gold Standard): 1. Clinical breast examination; 2. Imaging (Bilateral Digital Mammography + High-Resolution Breast Ultrasound; Breast MRI in young/dense breasts); 3. Pathological confirmation via Core Needle Biopsy with ER, PR, HER2-neu, and Ki-67 immunohistochemistry. Treatment: Breast-conserving surgery (lumpectomy) or modified radical mastectomy + Sentinel Lymph Node Biopsy (SLNB); Adjuvant/neoadjuvant chemotherapy, targeted Trastuzumab (HER2+), and hormonal therapy (Tamoxifen, Anastrozole)."),

    ("ICD10-C90.0", "Multiple Myeloma (Plasma Cell Dyscrasia - CRAB Criteria)", "C90.0", "Hematology / Oncology", "Hematological Malignancy",
     ["multiple myeloma", "crab criteria", "punched out bone lesions", "bence jones protein", "rouleaux formation", "hypercalcemia bone pain"],
     ["spinal cord compression from pathological vertebral collapse", "hypercalcemic crisis (confusion, coma, cardiac arrhythmias)", "acute hyperviscosity syndrome (retinal hemorrhages, stroke, mucosal bleeding)", "acute light-chain cast nephropathy / myeloma kidney"],
     ["the CRAB diagnostic criteria: 1. Calcium elevation (serum calcium > 11 mg/dL); 2. Renal insufficiency (creatinine > 2 mg/dL); 3. Anemia (normocytic normochromic Hb < 10 g/dL); 4. Bone lesions (lytic 'punched-out' bone lesions or pathological fractures, persistent deep back/rib pain)", "erythrocyte sedimentation rate (ESR) markedly elevated (> 100 mm/hr)", "recurrent bacterial infections (pneumonia, pyelonephritis from hypogammaglobulinemia)", "Rouleaux formation on peripheral blood smear"],
     ["absence of blastic/sclerotic bone lesions (lytic only)"],
     "Clonal neoplastic proliferation of plasma cells in the bone marrow producing excess monoclonal immunoglobulin (M-protein: IgG 50%, IgA 20%, or free light chains). Diagnostic workup: Serum and Urine Protein Electrophoresis (SPEP/UPEP) showing dense monoclonal M-spike, Serum Free Light Chain (sFLC) ratio, Bone Marrow Biopsy (> 10% clonal plasma cells), Whole-body low-dose CT or skeletal survey. Treatment: Triplet induction therapy (Bortezomib + Lenalidomide + Dexamethasone [VRd]); Autologous Stem Cell Transplantation (ASCT); Bisphosphonates (Zoledronic acid) for bone disease; Dialysis for myeloma kidney."),

    # 3. Endocrine, Nutritional & Metabolic
    ("ICD10-E21.0", "Primary Hyperparathyroidism (Hypercalcemic Stones, Bones, Groans)", "E21.0", "Endocrinology / Endocrine Surgery", "Endocrine",
     ["hyperparathyroidism", "high calcium", "bones stones groans", "parathyroid adenoma", "recurrent kidney stones"],
     ["hypercalcemic crisis (serum calcium > 14 mg/dL with confusion, cardiac arrhythmias, shortened QT)", "acute pancreatitis"],
     ["the classic mnemonic: 'Bones (osteopenia, subperiosteal bone resorption on radial side of digits, osteitis fibrosa cystica), Stones (recurrent nephrolithiasis/calcium phosphate renal calculi), Abdominal Groans (anorexia, nausea, constipation, peptic ulcer, pancreatitis), and Psychic Moans (fatigue, depression, cognitive impairment)'", "concomitant elevation of BOTH serum calcium AND intact parathyroid hormone (iPTH)"],
     ["absence of hypocalcemia", "normal serum alkaline phosphatase unless severe bone disease"],
     "Autonomous hypersecretion of parathyroid hormone (PTH), > 85% caused by a single benign parathyroid adenoma. Diagnosis: Serum total and ionized calcium, intact PTH, 24-hour urinary calcium excretion (differentiates from Familial Hypocalciuric Hypercalcemia), Sestamibi parathyroid scan and neck ultrasound. Treatment: Parathyroidectomy is the definitive curative treatment; Hydration with IV normal saline and bisphosphonates for acute hypercalcemic crisis."),

    ("ICD10-E27.1", "Primary Adrenal Insufficiency & Addisonian Crisis", "E27.1", "Endocrinology / Emergency Medicine", "Endocrine Emergency",
     ["addison disease", "adrenal crisis", "hyperpigmentation skin", "low sodium high potassium", "cortisol deficiency", "postural hypotension"],
     ["ADDISONIAN CRISIS: severe refractory hypotensive shock unresponsive to vasopressors and fluids", "severe hyperkalemic cardiac arrest", "hypoglycemic seizure / coma"],
     ["striking bronze hyperpigmentation of skin in sun-exposed areas and friction zones, accompanied by dark pigmentation of palmar creases, buccal mucosa, and surgical scars (due to high ACTH stimulating melanocytes)", "severe persistent orthostatic postural hypotension, salt craving, and chronic fatigue", "lab derangements: hyponatremia (low Na+), hyperkalemia (high K+), and non-anion gap metabolic acidosis from aldosterone deficiency"],
     ["hyperpigmentation is absent in secondary adrenal insufficiency (low ACTH)"],
     "Destruction of all layers of the adrenal cortex, most commonly autoimmune adrenalitis (Addison's) in developed nations or tuberculosis (adrenal TB) in developing countries. Diagnostic workup: Morning 8 AM serum cortisol (< 3 mcg/dL), plasma ACTH (markedly elevated), ACTH stimulation test (Synacthen test: failure of cortisol to rise > 18 mcg/dL). Acute Crisis Management: 1. STAT IV Hydrocortisone (100 mg IV bolus followed by 100 mg q8h); 2. Aggressive IV resuscitation with 0.9% Normal Saline with 5% Dextrose (treats hypotension, hyponatremia, hypoglycemia); 3. Oral Fludrocortisone (0.1 mg daily) added for chronic maintenance."),

    ("ICD10-E24.9", "Cushing Syndrome & Hypercortisolemia", "E24.9", "Endocrinology", "Endocrine",
     ["cushing syndrome", "moon face", "buffalo hump", "purple abdominal striae", "central obesity thin limbs", "high cortisol"],
     ["hypertensive encephalopathy / stroke", "severe opportunistic fungal/bacterial infections", "acute psychosis"],
     ["classic cushingoid habitus: progressive central truncal obesity with moon facies, supraclavicular fat pads, and dorsocervical 'buffalo hump', contrasting with wasted thin limbs (proximal muscle myopathy)", "wide (> 1 cm), violaceous, reddish-purple cutaneous striae on abdomen, flanks, and breasts", "skin fragility with easy bruising and poor wound healing", "hirsutism, acne, secondary amenorrhea, and new-onset hypertension and diabetes"],
     ["absence of striae or muscle weakness makes cushing unlikely"],
     "Signs and symptoms resulting from prolonged exposure to inappropriately high levels of glucocorticoids, most commonly exogenous iatrogenic steroid use, pituitary ACTH-secreting adenoma (Cushing's Disease 70%), or adrenal tumors. Diagnostic workup: 24-hour urinary free cortisol (UFC), overnight 1mg Dexamethasone Suppression Test (DST: failure to suppress cortisol < 1.8 mcg/dL), late-night salivary cortisol. Plasma ACTH measurement to distinguish ACTH-dependent from ACTH-independent causes."),

    ("ICD10-E51.1", "Thiamine Deficiency & Wernicke-Korsakoff Syndrome", "E51.1", "Neurology / Endocrinology / Emergency Medicine", "Nutritional Neurological",
     ["thiamine deficiency", "wernicke encephalopathy", "beriberi", "korsakoff psychosis", "ataxia confusion ophthalmoplegia"],
     ["irreversible Korsakoff amnesic confabulatory dementia if thiamine delayed", "acute high-output wet beriberi heart failure and shock"],
     ["classic Wernicke triad: 1. Encephalopathy (acute confusion, apathy, disorientation); 2. Oculomotor dysfunction (bilateral horizontal nystagmus, lateral rectus / CN VI palsy, conjugate gaze palsy); 3. Gait ataxia (wide-based unsteady gait)", "history of chronic alcohol abuse, hyperemesis gravidarum, prolonged fasting, or bariatric surgery", "Wet Beriberi: high-output congestive heart failure, bounding pulses, peripheral edema; Dry Beriberi: symmetrical peripheral sensorimotor neuropathy"],
     ["no focal motor stroke deficits"],
     "Critical nutritional emergency caused by deficiency of Vitamin B1 (thiamine pyrophosphate), a key coenzyme in cerebral carbohydrate metabolism. Medical imperative: Thiamine MUST ALWAYS be administered BEFORE any intravenous glucose solutions to prevent acute cerebral metabolic collapse. Protocol: High-dose IV Thiamine (Pabrinex: 500 mg IV TID for 3-5 days, then 250 mg daily); prompt reversal of ophthalmoplegia within hours confirms diagnosis."),

    ("ICD10-E53.8", "Pernicious Anemia & Subacute Combined Degeneration of Cord", "E53.8", "Hematology / Neurology", "Hematological Neurological",
     ["vitamin b12 deficiency", "pernicious anemia", "subacute combined degeneration", "loss of vibration position sense", "megaloblastic anemia", "beefy red tongue"],
     ["irreversible spastic paraparesis and permanent spinal cord ataxia", "pancytopenia and severe symptomatic anemia"],
     ["triad: 1. Megaloblastic anemia symptoms (fatigue, lemon-yellow pallor, dyspnea); 2. Atrophic glossitis (smooth, painful, beefy-red raw tongue / Hunter glossitis); 3. Neurological dysfunction (Subacute Combined Degeneration: loss of vibration and proprioception / joint position sense, sensory ataxia, positive Romberg sign, spasticity, and extensor plantar responses)", "hypersegmented neutrophils (>= 5 lobes in > 5% of PMNs) on peripheral blood smear"],
     ["folate deficiency DOES NOT cause neurological degeneration (crucial distinction)"],
     "Autoimmune destruction of gastric parietal cells leading to loss of Intrinsic Factor (IF) and inability to absorb Vitamin B12 in the terminal ileum. CRITICAL PEARL: Treating B12 deficiency with folic acid alone corrects anemia while allowing neurological destruction to progress irreversibly. Diagnostic workup: Serum Vitamin B12 (< 200 pg/mL), elevated serum methylmalonic acid (MMA) and homocysteine, Anti-Intrinsic Factor and Anti-Parietal Cell antibodies. Treatment: Intramuscular Cyanocobalamin / Hydroxocobalamin (1000 mcg IM daily for 1 week, then weekly for 1 month, then monthly for life)."),

    # 4. Neurological & Sense Organs
    ("ICD10-G44.00", "Cluster Headache (Trigeminal Autonomic Cephalgia)", "G44.00", "Neurology", "Neurological",
     ["cluster headache", "suicide headache", "severe eye pain with runny nose", "unilateral headache behind eye", "cluster attacks at night"],
     ["severe behavioral agitation, pacing, and suicidal ideation during agonizing attacks"],
     ["excruciating, strictly unilateral orbital, supraorbital, or temporal pain described as a 'hot poker in the eye', lasting 15-180 minutes", "accompanied by ipsilateral cranial parasympathetic autonomic features: conjunctival injection, lacrimation (eye tearing), nasal congestion, rhinorrhea, forehead sweating, and partial Horner syndrome (ptosis/miosis)", "striking circadian and circannual periodicity (attacks strike at same hour each night, clustering for weeks followed by remission)", "patient is intensely agitated and paces the room (differentiates from migraineur who prefers dark quiet stillness)"],
     ["no visual aura preceding pain", "absence of nausea and vomiting in typical attacks"],
     "Severe primary headache disorder classified under Trigeminal Autonomic Cephalgias (TACs), predominantly affecting males. Acute abortive treatment: 100% High-Flow Oxygen (12-15 L/min via non-rebreather mask for 15-20 min - response within 10 min is diagnostic) PLUS subcutaneous Sumatriptan (6 mg). Prophylactic maintenance: Oral Verapamil (high-dose 240-960 mg daily with ECG PR-interval monitoring)."),

    ("ICD10-G50.0", "Trigeminal Neuralgia (Tic Douloureux)", "G50.0", "Neurology / Neurosurgery", "Neurological",
     ["trigeminal neuralgia", "tic douloureux", "electric shock face pain", "facial pain touching cheek", "stabbing cheek pain"],
     ["severe weight loss and dehydration from inability to eat or drink due to fear of triggering pain attacks", "depression"],
     ["sudden, brief (< 1-2 seconds), excruciating, paroxysmal, electric-shock-like, stabbing pain strictly confined to distribution of one or more divisions of Cranial Nerve V (maxillary V2 or mandibular V3, rarely ophthalmic V1)", "attacks triggered by trivial non-noxious mechanical stimuli: light touch, shaving, washing face, brushing teeth, eating, talking, or cool breeze", "presence of identifiable cutaneous or intraoral 'trigger zones'", "refractory period between paroxysms during which pain cannot be triggered"],
     ["neurological examination is ENTIRELY NORMAL (any sensory loss or motor deficit indicates secondary trigeminal neuropathy)"],
     "Severe neuropathic facial pain syndrome, most commonly caused by neurovascular compression of the trigeminal sensory nerve root entry zone by an aberrant arterial loop (Superior Cerebellar Artery). First-line medical therapy: Carbamazepine (100-200 mg BID titrated to 800-1200 mg/day; monitor CBC for agranulocytosis and LFTs) or Oxcarbazepine. Surgical cure: Microvascular Decompression (Jannetta procedure) via retrosigmoid craniotomy."),

    ("ICD10-G20", "Parkinson's Disease (Idiopathic TRAP Signs)", "G20", "Neurology", "Neurodegenerative",
     ["parkinson disease", "resting tremor", "pill rolling tremor", "parkinsonism", "shuffling gait", "frozen gait", "cogwheel rigidity"],
     ["aspiration pneumonia from progressive dysphagia", "severe postural instability with frequent falls and hip fractures", "dopamine dysregulation syndrome"],
     ["the classic cardinal motor tetrad (TRAP): 1. Tremor (4-6 Hz resting 'pill-rolling' tremor of the hands, disappearing during purposeful voluntary action and sleep); 2. Rigidity ('cogwheel' or 'lead-pipe' resistance on passive limb movement); 3. Akinesia / Bradykinesia (progressive slowness, loss of facial expression / masked facies, hypophonia, micrographic small handwriting); 4. Postural instability (stooped forward posture, festinating shuffling small-stepped gait with reduced arm swing and en bloc turning)", "asymmetric onset with persistent asymmetry throughout disease course"],
     ["robust clinical improvement with Levodopa trial (confirms diagnosis)", "no early gaze palsy (excludes PSP) or early autonomic failure (excludes MSA)"],
     "Progressive neurodegenerative disorder characterized by loss of dopaminergic neurons in the substantia nigra pars compacta and intraneuronal Lewy bodies (alpha-synuclein). Treatment: Levodopa-Carbidopa (gold standard); Dopamine Agonists (Pramipexole); MAO-B inhibitors (Rasagiline); Deep Brain Stimulation (DBS) of subthalamic nucleus for advanced motor fluctuations."),

    ("ICD10-H81.1", "Benign Paroxysmal Positional Vertigo (BPPV - Canalithiasis)", "H81.1", "ENT / Neurology", "Vestibular",
     ["bppv", "positional vertigo", "dizzy turning head", "room spinning looking up", "dix hallpike", "epley maneuver"],
     ["injury or fractures sustained from sudden violent fall during positional turn"],
     ["brief, violent, episodic rotational vertigo (room spinning) lasting LESS THAN 60 SECONDS", "triggered strictly by changes in head position relative to gravity: turning over in bed, looking up at ceiling, or bending forward", "Dix-Hallpike positional maneuver reproduces the vertigo AND elicits pathognomonic torsional geotropic nystagmus with latency (2-5s) and fatigability", "complete absence of hearing loss, tinnitus, or neurological focal deficits"],
     ["no hearing loss or ear fullness (differentiates from Meniere disease)"],
     "Most common cause of peripheral vertigo, caused by free-floating calcium carbonate otoconia (canalithiasis) dislodged from the utricle into the posterior semicircular canal. Definitive bedside treatment: Particle repositioning maneuvers (Epley Maneuver for posterior canal; Semont maneuver) achieves > 85-90% instant cure without medications."),

    ("ICD10-H81.0", "Ménière's Disease (Endolymphatic Hydrops)", "H81.0", "ENT / Audiology", "Vestibular / Inner Ear",
     ["meniere disease", "endolymphatic hydrops", "vertigo with ringing in ear", "fluctuating hearing loss", "ear fullness with dizziness"],
     ["Tumarkin drop attacks (sudden catastrophic fall without loss of consciousness from otolithic crisis)", "permanent severe sensorineural hearing loss"],
     ["classic clinical tetrad: 1. Spontaneous recurrent episodes of rotational vertigo lasting 20 minutes to several hours; 2. Fluctuating low-frequency Sensorineural Hearing Loss (SNHL documented on audiometry); 3. Low-pitched roaring tinnitus in affected ear; 4. Aural fullness (sensation of pressure or plugging in affected ear)", "symptoms fluctuate, with hearing deteriorating during attacks and partially improving in early stages"],
     ["vertigo lasts hours (not seconds like BPPV)", "audiogram demonstrates low-frequency sensorineural deficit"],
     "Inner ear disorder characterized by excessive accumulation of endolymphatic fluid (endolymphatic hydrops) causing distension and periodic micro-ruptures of the membranous labyrinth. Treatment: Acute attacks: Vestibular suppressants (Betahistine, Dimenhydrinate); Long-term prevention: Low-salt diet (< 1.5-2 g/day), caffeine and alcohol restriction, oral Thiazide diuretics, intratympanic dexamethasone or gentamicin for refractory disease.")
]

# Append protocols
added = 0
for d in CONDITIONS:
    if d[0] not in existing_ids and d[1].lower() not in existing_topics:
        protocols.append({
            "id": d[0],
            "topic": d[1],
            "icd10": d[2],
            "specialty": d[3],
            "organ_system": d[4],
            "keywords": d[5],
            "red_flags": d[6],
            "clinical_hallmarks": d[7],
            "pertinent_negatives": d[8],
            "content": d[9]
        })
        existing_ids.add(d[0])
        existing_topics.add(d[1].lower())
        added += 1

print(f"Added {added} detailed protocols. Total so far: {len(protocols)}")

with open(KB_PATH, "w", encoding="utf-8") as f:
    json.dump(protocols, f, indent=2, ensure_ascii=False)

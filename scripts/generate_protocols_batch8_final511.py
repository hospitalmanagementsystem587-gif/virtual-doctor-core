#!/usr/bin/env python3
"""
Batch 8: Crosses 510+ protocols (Final expansion to 513).
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
    {
        "id": "ICD10-K61.0",
        "topic": "Acute Perianal & Ischiorectal Abscess (Cryptoglandular Drainage)",
        "icd10": "K61.0",
        "specialty": "Colorectal Surgery / General Surgery / Emergency Medicine",
        "organ_system": "Colorectal Surgical Emergency",
        "keywords": ["perianal abscess", "ischiorectal abscess", "throbbing anal pain sitting", "perianal fluctuant mass", "cruciate incision drainage", "cryptoglandular infection"],
        "red_flags": ["necrotizing fasciitis (Fournier gangrene)", "pelvic sepsis and horseshoe abscess extension", "fistula-in-ano formation"],
        "clinical_hallmarks": ["acute onset of constant, agonizing, throbbing, severe perianal or buttock pain that is MARKEDLY AGGRAVATED BY SITTING, WALKING, COUGHING, OR DEFECATION", "fever, chills, and malaise; difficulty and pain during micturition", "Perianal Abscess (most common 60%): visible, tender, erythematous, warm, FLUCTUANT SWELLING directly at the anal verge", "Ischiorectal Abscess (20-25%): deep, diffuse, brawny, exquisitely tender induration in the ischiorectal fossa; may lack superficial redness in early stages but produces excruciating pain on gentle rectal digital examination or buttock pressure", "predominant etiology: acute bacterial infection of the intersphincteric anal crypt glands (cryptoglandular hypothesis) involving E. coli, Bacteroides fragilis, and Enterococcus"],
        "pertinent_negatives": ["presence of fluctuant perianal mass warrants immediate drainage without waiting for antibiotic trial"],
        "content": "Suppurative infection arising in anal glands within the intersphincteric space, tracking downwards (perianal) or through external sphincter into ischioanal fossa. Emergency Rule: Abscesses in the anal region MUST BE SURGICALLY DRAINED IMMEDIATELY upon diagnosis; antibiotics alone are ineffective and lead to extensive tissue necrosis. Protocol: 1. STAT Emergency Incision and Drainage (I&D): Cruciate or elliptical skin excision over point of maximum fluctuance as close as possible to the anal verge (to minimize fistula tract length); 2. Breakdown of all internal loculations with gentle gloved finger; 3. Loose packing with iodophor gauze (removed at 24 hours); 4. Twice-daily warm sitz baths; 5. Antibiotics indicated only for concomitant cellulitis, diabetes, immunosuppression, or systemic sepsis."
    },
    {
        "id": "ICD10-M77.10",
        "topic": "Lateral Epicondylitis (Tennis Elbow - Cozen's Test & ECRB)",
        "icd10": "M77.10",
        "specialty": "Orthopedics / Sports Medicine / Primary Care",
        "organ_system": "Musculoskeletal Enthesopathy",
        "keywords": ["lateral epicondylitis", "tennis elbow", "cozen test", "extensor carpi radialis brevis ecrb", "lateral elbow pain shaking hands", "mills test", "counterforce forearm brace"],
        "red_flags": ["radial tunnel syndrome (posterior interosseous nerve entrapment)", "osteochondritis dissecans of the capitellum in young throwing athletes"],
        "clinical_hallmarks": ["predominantly affects adults aged 35 to 55 years (racquet athletes, manual laborers, typists, carpenters involving repetitive wrist extension and forearm pronation/supination)", "insidious onset of aching pain over the LATERAL PROMINENCE OF THE ELBOW, radiating down the extensor surface of the forearm", "pain is aggravated by gripping objects, shaking hands, turning doorknobs, or lifting a coffee cup ('coffee cup sign')", "PHYSICAL EXAMINATION HALLMARK: EXQUISITE, SHARPLY LOCALIZED POINT TENDERNESS DIRECTLY OVER THE LATERAL EPICONDYLE and approximately 1-2 cm distal into the tendon of the Extensor Carpi Radialis Brevis (ECRB)", "PATHOGNOMONIC PROVOCATIVE TESTS:", "1. COZEN'S TEST (positive: with elbow flexed to 90 degrees and forearm pronated, resisted active wrist extension with radial deviation reproduces severe lateral elbow pain);", "2. MILL'S TEST (passive wrist flexion with elbow extended stretches extensor muscles, reproducing pain);", "3. Resisted active extension of the middle finger (Maudsley test - stresses ECRB/EDC)"],
        "pertinent_negatives": ["normal passive elbow range of motion distinguishes epicondylitis from true intra-articular elbow arthritis"],
        "content": "Angiofibroblastic tendinosis (repetitive micro-tearing and degenerative vascular/collagen breakdown) at the origin of the Extensor Carpi Radialis Brevis (ECRB) muscle at the lateral humeral epicondyle. Treatment Protocol: 1. First-line Conservative: Activity modification, ergonomic adjustments, ice massage, and oral NSAIDs; 2. Counterforce Forearm Strap / Tennis Elbow Brace (worn 2-3 cm distal to epicondyle to dissipate muscle tension); 3. Eccentric extensor strengthening physiotherapy (Tyler twist using flexible resistance bar); 4. Ultrasound-guided Platelet-Rich Plasma (PRP) or Autologous Blood injection for chronic recalcitrant tendinosis (> 6 months); 5. Corticosteroid injections provide short-term pain relief but worsen long-term recurrence rates; 6. Surgical ECRB debridement and release for refractory cases."
    },
    {
        "id": "ICD10-M23.20",
        "topic": "Acute Meniscal Tear (Joint Line Tenderness & McMurray Test)",
        "icd10": "M23.20",
        "specialty": "Orthopedics / Sports Medicine / Trauma Surgery",
        "organ_system": "Knee Intra-Articular",
        "keywords": ["meniscal tear", "bucket handle meniscus tear", "mcmurray test", "joint line tenderness knee", "knee locking catching", "delayed knee effusion", "arthroscopic partial meniscectomy"],
        "red_flags": ["locked knee (bucket-handle tear wedged in intercondylar notch requiring urgent arthroscopy)", "secondary accelerated knee osteoarthritis"],
        "clinical_hallmarks": ["history of a twisting / rotational injury to a weight-bearing, flexed knee in athletes OR trivial squatting/turning in older adults with degenerative meniscal tissue", "patient frequently describes feeling a 'POP' OR 'TEARING' SENSATION on either medial or lateral side of the knee", "CARDINAL MECHANICAL SYMPTOMS: 1. MECHANICAL TRUE LOCKING (sudden inability to fully straighten or extend the knee due to a displaced bucket-handle fragment mechanically jamming the joint); 2. Catching, clicking, or giving way sensation during pivoting movements", "EFFUSION EVOLUTION: MILD-TO-MODERATE KNEE EFFUSION DEVELOPING GRADUALLY OVER 24 TO 48 HOURS post-injury (in sharp contrast to immediate hemarthrosis of ACL tear)", "DIAGNOSTIC CLINICAL TESTS:", "1. JOINT LINE TENDERNESS (SINGLE MOST SENSITIVE CLINICAL SIGN > 85%): exquisite point tenderness on firm palpation along the medial or lateral tibiofemoral joint line;", "2. MCMURRAY'S TEST (positive: with patient supine and knee flexed, axial loading with internal/external tibial rotation while extending the knee elicits a PALPABLE OR AUDIBLE 'CLICK' AND SHARP PAIN at the joint line);", "3. Apley's Compression Test and Thessaly Test (dynamic weight-bearing rotation at 20 degrees flexion)", "MRI of Knee (gold standard, accuracy > 90%): linear high signal traversing the meniscal substance and contacting an articular surface"],
        "pertinent_negatives": ["absence of true mechanical locking distinguishes stable tears from displaced bucket-handle tears"],
        "content": "Disruption of the fibrocartilaginous medial (more common, C-shaped) or lateral (O-shaped) meniscus. Tears in the peripheral vascularized 'red-red zone' (outer 10-25%) have high intrinsic healing capacity; tears in the avascular 'white-white zone' cannot heal spontaneously. Protocol: 1. Locked Knee: Urgent Arthroscopic Reduction and Meniscal Repair/Debridement; 2. Degenerative non-obstructive tears: Non-operative physical therapy and quadriceps strengthening; 3. Acute athletic tears: Arthroscopic Meniscal Repair (inside-out or all-inside suture fixation) is the preferred gold standard to preserve long-term chondroprotective joint biomechanics; Partial Meniscectomy performed only when tear is non-repairable."
    },
    {
        "id": "ICD10-G57.60",
        "topic": "Morton's Neuroma (Interdigital Perineural Fibrosis & Mulder's Click)",
        "icd10": "G57.60",
        "specialty": "Podiatry / Orthopedics / Primary Care",
        "organ_system": "Foot Compressive Neuropathy",
        "keywords": ["mortons neuroma", "interdigital neuroma", "mulders click sign", "pebble in shoe pain", "third intermetatarsal space pain", "burning forefoot pain", "high heels narrow shoes"],
        "red_flags": ["metatarsal stress fracture (swelling and dorsal bone tenderness)", "intractable chronic foot pain with walking limitation"],
        "clinical_hallmarks": ["predominantly affects women (female:male 5:1), strongly associated with wearing NARROW, POINTED-TOE SHOES OR HIGH HEELS", "CARDINAL PATHOGNOMONIC SYMPTOM: BURNING, ELECTRIC-SHOCK, OR SHARP SHOOTING PAIN IN THE FOREFOOT, radiating into the adjacent toes, universally described as 'WALKING ON A PEBBLE OR FOLDED SOCK IN MY SHOE'", "pain is characteristically relieved by removing shoes, resting, and vigorously massaging the forefoot", "PATHOGNOMONIC ANATOMICAL LOCATION: THIRD INTERMETATARSAL SPACE (between the 3rd and 4th metatarsal heads in > 80-85% of cases, because the 3rd common digital nerve receives anastomotic branches from both medial and lateral plantar nerves, making it thicker and tethered under the deep transverse metatarsal ligament)", "PATHOGNOMONIC PHYSICAL EXAMINATION SIGN: POSITIVE MULDER'S SIGN / MULDER'S CLICK (with the examiner's thumb and index finger applying direct plantar-to-dorsal pressure in the 3rd intermetatarsal space, the other hand squeezes the metatarsal heads transversely together: this produces a PALPABLE, AUDIBLE 'CLICK' AND SHARP PAIN as the enlarged neuroma subluxes plantarly)"],
        "pertinent_negatives": ["dorsal metatarsal tenderness with swelling indicates metatarsal stress fracture, NOT interdigital neuroma"],
        "content": "Perineural fibrosis, endoneurial edema, and demyelination of the common plantar digital nerve as it passes beneath the rigid deep transverse metatarsal ligament. Treatment Protocol: 1. Conservative (cures 70-80%): Wide toe-box shoes with low heels, metatarsal pads (placed proximal to metatarsal heads to elevate and splay them apart), and activity modification; 2. Ultrasound-Guided Corticosteroid Injection (Triamcinolone 20-40 mg + local anesthetic into the 3rd web space via dorsal approach) provides marked long-term pain relief; 3. Surgical Neurectomy: Excision of the Morton's neuroma via dorsal longitudinal incision for chronic refractory pain."
    },
    {
        "id": "ICD10-K56.0",
        "topic": "Paralytic Ileus (Adynamic Bowel & Postoperative Hypokalemia)",
        "icd10": "K56.0",
        "specialty": "General Surgery / Critical Care / Gastroenterology",
        "organ_system": "Gastrointestinal Neuro-Motility",
        "keywords": ["paralytic ileus", "adynamic ileus", "postoperative ileus", "absent bowel sounds silent abdomen", "diffuse gas small and large bowel", "hypokalemia ileus", "opioid induced ileus"],
        "red_flags": ["anastomotic leak with secondary peritonitis", "ischemic bowel", "severe electrolyte derangement (hypokalemia, hypomagnesemia)"],
        "clinical_hallmarks": ["develops typically following abdominal surgery (physiologic postoperative ileus resolves: small bowel 24h, stomach 24-48h, colon 48-72h; prolonged ileus persists > 3-5 days)", "secondary etiologies: SEVERE HYPOKALEMIA, hypomagnesemia, high-dose IV opioids, retroperitoneal hematoma, acute pancreatitis, or sepsis", "diffuse, dull abdominal fullness, bloating, mild non-colicky discomfort, nausea, and bilious vomiting upon feeding attempt", "complete absence of passage of flatus and feces", "PATHOGNOMONIC PHYSICAL EXAMINATION FINDING: COMPLETE AND PROFOUND ABSENCE OF BOWEL SOUNDS ON PROLONGED AUSCULTATION ('THE SILENT ABDOMEN' - auscultate for minimum 2-3 full minutes in each quadrant)", "abdomen is diffusely distended and non-tender (or mild generalized discomfort without peritoneal guarding)", "Plain Abdominal Radiograph: DIFFUSE, UNIFORM GAS AND FLUID DISTENSION THROUGHOUT BOTH SMALL INTESTINE AND LARGE INTESTINE (including stomach, small bowel loops, colon, and rectum) without any distinct cutoff or transition point"],
        "pertinent_negatives": ["uniform gas in both small AND large bowel with a silent abdomen distinguishes ileus from mechanical SBO (which has localized distension, no colonic gas, and high-pitched sounds)"],
        "content": "Temporary failure of coordinated gastrointestinal smooth muscle motility and peristalsis in the absence of mechanical obstruction, driven by sympathetic hyperactivity, local peritoneal macrophage inflammation, and mu-opioid receptor stimulation. Treatment Protocol: 1. Supportive: NPO, Nasogastric tube decompression for vomiting, IV fluid replacement; 2. AGGRESSIVE CORRECTION OF ELECTROLYTES: Replete serum Potassium (target K+ > 4.0 mEq/L) and Magnesium (target Mg > 2.0 mg/dL); 3. Minimization / cessation of systemic opioids (switch to multimodal non-opioid analgesia: IV Acetaminophen, Ketorolac, epidural analgesia); 4. Peripherally-acting mu-opioid receptor antagonist: Alvimopan (oral 12 mg BID) significantly accelerates gastrointestinal recovery; 5. Chewing gum (sham feeding stimulates cephalic-vagal motility) and early ambulation."
    },
    {
        "id": "ICD10-A98.0",
        "topic": "Crimean-Congo Hemorrhagic Fever (Hyalomma Tick & Ribavirin)",
        "icd10": "A98.0",
        "specialty": "Infectious Disease / Critical Care / Hematology",
        "organ_system": "Viral Hemorrhagic Fever Emergency",
        "keywords": ["crimean congo hemorrhagic fever", "cchf", "hyalomma tick bite", "livestock slaughterhouse blood", "severe petechiae ecchymosis hematuria", "ribavirin cchf", "high case fatality 30-50%"],
        "red_flags": ["exsanguinating multiorgan hemorrhage (GI, pulmonary, cerebral)", "fulminant Disseminated Intravascular Coagulation (DIC)", "severe nosocomial transmission to healthcare workers"],
        "clinical_hallmarks": ["history of tick bite by hard ticks of the genus Hyalomma, or direct contact with fresh blood/tissues of infected livestock (butchers, slaughterhouse workers, veterinarians), or nosocomial exposure in hospital", "incubation period 1 to 9 days", "abrupt onset of high spiking fever, rigors, severe frontal headache, dizziness, neck pain, and severe back and generalized myalgias", "facial flushing, conjunctival suffusion, and enanthem on soft palate", "HEMORRHAGIC PHASE (develops abruptly on day 3-5 of illness in severe disease):", "widespread cutaneous petechiae and massive ecchymoses, spontaneous epistaxis, gingival oozing, hematemesis, melena, macroscopic hematuria, and uncontrolled bleeding from venipuncture injection sites", "LABORATORY HALLMARKS: PROFOUND THROMBOCYTOPENIA (platelets often < 20,000 /mcL), leukopenia, prolonged PT/INR and aPTT, elevated transaminases (AST > 1,000 U/L indicates high mortality), and elevated D-Dimer", "high case-fatality rate: 30% to 50%"],
        "pertinent_negatives": ["requires strict Level 4 biosafety / contact and airborne isolation precautions"],
        "content": "Tick-borne zoonotic bunyavirus belonging to the genus Orthonairovirus (Nairoviridae family). Diagnostic workup: RT-PCR for CCHF viral RNA (days 1-7), IgM ELISA, CBC, coagulation profile. Statutory medical emergency with strict isolation. Protocol: 1. Strict barrier nursing and contact/droplet isolation in negative-pressure room; 2. Aggressive supportive replacement: Fresh Frozen Plasma, Cryoprecipitate, and Platelet transfusions; 3. SPECIFIC ANTIVIRAL THERAPY: Oral or IV Ribavirin (loading dose 30 mg/kg, then 15 mg/kg q6h for 4 days, then 7.5 mg/kg q8h for 6 days) initiated within the first 5 days of illness significantly reduces mortality."
    },
    {
        "id": "ICD10-A20.0",
        "topic": "Bubonic Plague (Yersinia Pestis & Axillary / Inguinal Bubo)",
        "icd10": "A20.0",
        "specialty": "Infectious Disease / Emergency Medicine / Critical Care",
        "organ_system": "Bacterial Zoonosis / Biosecurity",
        "keywords": ["plague", "bubonic plague", "yersinia pestis", "bubo painful lymphadenopathy", "xenopsylla cheopis rodent flea", "streptomycin gentamicin", "safety pin appearance wayson stain"],
        "red_flags": ["secondary Pneumonic Plague (airborne transmission, rapid fatal respiratory failure within 24 hours)", "Septicemic Plague with purpura fulminans / acral gangrene ('Black Death')", "septic shock"],
        "clinical_hallmarks": ["transmitted by the bite of an infected rodent flea (Xenopsylla cheopis / oriental rat flea) following rodent die-offs, or contact with infected wild rodents (marmots, prairie dogs, rats)", "incubation period 2 to 6 days", "abrupt onset of high fever (> 39-40C), shaking chills, severe headache, tachycardia, and profound prostration", "PATHOGNOMONIC PHYSICAL SIGN: THE 'BUBO' (an exquisitely painful, tender, tensely swollen, non-fluctuant lymph node measuring 1 to 10 cm, surrounded by brawny gelatinous erythematous edema, characteristically in the INGUINAL / FEMORAL REGION [60-70%], followed by axilla and neck)", "the pain in the bubo is so excruciating that the patient holds the affected limb in a fixed, motionless abducted posture to avoid any compression", "microscopic hallmark: Wayson or Giemsa stain of bubo aspirate demonstrates Gram-negative coccobacilli with characteristic BIPOLAR 'SAFETY-PIN' STAINING"],
        "pertinent_negatives": ["exquisite tenderness and surrounding non-pitting gelatinous edema distinguish plague bubo from painless venereal lymphadenopathy"],
        "content": "Zoonotic infection caused by the Gram-negative bacillus Yersinia pestis. Statutory Class A bioterrorism agent and global quarantine disease. Untreated bubonic plague has 50-60% mortality; pneumonic plague is 100% fatal without early antibiotics. STAT Treatment Protocol (MUST BE INITIATED IMMEDIATELY ON SUSPICION): 1. First-line Aminoglycosides: IM/IV Streptomycin (1g q12h) OR IV Gentamicin (5 mg/kg once daily for 10-14 days); 2. Alternative agents: IV Doxycycline (100 mg q12h) OR IV Chloramphenicol (for plague meningitis); 3. Droplet respiratory isolation for suspected pneumonic plague; 4. Chemoprophylaxis with oral Doxycycline (100 mg BID for 7 days) for all close contacts."
    },
    {
        "id": "ICD10-A01.1",
        "topic": "Paratyphoid Fever (Salmonella Paratyphi A, B, C)",
        "icd10": "A01.1",
        "specialty": "Infectious Disease / Tropical Medicine / Gastroenterology",
        "organ_system": "Enteric Invasive Infectious",
        "keywords": ["paratyphoid fever", "salmonella paratyphi", "enteric fever", "step ladder fever", "rose spots abdomen", "relative bradycardia faget sign", "blood culture paratyphi", "azithromycin ceftriaxone"],
        "red_flags": ["intestinal perforation from Peyer's patch ulceration (acute peritonitis)", "severe lower GI hemorrhage", "toxic encephalopathy"],
        "clinical_hallmarks": ["transmitted via food or water contaminated with feces of human cases or carriers; endemic in South Asia (accounting for up to 20-40% of all enteric fever cases)", "incubation period 1 to 10 days (typically shorter and milder course than Salmonella Typhi, but clinically indistinguishable)", "STEP-LADDER FEVER PATTERN: insidious, stepwise rise in body temperature over 3-5 days, peaking at 39-40C with headache, dry cough, malaise, and anorexia", "PATHOGNOMONIC PHYSICAL SIGNS: 1. FAGET'S SIGN (relative bradycardia: pulse rate is inappropriately slow for the height of temperature, e.g. pulse 80 with temp 39.5C); 2. ROSE SPOTS (in 10-30%: faint, transient, salmon-pink, blanching maculopapular spots [2-4 mm] appearing in crops on the upper abdomen and chest, resolving in 2-4 days); 3. Coated tongue with red tip and edges; 4. Soft, mild, palpable splenomegaly and hepatomegaly", "bowel habit: constipation is more frequent initially in adults; pea-soup diarrhea in children", "laboratory hallmarks: Leukopenia with relative lymphocytosis, mild transaminitis; Blood culture is positive in 60-80% during first week; Bone marrow culture has highest sensitivity (> 90%)"],
        "pertinent_negatives": ["absence of leukocytosis (leukopenia or normal WBC is typical; marked leukocytosis suggests secondary intestinal perforation)"],
        "content": "Systemic intracellular bacterial infection caused by Salmonella enterica serovars Paratyphi A (most common in India), Paratyphi B, or Paratyphi C. S. Paratyphi A lacks the Vi capsular polysaccharide antigen, rendering the standard Vi Typhoid vaccine completely ineffective against paratyphoid fever. Treatment: High rate of fluoroquinolone resistance in South Asia. Protocol: 1. Uncomplicated Outpatient: Oral Azithromycin (20 mg/kg/day or 1g day 1, then 500 mg daily for 7 days); 2. Inpatient Severe Enteric Fever: IV Ceftriaxone (2g IV daily for 10-14 days); 3. High-dose IV Dexamethasone for toxic encephalopathy or shock."
    },
    {
        "id": "ICD10-L70.0",
        "topic": "Severe Nodulocystic Acne (Acne Conglobata & Oral Isotretinoin)",
        "icd10": "L70.0",
        "specialty": "Dermatology",
        "organ_system": "Pilosebaceous Inflammatory",
        "keywords": ["acne vulgaris", "nodulocystic acne", "acne conglobata", "isotretinoin accutane protocol", "comedones papules pustules nodules", "burrowing sinus tracts acne", "ipledge pregnancy teratogenic"],
        "red_flags": ["Acne Fulminans (sudden painful ulcerating nodules with fever, leukocytosis, and polyarthritis)", "permanent disfiguring keloidal and ice-pick scarring", "severe depression / suicidal ideation"],
        "clinical_hallmarks": ["severe, recalcitrant, highly inflammatory follicular disorder of the pilosebaceous units of the face, neck, chest, shoulders, and upper back", "ELEMENTARY LESIONS: widespread open comedones ('blackheads'), closed comedones ('whiteheads'), inflammatory erythematous papules, pustules, and LARGE (> 5 mm), PAINFUL, DEEP, FLUCTUANT, ERYTHEMATOUS INFLAMMATORY NODULES AND CYSTS", "Acne Conglobata (most severe form): widespread burrowing interconnected abscesses, draining sinus tracts discharging foul, purulent, serosanguinous fluid, and prominent multi-pore giant comedones", "heals with severe, permanent, disfiguring cutaneous scars: 'ice-pick' pitted scars, 'boxcar' scars, rolling atrophic scars, and hypertrophic/keloidal bridging scars", "pathophysiological tetrad: 1. Follicular epidermal hyperkeratinization; 2. Hyperseborrhea (androgen-mediated); 3. Cutibacterium acnes colonization; 4. Host innate/adaptive immune inflammation"],
        "pertinent_negatives": ["TERATOGENICITY MANDATE: ORAL ISOTRETINOIN IS 100% TERATOGENIC (causes catastrophic craniofacial, cardiac, and thymic malformations); strict contraception with two forms is legally mandatory"],
        "content": "Severe nodulocystic acne refractory to oral antibiotics. FIRST-LINE DEFINITIVE THERAPY: ORAL ISOTRETINOIN (13-cis-retinoic acid - the ONLY medication that targets all four pathogenic acne factors simultaneously). Protocol: 1. Baseline liver function tests, fasting lipid panel, and two negative serum pregnancy tests (enrolled in iPLEDGE / pregnancy prevention program); 2. Dosing: 0.5 to 1.0 mg/kg/day orally taken with high-fat meals for 20-24 weeks, achieving a TARGET CUMULATIVE DOSE OF 120 TO 150 MG/KG (ensures permanent long-term cure and prevents relapse in > 80-85%); 3. Monthly monitoring of LFTs, triglycerides, and depression screening; 4. Mandatory dry lips/skin barrier emollients."
    },
    {
        "id": "ICD10-B35.3",
        "topic": "Tinea Pedis & Onychomycosis (Athlete's Foot & Trichophyton Rubrum)",
        "icd10": "B35.3",
        "specialty": "Dermatology / Podiatry / Primary Care",
        "organ_system": "Superficial Fungal Dermatophytosis",
        "keywords": ["tinea pedis", "athletes foot", "moccasin tinea", "onychomycosis tinea unguium", "trichophyton rubrum", "macerated interdigital toe webs", "potassium hydroxide koh mount", "terbinafine oral"],
        "red_flags": ["secondary bacterial cellulitis (entry portal for Group A Strep in diabetics)", "bacterial superinfection / lymphangitis", "tinea incognito from misuse of topical steroids"],
        "clinical_hallmarks": ["most common superficial fungal dermatophyte infection worldwide, overwhelmingly caused by the anthropophilic dermatophyte TRICHOPHYTON RUBRUM (70-80%) or Trichophyton mentagrophytes", "THREE DISTINCT CLINICAL PATTERNS OF TINEA PEDIS:", "1. Interdigital Type (most common): peeling, fissuring, scaling, and white, boggy MACERATION IN THE 4TH AND 3RD TOE WEB SPACES, accompanied by intense itching and burning;", "2. Moccasin Type (Hyperkeratotic): fine, silvery-white scale overlying diffuse erythema covering the soles, heels, and lateral borders of both feet in a slipper-like distribution ('two feet, one hand syndrome');", "3. Vesiculobullous Type: intensely pruritic vesicles on the instep/sole", "ONYCHOMYCOSIS (Tinea Unguium in > 80% with chronic tinea pedis): Distal Subungual pattern: thickened, opaque, yellow-brown dystrophic toenail, subungual crumbly hyperkeratotic debris, and onycholysis (separation of nail plate from bed)", "DIAGNOSTIC BEDSIDE TEST: 10% or 20% POTASSIUM HYDROXIDE (KOH) MOUNT of skin scrapings or subungual debris demonstrating CLEAR, REFRACTILE, BRANCHING, SEPTATE HYPHAE"],
        "pertinent_negatives": ["TOPICAL STEROIDS (Betamethasone, Clobetasol) ARE STRICTLY CONTRAINDICATED ALONE (cause 'Tinea Incognito' - masking symptoms while promoting rampant fungal spread)"],
        "content": "Dermatophyte infection utilizing epidermal and ungual keratin. Diagnostic workup: KOH preparation with fungal culture on Sabouraud agar or nail clipping PAS stain. Treatment: 1. Tinea Pedis (uncomplicated): Topical Allylamine (Terbinafine 1% cream applied BID for 1-2 weeks - superior mycological cure rate > 80%) or topical Imidazoles (Clotrimazole, Ketoconazole); 2. Onychomycosis / Extensive Moccasin Tinea: ORAL TERBINAFINE (250 mg daily orally for 12 weeks for toenails, 6 weeks for fingernails - check baseline ALT/AST; gold standard cure rate 70-80%); Alternative: Oral Itraconazole pulse therapy; Foot hygiene and keeping toe webs dry."
    },
    {
        "id": "ICD10-M84.50XA",
        "topic": "Pathological Bone Fracture (Osteolytic Metastasis & Mirels' Score)",
        "icd10": "M84.50XA",
        "specialty": "Orthopedic Oncology / Surgical Oncology / Endocrinology",
        "organ_system": "Skeletal Malignancy Emergency",
        "keywords": ["pathological fracture", "osteolytic bone metastasis", "mirels score", "fracture with trivial trauma", "multiple myeloma bone fracture", "prophylactic internal fixation", "hypercalcemia of malignancy"],
        "red_flags": ["spinal cord compression from vertebral pathological collapse", "malignant hypercalcemia (confusion, cardiac arrhythmias)", "catastrophic femoral neck displacement"],
        "clinical_hallmarks": ["bone fracture occurring as a result of MINIMAL, TRIVIAL TRAUMA (e.g. rolling over in bed, standing up, coughing) or spontaneously during activities of daily living, in bone weakened by pre-existing disease", "patient frequently reports weeks to months of PRECEDING DULL, DEEP, CONSTANT ACHING BONE PAIN THAT IS CHARACTERISTICALLY WORST AT NIGHT and not relieved by rest", "PRIMARY SITES OF ORIGIN (The 'BLT with a Kosher Pickle' Mnemonic):", "1. Breast; 2. Lung; 3. Thyroid; 4. Kidney (Renal Cell); 5. Prostate (osteoblastic); 6. Multiple Myeloma / Lymphoma", "plain radiograph: focal, well-defined or permeative radiolucent 'PUNCHED-OUT' OSTEOLYTIC DESTRUCTION, cortical erosion, or sclerotic (blastic) lesion with sudden cortical break", "MIRELS' OBJECTIVE RATING SCORE (assesses risk of impending pathological fracture in long bones to indicate prophylactic surgery; score >= 8 warrants prophylactic surgical stabilization):", "Scores 1-3 based on: Location (upper limb=1, lower limb=2, peritrochanteric=3); Pain (mild=1, moderate=2, functional=3); Lesion type (blastic=1, mixed=2, lytic=3); Size (< 1/3 cortex=1, 1/3-2/3=2, > 2/3 cortex=3)"],
        "pertinent_negatives": ["absence of high-energy trauma strongly indicates underlying bone pathology"],
        "content": "Disruption of osseous continuity occurring through an area of bone structurally compromised by neoplastic, metabolic, or infectious pathology. Management Protocol: 1. Whole-body CT/PET-CT and skeletal survey to identify primary tumor; 2. Biopsy confirmation of bone lesion before definitive instrumentation (avoids spreading sarcoma); 3. Impending Fracture (Mirels >= 8): PROPHYLACTIC SURGICAL FIXATION (Reamed Intramedullary Nailing + polymethylmethacrylate [PMMA] bone cement) PREVENTS CATASTROPHIC DISPLACEMENT; 4. Displaced Fracture: Modular Endoprosthetic Reconstruction or locked intramedullary nail; 5. Palliative External Beam Radiotherapy (8 Gy single fraction) + Bisphosphonates (Zoledronic acid) or Denosumab."
    },
    {
        "id": "ICD10-K29.0",
        "topic": "Acute Hemorrhagic Erosive Gastritis & Curling's Ulcer",
        "icd10": "K29.0",
        "specialty": "Gastroenterology / Critical Care / General Surgery",
        "organ_system": "Gastrointestinal Bleeding",
        "keywords": ["acute hemorrhagic gastritis", "stress related mucosal disease", "curling ulcer burn", "cushing ulcer brain trauma", "coffee ground emesis nsaid", "iv ppi infusion", "endoscopy mucosal erosions"],
        "red_flags": ["massive upper gastrointestinal exsanguination", "perforated stress ulcer with pneumoperitoneum", "hypovolemic shock in ICU patient"],
        "clinical_hallmarks": ["history of major physiological physiological stress in ICU (mechanical ventilation > 48h, severe sepsis, extensive burns [CURLING'S ULCER], severe head trauma / intracranial hypertension [CUSHING'S ULCER]) OR ingestion of high-dose NSAIDs, aspirin, or heavy acute alcohol binge", "CARDINAL CLINICAL PRESENTATION: sudden, painless or mild burning epigastric discomfort followed by COFFEE-GROUND EMESIS (hematemesis) or spontaneous melena (black, tarry stools)", "nasogastric tube aspiration reveals fresh red blood or coffee-ground secretions", "vital signs: tachycardia, postural orthostatic hypotension, or frank hypovolemic shock depending on rate of blood loss", "URGENT UPPER GI ENDOSCOPY (EGD - DIAGNOSTIC GOLD STANDARD):", "reveals MULTIPLE, SUPERFICIAL, PUNCTATE PETECHIAL HEMORRHAGES, ERYTHEMATOUS EROSIONS, AND SHALLOW ULCERATIONS diffusely scattered throughout the gastric fundus and body, with dark subepithelial hemorrhages"],
        "pertinent_negatives": ["mucosal erosions do NOT penetrate the muscularis mucosae (distinguishes erosive gastritis from deep chronic peptic ulcer)"],
        "content": "Disruption of the gastric mucosal defensive barrier (mucus-bicarbonate layer, mucosal blood flow, prostaglandin synthesis) by systemic hypoperfusion, catecholamines, or COX-1 inhibition, allowing luminal acid and pepsin to cause superficial mucosal necrosis and microvascular hemorrhage. Management: 1. STAT Hemodynamic Resuscitation: IV crystalloids and blood transfusion; 2. STAT HIGH-DOSE IV PROTON PUMP INHIBITOR: IV Pantoprazole or Esomeprazole (80 mg IV bolus followed by 8 mg/hr continuous IV infusion for 72 hours, maintaining intragastric pH > 6.0 to stabilize fibrin clots); 3. Endoscopic Hemostasis (argon plasma coagulation, hemoclips) for focal spurting vessels; 4. Universal ICU Prophylaxis: Enteral or IV PPI / H2-receptor antagonist for all ventilated (> 48h) or coagulopathic patients."
    },
    {
        "id": "ICD10-T63.441A",
        "topic": "Hymenoptera Envenomation & Anaphylaxis (Bee & Wasp Sting Protocol)",
        "icd10": "T63.441A",
        "specialty": "Allergy & Immunology / Emergency Medicine / Critical Care",
        "organ_system": "Immunologic / Envenomation Emergency",
        "keywords": ["bee sting", "wasp sting", "hymenoptera anaphylaxis", "epinephrine autoinjector epipen", "angioedema stridor wheezing", "venom immunotherapy vit", "remove stinger scrape"],
        "red_flags": ["acute asphyxiation from laryngeal angioedema", "distributive anaphylactic shock (hypotension, cardiovascular collapse)", "massive envenomation (> 50-100 stings) causing rhabdomyolysis and acute renal failure"],
        "clinical_hallmarks": ["history of sting by insects of the order Hymenoptera: Apidae (Honeybees - barbed stinger remains in skin; Bumblebees), Vespidae (Yellowjackets, Wasps, Hornets - unbarbed stingers, can sting repeatedly), or Solenopsis (Fire ants)", "LOCAL REACTION: immediate, intense, sharp, burning pain, erythema, and a raised wheal with central puncture site, resolving in hours", "LARGE LOCAL REACTION: extensive, painful swelling and induration > 10 cm in diameter lasting 3-7 days (IgE-mediated, benign, does NOT predict systemic anaphylaxis)", "SYSTEMIC ANAPHYLACTIC REACTION (develops rapidly WITHIN 10 TO 30 MINUTES of sting):", "1. Cutaneous: generalized pruritus, flushing, diffuse urticaria (hives), and ANGIOEDEMA (swelling of lips, tongue, uvula, and periorbital tissues);", "2. Respiratory: tightness in throat, hoarseness, INSPIRATORY STRIDOR, bronchospasm (expiratory wheezing), and severe dyspnea;", "3. Cardiovascular: severe hypotension, dizziness, syncope, diaphoresis, and cardiac arrest;", "4. Gastrointestinal: crampy abdominal pain, nausea, and explosive diarrhea"],
        "pertinent_negatives": ["DO NOT SQUEEZE THE HONEYBEE STINGER (scrape it off sideways with a fingernail or credit card to avoid expressing venom sac contents)"],
        "content": "Type I immediate hypersensitivity reaction mediated by venom-specific IgE antibodies bound to tissue mast cells and basophils, releasing histamine, leukotrienes, and tryptase upon venom re-exposure. STAT Life-Saving Protocol: 1. FIRST-LINE DRUG OF CHOICE: INTRAMUSCULAR EPINEPHRINE (1:1,000 / 1 mg/mL): 0.3 - 0.5 mg IM (0.01 mg/kg in children, max 0.3 mg) INJECTED STAT INTO THE ANTEROLATERAL THIGH (VASTUS LATERALIS); REPEAT EVERY 5-15 MINUTES IF SYMPTOMS PERSIST; 2. High-flow oxygen, aggressive IV fluid bolus (1-2 L Normal Saline for shock); 3. Second-line adjuncts: IV H1-antihistamine (Diphenhydramine 50 mg) + IV H2-blocker (Famotidine 20 mg) + IV Methylprednisolone (1-2 mg/kg); 4. Discharge with two Epinephrine Autoinjectors (EpiPen 0.3 mg) and referral for Venom Immunotherapy (VIT - achieves > 95% protection against future stings)."
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
            
    print(f"Batch 8 Final added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""
Batch 2: Nephrology, Neurology, Endocrinology, Hematology/Oncology protocols.
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
    # --- 4. NEPHROLOGY & UROLOGY (14) ---
    {
        "id": "ICD10-N04.9",
        "topic": "Nephrotic Syndrome (Minimal Change Disease & FSGS)",
        "icd10": "N04.9",
        "specialty": "Nephrology / Pediatrics",
        "organ_system": "Renal",
        "keywords": ["nephrotic syndrome", "massive proteinuria", "periorbital edema morning", "hypoalbuminemia edema", "frothy urine", "minimal change disease", "fsgs"],
        "red_flags": ["spontaneous bacterial peritonitis", "renal vein thrombosis (flank pain, hematuria)", "acute kidney injury"],
        "clinical_hallmarks": ["the classic nephrotic triad: 1. Heavy proteinuria (> 3.5 g/24 hours or urine protein-to-creatinine ratio > 3.0-3.5 mg/mg); 2. Profound hypoalbuminemia (serum albumin < 3.0 g/dL); 3. Severe generalized dependent pitting edema (anasarca, periorbital morning puffiness, ascites, scrotal edema)", "frothy, foamy urine due to high protein content", "hyperlipidemia (elevated total cholesterol, LDL, and triglycerides) and lipiduria ('Maltese cross' oval fat bodies under polarized microscopy)", "Minimal Change Disease (MCD): most common in children (85%), normal light microscopy, diffuse podocyte foot process effacement on electron microscopy, highly steroid-responsive"],
        "pertinent_negatives": ["no macroscopic hematuria or active RBC casts (distinguishes from nephritic syndrome)"],
        "content": "Glomerular disorder characterized by increased permeability of glomerular capillary filtration barrier to plasma proteins. Complications: thromboembolism (loss of Antithrombin III, Protein C/S in urine), infection (loss of immunoglobulins), and hypercholesterolemia. Diagnostic workup: 24h urine protein, serum albumin, lipid panel, complement (C3/C4), ANA, Renal Biopsy (mandatory in adults). Treatment: First-line for MCD: Oral Prednisone (60 mg/m2/day or 1 mg/kg/day for 4-16 weeks); Loop diuretics (Furosemide) + spironolactone for edema; ACE inhibitors or ARBs to reduce proteinuria; Statin for hyperlipidemia; Anticoagulation for high-risk thrombosis."
    },
    {
        "id": "ICD10-M31.0",
        "topic": "Goodpasture Syndrome (Anti-Glomerular Basement Membrane Disease)",
        "icd10": "M31.0",
        "specialty": "Nephrology / Pulmonology / Critical Care",
        "organ_system": "Pulmonary-Renal Autoimmune",
        "keywords": ["goodpasture syndrome", "anti gbm disease", "pulmonary renal syndrome", "hemoptysis with hematuria", "linear igg basement membrane", "crescentic glomerulonephritis"],
        "red_flags": ["massive asphyxiating pulmonary hemorrhage", "anuric acute renal failure needing dialysis"],
        "clinical_hallmarks": ["classic pulmonary-renal presentation: acute onset of hemoptysis (coughing fresh blood), dyspnea, and bilateral alveolar infiltrates combined with rapidly progressive acute glomerulonephritis (macroscopic hematuria, oliguria, rapid serum creatinine rise)", "frequently triggered by respiratory infections or hydrocarbon/cigarette smoke exposure in HLA-DRB1*1501 positive individuals", "laboratory hallmark: circulating high-titer Anti-GBM (anti-alpha-3 chain of Type IV collagen) antibodies in serum", "renal biopsy (pathognomonic): light microscopy shows extensive cellular crescent formation (> 50% crescents); Direct Immunofluorescence reveals continuous, linear ribbon-like deposition of IgG and C3 along glomerular capillary basement membranes"],
        "pertinent_negatives": ["negative ANCA (distinguishes from GPA or MPA, though double-positive variants exist)"],
        "content": "Life-threatening autoimmune small vessel vasculitis caused by circulating pathogenic antibodies directed against the non-collagenous domain of the alpha-3 chain of type IV collagen present in glomerular and alveolar basement membranes. Urgent Medical Protocol: 1. STAT Daily Plasmapheresis (Plasma Exchange: 4 L exchanges daily for 14 days) to rapidly clear pathogenic circulating anti-GBM antibodies; 2. High-dose pulse IV Methylprednisolone (1 g IV daily for 3 days) followed by oral Prednisone (1 mg/kg/day); 3. Oral or IV Cyclophosphamide (2 mg/kg/day for 2-3 months) to halt autoantibody synthesis."
    },
    {
        "id": "ICD10-D69.0",
        "topic": "Henoch-Schönlein Purpura (IgA Vasculitis - Pediatric Tetrad)",
        "icd10": "D69.0",
        "specialty": "Pediatrics / Nephrology / Rheumatology",
        "organ_system": "Systemic Small Vessel Vasculitis",
        "keywords": ["henoch schonlein purpura", "iga vasculitis", "palpable purpura buttocks legs", "pediatric belly pain with rash", "intussusception purpura", "normal platelet purpura"],
        "red_flags": ["ileo-ileal intussusception (target sign on ultrasound)", "gastrointestinal bleeding / bowel ischemia", "rapidly progressive glomerulonephritis"],
        "clinical_hallmarks": ["classic diagnostic tetrad (often preceded 1-3 weeks by an upper respiratory tract infection): 1. Palpable purpura: non-thrombocytopenic, raised, violaceous petechiae and purpura symmetrically distributed over gravity-dependent lower extremities and buttocks; 2. Arthralgias / non-destructive arthritis primarily affecting knees and ankles; 3. Colicky abdominal pain: diffuse periumbilical crampy pain, vomiting, or melena; 4. Renal involvement: microscopic or gross hematuria and proteinuria (IgA nephropathy)", "NORMAL platelet count and normal coagulation screen (rules out ITP, TTP, DIC, leukemia)"],
        "pertinent_negatives": ["normal platelet count confirms palpable purpura is vasculitic, not thrombocytopenic"],
        "content": "Most common systemic vasculitis of childhood, characterized by immune complex deposition containing predominantly Immunoglobulin A (IgA1) in small arterioles, capillaries, and post-capillary venules. EULAR/PRINTO/PRES criteria require palpable purpura plus >= 1 of: abdominal pain, IgA deposition, arthritis, or renal involvement. Diagnostic workup: Platelet count, urinalysis, serum creatinine, abdominal ultrasound if acute pain. Treatment: Supportive (adequate hydration, analgesia with Acetaminophen/NSAIDs for joint pain); Systemic corticosteroids (Prednisolone 1-2 mg/kg/day for 1-2 weeks) reserved for severe abdominal pain or scrotal swelling; ACE inhibitors for persistent proteinuria."
    },
    {
        "id": "ICD10-N00.9",
        "topic": "Post-Streptococcal Glomerulonephritis (PSGN & Nephritic Triad)",
        "icd10": "N00.9",
        "specialty": "Pediatrics / Nephrology",
        "organ_system": "Renal Post-Infectious",
        "keywords": ["post streptococcal glomerulonephritis", "psgn", "cola colored urine", "tea colored urine", "subepithelial humps", "aso titer low c3", "strep throat kidney"],
        "red_flags": ["hypertensive encephalopathy / seizures", "acute pulmonary edema from fluid overload", "anuric acute kidney failure"],
        "clinical_hallmarks": ["classic nephritic syndrome triad: 1. Macroscopic hematuria (dark, tea-colored, cola-colored, or smoky urine with dysmorphic RBCs and red cell casts); 2. Hypertension; 3. Oliguria with periorbital morning facial puffiness and mild dependent edema", "latent period: typically develops 1-2 weeks following streptococcal pharyngitis, or 3-6 weeks following streptococcal pyoderma / impetigo (caused by nephritogenic Group A beta-hemolytic Streptococcus strains)", "laboratory hallmarks: Markedly depressed serum Complement C3 level (normalizes within 6-8 weeks) with normal C4, accompanied by elevated Antistreptolysin O (ASO) titer or anti-DNase B titer", "renal biopsy (if performed): diffuse endocapillary proliferative glomerulonephritis with pathognomonic large subepithelial electron-dense 'humps' on electron microscopy"],
        "pertinent_negatives": ["no persistent low C3 beyond 8 weeks (persistent low C3 indicates MPGN or lupus nephritis)"],
        "content": "Immune complex-mediated glomerulonephritis triggered by nephritogenic streptococcal antigens (SpeB, NAPlr) that deposit in glomeruli and activate the alternative complement pathway. Overwhelmingly favorable prognosis in children (> 95% complete spontaneous recovery). Treatment: Supportive care is key: Strict fluid restriction, sodium-restricted diet, Loop diuretics (IV Furosemide) for volume overload and hypertension, Calcium Channel Blockers (Amlodipine) for severe hypertension; Course of oral Penicillin or Amoxicillin to eradicate residual streptococcal colonization."
    },
    {
        "id": "ICD10-Q61.2",
        "topic": "Autosomal Dominant Polycystic Kidney Disease (ADPKD & Berry Aneurysms)",
        "icd10": "Q61.2",
        "specialty": "Nephrology / Medical Genetics",
        "organ_system": "Renal Genetic",
        "keywords": ["adpkd", "polycystic kidney disease", "bilateral flank masses", "berry aneurysm", "subarachnoid hemorrhage polycystic", "polycystic liver", "pkd1 pkd2"],
        "red_flags": ["ruptured cerebral berry aneurysm (sudden thunderclap headache)", "cyst infection / sepsis", "rapidly progressing renal failure"],
        "clinical_hallmarks": ["strong family history of autosomal dominant kidney disease (PKD1 on chromosome 16 in 85%, PKD2 on chromosome 4 in 15%)", "bilateral palpable, huge, nodular, non-tender flank or abdominal masses", "early, refractory hypertension developing in young adults (often preceding renal decline)", "dull, chronic flank or low back pain punctuated by acute bouts of sharp pain from cyst hemorrhage, cyst infection, or nephrolithiasis", "extrarenal manifestations: hepatic cysts (in > 80% by age 30), intracranial saccular 'berry' aneurysms in Circle of Willis (10-15%), mitral valve prolapse (25%), and colonic diverticulosis"],
        "pertinent_negatives": ["absence of medullary cysts alone on ultrasound"],
        "content": "Progressive systemic genetic disorder characterized by the development and relentless expansion of multiple fluid-filled bilateral renal cysts, resulting in massive kidney enlargement, parenchymal destruction, and end-stage renal disease (ESRD) typically by the 5th or 6th decade. Diagnostic gold standard: Renal ultrasound (Ravine unified criteria based on age and bilateral cyst count). Treatment: Rigorous BP control (target < 110-120/75-80 mmHg with ACE inhibitors or ARBs); High water intake (> 3 L/day) to suppress endogenous vasopressin; Vasopressin V2-receptor antagonist (Tolvaptan) slows cyst growth and eGFR decline in rapidly progressing ADPKD; Hemodialysis/Peritoneal dialysis and Renal Transplantation for ESRD."
    },
    {
        "id": "ICD10-C64.9",
        "topic": "Renal Cell Carcinoma (Clear Cell & Classical Triad)",
        "icd10": "C64.9",
        "specialty": "Urology / Urologic Oncology",
        "organ_system": "Urological Neoplasm",
        "keywords": ["renal cell carcinoma", "rcc", "clear cell kidney cancer", "painless hematuria flank mass", "triad hematuria flank pain mass", "left varicocele rcc", "von hippel lindau"],
        "red_flags": ["inferior vena cava (ivc) tumor thrombus extension into right atrium", "pathological fractures / bone metastasis", "paraneoplastic hypercalcemia / polycythemia"],
        "clinical_hallmarks": ["classic clinical triad (present simultaneously in < 10% of cases, usually late stage): 1. Gross macroscopic painless hematuria; 2. Dull, aching flank pain; 3. Palpable abdominal/flank mass", "new-onset, non-reducing LEFT VARICOCELE (does not collapse when patient lies supine) caused by left renal vein occlusion by tumor thrombus blocking left testicular vein drainage", "paraneoplastic syndromes: polycythemia (excess erythropoietin secretion), hypercalcemia (PTHrP production), hypertension (renin), or Stauffer syndrome (reversible non-metastatic hepatic dysfunction)", "most common subtype: Clear Cell RCC (75-80%), strongly linked to VHL gene inactivation on chromosome 3p"],
        "pertinent_negatives": ["no fever or pyuria (distinguishes from acute pyelonephritis or renal abscess)"],
        "content": "Malignant neoplasm arising from renal tubular epithelial cells, predominantly clear cell histopathology. Over 60% are now discovered incidentally on abdominal imaging for unrelated reasons ('incidentaloma'). Diagnostic workup: Triphasic Contrast CT of abdomen and pelvis with nephrographic and excretory phases (solid, enhancing renal cortical mass with necrotic/cystic areas); Chest CT for pulmonary metastasis staging. Treatment: Localized disease (Stage I-III): Surgical resection (Radical or Partial Nephrectomy / nephron-sparing surgery); Advanced/Metastatic disease: Dual immunotherapy (Nivolumab + Ipilimumab) or VEGF-tyrosine kinase inhibitor combination (Pembrolizumab + Axitinib / Cabozantinib); RCC is notoriously resistant to conventional chemotherapy and radiotherapy."
    },
    {
        "id": "ICD10-N40.1",
        "topic": "Benign Prostatic Hyperplasia (BPH & Lower Urinary Tract Symptoms)",
        "icd10": "N40.1",
        "specialty": "Urology",
        "organ_system": "Urological",
        "keywords": ["benign prostatic hyperplasia", "bph", "luts", "hesitancy weak stream", "nocturia men", "post void dribbling", "tamsulosin bph", "turp"],
        "red_flags": ["acute urinary retention requiring urgent catheterization", "bilateral hydronephrosis with obstructive uropathy / renal failure", "recurrent gross hematuria"],
        "clinical_hallmarks": ["progressive Lower Urinary Tract Symptoms (LUTS) in aging men (> 50 years): 1. Voiding / Obstructive symptoms: hesitancy, weak intermittent urinary stream, straining, and prolonged post-void dribbling; 2. Storage / Irritative symptoms: nocturia (waking >= 2 times/night to urinate), daytime frequency, and sudden urgency", "sensation of incomplete bladder emptying", "Digital Rectal Examination (DRE): smoothly enlarged, non-tender, symmetrical, elastic, firm prostate with preserved median sulcus (absence of hard, irregular, stony nodules which characterize prostate cancer)", "elevated Post-Void Residual (PVR) volume (> 100-200 mL) on bedside bladder scan"],
        "pertinent_negatives": ["smooth elastic prostate on DRE rules out obvious palpable prostatic malignancy"],
        "content": "Non-malignant proliferation of stromal and epithelial cells in the prostate transitional zone, driven by dihydrotestosterone (DHT) synthesized from testosterone via 5-alpha reductase. Diagnostic workup: International Prostate Symptom Score (IPSS), DRE, Serum PSA, Urinalysis, Bladder ultrasound with PVR, Uroflowmetry (peak flow rate Qmax < 10-15 mL/s). Treatment: Mild symptoms (IPSS <= 7): watchful waiting; Moderate-severe: 1. Alpha-1 adrenergic antagonists (Tamsulosin 0.4 mg, Silodosin) relax smooth muscle at bladder neck, providing rapid symptom relief within days; 2. 5-alpha reductase inhibitors (Finasteride 5 mg, Dutasteride) block DHT, shrinking prostate volume by 20-25% over 6 months; 3. Surgical gold standard: Transurethral Resection of the Prostate (TURP) or Holmium Laser Enucleation of Prostate (HoLEP)."
    },
    {
        "id": "ICD10-N44.00",
        "topic": "Testicular Torsion (Spermatic Cord Twisting & Bell-Clapper Deformity)",
        "icd10": "N44.00",
        "specialty": "Urology / Pediatric Surgery / Emergency Medicine",
        "organ_system": "Urological Emergency",
        "keywords": ["testicular torsion", "scrotal pain acute", "absent cremasteric reflex", "bell clapper deformity", "negative prehn sign", "high riding testis", "twisted testicle"],
        "red_flags": ["ischemic testicular infarction / necrosis if untreated beyond 6 hours", "loss of testicle and fertility"],
        "clinical_hallmarks": ["sudden, abrupt, excruciating, severe unilateral scrotal pain, often awakening the patient from sleep or following vigorous exercise/minor trauma", "frequently accompanied by nausea, vomiting, and lower quadrant abdominal pain (often misdiagnosed as appendicitis)", "physical examination: affected testis is swollen, tender, HIGH-RIDING (elevated towards inguinal ring) with a HORIZONTAL LIE due to cord shortening and twisting", "pathognomonic sign: ABSENCE OF THE IPSILATERAL CREMASTERIC REFLEX (light stroking of superior inner thigh fails to cause normal ipsilateral testicular elevation)", "Negative Prehn's sign: manual elevation of the scrotum DOES NOT relieve the pain (and often worsens it)"],
        "pertinent_negatives": ["CLINICAL EMERGENCY: DO NOT DELAY SURGICAL EXPLORATION FOR IMAGING IF TORSION IS SUSPECTED"],
        "content": "Mechanical twisting of the spermatic cord along its axis, interrupting venous drainage and subsequently arterial blood supply to the testicle, predisposing to complete testicular necrosis within 6-8 hours. Anatomic predisposition: high investing tunica vaginalis ('bell-clapper deformity'). Diagnostic imaging: Emergent Scrotal Color Doppler Ultrasound (shows absent or severely decreased intratesticular blood flow with twisted cord 'whirlpool sign'). Treatment: STAT Emergency Surgical Exploration without delay: intraoperative detorsion and assessment of viability; Bilateral three-point Orchiopexy (fixation of BOTH testes to prevent future torsion of contralateral side) or orchiectomy if non-viable."
    },
    {
        "id": "ICD10-N45.1",
        "topic": "Acute Epididymo-Orchitis (Infective vs Sexually Transmitted)",
        "icd10": "N45.1",
        "specialty": "Urology / Infectious Disease / Primary Care",
        "organ_system": "Urological Infectious",
        "keywords": ["epididymitis", "epididymo orchitis", "positive prehn sign", "present cremasteric reflex", "tender swollen testicle", "chlamydia epididymitis", "e coli urinary infection"],
        "red_flags": ["scrotal abscess formation", "testicular infarction / gangrene", "chronic pain and infertility"],
        "clinical_hallmarks": ["gradual, progressive onset (developing over 24-48 hours) of unilateral scrotal aching pain, swelling, and localized tenderness", "associated symptoms: fever, dysuria, urethral discharge, urinary frequency, and pyuria", "physical examination: exquisitely tender, indurated, swollen epididymis distinctly palpable posterior to testis in early stages, progressing to diffuse scrotal enlargement and erythema", "pathognomonic sign: POSITIVE PREHN'S SIGN (manual gentle elevation of the affected hemiscrotum PROVIDES MARKED RELIEF of pain)", "cremasteric reflex is PRESERVED and normal"],
        "pertinent_negatives": ["normal horizontal lie is absent (testis remains in normal vertical orientation)"],
        "content": "Acute inflammation of the epididymis and adjoining testis, caused by retrograde ascent of pathogens from the urethra or bladder. Etiology: in sexually active men < 35 years: overwhelmingly Chlamydia trachomatis or Neisseria gonorrhoeae; in older men > 35 years or post-instrumentation: enteric urinary coliforms (Escherichia coli, Pseudomonas). Diagnostic workup: Scrotal Doppler ultrasound (shows hyperemia and massively increased blood flow to epididymis with normal or increased testicular perfusion), First-void urine NAAT for gonorrhea/chlamydia, urine culture. Treatment: 1. Sexually transmitted: Ceftriaxone 500 mg IM single dose PLUS Doxycycline 100 mg BID for 10-14 days (treat partner!); 2. Enteric: Levofloxacin 500 mg daily or Ofloxacin for 10-14 days; Scrotal elevation, ice packs, and NSAIDs."
    },
    {
        "id": "ICD10-N49.3",
        "topic": "Fournier's Gangrene (Necrotizing Fasciitis of Perineum)",
        "icd10": "N49.3",
        "specialty": "Urology / General Surgery / Critical Care / Emergency Medicine",
        "organ_system": "Urological / Soft Tissue Emergency",
        "keywords": ["fourniers gangrene", "perineal necrotizing fasciitis", "scrotal gangrene crepitus", "foul smelling scrotal necrosis", "dishwater pus perineum", "diabetic scrotal pain out of proportion"],
        "red_flags": ["septic shock and multiorgan failure", "cutaneous necrosis and widespread crepitus", "profound metabolic acidosis"],
        "clinical_hallmarks": ["predominantly affects diabetic, immunocompromised, alcoholic, or elderly males", "excruciating perineal, perianal, or scrotal pain that is initially completely out of proportion to early subtle skin redness", "rapid evolution over hours: skin becomes dusky, violaceous, bronze, blistered, and progresses to frank black necrotic sloughing", "pathognomonic clinical signs: PALPABLE SUBCUTANEOUS CREPITUS (gas in tissues produced by anaerobic fermentation) and foul, fetid, dishwater-like purulent discharge", "systemic toxicity: high fever, tachycardia, tachypnea, severe hypotension, and altered mental status"],
        "pertinent_negatives": ["simple scrotal cellulitis DOES NOT show crepitus, rapid tissue breakdown, or dishwater discharge"],
        "content": "Polymicrobial, synergistic necrotizing fasciitis of the perineal, genital, and perianal regions, spreading along Dartos, Colles', and Scarpa's fascial planes at rates of up to 2-3 cm/hour. Statutory surgical emergency with high mortality (20-40%). Protocol: 1. STAT aggressive fluid resuscitation and broad-spectrum IV triple antibiotics (Meropenem + Vancomycin + Clindamycin [blocks exotoxin synthesis]); 2. IMMEDIATE, RADICAL SURGICAL EXCISION and aggressive debridement of all necrotic non-viable skin and fascia down to bleeding margins in the operating room; 3. Mandatory repeat surgical look within 24-48 hours; 4. Hyperbaric oxygen and VAC therapy."
    },
    {
        "id": "ICD10-N35.9",
        "topic": "Urethral Stricture (Bulbar & Penile - Retrograde Urethrography)",
        "icd10": "N35.9",
        "specialty": "Urology",
        "organ_system": "Urological",
        "keywords": ["urethral stricture", "retrograde urethrography", "spraying urinary stream", "slow flow rate urine", "catheter trauma stricture", "urethroplasty"],
        "red_flags": ["acute complete urinary retention", "periurethral abscess / 'watering-can perineum'", "ascending urosepsis"],
        "clinical_hallmarks": ["progressive, insidious diminution of urinary stream: thin, narrow caliber, spraying, or splayed urinary stream with prolonged micturition time", "history of previous straddle injury to perineum, urethral catheterization, transurethral instrumentation/endoscopy, or prior gonococcal urethritis", "post-void urinary dribbling and sensation of incomplete bladder evacuation", "secondary complications: recurrent urinary tract infections, prostatitis, and bladder calculi", "flow rate evaluation: uroflowmetry shows flat, plateau-shaped curve with severely depressed peak flow rate (Qmax < 10-12 mL/s)"],
        "pertinent_negatives": ["normal non-enlarged prostate on DRE and ultrasound"],
        "content": "Fibrotic narrowing of the urethral lumen caused by contraction of dense spongiofibrosis within the corpus spongiosum following ischemic, traumatic, or infectious injury. Diagnostic gold standard: Retrograde Urethrography (RUG) combined with Voiding Cystourethrography (VCUG) to delineate stricture length, location, and degree of spongiofibrosis. Treatment: Short (< 1 cm) bulbar strictures: Direct Vision Internal Urethrotomy (DVIU) or dilatation (high recurrence rate); Definitive surgical gold standard: Open Urethroplasty (excision and primary end-to-end anastomosis for short strictures, or Buccal Mucosa Graft [BMG] substitution urethroplasty for longer strictures, achieving > 85-90% permanent cure rate)."
    },
    {
        "id": "ICD10-R33.9",
        "topic": "Acute Urinary Retention (Bladder Catheterization & Post-Obstructive Diuresis)",
        "icd10": "R33.9",
        "specialty": "Urology / Emergency Medicine",
        "organ_system": "Urological Emergency",
        "keywords": ["acute urinary retention", "inability to pass urine", "painful bladder distension", "post obstructive diuresis", "foley catheter insertion", "suprapubic tenderness fullness"],
        "red_flags": ["bladder rupture", "acute post-renal renal failure", "post-obstructive severe polyuric shock and hypokalemia"],
        "clinical_hallmarks": ["sudden, agonizing, complete inability to pass urine despite urgent, painful straining and urge", "excruciating, severe suprapubic abdominal pain and restless agitation", "physical examination: visible and palpable, tense, exquisitely tender, smooth, globular suprapubic mass that is DULL TO PERCUSSION and extends upward towards the umbilicus (distended urinary bladder)", "bedside ultrasound / bladder scan: massive retained urine volume typically > 500-1500 mL", "precipitating factors: constipation, cold weather, anticholinergic or sympathomimetic medications (decongestants, antihistamines), or post-operative general anesthesia"],
        "pertinent_negatives": ["complete absence of urine output with agonizing urge differentiates from anuric renal failure (no urge)"],
        "content": "Acute, painful inability to voluntarily void urine, representing the most common urological emergency. Etiology: BPH (50%), urethral stricture, blood clots, prostate cancer, neurological injury, or anticholinergic drugs. Immediate Emergency Treatment: STAT Urethral Catheterization with a 14-16 Fr Foley catheter (or emergency Suprapubic Cystostomy if urethral catheterization fails or is contraindicated); Record initial drained urine volume. Critical Post-Catheterization Care: Monitor for Post-Obstructive Diuresis (defined as urine output > 200 mL/hr for > 2 consecutive hours), replacing 50-75% of hourly urinary fluid and electrolyte losses (0.45% Saline) to prevent hypovolemic shock and fatal hypokalemia."
    },
    {
        "id": "ICD10-N10",
        "topic": "Acute Pyelonephritis (Costovertebral Angle Tenderness & Pyuria)",
        "icd10": "N10",
        "specialty": "Nephrology / Urology / Infectious Disease",
        "organ_system": "Renal Infectious",
        "keywords": ["acute pyelonephritis", "kidney infection", "cvat", "costovertebral angle tenderness", "fever chills flank pain", "wbc casts in urine", "escherichia coli pyelonephritis"],
        "red_flags": ["uroseptic shock", "emphysematous pyelonephritis (gas in renal parenchyma on CT)", "renal cortical / perinephric abscess"],
        "clinical_hallmarks": ["classic clinical triad: 1. High spiking fever with shaking chills and rigors; 2. Severe unilateral or bilateral flank pain; 3. Pronounced COSTOVERTEBRAL ANGLE TENDERNESS (CVAT / positive Murphy's renal punch test on gentle fist percussion over 12th rib posteriorly)", "associated lower urinary tract symptoms: dysuria, urgency, and frequency", "systemic symptoms: anorexia, nausea, and vomiting", "urinalysis: cloudy, foul urine with heavy pyuria (> 10 WBC/hpf), positive leukocyte esterase, positive nitrites, and pathognomonic WHITE BLOOD CELL (WBC) CASTS indicating upper renal tubular origin"],
        "pertinent_negatives": ["wbc casts differentiate upper urinary tract pyelonephritis from simple lower cystitis"],
        "content": "Bacterial infection and acute inflammation of the renal parenchyma and renal pelvis, caused by ascending infection from the lower urinary tract (Escherichia coli 75-90%, Klebsiella, Proteus mirabilis). Diagnostic workup: Urinalysis, urine culture and antibiotic sensitivity, CBC, serum creatinine, blood cultures; Contrast CT abdomen/pelvis indicated for non-responders at 48-72 hours to rule out renal abscess, obstruction, or emphysematous changes. Treatment: Outpatient mild: Oral Ciprofloxacin (500 mg BID for 7 days) or Levofloxacin (750 mg daily for 5 days); Inpatient moderate-severe: IV Ceftriaxone (1-2 g daily) or Piperacillin-Tazobactam."
    },
    {
        "id": "ICD10-N20.1",
        "topic": "Ureteral Calculi & Acute Renal Colic",
        "icd10": "N20.1",
        "specialty": "Urology / Emergency Medicine",
        "organ_system": "Urological",
        "keywords": ["renal colic", "ureteral calculus", "kidney stone", "flank pain radiating to groin", "hematuria stone", "non contrast ct kub", "tamsulosin stone expulsion"],
        "red_flags": ["obstructing ureteral stone WITH INFECTION / FEVER (stat urological emergency)", "anuria in solitary kidney", "intractable pain and dehydration"],
        "clinical_hallmarks": ["sudden onset of excruciating, agonizing, colicky flank pain that classically RADIATES ANTERIORLY DOWN THE ABDOMEN INTO THE GROIN, SCROTUM, OR LABIUM MAJUS (following genitofemoral and ilioinguinal nerve pathways)", "paroxysmal nature: pain peaks over 20-60 minutes, with patient RESTLESSLY PACING AND UNABLE TO FIND A COMFORTABLE POSITION (in sharp contrast to peritonitis where patient lies rigidly motionless)", "gross or microscopic hematuria present in > 85-90% of cases", "associated nausea, diaphoresis, and reflex vomiting", "irritative voiding symptoms (urgency, strangury) occur when the calculus lodges at the ureterovesical junction (UVJ)"],
        "pertinent_negatives": ["no peritoneal signs (soft, non-tender abdomen between spasms)"],
        "content": "Mechanical obstruction of the ureter by a calculus migrating from the kidney, producing proximal ureteral dilatation, renal pelvic hypertension, and prostaglandin-mediated capsular stretch. Diagnostic gold standard: Low-Dose Non-Contrast CT of Kidneys, Ureters, and Bladder (CT KUB - sensitivity and specificity > 97%). Emergency rule: An OBSTRUCTED AND INFECTED KIDNEY (stone + fever/pyuria) is a LIFE-THREATENING EMERGENCY requiring STAT urinary decompression (Double-J stent or percutaneous nephrostomy). Uncomplicated stones: IV NSAIDs (Ketorolac 30 mg IV is first-line, superior to opioids); Medical Expulsive Therapy (Tamsulosin 0.4 mg daily for stones 5-10 mm); Ureteroscopy (URS) with laser lithotripsy or ESWL."
    },

    # --- 5. NEUROLOGY & NEUROSURGERY (14) ---
    {
        "id": "ICD10-I62.00",
        "topic": "Subdural Hematoma (Acute vs Chronic - Bridging Vein Tear)",
        "icd10": "I62.00",
        "specialty": "Neurosurgery / Neurology / Emergency Medicine",
        "organ_system": "Neurological / Cranial Trauma",
        "keywords": ["subdural hematoma", "sdh", "crescent shaped hematoma", "bridging vein rupture", "chronic sdh elderly fall", "uncal herniation dilated pupil"],
        "red_flags": ["rapidly declining GCS", "unilateral fixed dilated 'blown' pupil (uncal herniation)", "Cushing triad (bradycardia, hypertension, irregular respiration)"],
        "clinical_hallmarks": ["Acute SDH: high-energy head trauma presenting with immediate coma or progressive neurological deterioration, hemiparesis, and ipsilateral pupil dilation", "Chronic SDH: insidious presentation weeks to months after trivial head bump in elderly or alcoholic individuals, mimicking dementia, transient ischemic attacks, progressive headache, unsteady gait, or personality changes", "Non-Contrast Head CT: pathognomonic CRESCENT-SHAPED (crescentic, concavo-convex) extra-axial hyperdense (acute) or hypodense/isodense (chronic) hemorrhage that CROSSES SUTURE LINES but is limited by the dural reflections (falx and tentorium)"],
        "pertinent_negatives": ["hematoma crosses suture lines (distinguishes decisively from biconvex epidural hematoma)"],
        "content": "Accumulation of blood beneath the inner layer of the dura mater and above the arachnoid membrane, caused by shearing rupture of the fragile cortical bridging veins that traverse the subdural space to drain into the superior sagittal sinus. Brain atrophy in the elderly stretches these veins, creating marked vulnerability. Management: Acute SDH with thickness > 10 mm or midline shift > 5 mm or declining GCS: Emergent decompressive craniotomy and hematoma evacuation; Chronic symptomatic SDH: Burr hole trephination and closed-system drainage, or mini-craniotomy; Correction of coagulopathies and antiepileptic prophylaxis."
    },
    {
        "id": "ICD10-I62.1",
        "topic": "Epidural Hematoma (Middle Meningeal Artery & Lucid Interval)",
        "icd10": "I62.1",
        "specialty": "Neurosurgery / Emergency Medicine / Trauma Surgery",
        "organ_system": "Neurological / Cranial Emergency",
        "keywords": ["epidural hematoma", "edh", "middle meningeal artery", "lucid interval", "biconvex lens shaped hematoma", "pterion fracture skull"],
        "red_flags": ["blown pupil from uncal herniation", "rapid respiratory arrest", "decerebrate posturing"],
        "clinical_hallmarks": ["classic clinical sequence: 1. Impact blunt head trauma to temporal fossa (pterion fracture); 2. Brief initial loss of consciousness; 3. Temporary 'LUCID INTERVAL' (patient awakens, feels normal or complains of headache for several minutes to hours); 4. Sudden, catastrophic neurological collapse with coma, ipsilateral mydriasis (fixed dilated pupil), and contralateral hemiparesis", "Non-Contrast Head CT (pathognomonic): BICONVEX, LENS-SHAPED (lenticular), sharply demarcated hyperdense extra-axial collection that DOES NOT CROSS SUTURE LINES (where dura is firmly adherent to the skull table)"],
        "pertinent_negatives": ["hematoma does NOT cross cranial sutures (distinguishes from subdural hematoma)"],
        "content": "Arterial hemorrhage into the potential space between the inner table of the skull and the outer periosteal layer of the dura mater, overwhelmingly (> 85%) caused by a temporal bone fracture tearing the Middle Meningeal Artery at the pterion. High arterial pressure produces rapid hematoma expansion and life-threatening uncal herniation compressing the brainstem and CN III. Management: Surgical emergency: Emergent Craniotomy and surgical evacuation of the hematoma with coagulation of the bleeding middle meningeal vessel. Patients treated before herniation achieve near-complete neurological recovery."
    },
    {
        "id": "ICD10-I60.9",
        "topic": "Subarachnoid Hemorrhage (Saccular Aneurysm & Thunderclap Headache)",
        "icd10": "I60.9",
        "specialty": "Neurosurgery / Neurology / Emergency Medicine",
        "organ_system": "Cerebrovascular Emergency",
        "keywords": ["subarachnoid hemorrhage", "sah", "thunderclap headache", "worst headache of life", "berry aneurysm rupture", "xanthochromia on lp", "nimodipine sah"],
        "red_flags": ["rebleeding (highest risk in first 24h)", "cerebral vasospasm / delayed cerebral ischemia", "acute obstructive hydrocephalus"],
        "clinical_hallmarks": ["sudden, explosive, instantaneous onset of excruciating headache reaching MAXIMUM INTENSITY WITHIN 1 MINUTE ('thunderclap headache'), universally described as 'THE WORST HEADACHE OF MY ENTIRE LIFE'", "frequently accompanied by neck stiffness (nuchal rigidity), photophobia, nausea, projectile vomiting, and transient loss of consciousness", "subhyaloid / preretinal flame hemorrhages on fundoscopy (Terson syndrome)", "Non-Contrast Head CT (within 6 hours sensitivity > 99%): hyperdense blood filling the basal cisterns, sylvian fissures, and subarachnoid spaces", "Lumbar Puncture (indicated if CT is negative but clinical suspicion persists): shows persistent blood in all 4 tubes and pathognomonic XANTHOCHROMIA (yellowish supernatant due to oxyhemoglobin/bilirubin breakdown) on spectrophotometry"],
        "pertinent_negatives": ["no preceding mild gradual headache; onset is instantaneous like a clap of thunder"],
        "content": "Rupture of an intracranial saccular ('berry') aneurysm (85% located in the Circle of Willis: ACom, PCom, MCA) releasing arterial blood under systemic pressure into the subarachnoid space. Hunt and Hess clinical scale. Diagnostic workup: Emergent Non-Contrast Head CT -> Lumbar Puncture if CT normal -> CT Angiography (CTA) or Digital Subtraction Angiography (DSA). Protocol: 1. STAT aneurysm securing within 24 hours (Endovascular Coiling or Microsurgical Clipping); 2. Enteral Nimodipine (60 mg q4h for 21 days) to prevent delayed ischemic neurological deficits from vasospasm; 3. Strict systolic BP control (< 140 mmHg) before clipping; 4. External Ventricular Drain (EVD) for hydrocephalus."
    },
    {
        "id": "ICD10-G35",
        "topic": "Multiple Sclerosis (Relapsing-Remitting & McDonald Criteria)",
        "icd10": "G35",
        "specialty": "Neurology",
        "organ_system": "Central Nervous System Autoimmune",
        "keywords": ["multiple sclerosis", "ms", "relapsing remitting ms", "optic neuritis eye pain", "uhthoff phenomenon", "lhermitte sign", "oligoclonal bands csf", "dawson fingers mri"],
        "red_flags": ["rapid quadriplegia / transverse myelitis", "acute respiratory muscle weakness"],
        "clinical_hallmarks": ["neurological deficits 'DISSEMINATED IN TIME AND SPACE' in young adults (20-40 years, female:male 3:1)", "Optic Neuritis: acute painful loss of central vision, impaired color vision (dyschromatopsia), and relative afferent pupillary defect (RAPD / Marcus Gunn pupil)", "Lhermitte's sign: transient electric-shock-like sensation shooting down spine and limbs upon neck flexion", "Uhthoff's phenomenon: reversible worsening of neurological deficits triggered by heat, hot showers, or exercise", "Brain/Spinal MRI with gadolinium (McDonald criteria): periventricular, juxtacortical, and infratentorial hyperintense T2/FLAIR lesions oriented perpendicular to lateral ventricles ('Dawson's fingers')", "Lumbar Puncture: CSF-specific Oligoclonal IgG Bands (OCBs) present in > 85-90% of patients"],
        "pertinent_negatives": ["absence of simultaneous bilateral optic nerve and long spinal cord lesions (which characterize NMO / AQP4-positive disease)"],
        "content": "Chronic, autoimmune, inflammatory demyelinating disease of the central nervous system characterized by immune-mediated attack against myelin basic protein and oligodendrocytes. Relapsing-Remitting MS (RRMS 85%). Treatment: Acute relapse: High-dose IV Methylprednisolone (1 g IV daily for 3-5 days); Disease-Modifying Therapies (DMTs) to reduce relapse frequency and disability accumulation: Injectables (Glatiramer acetate, Interferon-beta), Oral agents (Fingolimod, Dimethyl fumarate), Monoclonal antibodies (Ocrelizumab, Natalizumab, Alemtuzumab)."
    },
    {
        "id": "ICD10-G12.21",
        "topic": "Amyotrophic Lateral Sclerosis (ALS - Motor Neuron Disease)",
        "icd10": "G12.21",
        "specialty": "Neurology",
        "organ_system": "Neurodegenerative Motor System",
        "keywords": ["amyotrophic lateral sclerosis", "als", "motor neuron disease", "mnd", "fasciculations tongue", "combined umn and lmn signs", "progressive bulbar palsy", "riluzole als"],
        "red_flags": ["diaphragmatic respiratory failure (vital capacity < 50%)", "aspiration pneumonia from severe bulbar dysphagia"],
        "clinical_hallmarks": ["pathognomonic hallmark: SIMULTANEOUS UPPER MOTOR NEURON (UMN) AND LOWER MOTOR NEURON (LMN) SIGNS in the same limb or body segment, with progressive spread to adjacent segments", "LMN signs: muscle weakness, asymmetric wasting / atrophy, and diffuse widespread fasciculations (spontaneous muscle twitches, especially pathognomonic tongue fasciculations)", "UMN signs: hyperreflexia, spasticity, clonus, and extensor plantar responses (Babinski sign) in an atrophied limb", "Bulbar onset (25%): progressive dysarthria ('hot-potato' or slurred speech), dysphagia, sialorrhea, and pseudobulbar affect (inappropriate, involuntary laughing or crying)", "STRICT PRESERVATION OF: sensory examination, extraocular eye movements, and bowel/bladder sphincter function"],
        "pertinent_negatives": ["sensory exam is completely normal (any sensory deficit argues strongly against ALS)"],
        "content": "Fatal, relentlessly progressive neurodegenerative disorder caused by loss of upper motor neurons in the primary motor cortex and lower motor neurons in the brainstem and anterior horns of the spinal cord (El Escorial diagnostic criteria). Diagnostic workup: Electromyography and Nerve Conduction Studies (EMG/NCS: widespread active denervation and chronic reinnervation), Brain and Cervical MRI (rules out cervical spondylotic myelopathy). Treatment: Multidisciplinary palliative care; Disease-modifying pharmacotherapy: Riluzole (50 mg BID - antiglutamatergic, prolongs tracheostomy-free survival by 2-3 months), Edaravone (free radical scavenger); Non-invasive positive pressure ventilation (NIV / BiPAP) when FVC drops; Percutaneous Endoscopic Gastrostomy (PEG) tube for dysphagia."
    },
    {
        "id": "ICD10-G61.0",
        "topic": "Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyradiculoneuropathy)",
        "icd10": "G61.0",
        "specialty": "Neurology / Critical Care",
        "organ_system": "Peripheral Nervous System Emergency",
        "keywords": ["guillain barre syndrome", "gbs", "ascending symmetric paralysis", "areflexia", "albuminocytological dissociation", "campylobacter gbs", "ivig for gbs"],
        "red_flags": ["impending respiratory arrest (forced vital capacity < 20 mL/kg)", "autonomic storm (malignant arrhythmias, extreme bp swings)"],
        "clinical_hallmarks": ["acute or subacute onset of PROGRESSIVE, SYMMETRIC, ASCENDING MUSCLE WEAKNESS beginning in lower extremities and advancing proximally to involve trunk, upper limbs, and facial/bulbar musculature over days to weeks", "GLOBAL AREFLEXIA or profound hyporeflexia in affected limbs (loss of knee and ankle jerks is an absolute diagnostic prerequisite)", "mild distal paresthesias ('glove and stocking') or back/radicular pain preceding weakness", "preceded 1-4 weeks by a triggering respiratory or gastrointestinal illness (classically Campylobacter jejuni, CMV, EBV, or Zika virus)", "Lumbar Puncture (pathognomonic): ALBUMINOCYTOLOGICAL DISSOCIATION (elevated CSF protein [often > 100-200 mg/dL] with a NORMAL white cell count [< 5 cells/mcL])"],
        "pertinent_negatives": ["absence of fever at onset of paralysis", "absence of a discrete sensory spinal level"],
        "content": "Post-infectious autoimmune polyradiculoneuropathy caused by molecular mimicry between microbial lipooligosaccharides and human peripheral nerve gangliosides (GM1, GD1a), resulting in complement-mediated demyelination or axonal destruction. Diagnostic workup: Lumbar puncture, EMG/NCS, vital capacity monitoring. CRITICAL RULE: CORTICOSTEROIDS ARE INEFFECTIVE AND SHOULD NOT BE GIVEN. Definitive Emergency Treatment: 1. Intravenous Immunoglobulin (IVIG: 0.4 g/kg/day for 5 days) OR Plasma Exchange (Plasmapheresis: 5 exchanges over 1-2 weeks) initiated early; 2. Frequent monitoring of respiratory function ('20/30/40 rule': FVC < 20 mL/kg, NIF < -30 cmH2O, or 40% reduction warrants elective intubation in ICU); 3. Cardiac telemetry for autonomic instability."
    },
    {
        "id": "ICD10-G70.00",
        "topic": "Myasthenia Gravis & Myasthenic Crisis",
        "icd10": "G70.00",
        "specialty": "Neurology / Critical Care",
        "organ_system": "Neuromuscular Autoimmune",
        "keywords": ["myasthenia gravis", "fatigable muscle weakness", "fluctuating ptosis diplopia", "acetylcholine receptor antibody", "anti achr", "pyridostigmine", "tensilon test", "thymoma"],
        "red_flags": ["myasthenic crisis (respiratory failure requiring mechanical ventilation)", "severe bulbar weakness with aspiration"],
        "clinical_hallmarks": ["cardinal feature: PATHOLOGICAL, FATIGABLE MUSCLE WEAKNESS that WORSENS WITH REPETITIVE USE OR TOWARDS THE END OF THE DAY and IMPROVES PROMPTLY WITH REST", "ocular manifestations (> 85%): fluctuating, asymmetric ptosis (drooping eyelids) and binocular diplopia (double vision)", "bulbar symptoms: nasal slurred speech with prolonged talking, chewing fatigue, and difficulty swallowing liquids", "Ice Pack Test: placing an ice pack over ptotic eyelid for 2 minutes produces significant resolution of ptosis (sensitivity > 90% due to cold inhibiting acetylcholinesterase)", "associated with Thymic Hyperplasia (65%) or Thymoma (10-15%)"],
        "pertinent_negatives": ["pupillary reflexes are completely normal and spared", "deep tendon reflexes are brisk and preserved"],
        "content": "Autoimmune disease of the neuromuscular junction caused by pathogenic autoantibodies directed against the postsynaptic nicotinic Acetylcholine Receptor (Anti-AChR 85%) or Muscle-Specific Tyrosine Kinase (Anti-MuSK), leading to complement-mediated destruction of junctional folds and receptor loss. Diagnostic workup: Serum Anti-AChR and Anti-MuSK antibodies, Repetitive Nerve Stimulation (RNS: decremental response > 10%), Single-Fiber EMG, Contrast CT chest for thymoma. Treatment: 1. Symptomatic: Oral Pyridostigmine (60 mg q4-6h - acetylcholinesterase inhibitor); 2. Immunosuppression: Oral Prednisone + Azathioprine / Mycophenolate; 3. Thymectomy (improves long-term remission even in non-thymomatous AChR+ patients); 4. Myasthenic Crisis: IVIG or Plasmapheresis + ICU mechanical ventilation; AVOID beta-blockers, aminoglycosides, fluoroquinolones, and magnesium (which aggravate weakness)."
    },
    {
        "id": "ICD10-G91.2",
        "topic": "Normal Pressure Hydrocephalus (Hakim-Adams Triad & Ventriculomegaly)",
        "icd10": "G91.2",
        "specialty": "Neurology / Neurosurgery / Geriatrics",
        "organ_system": "Neurological / CSF Dynamic",
        "keywords": ["normal pressure hydrocephalus", "nph", "hakim adams triad", "wobbly wacky wet", "magnetic gait", "ventriculomegaly out of proportion", "tap test nph"],
        "red_flags": ["severe falls with intracranial hemorrhage", "complete immobility and incontinence"],
        "clinical_hallmarks": ["classic Hakim-Adams clinical triad (the mnemonic 'Wobbly, Wacky, Wet'): 1. Gait disturbance ('Wobbly' - earliest, most prominent feature): slow, wide-based, short-stepped, shuffling, 'magnetic gait' (feet appear glued to the floor, difficulty initiating steps and turning); 2. Cognitive impairment ('Wacky'): subcortical dementia with psychomotor slowing, apathy, executive dysfunction, and impaired recall; 3. Urinary incontinence ('Wet'): urinary urgency progressing to frequency and frontal-type urge incontinence", "Brain MRI/CT: ventriculomegaly (enlarged lateral and third ventricles with Evans index > 0.3) that is DISPROPORTIONATE TO CEREBRAL CORTICAL SULCAL ATROPHY, with tight high-convexity sulci and enlarged Sylvian fissures (DESH pattern)", "normal opening pressure on lumbar puncture"],
        "pertinent_negatives": ["magnetic gait with difficulty lifting feet distinguishes from Parkinson's festinating run"],
        "content": "Reversible neurological syndrome characterized by pathological accumulation of cerebrospinal fluid in cerebral ventricles with intermittent normal mean intracranial pressure, resulting from impaired CSF resorption through arachnoid granulations. Diagnostic confirmation: High-Volume Lumbar Tap Test (removal of 30-50 mL CSF via LP producing dramatic, measurable improvement in gait speed and balance within 2-4 hours). Definitive Treatment: Surgical insertion of a Ventriculoperitoneal (VP) Shunt with an adjustable programmable valve; achieving high rates of gait and cognitive recovery when performed early."
    },
    {
        "id": "ICD10-M31.5",
        "topic": "Giant Cell Arteritis & Polymyalgia Rheumatica (Temporal Arteritis)",
        "icd10": "M31.5",
        "specialty": "Rheumatology / Ophthalmology / Neurology",
        "organ_system": "Large Vessel Vasculitis",
        "keywords": ["giant cell arteritis", "temporal arteritis", "jaw claudication", "amaurosis fugax gca", "elevated esr crp elderly", "polymyalgia rheumatica", "temporal artery biopsy"],
        "red_flags": ["acute irreversible blindness (anterior ischemic optic neuropathy)", "aortic aneurysm / dissection"],
        "clinical_hallmarks": ["new-onset, severe, persistent, unilateral or bitemporal throbbing headache in an older patient (> 50 years, mean age 72)", "pathognomonic sign: JAW CLAUDICATION (ischemic pain and fatigue in masseter muscles upon chewing food or prolonged talking, with > 90% specificity for GCA)", "scalp tenderness (pain upon combing hair or resting head on pillow)", "palpation of temporal artery: thick, tender, nodular, tortuous, cord-like vessel with diminished or absent pulse", "visual disturbances: transient monocular vision loss (amaurosis fugax) or sudden catastrophic painless visual loss due to Arteritic Anterior Ischemic Optic Neuropathy (A-AION)", "strongly associated with Polymyalgia Rheumatica (50%: morning stiffness and aching in bilateral shoulders and hips)", "laboratory hallmarks: marked elevation of ESR (typically > 50-100 mm/hr) and CRP"],
        "pertinent_negatives": ["DO NOT WITHHOLD HIGH-DOSE CORTICOSTEROIDS while waiting for temporal artery biopsy"],
        "content": "Granulomatous large-vessel vasculitis predominantly affecting the temporal arteries and other cranial branches of the external carotid artery and aorta. Immediate Clinical Mandate: If GCA is suspected, IMMEDIATELY initiate high-dose systemic corticosteroids to prevent irreversible contralateral blindness. Diagnostic gold standard: Unilateral or bilateral Temporal Artery Biopsy (TAB: showing transmural granulomatous inflammation with multinucleated giant cells and disruption of internal elastic lamina); Color Doppler ultrasound (hypoechoic 'halo sign'). Treatment: Without visual loss: Oral Prednisone (40-60 mg daily); With impending/active visual loss: STAT IV pulse Methylprednisolone (1 g daily for 3 days) followed by high-dose oral steroids; IL-6 receptor antagonist (Tocilizumab) as a steroid-sparing agent."
    },
    {
        "id": "ICD10-G51.0",
        "topic": "Bell's Palsy (Idiopathic Facial Nerve Paralysis - LMN vs UMN)",
        "icd10": "G51.0",
        "specialty": "Neurology / ENT / Emergency Medicine",
        "organ_system": "Cranial Neuropathy",
        "keywords": ["bells palsy", "facial nerve palsy", "facial droop forehead involved", "inability to close eye", "bells phenomenon", "lmn vs umn facial palsy", "taste loss tongue"],
        "red_flags": ["corneal ulceration from lagophthalmos", "sparing of forehead (indicates central stroke/cva, NOT Bell's palsy)", "vesicles in ear canal (Ramsay Hunt syndrome)"],
        "clinical_hallmarks": ["acute onset (typically over 24-48 hours) of UNILATERAL COMPLETE FACIAL MUSCLE WEAKNESS", "CRITICAL CLINICAL DISTINCTION: LOWER MOTOR NEURON (LMN) LESION INVOLVES THE FOREHEAD (inability to wrinkle forehead, raise eyebrow, or fully close eye / lagophthalmos), because the upper facial nerve nucleus receives bilateral cortical innervation. By contrast, an Upper Motor Neuron (UMN / stroke) lesion SPARES THE FOREHEAD", "Bell's phenomenon: reflex upward and outward rolling of the eyeball when attempting to close the affected eye", "hyperacusis (painful sensitivity to sound from paralysis of stapedius muscle)", "loss of taste sensation (dysgeusia) on the anterior two-thirds of the tongue (chorda tympani involvement)", "drooling from corner of mouth and flattening of nasolabial fold"],
        "pertinent_negatives": ["forehead weakness confirms LMN etiology (excludes central cerebral infarction/stroke)"],
        "content": "Acute, idiopathic peripheral neuropathy of Cranial Nerve VII (Facial Nerve) within the fallopian canal, strongly linked to herpes simplex virus (HSV-1) reactivation and inflammatory edema. Treatment: 1. Oral Corticosteroids (Prednisone 60 mg daily for 5-7 days tapered over 5 days) MUST BE INITIATED WITHIN 72 HOURS OF ONSET to maximize complete recovery; 2. Oral antiviral (Valacyclovir 1000 mg TID for 7 days) in severe paralysis; 3. Eye care (CRITICAL: preservative-free artificial tears during the day, lubricating eye ointment and eye taping at night to prevent exposure keratitis and corneal blindness)."
    },
    {
        "id": "ICD10-G83.4",
        "topic": "Cauda Equina Syndrome vs Conus Medullaris Syndrome",
        "icd10": "G83.4",
        "specialty": "Neurosurgery / Orthopedic Spine Surgery / Emergency Medicine",
        "organ_system": "Spinal Cord & Radicular Emergency",
        "keywords": ["cauda equina syndrome", "saddle anesthesia", "urinary retention with overflow", "loss of anal sphincter tone", "conus medullaris", "massive lumbar disc herniation"],
        "red_flags": ["irreversible paraplegia / bowel and bladder incontinence if surgery delayed beyond 24-48 hours", "saddle numbness"],
        "clinical_hallmarks": ["Cauda Equina Syndrome (LMN compression of lumbosacral nerve roots L2-S5): 1. SADDLE ANESTHESIA (loss of sensation in perineum, buttocks, anus, and upper inner thighs - S3-S5 dermatomes); 2. Bladder dysfunction (urinary retention with overflow incontinence / large post-void residual volume); 3. Fecal incontinence with severely lax or ABSENT ANAL SPHINCTER TONE on digital rectal exam; 4. Severe bilateral sciatica / asymmetric lower limb weakness and absent ankle reflexes", "Conus Medullaris Syndrome (T12-L2 cord termination): sudden, bilateral, symmetric saddle numbness, early urinary/fecal incontinence, preserved or hyperactive ankle jerks (UMN component)", "most common etiology: massive central lumbar disc herniation (L4-L5 or L5-S1) or spinal tumor/hematoma"],
        "pertinent_negatives": ["absence of normal anal squeeze confirms sacral root denervation"],
        "content": "Surgical emergency caused by mechanical compression of the bundle of nerve roots forming the cauda equina distal to the conus medullaris. Diagnostic gold standard: STAT Emergency Whole-Spine MRI. Immediate Management: Emergency surgical decompression via decompressive Lumbar Laminectomy and Discectomy PERFORMED WITHIN 24-48 HOURS of symptom onset; delays beyond 48 hours dramatically increase the risk of permanent bladder/bowel incontinence and permanent sexual dysfunction."
    },
    {
        "id": "ICD10-G40.901",
        "topic": "Status Epilepticus (Generalized Convulsive - 5-Minute Definition)",
        "icd10": "G40.901",
        "specialty": "Neurology / Emergency Medicine / Critical Care",
        "organ_system": "Neurological Emergency",
        "keywords": ["status epilepticus", "prolonged seizure > 5 minutes", "recurrent seizures without recovery", "lorazepam for seizure", "levetiracetam status", "refractory status epilepticus"],
        "red_flags": ["hypoxic brain injury and neuronal death after 30 minutes", "severe rhabdomyolysis / acute renal failure", "hyperthermia and refractory acidosis"],
        "clinical_hallmarks": ["modern operational definition (ILAE): continuous, unremitting generalized convulsive seizure activity lasting GREATER THAN 5 MINUTES (t1 time point), OR two or more discrete seizures without complete recovery of consciousness between episodes", "tonic-clonic motor convulsions: sustained muscular contraction followed by violent rhythmic symmetric clonic jerking of all extremities", "autonomic surge: tachycardia, severe hypertension, hyperthermia, pupillary dilation, and copious oral secretions", "subtle status: in prolonged or sedated patients, visible motor jerks may dwindle to subtle rhythmic eye twitching or nystagmoid jerks despite continuous electrographic seizure activity on EEG"],
        "pertinent_negatives": ["no purposeful movements or response to voice during ictal state"],
        "content": "Life-threatening neurological emergency characterized by failure of the endogenous mechanisms responsible for seizure termination or initiation of mechanisms leading to abnormally prolonged seizures. Protocol (Time-Sensitive): Phase 1 (0-5 min): ABCs, high-flow O2, IV access, bedside capillary glucose (IV 50% Dextrose if hypoglycemic); Phase 2 (5-20 min - First-line Benzodiazepines): IV Lorazepam (0.1 mg/kg, typically 4 mg IV bolus) OR IM Midazolam (10 mg); repeat once if seizing continues; Phase 3 (20-40 min - Second-line Antiepileptics): IV Levetiracetam (60 mg/kg, max 4500 mg) OR IV Fosphenytoin (20 mg PE/kg) OR IV Valproate (40 mg/kg); Phase 4 (> 40 min - Refractory Status): General anesthesia and endotracheal intubation with IV continuous infusion of Propofol, Midazolam, or Ketamine with continuous EEG monitoring."
    },
    {
        "id": "ICD10-G43.109",
        "topic": "Migraine with Aura (Scintillating Scotoma & Cortical Spreading Depression)",
        "icd10": "G43.109",
        "specialty": "Neurology / Primary Care",
        "organ_system": "Neurological / Cephalgia",
        "keywords": ["migraine with aura", "scintillating scotoma", "fortification spectra", "unilateral throbbing headache photophobia", "triptans for migraine", "cgrp antagonists"],
        "red_flags": ["motor weakness during aura (hemiplegic migraine)", "headache reaching peak in < 1 minute (thunderclap - rules out SAH)", "aura lasting > 60 minutes or acute onset with negative symptoms"],
        "clinical_hallmarks": ["classic visual aura (in 25-30% of migraineurs): fully reversible focal neurological symptoms developing gradually over 5-20 minutes and lasting less than 60 minutes", "pathognomonic visual aura features: Scintillating Scotoma (a luminous, shimmering blind spot with jagged, flickering zigzag borders resembling walls of a medieval fortress / 'fortification spectra' spreading across visual field)", "followed within 60 minutes by a moderate-to-severe, unilateral, pulsating/throbbing headache", "pain is characteristically aggravated by routine physical activity (walking, climbing stairs)", "associated with intense photophobia, phonophobia, nausea, and vomiting; patient seeks dark, quiet room to lie motionless"],
        "pertinent_negatives": ["visual aura evolves gradually over minutes (distinguishes from sudden instantaneous vascular TIA/stroke)"],
        "content": "Neurovascular brain disorder driven by Cortical Spreading Depression (a wave of neuronal and glial depolarization) activating the trigeminovascular system and releasing calcitonin gene-related peptide (CGRP), neurokinin A, and Substance P. Treatment: 1. Acute abortive: 5-HT1B/1D receptor agonists (Triptans: oral Sumatriptan 50-100 mg, Rizatriptan) taken at onset of headache (NOT during aura); CGRP receptor antagonists (Gepants: Rimegepant); NSAIDs/Acetaminophen; 2. Prophylaxis (for >= 4 headache days/month): Beta-blockers (Propranolol), Topiramate, Amitriptyline, or monthly subcutaneous CGRP monoclonal antibodies (Erenumab, Fremanezumab)."
    },
    {
        "id": "ICD10-G45.9",
        "topic": "Transient Ischemic Attack (ABCD2 Score & Carotid Stenosis)",
        "icd10": "G45.9",
        "specialty": "Neurology / Vascular Surgery / Emergency Medicine",
        "organ_system": "Cerebrovascular",
        "keywords": ["transient ischemic attack", "tia", "mini stroke", "temporary facial droop weakness", "amaurosis fugax", "abcd2 score", "carotid endarterectomy"],
        "red_flags": ["high ABCD2 score (>= 4-6 indicates high 48-hour stroke risk)", "crescendo TIAs (multiple episodes over 24-48 hours)", "carotid artery stenosis > 70%"],
        "clinical_hallmarks": ["transient, reversible episode of neurological dysfunction caused by focal brain, spinal cord, or retinal ischemia, WITHOUT ACUTE INFARCTION on neuroimaging", "typical symptoms resolve completely within minutes to an hour (most last < 15-30 minutes)", "clinical manifestations: sudden unilateral arm/leg weakness, facial drooping, dysarthria, expressive aphasia, or monocular transient painless visual blackout ('amaurosis fugax' - transient curtain descending over one eye)", "ABCD2 Clinical Risk Score (predicts 2-day stroke risk up to 8%): Age >= 60 (1 pt); BP >= 140/90 (1 pt); Clinical features: unilateral weakness (2 pts) or speech disturbance without weakness (1 pt); Duration: >= 60 min (2 pts) or 10-59 min (1 pt); Diabetes (1 pt)"],
        "pertinent_negatives": ["complete resolution of neurological deficits on physical examination upon presentation"],
        "content": "Tissue-based definition: transient ischemia without structural tissue infarction. Represents an urgent harbinger of impending disabling ischemic stroke (10-15% of strokes occur within 90 days of a TIA, half within 48 hours). Diagnostic workup: STAT Brain MRI with Diffusion-Weighted Imaging (DWI) + MRA/CTA of head and neck, ECG, continuous telemetry for atrial fibrillation, Transthoracic/Transesophageal Echo. Protocol: 1. STAT Dual Antiplatelet Therapy (DAPT: Aspirin + Clopidogrel for 21 days, then monotherapy); 2. High-intensity Statin (Atorvastatin 80 mg); 3. Anticoagulation (DOAC) if atrial fibrillation; 4. Urgent Carotid Endarterectomy (CEA within 7-14 days) for symptomatic carotid stenosis 70-99%."
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
            
    print(f"Batch 2 added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

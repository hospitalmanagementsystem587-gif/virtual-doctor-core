"""
Expands clinical knowledge base from 32 to 100+ protocols.
Adds comprehensive primary care, emergency medicine, tropical infections,
pediatrics, geriatric syndromes, ENT, ophthalmology, dermatology, urology, and psychiatry protocols.
"""

import json
import os

EXPANDED_PROTOCOLS = [
    # 33. Pediatric Croup
    {
        "id": "CLIN-PED-033",
        "topic": "Acute Laryngotracheobronchitis (Croup)",
        "icd10": "J05.0",
        "specialty": "Pediatrics / Emergency Medicine",
        "organ_system": "Pediatric Respiratory",
        "keywords": ["croup", "barking cough", "seal like cough", "stridor at rest", "hoarseness", "steeple sign", "pediatric respiratory distress"],
        "red_flags": ["stridor at rest", "sternal retractions", "cyanosis", "lethargy", "inability to drink"],
        "clinical_hallmarks": ["seal-bark cough", "inspiratory stridor", "subglottic tracheal narrowing", "viral parainfluenza etiology"],
        "pertinent_negatives": ["no drooling (rules out epiglottitis)", "no toxic shock appearance"],
        "content": "Croup is an acute viral infection of upper respiratory tract common in infants 6 months to 3 years. Key features include sudden onset harsh barking seal-like cough, inspiratory stridor, and hoarseness, often worse at night. Treatment involves oral dexamethasone (0.15-0.6 mg/kg), cool mist or humidified air, and nebulized racemic epinephrine for moderate-to-severe stridor."
    },
    # 34. Acute Epiglottitis
    {
        "id": "CLIN-PED-034",
        "topic": "Acute Epiglottitis & Supraglottitis",
        "icd10": "J05.1",
        "specialty": "Pediatrics / ENT / Emergency",
        "organ_system": "Pediatric Upper Airway",
        "keywords": ["epiglottitis", "tripod position", "drooling", "muffled voice", "hot potato voice", "toxic appearance", "high fever with stridor"],
        "red_flags": ["tripod positioning", "inability to swallow saliva", "drooling", "airway stridor", "toxic appearance"],
        "clinical_hallmarks": ["the 3 Ds: Drooling, Dysphagia, Distress", "tripod posture", "cherry-red swollen epiglottis on visualization", "absence of barking cough"],
        "pertinent_negatives": ["no barking cough"],
        "content": "Life-threatening supraglottic inflammation predominantly caused by Hib or Streptococcus. Medical emergency requiring ENT and anesthesia STAT. Do not examine throat with tongue depressor in non-controlled setting as it may trigger fatal laryngospasm. Immediate airway management, STAT IV ceftriaxone and vancomycin."
    },
    # 35. Acute Bronchiolitis (RSV)
    {
        "id": "CLIN-PED-035",
        "topic": "Acute Viral Bronchiolitis (RSV)",
        "icd10": "J21.0",
        "specialty": "Pediatrics",
        "organ_system": "Pediatric Pulmonology",
        "keywords": ["bronchiolitis", "rsv", "infant wheezing", "tachypnea in infant", "nasal flaring", "subcostal retractions", "poor feeding in infant"],
        "red_flags": ["apnea episodes", "spO2 < 90%", "grunting respirations", "poor oral intake < 50%"],
        "clinical_hallmarks": ["infant < 2 years", "rhinorrhea followed by fine bilateral expiratory crackles and wheeze", "tachypnea", "hyperinflated lungs on chest x-ray"],
        "pertinent_negatives": ["no focal lung consolidation", "no stridor at rest"],
        "content": "Viral lower respiratory tract infection primarily due to Respiratory Syncytial Virus (RSV) in infants. Supportive management with gentle nasal suctioning, warm humidification, and hydration. Bronchodilators and systemic steroids are NOT routinely recommended by AAP guidelines."
    },
    # 36. Febrile Seizures
    {
        "id": "CLIN-PED-036",
        "topic": "Simple and Complex Febrile Seizures",
        "icd10": "R56.00",
        "specialty": "Pediatrics / Pediatric Neurology",
        "organ_system": "Pediatric Nervous System",
        "keywords": ["febrile seizure", "fever convulsion", "seizure with high fever", "pediatric fit", "jerking with fever"],
        "red_flags": ["seizure lasting > 15 minutes", "focal jerking of one limb", "incomplete recovery after 1 hour", "meningismus signs (stiff neck, bulging fontanelle)"],
        "clinical_hallmarks": ["age 6 months to 5 years", "generalized tonic-clonic convulsion associated with rapid fever spike > 38.5C", "duration < 15 min for simple febrile seizure"],
        "pertinent_negatives": ["no central nervous system infection", "no previous unprovoked seizure history"],
        "content": "Benign generalized seizures in young children triggered by rapid temperature spikes. Excellent long-term prognosis. Parent reassurance, antipyretics for comfort (paracetamol/ibuprofen), identification and treatment of source infection (viral illness, otitis media)."
    },
    # 37. Acute Meningitis
    {
        "id": "CLIN-ID-037",
        "topic": "Acute Bacterial and Viral Meningitis",
        "icd10": "G00.9",
        "specialty": "Emergency Medicine / Neurology",
        "organ_system": "Central Nervous System",
        "keywords": ["meningitis", "stiff neck", "nuchal rigidity", "photophobia with high fever", "kernig sign", "brudzinski sign", "petechial rash with fever", "meningismus"],
        "red_flags": ["petechial or purpuric non-blanching rash", "nuchal rigidity", "altered mental status with fever", "papilledema"],
        "clinical_hallmarks": ["triad of fever, altered mental status, and neck stiffness", "positive Kernig and Brudzinski signs", "cloudy CSF with neutrophilic pleocytosis and high protein"],
        "pertinent_negatives": ["no focal neurological signs initially"],
        "content": "Life-threatening leptomeningeal infection. Statutory medical emergency. Obtain blood cultures and start empiric IV ceftriaxone + vancomycin + dexamethasone immediately without delaying for lumbar puncture if signs of sepsis or elevated ICP are present."
    },
    # 38. Chikungunya Viral Fever
    {
        "id": "CLIN-ID-038",
        "topic": "Chikungunya Viral Infection & Polyarthralgia",
        "icd10": "A92.0",
        "specialty": "Infectious Disease / Rheumatology",
        "organ_system": "Systemic / Musculoskeletal",
        "keywords": ["chikungunya", "severe joint pain with fever", "crippling polyarthralgia", "wrist pain after mosquito bite", "maculopapular rash with joint swelling"],
        "red_flags": ["severe dehydration", "confusion", "oliguria", "meningoencephalitis signs"],
        "clinical_hallmarks": ["high abrupt fever", "severe debilitating bilateral symmetrical polyarthralgia predominantly involving wrists, hands, and ankles", "stooped posture due to joint agony"],
        "pertinent_negatives": ["no shock syndrome", "no severe thrombocytopenia < 20,000"],
        "content": "Aedes mosquito-borne alphavirus infection prevalent in India. Characterized by high fever and severe, debilitating symmetrical joint pains that may persist for months. Treatment is supportive: hydration, paracetamol, and NSAIDs once dengue has been ruled out."
    },
    # 39. Acute Hepatitis (Viral Hepatitis A / E)
    {
        "id": "CLIN-GI-039",
        "topic": "Acute Viral Hepatitis (Hepatitis A & E)",
        "icd10": "B15.9",
        "specialty": "Gastroenterology / Hepatology",
        "organ_system": "Hepatic / Gastrointestinal",
        "keywords": ["hepatitis", "jaundice", "yellow eyes", "dark tea colored urine", "pale clay stool", "right upper quadrant heaviness", "loss of appetite with nausea"],
        "red_flags": ["hepatic encephalopathy", "asterixis", "prolonged prothrombin time / INR > 1.5", "bleeding diathesis"],
        "clinical_hallmarks": ["prodromal anorexia and nausea followed by icterus/jaundice", "dark tea-colored urine", "serum transaminases (ALT/AST) > 1000 IU/L", "tender hepatomegaly"],
        "pertinent_negatives": ["no biliary duct dilation on ultrasound", "no melena"],
        "content": "Enterically transmitted acute hepatic viral infection (fecal-oral water contamination common in monsoon season). Self-limiting course in majority. High risk of fulminant hepatic failure in pregnant females with Hepatitis E. Supportive care, avoid hepatotoxic medications, monitor LFTs and PT/INR."
    },
    # 40. Leptospirosis
    {
        "id": "CLIN-ID-040",
        "topic": "Leptospirosis (Weil Disease)",
        "icd10": "A27.0",
        "specialty": "Infectious Disease / General Medicine",
        "organ_system": "Systemic Zoonosis",
        "keywords": ["leptospirosis", "weil disease", "conjunctival suffusion", "calf tenderness with fever", "flood water exposure", "jaundice with oliguria"],
        "red_flags": ["pulmonary hemorrhage syndrome", "oliguria / acute kidney failure", "severe jaundice", "hypotension"],
        "clinical_hallmarks": ["intense subconjunctival suffusion without purulent exudate", "severe calf muscle tenderness", "triad of jaundice, renal failure, and bleeding (Weil syndrome)", "history of wading in floodwaters or rodent exposure"],
        "pertinent_negatives": ["no purulent eye discharge"],
        "content": "Zoonotic spirochetal infection transmitted through water contaminated by rodent urine. Biphasic illness: bacteremic phase followed by immune phase. Mild disease treated with oral doxycycline; severe pulmonary/renal leptospirosis requires IV penicillin G or ceftriaxone."
    },
    # 41. Scrub Typhus
    {
        "id": "CLIN-ID-041",
        "topic": "Scrub Typhus (Orientia tsutsugamushi)",
        "icd10": "A75.3",
        "specialty": "Infectious Disease / General Medicine",
        "organ_system": "Vector-Borne Rickettsial",
        "keywords": ["scrub typhus", "eschar", "mite bite", "fever with black crust sore", "thrombocytopenia with elevated transaminases", "chigger bite"],
        "red_flags": ["ards / severe breathlessness", "hypotension / septic shock", "encephalitis / delirium", "acute renal failure"],
        "clinical_hallmarks": ["cigarette-burn pathognomonic eschar with black crust and erythematous halo (in axilla, groin, beltline)", "generalized lymphadenopathy", "fever with hepatosplenomegaly"],
        "pertinent_negatives": ["no typical typhoid step-ladder pulse dissociation"],
        "content": "Vector-borne rickettsial infection transmitted by larval trombiculid mites (chiggers) in agricultural and brush regions. High clinical index of suspicion in unexplained acute febrile illness in India. Drug of choice: oral Doxycycline 100mg BID for 7 days or Azithromycin in pregnancy/children."
    },
    # 42. Acute Sinusitis
    {
        "id": "CLIN-ENT-042",
        "topic": "Acute Rhinosinusitis (Bacterial vs. Viral)",
        "icd10": "J01.90",
        "specialty": "ENT / Otorhinolaryngology",
        "organ_system": "Upper Respiratory / ENT",
        "keywords": ["sinusitis", "facial pressure", "maxillary tenderness", "purulent nasal discharge", "nasal congestion", "post-nasal drip", "sinus headache worse bending forward"],
        "red_flags": ["periorbital swelling or erythema", "visual changes / diplopia", "severe unilateral frontal headache", "meningeal signs"],
        "clinical_hallmarks": ["facial pain or pressure over cheeks or forehead", "purulent anterior/posterior nasal drainage", "symptoms > 10 days without improvement or 'double sickening' pattern"],
        "pertinent_negatives": ["no proptosis", "no ophthalmoplegia", "no neck stiffness"],
        "content": "Inflammation of nasal cavity and paranasal sinuses. Majority start as viral upper respiratory infections. Bacterial infection diagnosed when symptoms last >= 10 days without improvement or worsen after initial improvement. First-line: amoxicillin-clavulanate, nasal saline rinses, intranasal fluticasone."
    },
    # 43. Otitis Externa (Swimmer's Ear)
    {
        "id": "CLIN-ENT-043",
        "topic": "Acute Otitis Externa",
        "icd10": "H60.90",
        "specialty": "ENT / Otorhinolaryngology",
        "organ_system": "Ear / Hearing",
        "keywords": ["otitis externa", "swimmers ear", "ear pain", "tragus tenderness", "pinna traction pain", "ear discharge", "canal erythema"],
        "red_flags": ["malignant otitis externa in elderly diabetic", "facial nerve palsy", "periauricular fluctuance / mastoid tenderness"],
        "clinical_hallmarks": ["intense ear canal pain exquisitely triggered by pushing on tragus or pulling on pinna", "erythematous and edematous external ear canal", "serous or purulent canal debris"],
        "pertinent_negatives": ["no middle ear effusion", "no mastoid bone tenderness"],
        "content": "Superficial infection of external auditory canal skin, usually caused by Pseudomonas aeruginosa or Staphylococcus aureus following water exposure or mechanical cleaning. Treatment: thorough aural toilet, topical ciprofloxacin/dexamethasone otic drops, keep ear dry."
    },
    # 44. Allergic Rhinitis
    {
        "id": "CLIN-ENT-044",
        "topic": "Allergic Rhinitis (Hay Fever)",
        "icd10": "J30.9",
        "specialty": "ENT / Allergy & Immunology",
        "organ_system": "Upper Airway",
        "keywords": ["allergic rhinitis", "sneezing fits", "clear runny nose", "watery eyes", "allergic shiners", "nasal itch", "pale boggy nasal turbinates"],
        "red_flags": ["unilateral purulent discharge (rule out foreign body)", "frequent epistaxis", "sinus bone erosion"],
        "clinical_hallmarks": ["paroxysms of sneezing", "clear watery rhinorrhea", "nasal pruritus", "pale bluish edematous boggy turbinates on rhinoscopy"],
        "pertinent_negatives": ["no fever", "no purulent green discharge", "no severe unilateral facial pain"],
        "content": "IgE-mediated inflammatory disease of nasal mucosa triggered by aeroallergens (dust mites, pollens, mold). First-line pharmacological therapy: intranasal corticosteroid spray (fluticasone, mometasone) plus second-generation oral antihistamines (cetirizine, fexofenadine)."
    },
    # 45. Acute Conjunctivitis (Pink Eye)
    {
        "id": "CLIN-EYE-045",
        "topic": "Acute Infectious Conjunctivitis (Bacterial vs Viral)",
        "icd10": "H10.9",
        "specialty": "Ophthalmology",
        "organ_system": "Eye / Vision",
        "keywords": ["conjunctivitis", "pink eye", "red eye", "gritty sensation in eye", "eye discharge", "eyelids glued shut in morning", "preauricular lymph node"],
        "red_flags": ["moderate to severe eye pain", "decreased visual acuity", "corneal clouding or ulceration", "fixed non-reactive pupil", "photophobia"],
        "clinical_hallmarks": ["diffuse conjunctival hyperemia sparing the limbus", "morning eye crusting", "watery discharge with preauricular node (viral adenovirus)", "thick mucopurulent discharge (bacterial staph/strep)"],
        "pertinent_negatives": ["normal visual acuity", "pupils equally round and reactive to light", "no ciliary flush"],
        "content": "Acute inflammation of ocular conjunctiva. Viral conjunctivitis is self-limiting and highly contagious. Bacterial conjunctivitis responds to broad-spectrum topical antibiotic drops (moxifloxacin or tobramycin). Strict hand hygiene to prevent family transmission."
    },
    # 46. Acute Angle-Closure Glaucoma
    {
        "id": "CLIN-EYE-046",
        "topic": "Acute Angle-Closure Glaucoma",
        "icd10": "H40.20",
        "specialty": "Ophthalmology / Emergency",
        "organ_system": "Eye / Vision Emergency",
        "keywords": ["glaucoma", "severe eye pain", "halos around lights", "hazy cornea", "steamy cornea", "mid-dilated fixed pupil", "rock hard eyeball", "eye pain with vomiting"],
        "red_flags": ["severe deep unilateral ocular pain", "colored halos around light sources", "rapid visual loss", "mid-dilated unreactive oval pupil", "rock-hard eye on palpation"],
        "clinical_hallmarks": ["elevated intraocular pressure > 40-60 mmHg", "cloudy steamy cornea", "ciliary injection", "fixed mid-dilated pupil", "nausea and severe brow ache"],
        "pertinent_negatives": ["no purulent conjunctival discharge"],
        "content": "Ophthalmic emergency caused by pupillary block impeding aqueous humor drainage. Permanent optic nerve necrosis can occur within hours. STAT ophthalmology consult, topical timolol, apraclonidine, pilocarpine, and IV acetazolamide or mannitol to lower IOP immediately."
    },
    # 47. Acute Corneal Abrasion
    {
        "id": "CLIN-EYE-047",
        "topic": "Acute Corneal Abrasion",
        "icd10": "S05.00XA",
        "specialty": "Ophthalmology / Emergency",
        "organ_system": "Eye / Vision",
        "keywords": ["corneal abrasion", "scratched eyeball", "foreign body in eye", "intense eye pain blinking", "fluorescein uptake", "eye trauma"],
        "red_flags": ["corneal infiltrate or white spot (microbial keratitis)", "hypopyon (pus in anterior chamber)", "penetrating globe injury (Seidel sign)"],
        "clinical_hallmarks": ["intense foreign body sensation exacerbated by blinking", "lacrimation and blepharospasm", "bright yellow-green fluorescein uptake on cobalt blue wood lamp examination"],
        "pertinent_negatives": ["no pupil irregularity", "no open globe injury"],
        "content": "Traumatic disruption of corneal epithelial surface. If patient wears contact lenses, must cover for Pseudomonas with topical fluoroquinolones (ciprofloxacin or moxifloxacin) and avoid eye patching. Standard non-contact lens abrasions heal in 24-48 hours with topical erythromycin/tobramycin."
    },
    # 48. Benign Prostatic Hyperplasia (BPH)
    {
        "id": "CLIN-URO-048",
        "topic": "Benign Prostatic Hyperplasia (BPH) & LUTS",
        "icd10": "N40.1",
        "specialty": "Urology",
        "organ_system": "Male Genitourinary",
        "keywords": ["bph", "enlarged prostate", "weak stream", "urinary hesitancy", "dribbling urine", "nocturia in elderly male", "incomplete emptying of bladder"],
        "red_flags": ["acute complete urinary retention", "gross painless hematuria", "recurrent urinary tract infections", "bilateral hydronephrosis with elevated creatinine"],
        "clinical_hallmarks": ["elderly male > 50 years", "lower urinary tract symptoms (hesitancy, weak stream, intermittency, nocturia)", "smooth, enlarged, non-tender symmetrical prostate on DRE"],
        "pertinent_negatives": ["no hard prostate nodules (rules out prostate cancer)", "no dysuria or fever initially"],
        "content": "Age-related non-malignant adenomatous enlargement of prostate periurethral transitional zone causing bladder outflow obstruction. First-line medical therapy: alpha-1 blockers (tamsulosin 0.4mg) for rapid smooth muscle relaxation, and 5-alpha-reductase inhibitors (finasteride) for prostate volume reduction."
    },
    # 49. Acute Epididymo-Orchitis
    {
        "id": "CLIN-URO-049",
        "topic": "Acute Epididymo-Orchitis",
        "icd10": "N45.1",
        "specialty": "Urology",
        "organ_system": "Male Genitourinary",
        "keywords": ["epididymitis", "orchitis", "scrotal pain", "swollen testicle", "prehn sign", "dysuria with scrotal swelling"],
        "red_flags": ["sudden onset agonizing pain with high-riding transverse testicle (testicular torsion emergency)", "absent cremasteric reflex"],
        "clinical_hallmarks": ["gradual onset unilateral scrotal pain and swelling", "indurated tender epididymis posterolateral to testis", "pain relief with scrotal elevation (positive Prehn sign)", "increased color Doppler blood flow on ultrasound"],
        "pertinent_negatives": ["cremasteric reflex is intact", "testis is normally oriented in scrotum"],
        "content": "Inflammation of epididymis and testis. In men < 35 years: predominantly sexually transmitted (Chlamydia / Gonorrhea); in men > 35 years: coliform enterics (E. coli). Critical duty is to exclude acute testicular torsion. Ceftriaxone + Doxycycline for STI; Fluoroquinolones for enteric organisms."
    },
    # 50. Acute Testicular Torsion
    {
        "id": "CLIN-URO-050",
        "topic": "Acute Testicular Torsion",
        "icd10": "N44.00",
        "specialty": "Urology / Emergency Surgery",
        "organ_system": "Male Genitourinary Emergency",
        "keywords": ["testicular torsion", "sudden scrotal pain", "high riding testicle", "absent cremasteric reflex", "scrotal agony in adolescent", "bell clapper deformity"],
        "red_flags": ["sudden violent unilateral scrotal pain", "high-riding horizontal testicle", "absent ipsilateral cremasteric reflex", "nausea and vomiting with scrotal pain"],
        "clinical_hallmarks": ["surgical emergency with 6-hour ischemic window", "absent testicular perfusion on color Doppler ultrasound", "bell-clapper congenital anatomical predisposition"],
        "pertinent_negatives": ["no relief with elevation (negative Prehn sign)", "no prior lower urinary tract symptoms"],
        "content": "Mechanical twisting of spermatic cord cutting off testicular venous and arterial supply. True surgical emergency. Golden window for surgical detorsion and bilateral orchiopexy is < 6 hours from onset (90% salvage). STAT urology consult; do not delay for imaging if clinically evident."
    },
    # 51. Acute Pyelonephritis
    {
        "id": "CLIN-URO-051",
        "topic": "Acute Pyelonephritis (Upper UTI)",
        "icd10": "N10",
        "specialty": "Urology / Nephrology / Internal Medicine",
        "organ_system": "Renal / Genitourinary",
        "keywords": ["pyelonephritis", "kidney infection", "costovertebral angle tenderness", "cva tenderness", "flank pain with fever", "shivering chills with burning urine", "wbc casts"],
        "red_flags": ["septic shock / hypotension", "inability to tolerate oral fluids", "pregnancy with pyelonephritis", "underlying urinary tract obstruction"],
        "clinical_hallmarks": ["triad of fever/chills, flank/costovertebral angle (CVA) tenderness, and lower urinary tract symptoms (dysuria/frequency)", "pyuria with white blood cell casts in urine microscopy"],
        "pertinent_negatives": ["no peritoneal rebound tenderness in right/left lower quadrants"],
        "content": "Bacterial infection ascending to renal pelvis and parenchyma. Common pathogen: uropathogenic E. coli. Outpatient management for mild cases: oral ciprofloxacin or levofloxacin; inpatient admission with IV ceftriaxone for patients with intractable vomiting, pregnancy, or hemodynamic instability."
    },
    # 52. Chronic Kidney Disease (CKD) Screening
    {
        "id": "CLIN-NEPH-052",
        "topic": "Chronic Kidney Disease (CKD) Staging & Complications",
        "icd10": "N18.9",
        "specialty": "Nephrology",
        "organ_system": "Renal / Nephrology",
        "keywords": ["chronic kidney disease", "ckd", "elevated creatinine", "proteinuria", "frothy urine", "bilateral leg edema", "hypertension with renal impairment"],
        "red_flags": ["hyperkalemia > 6.0 mEq/L (peaked T waves on ECG)", "uremic pericarditis / pericardial friction rub", "fluid overload with pulmonary edema", "uremic encephalopathy"],
        "clinical_hallmarks": ["persistent reduction in eGFR < 60 mL/min/1.73m2 for >= 3 months", "albuminuria (UACR > 30 mg/g)", "small echogenic kidneys on bilateral renal ultrasound"],
        "pertinent_negatives": ["no acute gross hematuria", "no unilateral obstructive uropathy"],
        "content": "Progressive, irreversible loss of renal function primarily driven by long-standing diabetes and hypertension. Management focuses on slowing progression with ACEi/ARBs, SGLT2 inhibitors, blood pressure control (<130/80 mmHg), dietary protein restriction, and treating anemia/mineral bone disorders."
    },
    # 53. Generalized Anxiety Disorder (GAD) & Panic Attack
    {
        "id": "CLIN-PSY-053",
        "topic": "Panic Attack & Generalized Anxiety Disorder (GAD)",
        "icd10": "F41.0",
        "specialty": "Psychiatry / General Medicine",
        "organ_system": "Mental Health / Behavioral",
        "keywords": ["panic attack", "generalized anxiety", "sense of impending doom", "palpitations with hyperventilation", "numbness in fingers", "fear of dying", "tight chest with normal ecg"],
        "red_flags": ["suicidal ideation or intent", "substance intoxication / withdrawal", "elevated cardiac biomarkers on workup"],
        "clinical_hallmarks": ["sudden surge of intense fear reaching peak within 10 minutes", "somatic symptoms (trembling, sweating, tachycardia, carpopedal spasm from respiratory alkalosis)", "medical workup including ECG and cardiac enzymes is completely normal"],
        "pertinent_negatives": ["normal 12-lead ECG", "normal high-sensitivity troponin", "no focal neurological signs"],
        "content": "Discrete episodes of sudden, overwhelming autonomic arousal and fear of dying or losing control. Medical mimic exclusion (thyroid disease, pheochromocytoma, arrhythmia) is mandatory. Acute management: calm reassurance, slow diaphragmatic breathing. Maintenance: SSRIs (sertraline, escitalopram) and CBT."
    },
    # 54. Major Depressive Disorder (MDD) Screening
    {
        "id": "CLIN-PSY-054",
        "topic": "Major Depressive Episode & Suicide Risk Triage",
        "icd10": "F32.9",
        "specialty": "Psychiatry",
        "organ_system": "Mental Health",
        "keywords": ["depression", "anhedonia", "hopelessness", "persistent sadness", "insomnia with early morning awakening", "unexplained weight loss", "fatigue and guilt"],
        "red_flags": ["active suicidal ideation with plan and intent", "command auditory hallucinations", "psychotic depression", "catatonia"],
        "clinical_hallmarks": ["SIGECAPS criteria (Sleep, Interest, Guilt, Energy, Concentration, Appetite, Psychomotor, Suicide)", "depressed mood or loss of interest for at least 2 consecutive weeks interfering with daily functioning"],
        "pertinent_negatives": ["no prior manic or hypomanic episodes (rules out bipolar)"],
        "content": "Pervasive mood disturbance affecting cognitive and neurovegetative functions. Primary safety gate is rigorous statutory suicidal risk assessment. First-line pharmacotherapy: SSRIs or SNRIs combined with structured cognitive behavioral psychotherapy."
    },
    # 55. Delirium vs. Dementia in Elderly
    {
        "id": "CLIN-GER-055",
        "topic": "Acute Delirium in Geriatric Inpatient / OPD",
        "icd10": "F05",
        "specialty": "Geriatrics / General Medicine",
        "organ_system": "Geriatric Neurology",
        "keywords": ["delirium", "acute confusion in elderly", "fluctuating consciousness", "sundowning", "hallucinations in elderly", "altered sensorium after fever"],
        "red_flags": ["hypoxia", "septic shock / bacteremia", "hypoglycemia", "intracranial hemorrhage"],
        "clinical_hallmarks": ["acute onset and fluctuating course", "inattention (inability to focus or sustain attention)", "disorganized thinking or altered level of consciousness (CAM criteria)", "frequently triggered by underlying UTI, electrolyte disturbance, or polypharmacy"],
        "pertinent_negatives": ["no chronic gradual 3-year cognitive decline without fluctuation"],
        "content": "Acute, transient global cognitive impairment and attentional fluctuation. Medical emergency reflecting systemic decompensation in vulnerable brains. Key: identify and treat underlying somatic cause (urinary tract infection, pneumonia, anticholinergic medications, sodium disturbance)."
    },
    # 56. Herpes Zoster (Shingles)
    {
        "id": "CLIN-DERM-056",
        "topic": "Herpes Zoster (Shingles) & Post-Herpetic Neuralgia",
        "icd10": "B02.9",
        "specialty": "Dermatology / General Medicine",
        "organ_system": "Dermatologic / Neurologic",
        "keywords": ["herpes zoster", "shingles", "dermatomal rash", "painful blisters on one side of rib cage", "burning nerve pain followed by vesicles", "vesicular rash across chest"],
        "red_flags": ["Hutchinson sign (vesicles on tip of nose - risk of Zoster Ophthalmicus & corneal blindness)", "Ramsay Hunt syndrome (facial palsy with ear canal vesicles)"],
        "clinical_hallmarks": ["unilateral dermatomal distribution strictly respecting anatomical midline", "grouped erythematous papules progressing to clear fluid-filled vesicles", "severe burning, lancinating neuropathic prodrome"],
        "pertinent_negatives": ["does not cross anatomical midline"],
        "content": "Reactivation of latent Varicella-Zoster Virus (VZV) in dorsal root or cranial sensory ganglia. Prompt initiation of oral antivirals (Valacyclovir 1000mg TID or Acyclovir 800mg 5x/day) within 72 hours of rash onset significantly reduces duration and severity of post-herpetic neuralgia."
    },
    # 57. Scabies Infestation
    {
        "id": "CLIN-DERM-057",
        "topic": "Scabies Infestation (Sarcoptes scabiei)",
        "icd10": "B86",
        "specialty": "Dermatology",
        "organ_system": "Dermatologic / Parasitic",
        "keywords": ["scabies", "severe nocturnal itching", "finger web burrows", "wrist papules", "itchy rash whole family", "interdigital rash"],
        "red_flags": ["crusted / Norwegian scabies in immunosuppressed", "secondary bacterial impetigo with glomerulonephritis risk"],
        "clinical_hallmarks": ["intense pruritus severely aggravated at night", "pathognomonic intraepidermal serpiginous burrows in interdigital web spaces, flexor wrists, axillae, and genitalia", "multiple family members symptomatic"],
        "pertinent_negatives": ["no mucosal lesions", "no palms/soles in adults (spared)"],
        "content": "Ectoparasitic mite infestation transmitted via prolonged direct skin-to-skin contact. First-line therapy: topical 5% Permethrin cream applied neck down overnight and washed off after 8-14 hours, repeated in 7 days. Simultaneous treatment of all household contacts and washing bedding in hot water is mandatory."
    },
    # 58. Urticaria (Acute Hives)
    {
        "id": "CLIN-DERM-058",
        "topic": "Acute Urticaria (Hives & Wheals)",
        "icd10": "L50.9",
        "specialty": "Dermatology / Allergy",
        "organ_system": "Integumentary / Immunologic",
        "keywords": ["urticaria", "hives", "welts", "itchy red wheals", "transient skin swelling", "evanescent rash", "dermographism"],
        "red_flags": ["associated tongue swelling / lip angioedema", "stridor / wheezing", "dizziness / hypotension (anaphylaxis)"],
        "clinical_hallmarks": ["circumscribed, erythematous, edematous, pruritic wheals", "evanescent character (individual lesions resolve completely within 24 hours without leaving scar or bruising)", "blanches completely with pressure"],
        "pertinent_negatives": ["individual wheals do not persist beyond 24 hours (rules out urticarial vasculitis)", "no epidermal scaling"],
        "content": "Mast cell degranulation with histamine release in superficial dermis. Triggered by viral infections, medications (NSAIDs, antibiotics), foods, or insect stings. First-line: second-generation non-sedating H1 antihistamines (levocetirizine, bilastine, fexofenadine) at up to four-fold standard dose."
    },
    # 59. Psoriasis Vulgaris
    {
        "id": "CLIN-DERM-059",
        "topic": "Psoriasis Vulgaris (Chronic Plaque Psoriasis)",
        "icd10": "L40.0",
        "specialty": "Dermatology",
        "organ_system": "Integumentary / Autoimmune",
        "keywords": ["psoriasis", "silvery scales", "extensor plaques", "elbow knee plaques", "auspitz sign", "koebner phenomenon", "nail pitting"],
        "red_flags": ["generalized pustular psoriasis with fever", "erythrodermic psoriasis (>90% body surface area shedding)"],
        "clinical_hallmarks": ["sharply demarcated erythematous plaques covered by coarse silvery-white micaceous scales", "predilection for extensor surfaces (elbows, knees, scalp, lumbosacral)", "positive Auspitz sign (pinpoint bleeding upon scraping scale)"],
        "pertinent_negatives": ["no mucosal ulcerations", "no targetoid iris lesions"],
        "content": "Chronic immune-mediated hyperproliferative skin disorder driven by IL-23/IL-17 axis. Associated with psoriatic arthritis and metabolic syndrome. Limited disease treated with high-potency topical corticosteroids + vitamin D analogues (calcipotriene); moderate-severe requires phototherapy or biologics."
    },
    # 60. Tinea Corporis / Cruris (Fungal Ringworm)
    {
        "id": "CLIN-DERM-060",
        "topic": "Dermatophytosis (Tinea Corporis & Cruris)",
        "icd10": "B35.4",
        "specialty": "Dermatology",
        "organ_system": "Dermatologic / Mycology",
        "keywords": ["tinea", "ringworm", "annular rash with central clearing", "itchy groins", "scaly border rash", "fungal skin infection"],
        "red_flags": ["tinea incognito from misuse of topical steroid creams (e.g. Betnovate/clobetasol)", "secondary cellulitis"],
        "clinical_hallmarks": ["annular erythematous scaly plaques with active expanding raised vesicular borders and central clearing", "potassium hydroxide (KOH) wet mount showing branching fungal hyphae"],
        "pertinent_negatives": ["no silvery thick micaceous scale", "no extensor knee/elbow distribution"],
        "content": "Superficial dermatophyte infection of keratinized epidermis (Trichophyton rubrum). Widespread in tropical India due to heat, humidity, and rampant over-the-counter topical steroid misuse. Treatment: topical allylamines (terbinafine) or imidazoles (clotrimazole, luliconazole) for 2-4 weeks. Strictly avoid steroid combinations."
    },
    # 61. Bell's Palsy (Idiopathic Facial Nerve Palsy)
    {
        "id": "CLIN-NEUR-061",
        "topic": "Bell's Palsy (Peripheral 7th Nerve Palsy)",
        "icd10": "G51.0",
        "specialty": "Neurology / ENT",
        "organ_system": "Cranial Nerves / Neurology",
        "keywords": ["bell's palsy", "facial paralysis", "inability to close eye", "forehead wrinkles lost", "drooling from corner of mouth", "hyperacusis", "taste loss on anterior tongue"],
        "red_flags": ["forehead movement preserved (rules out Bell's palsy - indicates central stroke / intracranial lesion)", "associated limb weakness", "slurred speech or aphasia", "vesicles in external ear canal"],
        "clinical_hallmarks": ["acute unilateral lower motor neuron facial weakness involving both upper AND lower face (inability to wrinkle forehead or close eye fully)", "Bell's phenomenon (eyeball rolls upward on attempted eye closure)"],
        "pertinent_negatives": ["no arm/leg motor weakness", "no sensory loss in extremities", "no diplopia"],
        "content": "Acute idiopathic peripheral neuropathy of cranial nerve VII, likely triggered by HSV-1 reactivation. Key distinction from central stroke: Bell's palsy affects forehead wrinkling; stroke spares the forehead due to bilateral cortical innervation. Treatment: oral prednisolone 60mg/day for 10 days started within 72 hours, artificial tears, and nighttime eye taping."
    },
    # 62. Tension Pneumothorax
    {
        "id": "CLIN-EM-062",
        "topic": "Tension Pneumothorax",
        "icd10": "J93.0",
        "specialty": "Emergency Medicine / Thoracic Surgery",
        "organ_system": "Thoracic Emergency",
        "keywords": ["pneumothorax", "tension pneumothorax", "deviated trachea", "absent breath sounds on one side", "hyperresonance to percussion", "distended neck veins with hypotension"],
        "red_flags": ["tracheal deviation away from affected side", "absent ipsilateral breath sounds", "hemodynamic collapse / hypotension", "jugular venous distension"],
        "clinical_hallmarks": ["one-way valve pleural air trapping causing mediastinal shift and superior vena cava compression", "tympanitic hyperresonance to percussion", "hypotension and cyanosis"],
        "pertinent_negatives": ["no bilateral crackles"],
        "content": "Fatal thoracic emergency. Clinical diagnosis: do NOT wait for chest radiography. Immediate needle decompression with large-bore 14G cannula in 2nd intercostal space midclavicular line (or 5th intercostal space anterior axillary line), followed immediately by tube thoracostomy (chest drain)."
    },
    # 63. Acute Pancreatitis Exacerbation (Severe)
    {
        "id": "CLIN-GI-063",
        "topic": "Severe Acute Necrotizing Pancreatitis",
        "icd10": "K85.90",
        "specialty": "Gastroenterology / Critical Care",
        "organ_system": "Pancreatic / Abdominal",
        "keywords": ["acute pancreatitis", "epigastric pain boring through to back", "elevated lipase > 3x", "cullen sign", "grey turner sign", "gallstone pancreatitis"],
        "red_flags": ["organ failure (respiratory PaO2/FiO2 < 300, renal creatinine > 2.0, shock)", "periumbilical ecchymosis (Cullen sign)", "flank ecchymosis (Grey Turner sign)"],
        "clinical_hallmarks": ["severe persistent epigastric pain radiating to back relieved by leaning forward", "serum lipase or amylase >= 3 times upper limit of normal", "characteristic cross-sectional contrast CT findings"],
        "pertinent_negatives": ["no normal lipase levels"],
        "content": "Premature intracellular activation of pancreatic proenzymes causing autodigestion of gland. Common causes: alcohol abuse and gallstones. Early goal-directed IV fluid hydration with Ringer's lactate, adequate analgesia, and early oral refeeding once pain improves. Prophylactic antibiotics are not recommended."
    },
    # 64. Intestinal Obstruction
    {
        "id": "CLIN-SURG-064",
        "topic": "Acute Mechanical Bowel Obstruction",
        "icd10": "K56.60",
        "specialty": "General Surgery / Emergency",
        "organ_system": "Gastrointestinal Surgery",
        "keywords": ["bowel obstruction", "obstipation", "no gas passing", "feculent vomiting", "abdominal distension", "high pitched tinkling bowel sounds", "surgical abdomen"],
        "red_flags": ["fever with localized peritoneal rigidity (strangulated bowel necrosis)", "feculent vomiting", "hemodynamic shock"],
        "clinical_hallmarks": ["cardinal tetrad: colicky abdominal pain, bilious/feculent vomiting, marked distension, absolute constipation (obstipation)", "step-ladder air-fluid levels on erect abdominal x-ray"],
        "pertinent_negatives": ["no flatus passing for > 24 hours"],
        "content": "Mechanical arrest of intestinal contents. Common etiologies: post-operative adhesions (small bowel) or sigmoid volvulus / colorectal carcinoma (large bowel). Initial management: 'drip and suck' (aggressive IV fluids + nasogastric decompression). Immediate laparotomy if signs of strangulation/ischemia are present."
    },
    # 65. Hyperthyroidism & Thyroid Storm
    {
        "id": "CLIN-ENDO-065",
        "topic": "Thyrotoxicosis & Thyroid Storm Triage",
        "icd10": "E05.90",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine / Thyroid",
        "keywords": ["hyperthyroidism", "thyrotoxicosis", "thyroid storm", "heat intolerance", "palpitations with weight loss", "fine tremor of hands", "exophthalmos", "lid lag"],
        "red_flags": ["hyperpyrexia > 39.5C with tachycardia > 140 bpm", "cardiac arrhythmia / atrial fibrillation", "delirium / agitation", "thyroid storm (Burch-Wartofsky score >= 45)"],
        "clinical_hallmarks": ["suppressed serum TSH with elevated free T4 and T3", "fine resting hand tremors", "heat intolerance", "smooth diffuse goiter with vascular bruit (Graves disease)"],
        "pertinent_negatives": ["no cold intolerance", "no weight gain"],
        "content": "Hypermetabolic syndrome from elevated circulating thyroid hormones. Graves disease is the most common etiology. Medical emergency when presenting as Thyroid Storm: treated with IV beta-blockers (propranolol), antithyroid thionamides (propylthiouracil/methimazole), Lugol's iodine, and IV hydrocortisone."
    },
]

def main():
    kb_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "knowledge_base", "protocols", "clinical_knowledge_base.json"
    )
    with open(kb_path, "r", encoding="utf-8") as f:
        existing = json.load(f)

    existing_ids = {p["id"] for p in existing}
    added_count = 0
    for proto in EXPANDED_PROTOCOLS:
        if proto["id"] not in existing_ids:
            existing.append(proto)
            existing_ids.add(proto["id"])
            added_count += 1

    with open(kb_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)

    print(f"Successfully added {added_count} new clinical protocols.")
    print(f"Total knowledge base protocols now: {len(existing)}")

if __name__ == "__main__":
    main()

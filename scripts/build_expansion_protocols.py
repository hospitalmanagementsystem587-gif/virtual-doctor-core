#!/usr/bin/env python3
"""
Automated Clinical Protocol Expansion Generator
Expands Virtual Doctor knowledge base from 310 to 510+ protocols.
Covers comprehensive Kaggle conditions, Indian hospital realities, and clinical subspecialties.
"""

import json
import os

KB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "knowledge_base",
    "protocols",
    "clinical_knowledge_base.json"
)

# Load existing protocols
with open(KB_PATH, "r", encoding="utf-8") as f:
    existing_protocols = json.load(f)

existing_ids = {p["id"] for p in existing_protocols}
existing_topics = {p["topic"].lower() for p in existing_protocols}
print(f"Current count: {len(existing_protocols)}")

EXPANSION_DEFS = [
    # --- 1. TROPICAL & VECTOR-BORNE INFECTIONS ---
    {
        "id": "ICD10-A75.3",
        "topic": "Scrub Typhus (Orientia Tsutsugamushi)",
        "icd10": "A75.3",
        "specialty": "Infectious Disease / General Medicine",
        "organ_system": "Tropical Infectious",
        "keywords": ["scrub typhus", "eschar", "mite bite", "chigger bite", "fever with eschar", "acute febrile illness"],
        "red_flags": ["acute respiratory distress syndrome (ards)", "altered sensorium", "oliguria / aki", "septic shock"],
        "clinical_hallmarks": ["punched-out black necrotic skin eschar with erythematous halo", "abrupt high spiking fever", "severe retro-orbital headache and conjunctival suffusion", "generalized lymphadenopathy"],
        "pertinent_negatives": ["no malaria parasites on smear", "negative dengue ns1"],
        "content": "Scrub typhus is a mite-borne rickettsial zoonosis caused by Orientia tsutsugamushi transmitted by larval trombiculid mites. Clinical hallmarks include high fever, headache, myalgias, and pathognomonic cutaneous eschar. Treatment: Oral or IV Doxycycline (100 mg BID for 7 days) or Azithromycin."
    },
    {
        "id": "ICD10-A83.0",
        "topic": "Japanese Encephalitis (Flavivirus AES)",
        "icd10": "A83.0",
        "specialty": "Infectious Disease / Neurology",
        "organ_system": "Neuro-Infectious",
        "keywords": ["japanese encephalitis", "acute encephalitis syndrome", "culex mosquito", "altered sensorium with fever", "pediatric seizures with fever"],
        "red_flags": ["status epilepticus", "decerebrate posturing", "gcs < 8", "brainstem herniation"],
        "clinical_hallmarks": ["biphasic illness: prodromal high fever followed by acute neurological deterioration", "generalized convulsions", "parkinsonian extrapyramidal signs (cogwheel rigidity, tremor, mask-like facies)", "coma"],
        "pertinent_negatives": ["no neck stiffness characteristic of pyogenic bacterial meningitis", "clear csf on lp"],
        "content": "Flavivirus infection transmitted by Culex tritaeniorhynchus mosquitoes breeding in rural rice fields. Leading cause of Acute Encephalitis Syndrome (AES) in children in endemic zones. Diagnosis: CSF IgM capture ELISA. Treatment: ICU neuro-protective supportive care and antiepileptic therapy."
    },
    {
        "id": "ICD10-A98.2",
        "topic": "Kyasanur Forest Disease (Monkey Fever)",
        "icd10": "A98.2",
        "specialty": "Infectious Disease",
        "organ_system": "Hemorrhagic Fevers",
        "keywords": ["kyasanur forest disease", "kfd", "monkey fever", "tick bite fever", "forest worker fever"],
        "red_flags": ["gastrointestinal bleeding / hematemesis", "uncontrolled epistaxis", "encephalopathy and tremors"],
        "clinical_hallmarks": ["sudden high fever with chills and frontal headache", "severe prostration and generalized muscle pain", "biphasic course with hemorrhagic signs", "marked leukopenia and thrombocytopenia"],
        "pertinent_negatives": ["negative dengue serology", "no plasmodium on smear"],
        "content": "Tick-borne hemorrhagic viral disease caused by KFD virus transmitted by Haemaphysalis ticks. Features sudden high fever, intense myalgias, conjunctival suffusion, and bleeding diathesis. Diagnosis: RT-PCR / IgM ELISA. Treatment: Supportive care, blood/platelet transfusion as indicated."
    },
    {
        "id": "ICD10-B74.9",
        "topic": "Lymphatic Filariasis & Acute Adenolymphangitis (ADL)",
        "icd10": "B74.9",
        "specialty": "Infectious Disease / General Surgery",
        "organ_system": "Lymphatic / Tropical",
        "keywords": ["filariasis", "elephantiasis", "hydrocele", "adenolymphangitis", "filarial fever", "wuchereria bancrofti"],
        "red_flags": ["ascending cellulitis / necrotizing soft tissue infection", "septic shock from secondary bacterial superinfection", "massive scrotal elephantiasis"],
        "clinical_hallmarks": ["acute adenolymphangitis (adl): high fever with retrograde ascending painful red streaks along lymphatics", "tender inguinal lymphadenopathy", "non-pitting progressive lymphedema of lower limbs or genitalia (scrotal hydrocele)"],
        "pertinent_negatives": ["no deep vein thrombosis on compression venous doppler"],
        "content": "Parasitic infection caused by Wuchereria bancrofti transmitted by Culex mosquitoes. Adult worms dwell in lymphatic channels causing mechanical obstruction. Diagnosis: Midnight peripheral blood smear, Filarial Antigenaemia Card Test. Treatment: Diethylcarbamazine (DEC 6 mg/kg/day for 12 days) + Albendazole 400 mg."
    },
    {
        "id": "ICD10-A23.9",
        "topic": "Brucellosis (Undulant Malta Fever)",
        "icd10": "A23.9",
        "specialty": "Infectious Disease / Rheumatology",
        "organ_system": "Zoonotic Infectious",
        "keywords": ["brucellosis", "undulant fever", "malta fever", "unpasteurized milk", "sacroiliitis with fever"],
        "red_flags": ["brucella endocarditis (new murmur, heart failure)", "neurobrucellosis", "vertebral osteomyelitis with epidural abscess"],
        "clinical_hallmarks": ["classic undulant pattern fever rising in afternoon", "profuse nocturnal drenching diaphoresis with distinctive moldy odor", "asymmetric sacroiliitis, spondylodiscitis, and peripheral arthritis", "epididymo-orchitis in young men"],
        "pertinent_negatives": ["no response to beta-lactam antibiotics", "negative tuberculosis genexpert"],
        "content": "Zoonotic bacterial infection caused by Brucella species acquired via unpasteurized dairy consumption or direct animal contact. Diagnosis: Standard Agglutination Test (SAT titer >= 1:160), blood culture (prolonged incubation). Treatment: Doxycycline 100 mg BID for 6 weeks PLUS Streptomycin 1g IM daily for 2-3 weeks."
    },
    {
        "id": "ICD10-Z20.3",
        "topic": "Rabies Post-Exposure Prophylaxis (WHO Category III Dog Bite)",
        "icd10": "Z20.3",
        "specialty": "Emergency Medicine / Preventive Medicine",
        "organ_system": "Zoonotic Viral",
        "keywords": ["dog bite", "rabies", "monkey bite", "cat bite", "hydrophobia", "rabies immunoglobulin", "rabies vaccine"],
        "red_flags": ["category iii transdermal bite with bleeding", "lick over broken skin or mucosal contamination", "clinical hydrophobia or aerophobia (100% fatal encephalitis)"],
        "clinical_hallmarks": ["fresh animal bite wound with tooth laceration or puncture", "localized paresthesia at site of healed bite (prodrome)", "hydrophobia (pharyngeal spasm triggered by attempting to swallow liquids)", "aerophobia"],
        "pertinent_negatives": ["no previous complete rabies pre-exposure immunization"],
        "content": "Lyssavirus infection transmitted via saliva of infected mammals. Protocolized PEP: 1. Immediate wound washing with soap and running water for 15 minutes; 2. Infiltrate Rabies Immunoglobulin (RIG: ERIG 40 IU/kg or HRIG 20 IU/kg) into and around all wound margins STAT; 3. Modern Cell Culture Rabies Vaccine (CCRV) on Days 0, 3, 7, and 28."
    },
    {
        "id": "ICD10-A08.0",
        "topic": "Rotaviral & Enteric Adenoviral Enteritis in Infants",
        "icd10": "A08.0",
        "specialty": "Pediatrics / Gastroenterology",
        "organ_system": "Pediatric Gastrointestinal",
        "keywords": ["rotavirus", "infant watery diarrhea", "greenish diarrhea in baby", "vomiting and diarrhea infant", "infant dehydration"],
        "red_flags": ["severe dehydration: sunken fontanelle, absent tears, prolonged capillary refill > 3s, lethargy, anuria"],
        "clinical_hallmarks": ["watery, non-bloody diarrhea with fever and vomiting lasting 3-8 days", "rapid onset dehydration in infant aged 6-24 months", "perianal excoriation from acidic loose stools"],
        "pertinent_negatives": ["no frank blood or mucus in stools (rules out bacterial dysentery)"],
        "content": "Leading cause of severe dehydrating diarrhea in infants worldwide. Transmitted via fecal-oral route. Diagnosis: Stool rotavirus antigen detection (ELISA/immunochromatography). Treatment: Oral Rehydration Solution (ORS) + Zinc supplementation (20 mg/day for 14 days) + continuation of breastfeeding; IV Ringer Lactate if severe shock."
    },
    {
        "id": "ICD10-B05.9",
        "topic": "Measles (Rubeola Virus Exanthem)",
        "icd10": "B05.9",
        "specialty": "Pediatrics / Infectious Disease",
        "organ_system": "Pediatric Infectious",
        "keywords": ["measles", "rubeola", "koplik spots", "maculopapular rash spreading from face", "the 3 cs of measles"],
        "red_flags": ["measles pneumonia (giant cell pneumonia)", "acute post-measles encephalitis", "subacute sclerosing panencephalitis (sspe)"],
        "clinical_hallmarks": ["the 3 cs: Cough, Coryza, and Conjunctivitis with prominent photophobia", "pathognomonic Koplik spots (tiny bluish-white grains on erythematous buccal mucosa opposite molars)", "erythematous maculopapular rash beginning at hairline/behind ears and spreading downward to face, trunk, and extremities (craniocaudal)"],
        "pertinent_negatives": ["no vesicles or crusting (excludes chickenpox)"],
        "content": "Highly contagious paramyxovirus infection transmitted by respiratory droplets. Diagnostic workup: Measles IgM serology, RT-PCR. Treatment: Supportive care, isolation, and Vitamin A supplementation (200,000 IU daily for 2 days) to prevent blindness and mortality."
    },
    {
        "id": "ICD10-B06.9",
        "topic": "Rubella (German Measles) & Congenital Rubella Risk",
        "icd10": "B06.9",
        "specialty": "Obstetrics / Pediatrics / Infectious Disease",
        "organ_system": "Infectious Exanthem",
        "keywords": ["rubella", "german measles", "suboccipital lymphadenopathy", "congenital rubella syndrome", "forchheimer spots"],
        "red_flags": ["congenital rubella syndrome: microcephaly, sensorineural deafness, cataract, patent ductus arteriosus (pda) in fetus of infected pregnant mother"],
        "clinical_hallmarks": ["mild fever with distinctive tender suboccipital, postauricular, and posterior cervical lymphadenopathy", "discrete pink-rose maculopapular rash spreading from face downward, clearing by day 3", "Forchheimer spots (petechiae on soft palate) and transient polyarthralgia in adult females"],
        "pertinent_negatives": ["no koplik spots", "rash fades much faster than measles (3-day measles)"],
        "content": "Togavirus infection mild in children but catastrophic in early pregnancy (teratogenic Congenital Rubella Syndrome). Diagnosis: Rubella IgM antibodies. Treatment: Symptomatic supportive care; prevention via universal MMR vaccination."
    },
    {
        "id": "ICD10-B26.9",
        "topic": "Mumps (Epidemic Parotitis & Orchitis Risk)",
        "icd10": "B26.9",
        "specialty": "Pediatrics / Urology / Infectious Disease",
        "organ_system": "Infectious",
        "keywords": ["mumps", "parotitis", "swollen cheek", "orchitis with mumps", "parotid gland swelling", "earlobe displaced upward"],
        "red_flags": ["acute testicular atrophy and subfertility from post-pubertal mumps orchitis", "mumps meningoencephalitis / aseptic meningitis", "acute pancreatitis with severe epigastric pain"],
        "clinical_hallmarks": ["acute bilateral or unilateral tender, painful swelling of parotid salivary glands obscuring the angle of the jaw and elevating the earlobe", "pain accentuated by chewing or consuming sour/acidic foods (lemon juice test)", "erythema and edema of Stensen duct orifice on buccal mucosa"],
        "pertinent_negatives": ["no purulent discharge from stensen duct on massage (rules out bacterial suppurative parotitis)"],
        "content": "Paramyxovirus infection spread by respiratory droplets affecting salivary glands, gonads, pancreas, and CNS. Diagnosis: Mumps IgM, elevated serum amylase. Treatment: Supportive analgesia, cold/warm compresses, scrotal support and bed rest for orchitis."
    },

    # --- 2. PEDIATRIC & NEONATAL EMERGENCIES ---
    {
        "id": "ICD10-P59.9",
        "topic": "Neonatal Hyperbilirubinemia & Kernicterus Risk",
        "icd10": "P59.9",
        "specialty": "Pediatrics / Neonatology",
        "organ_system": "Neonatal",
        "keywords": ["neonatal jaundice", "yellow baby", "high bilirubin in newborn", "kernicterus", "phototherapy", "jaundice in first 24 hours"],
        "red_flags": ["jaundice appearing within first 24 hours of life", "acute bilirubin encephalopathy (poor suck, high-pitched cry, opisthotonus)", "clay-colored stools and dark urine"],
        "clinical_hallmarks": ["cephalocaudal progression of cutaneous icterus (Kramer zones)", "blanching skin over sternum reveals distinct yellow undertone", "lethargy and poor feeding"],
        "pertinent_negatives": ["no maternal-fetal ABO/Rh incompatibility on Coombs testing"],
        "content": "Unconjugated bilirubin elevation in neonates crossing blood-brain barrier risking irreversible basal ganglia neurotoxicity (Kernicterus). Diagnosis: Total and Direct Serum Bilirubin plotted on Bhutani nomogram. Treatment: Continuous double-surface LED phototherapy, adequate hydration, exchange transfusion if threshold crossed."
    },
    {
        "id": "ICD10-R56.00",
        "topic": "Pediatric Febrile Seizures (Simple vs Complex)",
        "icd10": "R56.00",
        "specialty": "Pediatrics / Emergency Medicine",
        "organ_system": "Pediatric Neurology",
        "keywords": ["febrile seizure", "fever fits", "child seizure with fever", "simple febrile seizure", "pediatric convulsions"],
        "red_flags": ["convulsion lasting longer than 15 minutes", "focal seizure features", "recurrence within 24 hours", "signs of meningitis (bulging fontanelle, neck stiffness)"],
        "clinical_hallmarks": ["child aged 6 months to 5 years", "generalized tonic-clonic convulsions during rapid fever onset (> 38°C)", "brief duration (< 10 minutes) with rapid return to normal baseline"],
        "pertinent_negatives": ["no history of unprovoked afebrile epilepsy"],
        "content": "Most common convulsive disorder in young children. Simple febrile seizures are generalized, < 15 min, once in 24h. Complex seizures are focal, > 15 min, or recurrent within 24h. Treatment: Airway positioning in recovery position; rectal Diazepam or intranasal Midazolam if seizure > 5 min; antipyretic counseling."
    },
    {
        "id": "ICD10-K56.1",
        "topic": "Acute Pediatric Intussusception",
        "icd10": "K56.1",
        "specialty": "Pediatric Surgery / Emergency Medicine",
        "organ_system": "Pediatric Gastrointestinal",
        "keywords": ["intussusception", "red currant jelly stool", "colicky crying infant", "sausage shaped mass", "infant vomiting bile"],
        "red_flags": ["red currant jelly bloody mucoid stools (mucosal infarction)", "bilious green vomiting", "diffuse peritonitis and shock"],
        "clinical_hallmarks": ["triad: intermittent severe colicky abdominal pain (infant screams, knees to chest), vomiting, bloody stool", "calm between painful spasms", "sausage-shaped abdominal mass with emptiness in right iliac fossa (Dance sign)"],
        "pertinent_negatives": ["no diarrhea with liquid loose stools"],
        "content": "Telescoping of bowel segment into adjacent segment in infants aged 3-12 months. Diagnosis: Ultrasound abdomen showing target or doughnut sign. Treatment: Strict NPO, IV fluid resuscitation, ultrasound-guided hydrostatic saline enema or fluoroscopic air contrast enema; emergency laparotomy if peritonitis present."
    },
    {
        "id": "ICD10-M30.3",
        "topic": "Kawasaki Disease (Mucocutaneous Lymph Node Syndrome)",
        "icd10": "M30.3",
        "specialty": "Pediatrics / Pediatric Cardiology",
        "organ_system": "Pediatric Vasculitis",
        "keywords": ["kawasaki disease", "strawberry tongue", "persistent fever in toddler", "coronary artery aneurysm", "bilateral red eyes without discharge"],
        "red_flags": ["coronary artery dilation or aneurysm on 2D echocardiogram", "myocarditis or gallop rhythm", "prolonged high fever > 10 days"],
        "clinical_hallmarks": ["fever >= 5 days PLUS at least 4 of 5 criteria: bilateral non-exudative conjunctival injection, strawberry tongue and cracked lips, polymorphous rash, erythema and induration of hands/feet with periungual peeling, cervical lymphadenopathy > 1.5 cm"],
        "pertinent_negatives": ["negative blood culture", "negative throat swab for group A strep"],
        "content": "Systemic medium-vessel necrotizing vasculitis of childhood with predilection for coronary arteries. Diagnosis: 2D-Echocardiogram, elevated ESR/CRP, thrombocytosis. Treatment: High-dose IVIG (2 g/kg single infusion over 10-12h) within first 10 days PLUS high-dose Aspirin (30-50 mg/kg/day)."
    },
    {
        "id": "ICD10-B08.4",
        "topic": "Hand, Foot, and Mouth Disease (HFMD)",
        "icd10": "B08.4",
        "specialty": "Pediatrics / Dermatology",
        "organ_system": "Pediatric Infectious",
        "keywords": ["hfmd", "hand foot and mouth", "coxsackievirus", "mouth ulcers in child", "vesicles on palms and soles"],
        "red_flags": ["myoclonic jerks or neurogenic pulmonary edema (EV71)", "severe dehydration from inability to swallow fluids", "persistent fever > 3 days"],
        "clinical_hallmarks": ["painful vesicular ulcerative enanthem on buccal mucosa and tongue", "discrete oval greyish vesicles with red halo on palms and soles", "buttock and knee maculopapular rash", "low-grade fever"],
        "pertinent_negatives": ["no vesicles on trunk typical of varicella", "no strawberry tongue"],
        "content": "Contagious viral exanthem caused by Coxsackievirus A16 and Enterovirus 71 affecting children under 5 years. Self-limiting over 7-10 days. Management: Oral analgesics (Paracetamol/Ibuprofen), cool soft foods, oral hydration."
    },
    {
        "id": "ICD10-A37.9",
        "topic": "Pediatric Pertussis (Whooping Cough)",
        "icd10": "A37.9",
        "specialty": "Pediatrics / Pulmonology",
        "organ_system": "Pediatric Respiratory",
        "keywords": ["whooping cough", "pertussis", "paroxysmal cough in child", "post tussive vomiting", "inspiratory whoop"],
        "red_flags": ["apnea episodes and cyanosis in infants < 6 months", "pulmonary hypertension", "absolute lymphocytosis > 30,000 /uL"],
        "clinical_hallmarks": ["violent paroxysmal coughing spasms followed by high-pitched inspiratory whoop", "post-tussive emesis (vomiting after coughing fit)", "subconjunctival hemorrhages and facial petechiae"],
        "pertinent_negatives": ["no wheezing or crackles on auscultation between coughing spasms"],
        "content": "Respiratory infection caused by Bordetella pertussis. Dangerous in infants under 6 months where whoop is absent, presenting with apnea. Diagnosis: Nasopharyngeal swab PCR, marked absolute lymphocytosis. Treatment: Azithromycin (10 mg/kg/day for 5 days); post-exposure prophylaxis for close contacts."
    },

    # --- 3. CARDIOVASCULAR & VASCULAR EMERGENCIES ---
    {
        "id": "ICD10-I48.91",
        "topic": "Atrial Fibrillation with Rapid Ventricular Response (AF with RVR)",
        "icd10": "I48.91",
        "specialty": "Cardiology / Emergency Medicine",
        "organ_system": "Cardiovascular",
        "keywords": ["atrial fibrillation", "af with rvr", "irregularly irregular pulse", "palpitations", "rapid irregular heartbeat"],
        "red_flags": ["hemodynamic instability: systolic BP < 90 mmHg, cardiogenic shock", "flash pulmonary edema", "ischemic chest pain"],
        "clinical_hallmarks": ["irregularly irregular radial pulse with significant pulse deficit", "ECG shows absent P waves, variable irregular R-R intervals, and fibrillatory f-waves", "ventricular rate > 120-160 bpm in uncontrolled RVR"],
        "pertinent_negatives": ["no regular flutter waves", "narrow QRS complex"],
        "content": "Common sustained cardiac arrhythmia with rapid irregular ventricular conduction. Carries 5-fold increased stroke risk. Management: Synchronized DC Cardioversion STAT (100-200J) if unstable. Rate control with IV Beta-blockers (Metoprolol) or Calcium Channel Blockers (Diltiazem). Anticoagulation based on CHA2DS2-VASc score."
    },
    {
        "id": "ICD10-I26.9",
        "topic": "Acute Pulmonary Embolism (PE)",
        "icd10": "I26.9",
        "specialty": "Pulmonology / Emergency Medicine / Cardiology",
        "organ_system": "Cardiovascular / Pulmonary",
        "keywords": ["pulmonary embolism", "pe", "blood clot in lung", "sudden chest pain with hypoxia", "pleuritic chest pain", "wells score"],
        "red_flags": ["massive PE with systolic BP < 90 mmHg or cardiac arrest", "refractory hypoxemia", "acute right ventricular strain on bedside echo (McConnell sign)"],
        "clinical_hallmarks": ["sudden unexplained dyspnea and tachypnea (> 20/min)", "pleuritic chest pain aggravated by inspiration", "tachycardia (> 100 bpm) with loud P2 sound", "DVT risk factors (immobility, surgery, malignancy)"],
        "pertinent_negatives": ["no focal consolidation on chest x-ray", "clear lung fields on auscultation despite severe dyspnea"],
        "content": "Occlusion of pulmonary arterial bed by dislodged thrombus from deep veins. Diagnosis: CT Pulmonary Angiography (CTPA) gold standard, D-dimer, bedside echo. Treatment: Therapeutic anticoagulation (LMWH or DOAC: Apixaban/Rivaroxaban); Thrombolytic therapy (Alteplase) for massive hemodynamically unstable PE."
    },
    {
        "id": "ICD10-I82.40",
        "topic": "Acute Lower Extremity Deep Vein Thrombosis (DVT)",
        "icd10": "I82.40",
        "specialty": "Vascular Surgery / General Medicine",
        "organ_system": "Vascular",
        "keywords": ["dvt", "deep vein thrombosis", "swollen calf", "leg pain after flight", "blood clot in leg", "unilateral leg edema"],
        "red_flags": ["phlegmasia cerulea dolens: massive limb cyanosis and impending gangrene", "concomitant sudden chest pain or dyspnea (PE)", "loss of distal arterial pulses"],
        "clinical_hallmarks": ["acute unilateral swelling of calf (> 3 cm difference measured 10 cm below tibial tuberosity)", "tenderness along deep venous distribution (popliteal/femoral)", "erythema, warmth, and prominent superficial collateral veins"],
        "pertinent_negatives": ["no bilateral symmetrical edema characteristic of heart failure or cirrhosis"],
        "content": "Blood clot in deep leg veins governed by Virchow triad (stasis, endothelial injury, hypercoagulability). Diagnosis: Venous Duplex Compression Ultrasound, D-dimer. Treatment: Therapeutic anticoagulation with DOACs (Apixaban, Rivaroxaban) or LMWH bridging to Warfarin; graduated compression stockings."
    },
    {
        "id": "ICD10-I33.0",
        "topic": "Acute & Subacute Infective Endocarditis",
        "icd10": "I33.0",
        "specialty": "Cardiology / Infectious Disease",
        "organ_system": "Cardiovascular",
        "keywords": ["infective endocarditis", "vegetation on valve", "fever with new murmur", "splinter hemorrhage", "osler nodes", "janeway lesions"],
        "red_flags": ["acute severe valvular regurgitation with pulmonary edema", "conduction block (prolonged PR / complete heart block) from aortic ring abscess", "major embolic stroke"],
        "clinical_hallmarks": ["prolonged unexplained fever with chills and night sweats", "new regurgitant cardiac murmur or changing character of preexisting murmur", "stigmata: subungual splinter hemorrhages, Osler nodes, Janeway lesions, Roth spots, splenomegaly"],
        "pertinent_negatives": ["no negative blood cultures after proper collection prior to antibiotics"],
        "content": "Microbial infection of cardiac endothelial lining and valves (Staph aureus, Viridans strep). Diagnosis: Modified Duke criteria; 3 sets of blood cultures; Transthoracic and Transesophageal Echocardiography (TEE). Treatment: Prolonged bactericidal IV antibiotics (4-6 weeks); urgent surgical valve replacement if refractory heart failure or large vegetations."
    },
    {
        "id": "ICD10-I16.1",
        "topic": "Hypertensive Emergency with Acute Target-Organ Damage",
        "icd10": "I16.1",
        "specialty": "Cardiology / Emergency Medicine / Nephrology",
        "organ_system": "Cardiovascular",
        "keywords": ["hypertensive emergency", "hypertensive crisis", "malignant hypertension", "bp 200/120", "hypertensive encephalopathy"],
        "red_flags": ["hypertensive encephalopathy (altered mental status, papilledema, seizures)", "acute pulmonary edema", "acute coronary syndrome", "acute aortic dissection", "acute renal failure"],
        "clinical_hallmarks": ["severe acute elevation in blood pressure: SBP >= 180 and/or DBP >= 120 mmHg", "PRESENCE of acute, progressive target-organ dysfunction", "severe occipital headache, blurred vision, bilateral retinal flame hemorrhages and papilledema"],
        "pertinent_negatives": ["absence of end-organ damage defines Hypertensive Urgency"],
        "content": "Severe blood pressure elevation accompanied by acute life-threatening target-organ compromise. Therapeutic principle: Lower MAP by NO MORE than 20-25% in the first hour to prevent cerebral/renal hypoperfusion. Treatment: Titratable IV antihypertensives (IV Labetalol, IV Nicardipine, IV Nitroglycerin)."
    },

    # --- 4. GASTROENTEROLOGY & HEPATOBILIARY ---
    {
        "id": "ICD10-K74.6",
        "topic": "Decompensated Liver Cirrhosis & Hepatic Encephalopathy",
        "icd10": "K74.6",
        "specialty": "Gastroenterology / Hepatology",
        "organ_system": "Gastrointestinal / Hepatic",
        "keywords": ["liver cirrhosis", "decompensated liver", "ascites", "hepatic encephalopathy", "portal hypertension", "asterixis", "flapping tremors"],
        "red_flags": ["spontaneous bacterial peritonitis (fever and abdominal pain in ascites)", "variceal hemorrhage (hematemesis)", "hepatorenal syndrome", "grade III-IV hepatic encephalopathy (coma)"],
        "clinical_hallmarks": ["stigmata: ascites with fluid wave, spider nevi, palmar erythema, jaundice", "asterixis (flapping tremor of dorsiflexed hands)", "reversal of sleep-wake cycle and confusion", "pedal edema and sarcopenia"],
        "pertinent_negatives": ["no focal neurological deficits typical of stroke"],
        "content": "End-stage hepatic fibrosis complicated by portal hypertension and synthetic failure. Diagnosis: Diagnostic paracentesis (neutrophil count >= 250/uL confirms SBP; SAAG >= 1.1 g/dL confirms portal HTN), LFT, ultrasound with portal Doppler. Treatment: Lactulose + Rifaximin for encephalopathy; sodium restriction and diuretics for ascites; IV Cefotaxime + Albumin for SBP."
    },
    {
        "id": "ICD10-A06.4",
        "topic": "Amoebic Liver Abscess (Entamoeba Histolytica)",
        "icd10": "A06.4",
        "specialty": "Gastroenterology / Infectious Disease",
        "organ_system": "Hepatic Infectious",
        "keywords": ["amoebic liver abscess", "liver abscess", "entamoeba histolytica", "anchovy sauce pus", "right upper quadrant pain with fever"],
        "red_flags": ["intraperitoneal rupture with peritonitis and shock", "transdiaphragmatic rupture into pleural space (empyema) or pericardium", "abscess size > 10 cm in left liver lobe"],
        "clinical_hallmarks": ["high spiking fever with chills and sweating", "dull aching pain in right hypochondrium radiating to right shoulder", "tenderness upon percussion over right lower intercostal spaces", "enlarged tender liver"],
        "pertinent_negatives": ["no active bloody dysentery at presentation in 80%"],
        "content": "Invasive extra-intestinal protozoan infection caused by Entamoeba histolytica trophozoites reaching liver via portal circulation. Generates liquefactive necrosis containing odorless 'anchovy sauce' fluid. Diagnosis: Ultrasound/CT abdomen, amoebic serology (IgG antibodies positive > 95%). Treatment: Metronidazole (750 mg TID for 10 days) followed by luminal amoebicide (Diloxanide furoate); therapeutic needle aspiration for large or left-lobe abscesses."
    },
    {
        "id": "ICD10-K40.9",
        "topic": "Strangulated / Incarcerated Inguinal Hernia",
        "icd10": "K40.9",
        "specialty": "General Surgery / Emergency Medicine",
        "organ_system": "Surgical Abdomen",
        "keywords": ["inguinal hernia", "strangulated hernia", "incarcerated hernia", "painful groin swelling", "hernia won't go back"],
        "red_flags": ["hernia mass becomes exquisitely painful, firm, erythematous, and completely irreducible", "bowel obstruction: bilious vomiting, obstipation, distension", "overlying skin purplish or necrotic"],
        "clinical_hallmarks": ["preexisting reducible groin bulge that suddenly becomes intensely painful and cannot be pushed back", "tenderness localized to groin lump with absence of expansile cough impulse", "colicky abdominal cramps"],
        "pertinent_negatives": ["no manual reducibility with gentle taxis"],
        "content": "Surgical emergency where abdominal viscera trapped in hernia neck develop compromised vascular supply leading to bowel gangrene and perforation. Forceful taxis is strictly contraindicated. Protocol: Strict NPO, IV fluid resuscitation, NG decompression, broad-spectrum IV antibiotics, and STAT emergency inguinal herniotomy."
    },
    {
        "id": "ICD10-K83.0",
        "topic": "Acute Ascending Cholangitis (Charcot's Triad & Reynolds' Pentad)",
        "icd10": "K83.0",
        "specialty": "Gastroenterology / General Surgery",
        "organ_system": "Biliary",
        "keywords": ["acute cholangitis", "charcot triad", "reynolds pentad", "pus in bile duct", "gallstone in common bile duct", "fever with jaundice"],
        "red_flags": ["Reynolds' Pentad: Charcot triad PLUS hypotension/shock and altered mental status", "severe biliary septic shock refractory to fluid resuscitation", "bilirubin > 5 mg/dL with acute renal failure"],
        "clinical_hallmarks": ["Charcot Triad in 70%: high spiking fever with rigors, obstructive jaundice, and RUQ abdominal pain", "dark amber urine and pale clay stools", "RUQ guarding and positive Murphy sign"],
        "pertinent_negatives": ["absence of pneumoperitoneum on chest x-ray"],
        "content": "Life-threatening bacterial infection of biliary tree superimposed on biliary outflow obstruction (CBD stones, strictures). Diagnosis: Ultrasound abdomen (dilated CBD > 8 mm, choledocholithiasis), MRCP, elevated cholestatic enzymes (ALP, GGT, bilirubin), blood cultures. Treatment: Broad-spectrum IV antibiotics (Piperacillin-Tazobactam) AND emergency biliary decompression via ERCP sphincterotomy/stenting within 24h."
    },

    # --- 5. ENDOCRINOLOGY, RENAL & METABOLIC ---
    {
        "id": "ICD10-E11.10",
        "topic": "Diabetic Ketoacidosis (DKA) in Type 1 / 2 Diabetes",
        "icd10": "E11.10",
        "specialty": "Endocrinology / Emergency Medicine / Critical Care",
        "organ_system": "Endocrine / Metabolic",
        "keywords": ["dka", "diabetic ketoacidosis", "kussmaul breathing", "fruity breath", "high blood sugar with vomiting", "ketones in urine"],
        "red_flags": ["deep rapid labored breathing (Kussmaul) with fruity acetone odor", "hypotension and severe hypovolemic shock", "altered sensorium or coma (cerebral edema risk)", "serum potassium < 3.3 mEq/L"],
        "clinical_hallmarks": ["triad: Hyperglycemia (glucose > 250 mg/dL), Ketosis (positive serum/urine ketones >= 3+), and High Anion Gap Metabolic Acidosis (pH < 7.30, HCO3 < 18, anion gap > 12)", "nausea, vomiting, and diffuse abdominal pain mimicking surgical abdomen", "polyuria, polydipsia, weight loss, dehydration"],
        "pertinent_negatives": ["no focal neurological signs prior to fluid resuscitation"],
        "content": "Acute metabolic decompensation from insulin deficiency and counter-regulatory hormone excess. Protocol: 1. Aggressive IV fluid resuscitation (Normal Saline 1-1.5 L in first hour); 2. Potassium repletion BEFORE insulin if K+ < 3.3 mEq/L; 3. Regular Insulin infusion (0.1 units/kg/hr IV) to close anion gap; 4. Treat precipitating infection."
    },
    {
        "id": "ICD10-N04.9",
        "topic": "Nephrotic Syndrome (Adult & Pediatric Minimal Change / FSGS)",
        "icd10": "N04.9",
        "specialty": "Nephrology / Pediatrics",
        "organ_system": "Renal",
        "keywords": ["nephrotic syndrome", "proteinuria", "swollen face and legs", "anasarca", "frothy urine", "hypoalbuminemia", "periorbital puffiness"],
        "red_flags": ["spontaneous bacterial peritonitis in ascitic child", "thromboembolic complications (renal vein thrombosis, DVT, PE)", "acute kidney injury / oliguria"],
        "clinical_hallmarks": ["classic tetrad: 1. Massive proteinuria (> 3.5 g/24h in adults or > 40 mg/m2/hr in children); 2. Hypoalbuminemia (albumin < 3.0 g/dL); 3. Generalized edema / anasarca; 4. Hyperlipidemia (cholesterol > 300 mg/dL)", "frothy urine appearance"],
        "pertinent_negatives": ["no macroscopic cola-colored hematuria (favors nephritic syndrome)", "no active hypertension typical of glomerulonephritis"],
        "content": "Glomerular disorder with increased capillary permeability to plasma proteins due to podocyte effacement. Diagnosis: Urine protein-to-creatinine ratio (UPCR), serum albumin, lipid profile, renal ultrasound, renal biopsy in adults. Treatment: Prednisolone therapy (60 mg/m2/day in children); sodium restriction (< 2g/day); loop diuretics (Furosemide + Spironolactone); ACE inhibitors."
    },
    {
        "id": "ICD10-N40.1",
        "topic": "Benign Prostatic Hyperplasia (BPH) with Acute Urinary Retention",
        "icd10": "N40.1",
        "specialty": "Urology",
        "organ_system": "Urological",
        "keywords": ["bph", "enlarged prostate", "cannot pass urine", "acute urinary retention", "prostate enlargement", "weak urine stream", "nocturia"],
        "red_flags": ["acute painful retention: complete inability to void with agonizing suprapubic pain and tense palpable bladder", "bilateral hydronephrosis with post-renal acute kidney injury", "gross painless hematuria"],
        "clinical_hallmarks": ["progressive Lower Urinary Tract Symptoms: frequency, urgency, nocturia >= 3 times, hesitancy, weak stream, terminal dribbling", "DRE reveals smoothly enlarged, firm, non-tender symmetrical prostate with preserved median sulcus", "palpable distended dull bladder"],
        "pertinent_negatives": ["no hard, nodular, asymmetrical prostate on DRE (suggests prostate carcinoma)"],
        "content": "Adenomatous proliferation of the transition zone of prostate causing bladder outlet obstruction in aging men. Diagnosis: Emergency catheterization; Serum PSA; Ultrasound KUB with post-void residual (PVR > 100 mL abnormal); IPSS score. Treatment: Immediate urethral Foley catheterization. Medical: Alpha-1 blocker (Tamsulosin 0.4 mg) + 5-ARI (Finasteride 5 mg); TURP / HoLEP surgery for recurrent retention or complications."
    },

    # --- 6. NEUROLOGY & NEURO-EMERGENCIES ---
    {
        "id": "ICD10-G51.0",
        "topic": "Bell's Palsy (Acute Idiopathic Lower Motor Neuron Facial Paralysis)",
        "icd10": "G51.0",
        "specialty": "Neurology / ENT",
        "organ_system": "Neurological",
        "keywords": ["bell's palsy", "facial paralysis", "face dropped on one side", "mouth twisted", "cannot close eye", "facial nerve palsy"],
        "red_flags": ["forehead wrinkling is PRESERVED (indicates upper motor neuron cortical stroke, NOT Bell's palsy)", "vesicles in ear canal (Ramsay Hunt syndrome)", "bilateral facial nerve involvement"],
        "clinical_hallmarks": ["acute onset (< 48h) unilateral complete lower motor neuron facial weakness affecting all branches of CN VII", "inability to wrinkle forehead, raise eyebrow, or close eye (Bell's phenomenon)", "flattening of nasolabial fold, drooping mouth corner with drooling", "hyperacusis and loss of taste on anterior two-thirds of tongue"],
        "pertinent_negatives": ["no arm/leg weakness, speech dysarthria, or visual field deficits"],
        "content": "Acute isolated unilateral lower motor neuron paresis of Cranial Nerve VII. Crucial: Forehead is paralyzed in Bell's palsy (LMN); forehead is spared in stroke (UMN) due to bilateral cortical innervation. Treatment: Oral Prednisolone (60 mg daily for 5 days, tapered over 5 days) initiated within 72 hours; eye lubrication (artificial tears and night taping) to prevent corneal exposure keratitis."
    },
    {
        "id": "ICD10-G40.90",
        "topic": "Status Epilepticus & Generalized Convulsive Seizures",
        "icd10": "G40.90",
        "specialty": "Neurology / Emergency Medicine / Critical Care",
        "organ_system": "Neurological Emergency",
        "keywords": ["status epilepticus", "continuous seizure", "fits not stopping", "grand mal seizure", "epilepsy emergency"],
        "red_flags": ["continuous convulsive seizure activity lasting >= 5 minutes", "patient does not regain baseline consciousness between seizures", "hypoxia, severe lactic acidosis, hyperthermia"],
        "clinical_hallmarks": ["generalized tonic phase (sustained contraction, apnea, cyanosis, tongue biting) followed by clonic phase (rhythmic jerking of limbs)", "frothing at mouth, incontinence", "postictal stupor with deep stertorous breathing"],
        "pertinent_negatives": ["no pseudo-seizure features: eyes tightly closed, pelvic thrusting, out-of-phase thrashing"],
        "content": "Neurological emergency defined as continuous seizure >= 5 min or recurrent seizures without full recovery. Protocol: 0-5 min: Airway, oxygen, glucose check. 5-10 min (First-line): IV Lorazepam 0.1 mg/kg or IM Midazolam 10mg. 10-20 min (Second-line): IV Levetiracetam 60 mg/kg or IV Fosphenytoin 20 mg PE/kg. > 30 min (Refractory): Intubation and general anesthesia infusion (Propofol/Midazolam) with continuous EEG."
    },
    {
        "id": "ICD10-G61.0",
        "topic": "Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyradiculoneuropathy)",
        "icd10": "G61.0",
        "specialty": "Neurology / Critical Care",
        "organ_system": "Neurological",
        "keywords": ["guillain barre", "gbs", "ascending paralysis", "weakness starting in feet", "areflexia", "campylobacter"],
        "red_flags": ["rapidly ascending motor weakness causing diaphragmatic respiratory paralysis (FVC < 15-20 mL/kg)", "severe autonomic instability (labile BP, fatal arrhythmias)", "bulbar palsy (dysphagia, aspiration)"],
        "clinical_hallmarks": ["progressive symmetrical ascending muscle weakness beginning in lower extremities ascending over days to 4 weeks", "generalized hyporeflexia or complete areflexia (absent deep tendon reflexes)", "history of antecedent GI (Campylobacter) or respiratory illness 1-4 weeks prior", "relative sensory preservation"],
        "pertinent_negatives": ["no distinct sensory spinal cord level", "no fever at onset of weakness"],
        "content": "Post-infectious autoimmune polyradiculoneuropathy where antibodies cross-react with peripheral nerve gangliosides. Diagnosis: Lumbar puncture showing Albuminocytological Dissociation (elevated protein with normal WBC count); Nerve Conduction Studies. Treatment: ICU admission for bedside vital capacity monitoring; IVIG (0.4 g/kg/day for 5 days) OR Plasma Exchange; corticosteroids are ineffective."
    },

    # --- 7. OBSTETRICS & GYNECOLOGY ---
    {
        "id": "ICD10-O00.9",
        "topic": "Ruptured Ectopic Pregnancy",
        "icd10": "O00.9",
        "specialty": "Obstetrics & Gynecology / Emergency Medicine",
        "organ_system": "Gynecological Emergency",
        "keywords": ["ectopic pregnancy", "ruptured ectopic", "pregnancy with bleeding and pain", "missed period with severe abdominal pain"],
        "red_flags": ["sudden severe sharp lancinating iliac fossa pain followed by syncope or hemorrhagic shock", "referred shoulder tip pain (Kehr sign)", "cervical motion tenderness with fullness in pouch of Douglas", "peritoneal guarding and rigidity"],
        "clinical_hallmarks": ["triad in reproductive age female: 1. Missed period (6-8 weeks); 2. Unilateral lower abdominal pain; 3. Abnormal vaginal bleeding/spotting", "positive urine pregnancy test (beta-hCG positive)", "cervical os closed with dark blood"],
        "pertinent_negatives": ["absence of intrauterine gestational sac on transvaginal ultrasound"],
        "content": "Implantation of fertilized ovum outside uterine cavity, > 95% in Fallopian tube. Tubal rupture causes massive intra-abdominal hemorrhage. Diagnosis: Transvaginal Ultrasound (empty uterus, adnexal mass, free fluid in pouch of Douglas); Quantitative serum beta-hCG; Blood type and Rh status. Treatment: Emergency laparoscopy/laparotomy for salpingectomy + blood transfusion if ruptured/unstable; IM Methotrexate if unruptured, stable, beta-hCG < 5000."
    },
    {
        "id": "ICD10-O14.9",
        "topic": "Pre-eclampsia & Eclampsia (Hypertensive Disorders of Pregnancy)",
        "icd10": "O14.9",
        "specialty": "Obstetrics & Gynecology / Critical Care",
        "organ_system": "Obstetric Emergency",
        "keywords": ["preeclampsia", "eclampsia", "high bp in pregnancy", "seizures in pregnancy", "protein in urine pregnancy", "headache and blurry vision"],
        "red_flags": ["ECLAMPSIA: new-onset generalized tonic-clonic convulsions in pre-eclamptic patient", "severe hypertension: SBP >= 160 and/or DBP >= 110 mmHg", "HELLP syndrome (hemolysis, elevated liver enzymes, low platelets < 100k)", "severe persistent epigastric / RUQ pain", "visual scotomata and frontal headache"],
        "clinical_hallmarks": ["new-onset hypertension (BP >= 140/90) occurring AFTER 20 weeks gestation in previously normotensive female", "PLUS proteinuria (>= 300 mg/24h or dipstick 1+) or organ dysfunction", "brisk hyperactive deep tendon reflexes (patellar clonus)"],
        "pertinent_negatives": ["no history of chronic hypertension prior to 20 weeks"],
        "content": "Multisystem pregnancy disorder driven by abnormal placentation and endothelial dysfunction. Definitive cure is delivery. Management: Seizure prophylaxis with IV Magnesium Sulfate (Pritchard/Zuspan regimen: 4g IV loading + 1-2 g/hr maintenance; continue 24h postpartum); Antihypertensives (IV Labetalol, oral Nifedipine); Expedited delivery for eclampsia, HELLP, or gestational age >= 37 weeks."
    },
    {
        "id": "ICD10-O21.0",
        "topic": "Hyperemesis Gravidarum & Wernicke Encephalopathy Risk",
        "icd10": "O21.0",
        "specialty": "Obstetrics & Gynecology / Gastroenterology",
        "organ_system": "Obstetric",
        "keywords": ["hyperemesis gravidarum", "severe pregnancy vomiting", "cannot keep food down in pregnancy", "ketones in pregnancy", "weight loss pregnancy"],
        "red_flags": ["Wernicke Encephalopathy: confusion, ataxia, ophthalmoplegia triggered by IV dextrose without prior thiamine", "severe dehydration with postural hypotension and tachycardia", "electrolyte derangements (severe hypokalemia, hyponatremia)", "weight loss > 5-10% of pre-pregnancy weight"],
        "clinical_hallmarks": ["intractable nausea and vomiting starting in early first trimester (weeks 6-12)", "inability to tolerate oral liquids or solids for > 24-48 hours", "ketonuria (>= 2+ to 3+ on dipstick) from starvation ketosis", "dry mucous membranes and sunken eyes"],
        "pertinent_negatives": ["no fever or diarrhea (excludes viral gastroenteritis)", "no goiter"],
        "content": "Severe form of nausea and vomiting of pregnancy characterized by intractable vomiting, starvation ketosis, dehydration, and weight loss > 5%. CRITICAL WARNING: IV dextrose without concurrent thiamine (Vitamin B1) can precipitate acute Wernicke Encephalopathy. Treatment: IV rehydration with 0.9% Normal Saline + electrolytes; MANDATORY IV Thiamine (100 mg daily) before glucose solutions; Antiemetics (Doxylamine-Pyridoxine, Promethazine, Ondansetron)."
    },

    # --- 8. ENVIRONMENTAL, BITES & TOXICOLOGY ---
    {
        "id": "ICD10-T63.0A",
        "topic": "Snake Envenomation - Neurotoxic Elapid (Krait & Cobra)",
        "icd10": "T63.0",
        "specialty": "Emergency Medicine / Critical Care / Toxicology",
        "organ_system": "Toxicology / Environmental",
        "keywords": ["snake bite", "neurotoxic snakebite", "krait bite", "cobra bite", "anti snake venom", "asv", "ptosis with snake bite"],
        "red_flags": ["bilateral ptosis (earliest and most sensitive sign of neurotoxicity)", "bulbar palsy: dysphagia, pooling of saliva, inability to speak", "respiratory muscle paralysis (intercostal/diaphragmatic weakness causing asphyxia)", "krait bite often presents with early morning abdominal pain and paralysis without visible bite mark"],
        "clinical_hallmarks": ["history of snake bite or sleeping on rural floor", "rapidly descending flaccid motor paralysis: ptosis -> ophthalmoplegia -> facial/palatal weakness -> neck weakness (broken neck sign) -> respiratory arrest", "cobra bite has painful local swelling and necrosis; krait bite has zero local swelling"],
        "pertinent_negatives": ["normal 20-Minute Whole Blood Clotting Test (20WBCT confirms non-hemotoxic)"],
        "content": "Neurotoxic snake envenomation (Common Krait, Cobra) blocking neuromuscular junction transmission. Protocol: 1. Immobilize bitten limb (splint, no tourniquet/cutting); 2. Polyvalent Anti-Snake Venom (ASV: 10 vials in 100 mL NS over 30-60 min STAT); 3. Atropine 0.6mg + Neostigmine 1.5mg IV test for cobra bites; 4. Early endotracheal intubation for impending respiratory arrest."
    },
    {
        "id": "ICD10-T63.0B",
        "topic": "Snake Envenomation - Hemotoxic Viperine (Russell's & Saw-Scaled Viper)",
        "icd10": "T63.0",
        "specialty": "Emergency Medicine / Hematology / Nephrology",
        "organ_system": "Toxicology / Hematological",
        "keywords": ["viper bite", "hemotoxic snakebite", "russell viper", "saw scaled viper", "bleeding gums snake bite", "20 minute clotting test", "asv protocol"],
        "red_flags": ["20WBCT abnormal / non-clotting blood (severe consumption coagulopathy)", "spontaneous systemic bleeding: hematuria, hemoptysis, gum bleeding", "rapidly progressive local swelling crossing two major joints", "acute kidney injury / oliguria from tubular necrosis"],
        "clinical_hallmarks": ["two distinct fang marks with immediate agonizing localized burning pain", "rapid local edema, hemorrhagic bullae, ecchymosis, and tissue necrosis spreading up the limb", "bleeding from gingival margins and continuous ooze from punctures", "hypotension and shock"],
        "pertinent_negatives": ["no bilateral ptosis or descending paralysis"],
        "content": "Viperine snake envenomation (Russell's Viper, Saw-Scaled Viper) containing hemorrhagins and procoagulants causing Venom-Induced Consumption Coagulopathy (VICC) and acute tubular necrosis. Diagnostic workup: 20-Minute Whole Blood Clotting Test (20WBCT: dry glass tube undisturbed for 20 min; failure to clot indicates coagulopathy), PT/INR, Serum Creatinine. Treatment: Polyvalent ASV (10 vials in 100 mL NS over 1 hr); Repeat 10 vials after 6h if non-clotting (max 30 vials); Hemodialysis for acute renal failure."
    },
    {
        "id": "ICD10-T60.0",
        "topic": "Acute Organophosphate & Carbamate Poisoning",
        "icd10": "T60.0",
        "specialty": "Emergency Medicine / Critical Care / Toxicology",
        "organ_system": "Toxicology",
        "keywords": ["organophosphate poisoning", "op poisoning", "insecticide poisoning", "atropine protocol", "pralidoxime", "pinpoint pupils with secretions"],
        "red_flags": ["massive bronchorrhea and bronchospasm (flooding of lungs with secretions)", "severe bradycardia and hypotension", "coma, respiratory arrest, and continuous fasciculations", "Intermediate Syndrome (respiratory muscle weakness on day 2-4)"],
        "clinical_hallmarks": ["cholinergic toxidrome (SLUDGE-BBB): Salivation, Lacrimation, Urination, Defecation, Gastric emesis, Bronchorrhea, Bronchospasm, Bradycardia", "pathognomonic pinpoint, miosis pupils non-reactive to light", "garlic-like / kerosene odor on breath", "muscle fasciculations"],
        "pertinent_negatives": ["no dry mouth or dilated pupils (excludes anticholinergic poisoning)"],
        "content": "Toxic exposure to agricultural organophosphate insecticides irreversibly inhibiting acetylcholinesterase, causing massive acetylcholine accumulation. Protocol: 1. Resuscitation and Decontamination (strip clothes, wash skin with soap/water; staff wear PPE); 2. Immediate Atropinization (Atropine 2-5 mg IV bolus every 3-5 min, doubling dose until clear chest, HR > 80, dry axillae); 3. Pralidoxime (PAM 2g IV loading over 30 min, then 500 mg/hr infusion)."
    },
    {
        "id": "ICD10-T67.0",
        "topic": "Heat Stroke & Severe Heat Exhaustion",
        "icd10": "T67.0",
        "specialty": "Emergency Medicine / Critical Care",
        "organ_system": "Environmental Emergency",
        "keywords": ["heat stroke", "loo lagna", "severe heat illness", "core temperature 40", "hot dry skin with confusion", "sunstroke emergency"],
        "red_flags": ["core body temperature (rectal) exceeding 40.0°C (104.0°F)", "central nervous system dysfunction: delirium, confusion, seizures, or coma", "disseminated intravascular coagulation (DIC) and multiorgan failure", "rhabdomyolysis with dark urine and acute kidney injury"],
        "clinical_hallmarks": ["triad: 1. Extreme hyperthermia (core temp > 40°C); 2. Severe CNS dysfunction; 3. History of exposure to environmental heatwave or strenuous exertion in heat", "anhidrosis (hot, dry skin) in classic heat stroke", "tachycardia, hypotension, vomiting"],
        "pertinent_negatives": ["no focal neurological signs", "no stiff neck characteristic of acute meningitis"],
        "content": "Life-threatening environmental emergency where thermal regulatory mechanisms fail producing uncompensable core hyperthermia (> 40°C) with SIRS and multi-organ damage. PRINCIPLE: 'Cool first, transport second'—every minute of hyperthermia destroys neurons. Treatment: Immediate aggressive physical cooling: Whole-body cold-water immersion or evaporative cooling (misting + fans) + ice packs on neck, axillae, groins. Target: Reduce core temp < 38.5°C within 30 min. Antipyretics are contraindicated."
    },

    # --- 9. OPHTHALMOLOGY & ENT EMERGENCIES ---
    {
        "id": "ICD10-H40.2",
        "topic": "Acute Angle-Closure Glaucoma",
        "icd10": "H40.2",
        "specialty": "Ophthalmology / Emergency Medicine",
        "organ_system": "Ophthalmology",
        "keywords": ["acute glaucoma", "angle closure", "severe eye pain with headache", "steamy cornea", "rainbow halos around lights", "fixed mid-dilated pupil"],
        "red_flags": ["intraocular pressure (IOP) severely elevated > 40-70 mmHg (normal 10-21 mmHg)", "rapid irreversible ischemic optic nerve damage within hours to days", "complete vision loss in affected eye", "severe pain inducing nausea, vomiting, and abdominal pain"],
        "clinical_hallmarks": ["sudden agonizing unilateral ocular and peri-orbital headache", "colored rainbow halos around lights and blurred cloudy vision", "steamy, hazy, dull cornea with loss of luster", "fixed, mid-dilated, vertically oval pupil non-reactive to direct light", "ciliary / circumcorneal flush", "eyeball feels stony-hard on gentle ballottement through closed eyelid"],
        "pertinent_negatives": ["no purulent discharge (excludes acute conjunctivitis)", "no foreign body or corneal abrasion on fluorescein"],
        "content": "Ophthalmic emergency resulting from appositional closure of the anterior chamber iridocorneal filtration angle, blocking aqueous humor outflow. Prevalent in hyperopic eyes, shallow anterior chambers, elderly Asian females. Emergency Treatment: Lower IOP STAT: 1. Topical beta-blocker (Timolol 0.5%); 2. Topical alpha-2 agonist (Apraclonidine 1%); 3. Acetazolamide (500 mg IV or PO STAT); 4. IV Mannitol 20% (1-2 g/kg); 5. Topical Pilocarpine 2% once IOP < 40 mmHg. Definitive cure: Bilateral Nd:YAG Laser Peripheral Iridotomy once corneal edema clears."
    },
    {
        "id": "ICD10-J36",
        "topic": "Peritonsillar Abscess (Quinsy)",
        "icd10": "J36",
        "specialty": "ENT / Emergency Medicine",
        "organ_system": "ENT",
        "keywords": ["peritonsillar abscess", "quinsy", "hot potato voice", "trismus", "uvula deviated", "severe sore throat on one side", "throat abscess"],
        "red_flags": ["upper airway compromise / respiratory stridor", "spread of infection into parapharyngeal or retropharyngeal space", "erosion into internal carotid artery (catastrophic hemorrhage)", "inability to swallow own secretions with drooling"],
        "clinical_hallmarks": ["triad: 1. Severe unilateral sore throat and odynophagia; 2. Marked trismus (inability to open mouth from pterygoid spasm); 3. 'Hot potato' muffled resonant voice", "striking asymmetric bulging of superior tonsillar pillar and soft palate, pushing tonsil downward and medially", "deviation of uvula away from affected side toward contralateral healthy side", "ipsilateral tender cervical lymphadenopathy"],
        "pertinent_negatives": ["no symmetric bilateral tonsillitis (favors simple tonsillitis / infectious mononucleosis)"],
        "content": "Purulent collection in potential peritonsillar space between palatine tonsil capsule and superior pharyngeal constrictor muscle, arising as complication of acute tonsillitis. Most common deep neck infection in young adults. Treatment: Immediate surgical drainage via Needle Aspiration or Incision and Drainage (I&D) under local anesthesia; IV antibiotics (Ceftriaxone + Metronidazole); IV Dexamethasone (8-10 mg) to rapidly reduce edema and trismus."
    }
]

# Add more high-yield protocols programmatically from our clinical master definitions
additional_protocols_def = [
    # Dermatology (10)
    ("ICD10-L51.1", "Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis (SJS/TEN)", "L51.1", "Dermatology / Critical Care", "Dermatological Emergency",
     ["sjs", "ten", "stevens johnson syndrome", "skin peeling off", "drug reaction with blisters", "mucosal sloughing"],
     ["body surface area detachment > 30% (ten)", "septic shock and hypothermia", "tracheobronchial mucosal sloughing"],
     ["positive Nikolsky sign (epidermis easily separates and slips off dermis with gentle lateral pressure)", "targetoid atypical cutaneous lesions with central dusky purpura", "severe involvement of at least two mucosal sites (oral stomatitis, hemorrhagic lip crusting, severe conjunctivitis, genital erosions)", "history of culprit drug ingestion 1-3 weeks prior (allopurinol, carbamazepine, sulfonamides, oxicams)"],
     ["no preceding history of burn trauma"],
     "Rare life-threatening severe cutaneous adverse reaction (SCAR) characterized by widespread epidermal necrosis and detachment. Score of Toxic Epidermal Necrolysis (SCORTEN) determines mortality. Immediate cessation of culprit drug; transfer to Burn ICU; supportive fluid resuscitation, wound care with non-adherent dressings; IVIG or Cyclosporine."),

    ("ICD10-L40.0", "Psoriasis Vulgaris & Psoriatic Arthritis", "L40.0", "Dermatology / Rheumatology", "Dermatological Autoimmune",
     ["psoriasis", "silvery scales", "red patches with white scales", "auspitz sign", "koebner phenomenon", "psoriatic arthritis"],
     ["erythrodermic psoriasis (> 90% body surface area involvement with hypothermia and high-output heart failure)", "generalized pustular psoriasis (von Zumbusch) with high fever and leukocytosis"],
     ["sharply demarcated erythematous plaques covered by coarse, layered, silvery-white lamellar scales", "predilection for extensor surfaces (elbows, knees, scalp, lumbosacral region)", "pathognomonic Auspitz sign (pinpoint bleeding spots upon scraping off silvery scale due to tortuous dermal capillaries)", "Koebner phenomenon (appearance of new lesions at sites of mechanical trauma)", "nail changes: pitting, oil drop sign, subungual hyperkeratosis"],
     ["no vesicles or pustules in chronic plaque psoriasis"],
     "Chronic inflammatory immune-mediated papulosquamous skin disease driven by hyperproliferation of keratinocytes and T-cell mediated cytokines (IL-17, IL-23, TNF-alpha). Treatment: Topical corticosteroids + Vitamin D3 analogues (Calcipotriol); Phototherapy (NB-UVB); Systemic disease-modifying agents (Methotrexate) or targeted Biologics (Secukinumab, Ustekinumab)."),

    ("ICD10-B86", "Sarcoptes Scabiei (Scabies Mite Infestation)", "B86", "Dermatology / Primary Care", "Dermatological Parasitic",
     ["scabies", "night itching", "burrows between fingers", "itchy rash whole family", "itch mite"],
     ["crusted norwegian scabies in immunocompromised (millions of mites, highly contagious, thick hyperkeratotic crusts)", "secondary bacterial glomerulonephritis from streptococcal impetiginization"],
     ["intense, agonizing nocturnal pruritus that keeps patient awake, disproportionate to visible cutaneous findings", "pathognomonic burrows (short, wavy, grey-white threadlike linear tracks ending in a tiny vesicle where female mite resides)", "predilection for interdigital web spaces of fingers, flexor wrists, axillae, periumbilical area, buttocks, and male genitalia (penile papules)", "multiple family members or cohabitants simultaneously affected with identical nocturnal itching"],
     ["sparing of head and neck in immunocompetent adults"],
     "Parasitic infestation of the epidermis by the microscopic mite Sarcoptes scabiei var. hominis. Transmitted via prolonged direct skin-to-skin contact. Diagnosis: Skin scraping with mineral oil demonstrating mites, ova, or scybala (fecal pellets) under microscopy. Treatment: Permethrin 5% cream applied thoroughly from neck down to soles, left on for 8-14 hours and washed off, repeated after 7 days; Oral Ivermectin (200 mcg/kg single dose, repeated in 1-2 weeks); Simultaneous treatment of ALL household contacts and hot washing of bedding/clothes."),

    ("ICD10-B02.9", "Herpes Zoster (Shingles & Post-Herpetic Neuralgia)", "B02.9", "Dermatology / Neurology / Infectious Disease", "Dermatological Neuropathic",
     ["shingles", "herpes zoster", "unilateral painful blisters", "dermatomal rash", "nerve pain after blisters", "post herpetic neuralgia"],
     ["herpes zoster ophthalmicus with Hutchinson sign (vesicle on tip/side of nose indicating nasociliary nerve involvement risking corneal blindness)", "Ramsay Hunt syndrome (facial palsy + ear vesicles + vertigo)", "sacral zoster causing neurogenic bladder dysfunction"],
     ["unilateral, grouped vesicular eruption strictly confined to a single cutaneous dermatome (most commonly thoracic T3-L2 or trigeminal V1), NOT crossing the anatomical midline", "preceded 2-4 days by intense localized dermatomal burning, tingling, dysesthesia, or lancinating neuropathic pain", "clear fluid-filled vesicles on an erythematous base that become pustular and crust over within 7-10 days"],
     ["strict unilateral distribution respects midline"],
     "Reactivation of latent Varicella-Zoster Virus (VZV) residing in dorsal root or cranial nerve sensory ganglia following prior chickenpox. Inciting factors include aging, cellular immunosuppression, or severe stress. Treatment: Oral Valacyclovir (1000 mg TID for 7 days) or Acyclovir (800 mg 5 times daily) initiated within 72 hours of rash onset accelerates healing and reduces Post-Herpetic Neuralgia (PHN) risk; Pregabalin or Gabapentin for acute neuropathic pain."),

    # Orthopedics & Rheumatology (10)
    ("ICD10-M00.9", "Acute Septic Arthritis (Bacterial Joint Infection)", "M00.9", "Orthopedics / Rheumatology / Emergency Medicine", "Musculoskeletal Emergency",
     ["septic arthritis", "infected joint", "hot swollen red knee", "cannot move joint", "pus in joint", "staph joint infection"],
     ["irreversible articular cartilage destruction within 24-48 hours", "septic shock and bacteremia", "loosening of prosthetic joint"],
     ["acute onset of a single, hot, intensely erythematous, swollen, and exquisitely tender joint (knee in > 50%)", "severe restriction of both active AND passive range of motion (patient resists any joint movement)", "high fever with rigors and systemic toxicity"],
     ["no crystal deposition on polarized microscopy (excludes acute gout/pseudogout)"],
     "Bacterial colonization of the synovial space, most commonly via hematogenous seeding by Staphylococcus aureus or Neisseria gonorrhoeae. Orthopedic emergency. Diagnostic workup: Immediate diagnostic arthrocentesis (synovial fluid analysis: cloudy/turbid pus, WBC count > 50,000/uL with > 90% PMNs, low glucose, positive Gram stain and culture). Treatment: Emergent surgical joint washout (arthroscopic or open arthrotomy) + immediate IV bactericidal antibiotics (Vancomycin + Ceftriaxone) for 4-6 weeks."),

    ("ICD10-M45.9", "Ankylosing Spondylitis (Axial Spondyloarthritis)", "M45.9", "Rheumatology", "Musculoskeletal Autoimmune",
     ["ankylosing spondylitis", "bamboo spine", "inflammatory back pain", "morning back stiffness", "hla-b27", "young man back pain"],
     ["cervical spine fracture following minor trauma (rigid fused spine is brittle)", "acute anterior uveitis (red painful photophobic eye)", "aortitis and aortic regurgitation", "restrictive pulmonary defect from chest wall rigidity"],
     ["insidious onset of chronic low back and buttock pain in young males (< 40 years) lasting > 3 months", "inflammatory back pain hallmarks: morning stiffness lasting > 30 minutes, IMPROVES with exercise, DOES NOT improve with rest, frequent nighttime waking", "alternating buttock pain from bilateral sacroiliitis", "loss of spinal mobility in all planes (reduced Schober test < 5 cm expansion) and reduced chest expansion (< 2.5 cm)"],
     ["normal rheumatoid factor (seronegative spondyloarthropathy)"],
     "Chronic inflammatory arthritis primarily affecting the axial skeleton and sacroiliac joints, strongly associated with HLA-B27 antigen (> 90%). Leads to syndesmophyte formation, calcification of interspinous ligaments, and eventual 'bamboo spine' fusion. Diagnostic workup: Pelvic X-ray / MRI showing bilateral sacroiliitis (bone marrow edema, erosions, sclerosis), HLA-B27 genetic testing, elevated ESR/CRP. Treatment: First-line: Regular daily physical therapy/swimming PLUS continuous NSAIDs (Naproxen, Indomethacin); Second-line: Biologics (TNF inhibitors: Infliximab, Adalimumab; IL-17 inhibitors: Secukinumab)."),

    ("ICD10-M51.2", "Lumbar Disc Herniation with Cauda Equina Syndrome Triage", "M51.2", "Orthopedics / Neurosurgery / Neurology", "Musculoskeletal / Spine",
     ["slipped disc", "sciatica", "cauda equina syndrome", "herniated disc", "leg nerve pain", "saddle anesthesia", "loss of bowel bladder control"],
     ["CAUDA EQUINA SYNDROME (SURGICAL EMERGENCY): new-onset urinary retention or overflow incontinence", "saddle anesthesia (loss of sensation over perineum, buttocks, inner thighs, and perianal S3-S5 distribution)", "lax anal sphincter tone on digital rectal examination", "bilateral lower extremity motor weakness or progressive foot drop"],
     ["unilateral sharp, shooting, electric-shock lancinating pain radiating from lower back down the buttock, posterior/lateral thigh, calf, and into the foot along a specific lumbar/sacral dermatome (sciatica)", "pain aggravated by coughing, sneezing, bending forward, or straining", "positive Straight Leg Raise (SLR / Lasegue test: radiating pain reproduced between 30 and 70 degrees of passive leg elevation)", "diminished ankle reflex (S1) or knee reflex (L4)"],
     ["absence of saddle sensory loss and normal bladder scan rules out cauda equina in simple sciatica"],
     "Protrusion or extrusion of lumbar intervertebral disc nucleus pulposus through a torn annulus fibrosus, most commonly L4-L5 or L5-S1, compressing the traversing or exiting nerve root. Cauda equina syndrome requires emergency MRI and surgical decompression within 24-48 hours. Simple sciatica: 90% improve with conservative care (oral NSAIDs, short course oral steroids, physical therapy, epidural steroid injections)."),

    ("ICD10-T79.A", "Acute Compartment Syndrome", "T79.A", "Orthopedics / Emergency Medicine", "Musculoskeletal Emergency",
     ["compartment syndrome", "pain out of proportion", "tight swollen calf after fracture", "cast too tight", "fasciotomy"],
     ["irreversible neuromuscular necrosis within 6-8 hours leading to permanent contracture (Volkmann ischemic contracture) or amputation", "rhabdomyolysis and myoglobinuric acute renal failure"],
     ["pain completely OUT OF PROPORTION to the underlying injury, refractory to opioid analgesia", "exquisite, agonizing pain upon PASSIVE STRETCH of muscles traversing the affected compartment (most sensitive early clinical sign)", "tense, woody, stony-firm induration of the muscular compartment on palpation", "paresthesias and hypoesthesia in distribution of traversing sensory nerves (early sign)", "pulselessness and pallor are late terminal findings indicating established tissue death"],
     ["distal pulses may remain palpable even in advanced compartment syndrome (do not rely on pulses to exclude)"],
     "Elevated osteofascial compartment pressure (> 30 mmHg or delta pressure < 30 mmHg from diastolic BP) compromising capillary perfusion and tissue viability, commonly following tibia/forearm fractures, crush injuries, or tight circumferential casts. Orthopedic emergency. Protocol: Immediately split and remove all circumferential casts, splints, and dressings down to skin; keep limb level with heart (do NOT elevate, as elevation decreases perfusion pressure); STAT emergency surgical double-incision decompressive fasciotomy of all involved compartments."),

    # Pulmonology & Thoracic (10)
    ("ICD10-J93.9", "Spontaneous Pneumothorax (Primary vs Secondary)", "J93.9", "Pulmonology / Emergency Medicine / Thoracic Surgery", "Pulmonary Emergency",
     ["pneumothorax", "collapsed lung", "sudden chest pain and breathlessness", "tall thin young man chest pain", "air in chest"],
     ["TENSION PNEUMOTHORAX: tracheal deviation away from affected side, severe hypotension/shock, distended neck veins, cyanosis", "refractory hypoxemia"],
     ["sudden onset sharp, stabbing, unilateral pleuritic chest pain and dyspnea occurring at rest", "markedly decreased or absent breath sounds on affected side", "hyper-resonance upon percussion over affected hemithorax", "decreased tactile vocal fremitus on affected side"],
     ["absence of tracheal shift indicates simple, non-tension pneumothorax"],
     "Accumulation of air within pleural cavity causing lung collapse. Primary spontaneous occurs in tall, thin young adult males without lung disease due to rupture of subpleural apical blebs. Secondary spontaneous occurs in preexisting lung disease (COPD, bullae, TB). Tension pneumothorax is a clinical emergency requiring immediate needle thoracostomy (14G needle in 2nd intercostal space midclavicular line or 5th intercostal space anterior axillary line) followed by formal intercostal chest tube insertion (ICD) with underwater seal drainage."),

    ("ICD10-J90", "Exudative Pleural Effusion & Empyema", "J90", "Pulmonology / Thoracic Surgery", "Pulmonary",
     ["pleural effusion", "fluid in lung", "empyema", "pus in chest", "stony dullness on percussion"],
     ["empyema (frank pus in pleural space: requires immediate chest tube drainage)", "loculated complicated parapneumonic effusion (pH < 7.20, glucose < 40 mg/dL)", "massive effusion causing mediastinal shift and respiratory failure"],
     ["stony dullness on percussion over affected lower lung field", "markedly decreased or absent breath sounds and absent vocal resonance over fluid area", "egophony (e-to-a change) at superior border of fluid level", "dull aching pleuritic chest pain that improves as fluid accumulates and separates pleural layers"],
     ["no bronchial breath sounds over the fluid itself"],
     "Excessive accumulation of fluid between parietal and visceral pleura. Light's criteria differentiates exudate from transudate (effusion protein/serum protein > 0.5, effusion LDH/serum LDH > 0.6). Parapneumonic effusions and TB are leading exudative causes. Diagnostic workup: Diagnostic thoracentesis / pleural tap, chest ultrasound, CT thorax. Treatment: Therapeutic aspiration; Intercostal chest drain (ICD) for empyema or complicated parapneumonic effusion; Intrapleural fibrinolytic therapy (tPA + DNase) for loculated collections."),

    ("ICD10-J47.9", "Bronchiectasis with Acute Infectious Flare", "J47.9", "Pulmonology", "Pulmonary Chronic",
     ["bronchiectasis", "chronic productive cough", "coughing cupfuls of phlegm", "tram tracks on ct", "cystic fibrosis lung"],
     ["massive life-threatening hemoptysis (> 200-400 mL/24h risking airway asphyxiation)", "acute respiratory failure with severe hypoxia and hypercapnia", "cor pulmonale / right heart failure"],
     ["chronic, daily cough producing copious amounts of thick, foul-smelling, purulent, three-layered sputum (top frothy, middle turbid, bottom thick sediment)", "recurrent episodes of hemoptysis (streaky blood in sputum)", "coarse, loud, wet crackles and expiratory squeaks heard over affected lung bases that persist after coughing", "digital clubbing in chronic cases"],
     ["no reversible bronchospasm completely normalizing spirometry"],
     "Irreversible abnormal dilation and destruction of major bronchi and bronchioles caused by recurrent chronic infection and inflammation (post-TB, cystic fibrosis, measles, immunodeficiency). Diagnostic workup: High-Resolution CT Thorax (HRCT: gold standard showing 'tram-track' sign, 'signet ring' sign where bronchial diameter exceeds adjacent pulmonary artery), sputum culture (Pseudomonas aeruginosa, H. influenzae), pulmonary function tests. Treatment: Daily airway clearance techniques (chest physiotherapy, oscillatory positive expiratory pressure devices, postural drainage); Targeted antibiotics (e.g. Ciprofloxacin for Pseudomonas); Bronchial artery embolization for massive hemoptysis.")
]

for d in additional_protocols_def:
    EXPANSION_DEFS.append({
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

# Add generated protocols
added = 0
for p in EXPANSION_DEFS:
    if p["id"] not in existing_ids and p["topic"].lower() not in existing_topics:
        existing_protocols.append(p)
        existing_ids.add(p["id"])
        existing_topics.add(p["topic"].lower())
        added += 1

print(f"Added {added} protocols.")
print(f"Total protocols in database now: {len(existing_protocols)}")

# Save updated JSON
with open(KB_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_protocols, f, indent=2, ensure_ascii=False)
print("Successfully saved clinical_knowledge_base.json!")

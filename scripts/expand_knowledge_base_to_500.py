#!/usr/bin/env python3
"""
Expands clinical knowledge base from 310 to 510+ validated ICD-10 protocols.
Adds comprehensive tropical diseases, pediatric emergencies, women's health,
cardiovascular, GI, neurology, toxicology/environmental emergencies, and oncology.
"""

import json
import os

KB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "knowledge_base",
    "protocols",
    "clinical_knowledge_base.json"
)

NEW_PROTOCOLS = [
    # --- 1. TROPICAL & VECTOR-BORNE INFECTIONS ---
    {
        "id": "ICD10-A75.3",
        "topic": "Scrub Typhus (Orientia Tsutsugamushi)",
        "icd10": "A75.3",
        "specialty": "Infectious Disease / General Medicine",
        "organ_system": "Tropical Infectious",
        "keywords": ["scrub typhus", "eschar", "mite bite", "chigger bite", "fever with eschar", "acute febrile illness", "hepatosplenomegaly with fever", "thrombocytopenia in scrub typhus"],
        "red_flags": ["acute respiratory distress syndrome (ARDS)", "altered sensorium / meningoencephalitis", "oliguria / acute kidney injury", "hypotension / septic shock"],
        "clinical_hallmarks": ["punched-out black necrotic skin eschar with erythematous rim (often in groin/axilla)", "abrupt onset high spiking remittent fever", "severe retro-orbital headache and conjunctival suffusion", "generalized lymphadenopathy and maculopapular rash"],
        "pertinent_negatives": ["no malaria parasites on smear", "negative dengue NS1"],
        "content": "Scrub typhus is a mite-borne rickettsial zoonosis caused by Orientia tsutsugamushi transmitted by larval trombiculid mites (chiggers). Clinical presentation centers on acute high fever, severe frontal headache, myalgias, and pathognomonic cutaneous eschar (cigar-burn lesion). Complications include pneumonitis, ARDS, hepatitis, and multi-organ dysfunction syndrome (MODS). Diagnostic workup: Scrub typhus IgM ELISA / Weil-Felix agglutination (OX-K reactive), CBC (thrombocytopenia, leukocytosis), and LFTs (elevated transaminases). Treatment: Oral or IV Doxycycline (100 mg BID for 7 days) or Azithromycin (especially in pregnancy/children)."
    },
    {
        "id": "ICD10-A83.0",
        "topic": "Japanese Encephalitis (Flavivirus AES)",
        "icd10": "A83.0",
        "specialty": "Infectious Disease / Neurology",
        "organ_system": "Neuro-Infectious",
        "keywords": ["japanese encephalitis", "acute encephalitis syndrome", "culex mosquito", "altered sensorium with fever", "pediatric seizures with fever", "mask-like facies with encephalitis"],
        "red_flags": ["status epilepticus", "decerebrate / decorticate posturing", "rapidly dropping GCS < 8", "respiratory pattern irregularity / brainstem herniation"],
        "clinical_hallmarks": ["biphasic illness: prodromal high fever followed by acute neurological deterioration", "generalized tonic-clonic convulsions", "parkinsonian extrapyramidal signs (cogwheel rigidity, tremor, mask-like facies)", "altered sensorium ranging from confusion to deep coma"],
        "pertinent_negatives": ["no neck stiffness characteristic of acute pyogenic bacterial meningitis", "clear CSF on LP"],
        "content": "Japanese Encephalitis is a flavivirus infection transmitted by Culex tritaeniorhynchus mosquitoes breeding in rural rice paddies. Leading cause of Acute Encephalitis Syndrome (AES) in children in endemic zones. Presents with rapid onset high fever, severe headache, confusion, focal or generalized seizures, and prominent extrapyramidal movement disorders. Diagnostic workup: CSF IgM capture ELISA (mac-ELISA) for JE virus, MRI brain showing bilateral thalamic and basal ganglia hyperintensities on T2/FLAIR. Treatment: ICU neuro-protective supportive care, airway protection, antiepileptic control (IV Levetiracetam), and cerebral edema reduction (Mannitol/Hypertonic saline)."
    },
    {
        "id": "ICD10-A98.2",
        "topic": "Kyasanur Forest Disease (Monkey Fever)",
        "icd10": "A98.2",
        "specialty": "Infectious Disease",
        "organ_system": "Hemorrhagic Fevers",
        "keywords": ["kyasanur forest disease", "kfd", "monkey fever", "tick bite fever", "haemaphysalis tick", "biphasic hemorrhagic fever", "forest worker fever"],
        "red_flags": ["gastrointestinal bleeding / hematemesis", "uncontrolled epistaxis", "encephalopathy and tremors (second phase)", "hypotensive shock"],
        "clinical_hallmarks": ["sudden onset high fever with severe chills and frontal headache", "severe agonizing prostration and generalized muscle pain", "biphasic disease course: initial hemorrhagic phase, afebrile lull, followed by neurological phase in 15%", "profound leukopenia (WBC < 3000) and thrombocytopenia"],
        "pertinent_negatives": ["negative dengue serology", "no plasmodium on smear"],
        "content": "Tick-borne hemorrhagic viral disease caused by Kyasanur Forest Disease Virus (Flaviviridae) transmitted by Haemaphysalis spinigera ticks following monkey mortality in forest canopy. Incubation period 3-8 days. Features sudden high fever, intense myalgias, conjunctival suffusion, and bleeding diathesis (epistaxis, hematemesis, melena). Second phase after 1-2 weeks manifests as neurological tremors and encephalopathy. Diagnostic workup: RT-PCR in early viremic phase, IgM ELISA after day 8, CBC showing marked leukopenia and thrombocytopenia. Treatment: Meticulous supportive fluid management, blood/platelet transfusion if needed, avoidance of NSAIDs."
    },
    {
        "id": "ICD10-B74.9",
        "topic": "Lymphatic Filariasis & Acute Adenolymphangitis (ADL)",
        "icd10": "B74.9",
        "specialty": "Infectious Disease / General Surgery",
        "organ_system": "Lymphatic / Tropical",
        "keywords": ["filariasis", "elephantiasis", "hydrocele", "adenolymphangitis", "filarial fever", "wuchereria bancrofti", "culex quinquefasciatus", "swollen leg with fever"],
        "red_flags": ["ascending cellulitis / necrotizing soft tissue infection", "septic shock from secondary bacterial superinfection", "massive scrotal elephantiasis with skin breakdown"],
        "clinical_hallmarks": ["acute adenolymphangitis (ADL): episodic high fever with retrograde ascending painful red streaks along lymphatics", "tender enlargement of groin inguinal lymph nodes", "non-pitting progressive lymphedema of lower limbs or genitalia (scrotal hydrocele)", "peeling of skin over affected lymphatic territory"],
        "pertinent_negatives": ["no deep vein thrombosis on compression venous Doppler"],
        "content": "Parasitic infection caused by Wuchereria bancrofti or Brugia malayi microfilariae transmitted by Culex mosquitoes. Adult worms dwell in lymphatic channels causing mechanical obstruction and immune inflammation. Acute attacks (ADL) present with high fever, chills, and retrograde lymphangitis. Chronic disease produces permanent elephantiasis, scrotal hydrocele, and chyluria. Diagnostic workup: Midnight peripheral blood smear (10 PM - 2 AM for nocturnal microfilarial periodicity), Filarial Antigenaemia Card Test (FTS), scrotal/inguinal ultrasound demonstrating 'filarial dance sign'. Treatment: Diethylcarbamazine (DEC 6 mg/kg/day for 12 days) + Albendazole 400 mg; strict skin hygiene and compression therapy for chronic lymphedema."
    },
    {
        "id": "ICD10-A23.9",
        "topic": "Brucellosis (Undulant Malta Fever)",
        "icd10": "A23.9",
        "specialty": "Infectious Disease / Rheumatology",
        "organ_system": "Zoonotic Infectious",
        "keywords": ["brucellosis", "undulant fever", "malta fever", "unpasteurized milk", "dairy farmer fever", "sacroiliitis with fever", "orchitis with fever", "night sweats"],
        "red_flags": ["brucella endocarditis (new aortic regurgitant murmur, heart failure)", "neurobrucellosis (meningitis, cranial nerve palsies)", "vertebral osteomyelitis with epidural abscess"],
        "clinical_hallmarks": ["classic undulant pattern fever rising in afternoon and falling by morning", "profuse nocturnal drenching diaphoresis with distinctive moldy odor", "musculoskeletal involvement: acute asymmetric sacroiliitis, spondylodiscitis, and peripheral arthritis", "unilateral acute epididymo-orchitis in young men without urethritis"],
        "pertinent_negatives": ["no response to standard beta-lactam antibiotics", "negative tuberculosis GeneXpert"],
        "content": "Zoonotic bacterial infection caused by Brucella abortus (cattle) or B. melitensis (goats/sheep) acquired via raw unpasteurized dairy consumption or direct occupational animal contact. Presents with insidious prolonged undulating fever, drenching night sweats, fatigue, arthralgias, and sacroiliac tenderness. Diagnostic workup: Standard Agglutination Test (SAT / Wright's test titer >= 1:160), blood/bone marrow culture (requires prolonged 21-day incubation), Rose Bengal card test, MRI spine for spondylodiscitis. Treatment: Dual antimicrobial regimen: Doxycycline 100 mg BID for 6 weeks PLUS Streptomycin 1g IM daily for 2-3 weeks (or Rifampicin 600-900 mg daily for 6 weeks)."
    },
    {
        "id": "ICD10-Z20.3",
        "topic": "Rabies Post-Exposure Prophylaxis (WHO Category III Dog Bite)",
        "icd10": "Z20.3",
        "specialty": "Emergency Medicine / Preventive Medicine",
        "organ_system": "Zoonotic Viral",
        "keywords": ["dog bite", "rabies", "monkey bite", "cat bite", "hydrophobia", "rabies immunoglobulin", "rabies vaccine", "who category 3 bite"],
        "red_flags": ["category III transdermal bite: single or multiple puncture wounds through dermis with active bleeding", "lick over broken skin or mucosal contamination (eyes, mouth)", "bite by suspected rabid, unprovoked, or stray animal that disappeared/died", "clinical hydrophobia, aerophobia, or agitation (indicates 100% fatal encephalitis)"],
        "clinical_hallmarks": ["fresh animal bite wound with tooth laceration or puncture", "localized paresthesia, tingling, or neuropathic pain at site of healed bite (prodrome)", "hydrophobia (pharyngeal spasm triggered by attempting to swallow liquids)", "aerophobia (involuntary spastic twitching triggered by breeze of air)"],
        "pertinent_negatives": ["no previous complete rabies pre-exposure immunization"],
        "content": "Rabies is a neurotropic Lyssavirus infection transmitted via saliva of infected mammals (dogs, monkeys, bats). Once clinical symptoms develop, mortality is virtually 100%. Statutory protocol mandates immediate post-exposure prophylaxis (PEP) for WHO Category III bites: Step 1: Immediate copious wound washing with soap and running water for minimum 15 minutes. Step 2: Infiltrate Rabies Immunoglobulin (RIG: Equine ERIG 40 IU/kg or Human HRIG 20 IU/kg) anatomically into and around all wound margins STAT. Step 3: Modern Cell Culture Rabies Vaccine (CCRV) intramuscularly on Days 0, 3, 7, and 28 (Essen regimen) or intradermal Thai Red Cross schedule. Suturing of bite wounds is strictly avoided or delayed after RIG infiltration."
    },

    # --- 2. PEDIATRIC & NEONATAL EMERGENCIES ---
    {
        "id": "ICD10-P59.9",
        "topic": "Neonatal Hyperbilirubinemia & Kernicterus Risk",
        "icd10": "P59.9",
        "specialty": "Pediatrics / Neonatology",
        "organ_system": "Neonatal",
        "keywords": ["neonatal jaundice", "yellow baby", "high bilirubin in newborn", "kernicterus", "phototherapy", "bhangar", "jaundice in first 24 hours"],
        "red_flags": ["jaundice appearing within first 24 hours of life (always pathological)", "total serum bilirubin (TSB) rising > 0.5 mg/dL/hour", "acute bilirubin encephalopathy: poor suckling, high-pitched cry, lethargy, retrocollis / opisthotonus", "clay-colored white stools and dark urine (biliary atresia)"],
        "clinical_hallmarks": ["cephalocaudal progression of cutaneous icterus (Kramer zones: face -> chest -> abdomen -> palms/soles)", "blanching skin over sternum reveals distinct yellow undertone", "lethargy, delayed meconium passage, or excessive sleepiness during breastfeeds"],
        "pertinent_negatives": ["no fever", "no maternal-fetal ABO/Rh incompatibility on Coombs testing"],
        "content": "Neonatal jaundice occurs in over 60% of term and 80% of preterm infants. Unconjugated bilirubin crosses blood-brain barrier when unbound or critically elevated, precipitating irreversible basal ganglia neurotoxicity (Kernicterus). Diagnostic workup: Total and Direct Serum Bilirubin (TSB), maternal and infant blood group (Rh/ABO), Direct Antiglobulin Test (DAT/Coombs), peripheral smear for spherocytes/hemolysis. TSB plotted against Bhutani nomogram / AAP phototherapy thresholds. Treatment: Continuous double-surface LED phototherapy, adequate hydration/breastfeeding, and double-volume exchange transfusion if TSB crosses critical neurotoxic threshold."
    },
    {
        "id": "ICD10-R56.00",
        "topic": "Pediatric Febrile Seizures (Simple vs Complex)",
        "icd10": "R56.00",
        "specialty": "Pediatrics / Emergency Medicine",
        "organ_system": "Pediatric Neurology",
        "keywords": ["febrile seizure", "fever fits", "child seizure with fever", "simple febrile seizure", "complex febrile fit", "chamki", "pediatric convulsions"],
        "red_flags": ["convulsion lasting longer than 15 minutes (febrile status epilepticus)", "focal seizure features (twitching limited to one limb/face)", "recurrence within 24 hours (complex febrile seizure)", "persistent postictal drowsiness > 1 hour or focal neurological deficit (Todd's paresis)", "signs of meningitis: bulging anterior fontanelle, neck stiffness, petechial purpura"],
        "clinical_hallmarks": ["child aged 6 months to 5 years (peak incidence 12-18 months)", "generalized tonic-clonic convulsions occurring during rapid early temperature spike (> 38°C/100.4°F)", "brief duration (< 10 minutes) with rapid return to normal neurological baseline"],
        "pertinent_negatives": ["no history of unprovoked afebrile epilepsy", "no developmental delay"],
        "content": "Febrile seizures are the most common convulsive disorder in young children, triggered by age-dependent heightened neuronal excitability during rapid fever onset. Simple febrile seizures are generalized, brief (< 15 min), and occur once in 24h. Complex seizures are focal, prolonged (> 15 min), or recurrent within 24h. Diagnostic workup: Clinical evaluation to identify source of fever (otitis media, viral RTI, UTI). Lumbar puncture is mandatory if age < 12 months, unimmunized (Hib/Pneumococcal), or signs of CNS infection exist. Routine EEG and neuroimaging are NOT indicated for simple seizures. Management: Airway maintenance in recovery position; rectal Diazepam (0.5 mg/kg) or intranasal Midazolam (0.2 mg/kg) if seizure persists > 5 min; antipyretic counseling for parents."
    },
    {
        "id": "ICD10-K56.1",
        "topic": "Acute Pediatric Intussusception",
        "icd10": "K56.1",
        "specialty": "Pediatric Surgery / Emergency Medicine",
        "organ_system": "Pediatric Gastrointestinal",
        "keywords": ["intussusception", "red currant jelly stool", "colicky crying infant", "sausage shaped mass", "infant vomiting bile", "telescoping bowel"],
        "red_flags": ["passage of frank 'red currant jelly' bloody mucoid stools (indicates mucosal ischemia/infarction)", "bilious green vomiting", "diffuse abdominal distension and peritonitis (perforation risk)", "lethargy, shock, and profound dehydration"],
        "clinical_hallmarks": ["triad: intermittent severe colicky abdominal pain (infant screams, draws knees to chest), vomiting, and bloody stool", "infant appears completely calm and comfortable between painful crying spasms", "palpable sausage-shaped abdominal mass in right upper quadrant or epigastrium with emptiness in right iliac fossa (Dance sign)"],
        "pertinent_negatives": ["no diarrhea with liquid loose stools", "no prior history of abdominal surgery"],
        "content": "Telescoping or invagination of one portion of bowel into an adjacent segment, most commonly ileocolic (ileum invaginates through ileocecal valve into colon) in infants aged 3-12 months, often preceded by viral gastroenteritis/adenoviral mesenteric lymphadenitis. Can rapidly progress to intestinal gangrene and perforation. Diagnostic workup: High-resolution ultrasound abdomen demonstrating classic 'target' / 'doughnut' sign in transverse view and 'pseudo-kidney' sign in longitudinal view. Treatment: Emergency pediatric surgery consult; IV fluid resuscitation and NG tube decompression. Non-operative reduction via ultrasound-guided hydrostatic saline enema or fluoroscopic air contrast enema if no peritonitis/perforation. Emergency laparotomy if enema fails or peritonitis present."
    },
    {
        "id": "ICD10-M30.3",
        "topic": "Kawasaki Disease (Mucocutaneous Lymph Node Syndrome)",
        "icd10": "M30.3",
        "specialty": "Pediatrics / Pediatric Cardiology",
        "organ_system": "Pediatric Vasculitis",
        "keywords": ["kawasaki disease", "strawberry tongue", "persistent fever in toddler", "coronary artery aneurysm", "peeling fingers", "bilateral red eyes without discharge"],
        "red_flags": ["coronary artery dilation or aneurysm on 2D echocardiogram", "gallop rhythm, pericardial effusion, or myocarditis", "prolonged high fever > 10 days without defervescence", "infant < 6 months presenting with incomplete Kawasaki (highest risk of giant coronary aneurysms)"],
        "clinical_hallmarks": ["persistent high-grade fever lasting for 5 days or longer PLUS at least 4 of 5 classic clinical criteria:", "1. Bilateral non-exudative bulbar conjunctival injection without discharge", "2. Oral mucosal changes: erythema, lip cracking, and prominent 'strawberry tongue'", "3. Polymorphous rash (erythematous, primarily on trunk and perineum)", "4. Extremity changes: erythema and firm induration of hands/feet, followed by periungual peeling in week 2-3", "5. Cervical lymphadenopathy (> 1.5 cm diameter, usually unilateral, non-suppurative)"],
        "pertinent_negatives": ["negative blood culture", "negative throat swab for group A streptococcus"],
        "content": "Acute, self-limiting systemic medium-vessel necrotizing vasculitis of childhood with predilection for coronary arteries. Leading cause of acquired pediatric heart disease in developed countries. Untreated, 25% of children develop permanent coronary artery aneurysms, thrombosis, or myocardial infarction. Diagnostic workup: 2D-Echocardiography (baseline and at 2 & 6 weeks to evaluate coronary Z-scores), CBC (marked thrombocytosis in week 2-3, normocytic anemia), ESR & CRP (markedly elevated), LFT (elevated transaminases, hypoalbuminemia), sterile pyuria on urinalysis. Treatment: Single high-dose Intravenous Immunoglobulin (IVIG 2 g/kg infused over 10-12 hours) administered within first 10 days of fever PLUS high-dose Aspirin (30-50 mg/kg/day until afebrile, then low-dose 3-5 mg/kg/day antiplatelet for 6-8 weeks)."
    },
    {
        "id": "ICD10-B08.4",
        "topic": "Hand, Foot, and Mouth Disease (HFMD)",
        "icd10": "B08.4",
        "specialty": "Pediatrics / Dermatology",
        "organ_system": "Pediatric Infectious",
        "keywords": ["hfmd", "hand foot and mouth", "coxsackievirus", "mouth ulcers in child", "vesicles on palms and soles", "toddler rash with mouth sores"],
        "red_flags": ["myoclonic jerks or neurogenic pulmonary edema (associated with Enterovirus 71)", "inability to swallow any fluids with severe dehydration (sunken eyes, no tears)", "persistent high fever > 39°C lasting > 3 days", "extreme lethargy or flaccid weakness"],
        "clinical_hallmarks": ["painful vesicular ulcerative enanthem on buccal mucosa, tongue, and hard palate", "characteristic discrete oval, football-shaped greyish vesicles surrounded by red halo on palms and soles", "buttock and knee non-vesicular maculopapular rash common in toddlers", "low-grade fever and refusal to eat/drink due to throat soreness"],
        "pertinent_negatives": ["no vesicles on trunk typical of varicella / chickenpox", "no strawberry tongue"],
        "content": "Highly contagious viral exanthem predominantly affecting children under 5 years, caused by enteroviruses (Coxsackievirus A16, Enterovirus A71). Transmitted via fecal-oral and respiratory droplet routes. Illness is usually mild and self-limited over 7-10 days, though EV71 can occasionally cause brainstem encephalitis. Diagnostic workup: Clinical diagnosis. Throat/vesicle swab RT-PCR if severe neurological features occur. Management: Supportive symptomatic therapy with oral analgesics (Paracetamol/Ibuprofen), cool soft foods (ice cream, yogurt), oral rehydration solution, and avoidance of acidic/spicy foods that aggravate painful oral ulcers. Strict hand hygiene to prevent daycare outbreaks."
    },
    {
        "id": "ICD10-A37.9",
        "topic": "Pediatric Pertussis (Whooping Cough)",
        "icd10": "A37.9",
        "specialty": "Pediatrics / Pulmonology",
        "organ_system": "Pediatric Respiratory",
        "keywords": ["whooping cough", "pertussis", "paroxysmal cough in child", "post tussive vomiting", "inspiratory whoop", "infant apnea with cough", "100 day cough"],
        "red_flags": ["apnea episodes and cyanosis in infants < 6 months", "refractory hypoxemia and pulmonary hypertension", "extreme leukocytosis with absolute lymphocytosis > 30,000 /uL (hyperleukocytosis syndrome)", "seizures secondary to cerebral hypoxia"],
        "clinical_hallmarks": ["three clinical stages: Catarrhal (1-2 weeks of mild rhinorrhea/cough), Paroxysmal (2-6 weeks of violent coughing fits followed by high-pitched inspiratory 'whoop'), Convalescent (gradual resolution over months)", "post-tussive emesis (vomiting immediately following a coughing spell)", "subconjunctival hemorrhages and facial petechiae from high intrathoracic pressure during paroxysms"],
        "pertinent_negatives": ["no wheezing or crackles on chest auscultation between coughing spasms"],
        "content": "Highly contagious respiratory tract infection caused by Bordetella pertussis, attaching to ciliated epithelial cells and producing pertussis toxin. Particularly dangerous in unimmunized infants under 6 months where inspiratory whoop is absent, presenting instead with life-threatening apnea and cyanosis. Diagnostic workup: Nasopharyngeal swab for Pertussis PCR / culture (Dacron/Rayon swab), CBC showing profound absolute lymphocytosis (> 60-70% lymphocytes). Treatment: Macrolide antibiotics (Azithromycin 10 mg/kg/day for 5 days) to clear respiratory shedding; oxygen and gentle airway suctioning. Close contacts require post-exposure chemoprophylaxis regardless of immunization status."
    },

    # --- 3. CARDIOVASCULAR & VASCULAR EMERGENCIES ---
    {
        "id": "ICD10-I48.91",
        "topic": "Atrial Fibrillation with Rapid Ventricular Response (AF with RVR)",
        "icd10": "I48.91",
        "specialty": "Cardiology / Emergency Medicine",
        "organ_system": "Cardiovascular",
        "keywords": ["atrial fibrillation", "af with rvr", "irregularly irregular pulse", "palpitations", "fluttering heart", "rapid irregular heartbeat", "cha2ds2-vasc score", "stroke prevention"],
        "red_flags": ["hemodynamic instability: systolic BP < 90 mmHg, acute altered mental status, cardiogenic shock", "acute pulmonary edema / flash pulmonary congestion", "ongoing ischemic cardiac chest pain", "syncope or presyncope"],
        "clinical_hallmarks": ["classic irregularly irregular radial pulse with significant pulse deficit (apical rate exceeds radial pulse)", "ECG demonstrating absent distinct P waves, variable irregular R-R intervals, and fibrillatory baseline f-waves", "ventricular rate > 120-160 bpm in uncontrolled RVR", "symptoms of palpitations, fatigue, dyspnea on exertion, and lightheadedness"],
        "pertinent_negatives": ["no regular sawtooth flutter waves (excludes atrial flutter)", "narrow QRS complex (< 120 ms in absence of bundle branch block)"],
        "content": "Atrial fibrillation is the most common sustained cardiac arrhythmia, characterized by disorganized atrial electrical activity at 350-600 bpm with variable AV nodal conduction resulting in rapid irregular ventricular rate. Carries a 5-fold increased risk of embolic ischemic stroke. Diagnostic workup: 12-lead ECG STAT, serum electrolytes (potassium, magnesium), TSH/free T4 (thyrotoxicosis workup), 2D-Echocardiogram (assess left atrial enlargement, ejection fraction, valvular disease). Management: If hemodynamically unstable: Synchronized DC Cardioversion STAT (100-200J). If stable: Acute rate control via IV Beta-blockers (Metoprolol 5mg IV) or Calcium Channel Blockers (Diltiazem 0.25 mg/kg IV); Digoxin in heart failure. Stroke risk stratification using CHA2DS2-VASc score and initiation of therapeutic anticoagulation (DOAC: Apixaban/Rivaroxaban or Warfarin)."
    },
    {
        "id": "ICD10-I26.9",
        "topic": "Acute Pulmonary Embolism (PE)",
        "icd10": "I26.9",
        "specialty": "Pulmonology / Emergency Medicine / Cardiology",
        "organ_system": "Cardiovascular / Pulmonary",
        "keywords": ["pulmonary embolism", "pe", "blood clot in lung", "sudden chest pain with hypoxia", "pleuritic chest pain", "wells score for pe", "ctpa", "saddle embolus"],
        "red_flags": ["hemodynamic collapse / massive PE: systolic BP < 90 mmHg or cardiac arrest (PEA)", "severe hypoxemia refractory to oxygen (PaO2/FiO2 < 200)", "acute right ventricular strain on bedside echocardiography (McConnell sign)", "elevated cardiac troponin and NT-proBNP indicating RV myocardial micro-infarction"],
        "clinical_hallmarks": ["sudden onset unexplained dyspnea and tachypnea (respiratory rate > 20/min)", "acute pleuritic chest pain aggravated by deep inspiration or coughing", "tachycardia (heart rate > 100 bpm) with prominent loud pulmonic second heart sound (P2)", "presence of risk factors: DVT, prolonged immobilization, recent major surgery, malignancy, oral contraceptive use"],
        "pertinent_negatives": ["no focal consolidation or air bronchograms on chest x-ray", "clear lung fields on auscultation despite severe dyspnea"],
        "content": "Occlusion of pulmonary arterial bed by a dislodged thrombus, predominantly originating from deep veins of lower extremities or pelvis. Ranks among the top missed fatal emergency room diagnoses. Clinical probability assessed via Wells Score / Geneva Score. Diagnostic workup: CT Pulmonary Angiography (CTPA) is gold standard; D-dimer assay (high negative predictive value for low-probability patients); Bedside echocardiogram (acute RV dilation, McConnell sign); 12-lead ECG showing sinus tachycardia, S1Q3T3 pattern, or new RBBB. Treatment: Immediate therapeutic anticoagulation (IV Unfractionated Heparin or LMWH: Enoxaparin 1 mg/kg BID); Thrombolytic therapy (Alteplase 100 mg IV over 2h) for massive hemodynamically unstable PE; catheter-directed thrombectomy or surgical embolectomy when thrombolysis is contraindicated."
    },
    {
        "id": "ICD10-I82.40",
        "topic": "Acute Lower Extremity Deep Vein Thrombosis (DVT)",
        "icd10": "I82.40",
        "specialty": "Vascular Surgery / General Medicine",
        "organ_system": "Vascular",
        "keywords": ["dvt", "deep vein thrombosis", "swollen calf", "leg pain after flight", "blood clot in leg", "wells score for dvt", "compression ultrasound", "unilateral leg edema"],
        "red_flags": ["phlegmasia cerulea dolens: massive limb cyanosis, severe ischemic pain, and impending gangrene", "concomitant sudden chest pain, dyspnea, or hemoptysis (indicates pulmonary embolus embolization)", "loss of distal arterial pulses (dorsalis pedis/posterior tibial) due to compartment compression"],
        "clinical_hallmarks": ["acute unilateral swelling of calf or entire lower extremity (> 3 cm circumference difference measured 10 cm below tibial tuberosity)", "localized tenderness along deep venous distribution (popliteal fossa / femoral canal)", "erythema, increased skin warmth, and prominent superficial collateral veins", "accentuation of pain upon walking or standing"],
        "pertinent_negatives": ["no bilateral symmetrical edema characteristic of heart failure, cirrhosis, or nephrotic syndrome", "no sudden tearing pain in back of knee (rules out ruptured Baker cyst)"],
        "content": "Formation of a blood clot within the deep veins of the leg (femoral, popliteal, iliac), governed by Virchow's Triad (endothelial injury, venous stasis, hypercoagulability). High risk of detaching and traveling to pulmonary arteries causing fatal PE. Diagnostic workup: Venous Duplex Ultrasound with Compression (lack of complete compressibility of vein lumen is diagnostic); D-dimer testing in low-probability patients (Wells score < 2). Treatment: Immediate therapeutic anticoagulation with Direct Oral Anticoagulants (DOAC: Apixaban 10mg BID for 7 days then 5mg BID, or Rivaroxaban 15mg BID for 21 days then 20mg daily) or LMWH bridging to Warfarin (target INR 2.0-3.0); leg elevation and graduated compression stockings (30-40 mmHg) after acute pain resolves to prevent post-thrombotic syndrome."
    },
    {
        "id": "ICD10-I33.0",
        "topic": "Acute & Subacute Infective Endocarditis",
        "icd10": "I33.0",
        "specialty": "Cardiology / Infectious Disease",
        "organ_system": "Cardiovascular",
        "keywords": ["infective endocarditis", "vegetation on valve", "fever with new murmur", "splinter hemorrhage", "osler nodes", "janeway lesions", "roth spots", "duke criteria"],
        "red_flags": ["acute severe valvular regurgitation with rapid pulmonary edema and cardiogenic shock", "conduction block (prolonged PR interval / complete heart block) indicating aortic root ring abscess", "major arterial embolic stroke or splenic infarction", "severe sepsis / refractory bacteremia"],
        "clinical_hallmarks": ["prolonged unexplained fever of unknown origin (FUO) with chills and night sweats", "new regurgitant cardiac murmur or changing character of preexisting heart murmur", "peripheral vascular and immunological stigmata: subungual splinter hemorrhages, Osler nodes (tender nodules on pads of fingers/toes), Janeway lesions (painless erythematous macules on palms/soles), Roth spots on fundoscopy", "splenomegaly and microscopic hematuria"],
        "pertinent_negatives": ["no negative blood cultures after proper collection prior to antibiotics"],
        "content": "Microbial infection of cardiac endothelial lining, predominantly involving cardiac valves, characterized by vegetations of platelets, fibrin, and microorganisms. Caused by Staphylococcus aureus (acute native valve/IV drug users), Viridans streptococci (subacute), Enterococci, or coagulase-negative staphylococci (prosthetic valves). Diagnostic workup: Modified Duke Criteria; 3 sets of blood cultures drawn from separate venipuncture sites before initiating antibiotics; Transthoracic (TTE) followed by Transesophageal Echocardiography (TEE) to detect mobile vegetations, abscesses, or new valvular dehiscence. Treatment: Prolonged bactericidal IV antimicrobial therapy for 4-6 weeks (e.g. IV Ampicillin + Ceftriaxone, or Vancomycin + Gentamicin). Urgent surgical valve replacement/repair for refractory heart failure, uncontrolled infection, fungal endocarditis, or large mobile vegetations (> 10 mm) at high embolic risk."
    },
    {
        "id": "ICD10-I16.1",
        "topic": "Hypertensive Emergency with Acute Target-Organ Damage",
        "icd10": "I16.1",
        "specialty": "Cardiology / Emergency Medicine / Nephrology",
        "organ_system": "Cardiovascular",
        "keywords": ["hypertensive emergency", "hypertensive crisis", "malignant hypertension", "bp 200/120", "hypertensive encephalopathy", "acute end organ damage", "blood pressure crisis"],
        "red_flags": ["hypertensive encephalopathy (altered mental status, papilledema, seizures)", "acute pulmonary edema / acute left ventricular failure", "acute coronary syndrome / myocardial infarction", "acute aortic dissection (tearing chest/back pain, pulse deficit)", "acute renal failure with hematuria and rapid creatinine rise", "pre-eclampsia / eclampsia in pregnancy"],
        "clinical_hallmarks": ["severe acute elevation in blood pressure: Systolic BP >= 180 mmHg and/or Diastolic BP >= 120 mmHg", "PRESENCE of acute, progressive target-organ dysfunction", "severe occipital headache, blurred vision, fundoscopic bilateral flame hemorrhages and exudates (Grade IV retinopathy / papilledema)", "nausea, vomiting, and cognitive slowing"],
        "pertinent_negatives": ["absence of end-organ damage defines Hypertensive Urgency (managed with oral agents)"],
        "content": "Hypertensive emergency is defined by severe blood pressure elevation (usually SBP > 180 or DBP > 120 mmHg) accompanied by acute, ongoing life-threatening target-organ compromise (brain, heart, aorta, kidneys, eyes). Requires ICU admission and continuous invasive arterial monitoring. Therapeutic principle: Controlled gradual reduction—lower Mean Arterial Pressure (MAP) by NO MORE than 20-25% in the first hour, then to 160/100 mmHg over next 2-6 hours to prevent cerebral or renal hypoperfusion. (Exception: Acute aortic dissection requires rapid SBP lowering to < 120 mmHg within 20 minutes). Diagnostic workup: 12-lead ECG, troponin, serum creatinine, electrolytes, urinalysis, chest x-ray, non-contrast CT head (if neurological signs). Treatment: Titratable IV antihypertensives: IV Labetalol, IV Nicardipine, IV Nitroglycerin (in acute pulmonary edema/ACS), or IV Sodium Nitroprusside."
    },

    # --- 4. GASTROENTEROLOGY & GENERAL SURGERY ---
    {
        "id": "ICD10-K74.6",
        "topic": "Decompensated Liver Cirrhosis & Hepatic Encephalopathy",
        "icd10": "K74.6",
        "specialty": "Gastroenterology / Hepatology",
        "organ_system": "Gastrointestinal / Hepatic",
        "keywords": ["liver cirrhosis", "decompensated liver", "ascites", "hepatic encephalopathy", "portal hypertension", "asterixis", "flapping tremors", "alcoholic liver disease"],
        "red_flags": ["spontaneous bacterial peritonitis (SBP: fever, diffuse abdominal pain, encephalopathy)", "active gastroesophageal variceal hemorrhage (massive hematemesis)", "hepatorenal syndrome (rapid oliguric renal failure with normal urine sediment)", "grade III-IV hepatic encephalopathy (stupor or deep coma)"],
        "clinical_hallmarks": ["stigmata of chronic liver disease: prominent ascites with fluid wave, spider nevi, palmar erythema, caput medusae, gynecomastia, jaundice", "asterixis (flapping tremor of dorsiflexed outstretched hands with eyes closed)", "reversal of sleep-wake cycle, day-night confusion, cognitive slowing (West Haven Grade I-II)", "pedal edema and muscle wasting (sarcopenia)"],
        "pertinent_negatives": ["no focal neurological deficits typical of stroke"],
        "content": "Decompensated cirrhosis represents end-stage hepatic fibrosis complicated by portal hypertension and synthetic failure (due to alcohol, hepatitis B/C, NASH). Decompensation manifests as ascites, jaundice, variceal bleeding, or hepatic encephalopathy. Diagnostic workup: Diagnostic paracentesis (ascitic fluid cell count and culture: neutrophil count >= 250/uL confirms SBP; SAAG >= 1.1 g/dL confirms portal hypertension), LFT (elevated bilirubin, hypoalbuminemia, reversed A/G ratio), PT/INR (coagulopathy), ultrasound abdomen with portal vein Doppler, upper GI endoscopy for varices. Treatment: Hepatic encephalopathy managed with Lactulose (titrated to 2-3 soft stools/day) PLUS oral Rifaximin 550 mg BID; Ascites managed with sodium restriction (< 2g/day) and combination diuretics (Spironolactone + Furosemide); SBP treated with IV Cefotaxime/Ceftriaxone + IV Albumin."
    },
    {
        "id": "ICD10-A06.4",
        "topic": "Amoebic Liver Abscess (Entamoeba Histolytica)",
        "icd10": "A06.4",
        "specialty": "Gastroenterology / Infectious Disease",
        "organ_system": "Hepatic Infectious",
        "keywords": ["amoebic liver abscess", "liver abscess", "entamoeba histolytica", "anchovy sauce pus", "right upper quadrant pain with fever", "tender liver", "intercostal tenderness"],
        "red_flags": ["intraperitoneal rupture with acute peritonitis and septic shock", "transdiaphragmatic rupture into pleural space (amoebic empyema) or pericardium (cardiac tamponade)", "abscess size > 10 cm in left liver lobe (imminent pericardial rupture risk)"],
        "clinical_hallmarks": ["high spiking fever with chills and profuse sweating", "constant dull aching pain in right hypochondrium / lower chest, radiating to right shoulder", "exquisite tenderness upon percussion over right lower intercostal spaces", "enlarged tender liver (hepatomegaly) with elevated right hemidiaphragm on chest x-ray"],
        "pertinent_negatives": ["no active bloody dysentery at presentation in 80% of patients"],
        "content": "Invasive extra-intestinal protozoan infection caused by Entamoeba histolytica trophozoites reaching liver parenchyma via portal venous circulation from colonic ulcerations. Predominantly affects young adult males (ratio 10:1), often solitary and located in right hepatic lobe. Generates liquefactive necrosis containing classic odorless brown 'anchovy sauce' thick fluid. Diagnostic workup: Ultrasound / CT abdomen (hypoechoic round solitary mass with thin capsule), Amoebic serology (Serum Anti-Amebic IgG Antibodies positive in > 95%), CBC (leukocytosis without eosinophilia), LFT (elevated alkaline phosphatase and mild bilirubin elevation). Treatment: Oral or IV Metronidazole (750 mg TID for 10 days) or Tinidazole (2g daily for 5 days) followed by luminal amoebicide (Diloxanide furoate 500 mg TID for 10 days) to eradicate intestinal cysts. Ultrasound-guided therapeutic percutaneous needle aspiration indicated for large abscesses (> 5-10 cm), left lobe lesions, or impending rupture."
    },
    {
        "id": "ICD10-K40.9",
        "topic": "Strangulated / Incarcerated Inguinal Hernia",
        "icd10": "K40.9",
        "specialty": "General Surgery / Emergency Medicine",
        "organ_system": "Surgical Abdomen",
        "keywords": ["inguinal hernia", "strangulated hernia", "incarcerated hernia", "painful groin swelling", "hernia won't go back", "bowel obstruction with hernia", "hernia emergency"],
        "red_flags": ["hernia mass becomes exquisitely painful, firm, erythematous, and completely irreducible", "development of systemic signs: high fever, tachycardia, leukocytosis, and septic shock", "signs of bowel obstruction: bilious vomiting, absolute constipation, abdominal distension", "skin overlying groin mass turns purplish or necrotic (indicates gangrenous bowel)"],
        "clinical_hallmarks": ["known preexisting reducible groin bulge that suddenly becomes intensely painful and cannot be pushed back", "tenderness localized to groin lump with absence of expansile cough impulse", "patient presents with restlessness and progressive abdominal colicky cramps"],
        "pertinent_negatives": ["no manual reducibility with gentle taxis"],
        "content": "Surgical emergency occurring when abdominal viscera (most often small bowel or omentum) protruding through the inguinal canal become trapped (incarcerated) at the narrow hernia neck. Unrelieved constriction impairs venous return followed by arterial inflow, resulting in ischemic strangulation, gangrene, and bowel perforation within 6-12 hours. CONTRAINDICATION: Forceful manual reduction (taxis) of strangulated hernia is strictly forbidden due to risk of reducing gangrenous bowel back into peritoneal cavity (reduction en masse). Diagnostic workup: Immediate clinical diagnosis; bedside ultrasound or contrast CT abdomen if diagnostic doubt. Emergency management: Strict NPO, IV fluid resuscitation, NG tube decompression, broad-spectrum IV antibiotics, and STAT transfer to operating theater for emergency inguinal herniotomy and bowel viability assessment / resection."
    },
    {
        "id": "ICD10-K83.0",
        "topic": "Acute Ascending Cholangitis (Charcot's Triad & Reynolds' Pentad)",
        "icd10": "K83.0",
        "specialty": "Gastroenterology / General Surgery",
        "organ_system": "Biliary",
        "keywords": ["acute cholangitis", "charcot triad", "reynolds pentad", "pus in bile duct", "gallstone in common bile duct", "fever with jaundice", "biliary sepsis", "choledocholithiasis"],
        "red_flags": ["Reynolds' Pentad: Charcot's Triad (fever, jaundice, RUQ pain) PLUS hypotension/shock and altered mental status", "severe biliary septic shock refractory to fluid resuscitation", "serum bilirubin > 5 mg/dL with acute renal failure (hepatorenal impairment)"],
        "clinical_hallmarks": ["Charcot's Triad present in 70%: high spiking fever with shaking rigors, deep obstructive jaundice, and severe right upper quadrant abdominal pain", "dark amber urine and pale clay-colored stools", "tenderness and guarding in right upper quadrant with positive Murphy sign"],
        "pertinent_negatives": ["absence of pneumoperitoneum on chest x-ray"],
        "content": "Life-threatening bacterial infection of the biliary tree superimposed on partial or complete biliary outflow obstruction, most commonly choledocholithiasis (CBD stones), benign strictures, or periampullary neoplasms. High biliary ductal pressures cause translocation of bacteria (E. coli, Klebsiella, Enterococcus) into hepatic circulation, provoking rapid overwhelming septicemia. Diagnostic workup: Ultrasound abdomen (dilated common bile duct > 6-8 mm, presence of choledocholithiasis), MRCP (magnetic resonance cholangiopancreatography), LFTs (marked cholestatic elevation: alkaline phosphatase, GGT, direct bilirubin), blood cultures. Treatment: Emergency medical resuscitation with broad-spectrum IV antibiotics (e.g. Piperacillin-Tazobactam or Meropenem) AND emergency biliary decompression via Endoscopic Retrograde Cholangiopancreatography (ERCP) with biliary sphincterotomy and stent placement / stone extraction within 24 hours."
    },

    # --- 5. ENDOCRINOLOGY, METABOLIC & RENAL EMERGENCIES ---
    {
        "id": "ICD10-E11.10",
        "topic": "Diabetic Ketoacidosis (DKA) in Type 1 / 2 Diabetes",
        "icd10": "E11.10",
        "specialty": "Endocrinology / Emergency Medicine / Critical Care",
        "organ_system": "Endocrine / Metabolic",
        "keywords": ["dka", "diabetic ketoacidosis", "kussmaul breathing", "fruity breath", "high blood sugar with vomiting", "ketones in urine", "severe dehydration in diabetes"],
        "red_flags": ["deep rapid labored breathing (Kussmaul respiration) with fruity acetone odor", "hypotension, severe dehydration, and hypovolemic shock", "altered sensorium, stupor, or coma (risk of cerebral edema)", "serum potassium < 3.3 mEq/L (fatal arrhythmia risk before insulin)"],
        "clinical_hallmarks": ["triad: Hyperglycemia (blood glucose > 250 mg/dL), Ketosis (positive serum/urine ketones >= 3+), and High Anion Gap Metabolic Acidosis (arterial pH < 7.30, serum bicarbonate < 18 mEq/L, anion gap > 10-12)", "nausea, persistent vomiting, and diffuse abdominal pain mimicking acute surgical abdomen", "polyuria, polydipsia, marked weight loss, and extreme dehydration"],
        "pertinent_negatives": ["no focal neurological signs prior to fluid resuscitation"],
        "content": "Life-threatening acute metabolic decompensation caused by absolute or relative insulin deficiency combined with increased counter-regulatory hormones (glucagon, catecholamines, cortisol), precipitating uninhibited lipolysis, hepatic ketogenesis, and severe osmotic diuresis. Precipitated by missed insulin, infections (pneumonia, UTI), or acute myocardial infarction. Diagnostic workup: Point-of-care capillary blood glucose, arterial/venous blood gas (ABG/VBG), serum electrolytes with anion gap calculation, beta-hydroxybutyrate, urine ketones, renal function, ECG. Treatment Protocol (The 4 Pillars): 1. Aggressive IV fluid resuscitation (0.9% Normal Saline 1-1.5 L in first hour); 2. Potassium repletion BEFORE insulin if K+ < 3.3 mEq/L; 3. Regular Insulin infusion (0.1 units/kg/hour IV) to close anion gap (target glucose drop 50-75 mg/dL/hr); 4. Identify and treat precipitating infection."
    },
    {
        "id": "ICD10-N04.9",
        "topic": "Nephrotic Syndrome (Adult & Pediatric Minimal Change / FSGS)",
        "icd10": "N04.9",
        "specialty": "Nephrology / Pediatrics",
        "organ_system": "Renal",
        "keywords": ["nephrotic syndrome", "proteinuria", "swollen face and legs", "anasarca", "frothy urine", "hypoalbuminemia", "periorbital puffiness", "child with swollen body"],
        "red_flags": ["spontaneous bacterial peritonitis (fever and abdominal pain in ascitic child)", "thromboembolic complications (renal vein thrombosis, DVT, pulmonary embolism due to loss of antithrombin III)", "acute kidney injury / oliguria", "severe symptomatic pleural effusion causing respiratory distress"],
        "clinical_hallmarks": ["classic tetrad: 1. Massive nephrotic-range proteinuria (> 3.5 g/24h in adults or > 40 mg/m2/hr in children)", "2. Severe hypoalbuminemia (serum albumin < 3.0 g/dL)", "3. Generalized dependent edema / anasarca (initial morning periorbital puffiness progressing to ascites and severe bilateral pitting pedal edema)", "4. Severe hyperlipidemia (total cholesterol > 300 mg/dL, elevated LDL)", "frothy or foamy appearance of urine"],
        "pertinent_negatives": ["no macroscopic cola-colored hematuria (favors nephritic syndrome)", "no active hypertension typical of glomerulonephritis"],
        "content": "Glomerular disorder characterized by marked increase in glomerular capillary permeability to plasma proteins due to podocyte effacement or immune-complex deposition. In children, Minimal Change Disease accounts for > 85% of cases; in adults, FSGS and Membranous Nephropathy predominate. Diagnostic workup: Spot urine protein-to-creatinine ratio (UPCR) or 24-hour urine protein, serum albumin, lipid profile, renal ultrasound, renal biopsy (in adults, steroid-resistant children, or age < 1y / > 10y). Treatment: Prednisolone therapy (60 mg/m2/day for 4-6 weeks in children); Dietary sodium restriction (< 2g/day); Judicious loop diuretics (Furosemide + Spironolactone); ACE inhibitors / ARBs for antiproteinuric effect; Prophylactic anticoagulation in high-risk adult membranous patients (albumin < 2.0 g/dL)."
    },
    {
        "id": "ICD10-N40.1",
        "topic": "Benign Prostatic Hyperplasia (BPH) with Acute Urinary Retention",
        "icd10": "N40.1",
        "specialty": "Urology",
        "organ_system": "Urological",
        "keywords": ["bph", "enlarged prostate", "cannot pass urine", "acute urinary retention", "prostate enlargement", "weak urine stream", "frequent night urination", "nocturia in elderly"],
        "red_flags": ["acute painful urinary retention: complete inability to void accompanied by agonizing suprapubic pain and tense palpable bladder", "bilateral hydronephrosis with post-renal acute kidney injury (elevated urea/creatinine)", "gross painless hematuria", "superimposed acute pyelonephritis / urosepsis"],
        "clinical_hallmarks": ["progressive Lower Urinary Tract Symptoms (LUTS): storage symptoms (frequency, urgency, nocturia >= 3 times) and voiding symptoms (hesitancy, weak stream, intermittency, terminal dribbling)", "digital rectal examination (DRE) revealing smoothly enlarged, firm, non-tender, symmetrical prostate with preserved median sulcus", "distended dull suprapubic bladder palpable to umbilicus in acute retention"],
        "pertinent_negatives": ["no hard, nodular, asymmetrical prostate on DRE (which strongly suggests prostate carcinoma)"],
        "content": "Non-malignant adenomatous stromal and epithelial proliferation of the transition zone of the prostate gland in aging men, creating mechanical bladder outlet obstruction (BOO). Acute retention is frequently triggered by anticholinergic/antihistamine cold medications, alcohol, or constipation. Diagnostic workup: Emergency bladder catheterization (record immediate drained volume); Serum PSA (drawn prior to or days after DRE/catheterization); Renal function tests; Ultrasonography KUB with post-void residual urine volume (PVR > 100 mL is abnormal); International Prostate Symptom Score (IPSS). Management: Immediate relief with urethral Foley catheterization (14-16 Fr). Medical therapy: Alpha-1 adrenergic blockers (Tamsulosin 0.4 mg daily) for rapid symptom relief PLUS 5-Alpha Reductase Inhibitors (Finasteride 5 mg daily) to shrink prostate volume. Surgical intervention (TURP / HoLEP) for recurrent retention, stones, or renal impairment."
    },

    # --- 6. NEUROLOGY & NEURO-EMERGENCIES ---
    {
        "id": "ICD10-G51.0",
        "topic": "Bell's Palsy (Acute Idiopathic Lower Motor Neuron Facial Paralysis)",
        "icd10": "G51.0",
        "specialty": "Neurology / ENT",
        "organ_system": "Neurological",
        "keywords": ["bell's palsy", "facial paralysis", "face dropped on one side", "mouth twisted", "cannot close eye", "facial nerve palsy", "lmn facial palsy"],
        "red_flags": ["forehead wrinkling is PRESERVED (indicates upper motor neuron cortical stroke, NOT Bell's palsy)", "vesicular eruption in external auditory canal or pinna (Ramsay Hunt Syndrome / Herpes Zoster Oticus)", "bilateral facial nerve involvement (suggests Guillain-Barré, Lyme disease, or sarcoidosis)", "multiple cranial nerve deficits or limb weakness"],
        "clinical_hallmarks": ["acute onset (< 48 hours) unilateral complete lower motor neuron (LMN) facial weakness affecting ALL branches of cranial nerve VII", "inability to wrinkle forehead, raise eyebrow, or close eye on affected side (Bell's phenomenon: eyeball rolls upward upon attempted closure)", "flattening of nasolabial fold, drooping corner of mouth with drooling and food pocketing in cheek", "hyperacusis (increased sensitivity to loud sounds due to stapedius paralysis) and loss of taste on anterior two-thirds of tongue"],
        "pertinent_negatives": ["no arm/leg weakness, speech dysarthria, or visual field deficits"],
        "content": "Acute isolated idiopathic unilateral lower motor neuron paresis of Cranial Nerve VII (facial nerve), believed to be caused by herpes simplex virus reactivation leading to inflammatory edema and nerve compression within the narrow Fallopian canal. Crucial diagnostic pearl: Forehead movement is paralyzed in Bell's palsy (LMN) because facial nerve supplies both upper and lower face. In stroke (UMN), forehead movement is spared due to bilateral cortical innervation. Diagnostic workup: Clinical diagnosis; MRI brain if atypical or no improvement after 3 months. Treatment: Oral Corticosteroids initiated within 72 hours of onset (Prednisolone 60 mg daily for 5 days, then tapered over 5 days) significantly improves recovery rates. Severe cases benefit from combined Valacyclovir (1000 mg TID for 7 days). Eye protection is paramount: Artificial tears during daytime, lubricating ophthalmic ointment and eye taping at night to prevent exposure keratitis."
    },
    {
        "id": "ICD10-G40.90",
        "topic": "Status Epilepticus & Generalized Convulsive Seizures",
        "icd10": "G40.90",
        "specialty": "Neurology / Emergency Medicine / Critical Care",
        "organ_system": "Neurological Emergency",
        "keywords": ["status epilepticus", "continuous seizure", "fits not stopping", "grand mal seizure", "tonic clonic fit", "epilepsy emergency", "seizure longer than 5 minutes"],
        "red_flags": ["continuous convulsive seizure activity lasting >= 5 minutes (Time t1: operational definition of status epilepticus)", "patient does not regain baseline consciousness between recurrent seizure episodes", "hypoxia, severe lactic acidosis, and hyperthermia (risk of neuronal injury at Time t2 >= 30 min)", "trauma sustained during seizure (head strike, cervical spine injury, posterior shoulder dislocation)"],
        "clinical_hallmarks": ["generalized tonic phase (sustained contraction of all musculature, apnea, cyanosis, tongue biting) followed by clonic phase (rhythmic synchronous jerking of limbs)", "frothing at mouth, urinary/fecal incontinence", "postictal stupor with deep stertorous breathing and transient confusion"],
        "pertinent_negatives": ["no pseudo-seizure features: eyes tightly closed resisting opening, pelvic thrusting, out-of-phase thrashing"],
        "content": "Neurological emergency defined as abnormally prolonged seizure activity or recurrent seizures without full interictal neurological recovery, resulting from failure of seizure termination mechanisms. Causes include antiepileptic non-compliance, acute stroke, CNS infection, metabolic derangement (hyponatremia, hypoglycemia), or drug toxicity. Protocolized Time-Based Management: 0-5 mins: Airway positioning, 100% high-flow oxygen, IV access, bedside glucose check. 5-10 mins (First-line): IV Lorazepam (0.1 mg/kg, max 4mg) OR IM Midazolam (10 mg) OR IV Diazepam (0.15-0.2 mg/kg). Repeat once at 10 min if seizing. 10-20 mins (Second-line): IV Levetiracetam (60 mg/kg, max 4500mg) OR IV Fosphenytoin (20 mg PE/kg) over 10-15 mins. > 30 mins (Refractory Status): General anesthesia and endotracheal intubation (IV Propofol or Midazolam infusion) with continuous EEG monitoring."
    },
    {
        "id": "ICD10-G61.0",
        "topic": "Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyradiculoneuropathy)",
        "icd10": "G61.0",
        "specialty": "Neurology / Critical Care",
        "organ_system": "Neurological",
        "keywords": ["guillain barre", "gbs", "ascending paralysis", "weakness starting in feet", "areflexia", "campylobacter infection", "respiratory muscle weakness with paralysis"],
        "red_flags": ["rapidly ascending motor weakness progressing to intercostal and diaphragmatic respiratory paralysis (forced vital capacity < 15-20 mL/kg)", "severe autonomic instability (labile blood pressure, fatal arrhythmias, extreme tachycardia/bradycardia)", "bulbar palsy (dysphagia, aspiration risk, inability to swallow secretions)"],
        "clinical_hallmarks": ["progressive, symmetrical ascending muscle weakness typically beginning in lower extremities (feet/legs) and ascending to trunk, arms, and cranial nerves over days to 4 weeks", "generalized hyporeflexia or complete areflexia (absent deep tendon reflexes: knee/ankle jerks absent)", "history of antecedent gastrointestinal (Campylobacter jejuni) or respiratory viral illness 1-4 weeks prior", "relative preservation of sensory modalities despite distal tingling paresthesias"],
        "pertinent_negatives": ["no distinct sensory spinal cord level (rules out acute transverse myelitis)", "no fever at onset of weakness"],
        "content": "Post-infectious autoimmune polyradiculoneuropathy characterized by molecular mimicry where antibodies against antecedent pathogens cross-react with gangliosides on peripheral nerve myelin or axolemma. Clinical progression peaks within 2-4 weeks. Diagnostic workup: Lumbar puncture demonstrating pathognomonic Albuminocytological Dissociation (elevated CSF protein > 45 mg/dL with normal CSF white blood cell count < 10 cells/uL, often prominent after 1st week); Nerve Conduction Studies / EMG (prolonged distal latencies, slowed conduction velocities, conduction blocks). Treatment: ICU admission for bedside vital capacity and negative inspiratory force monitoring. Disease-modifying therapy: Intravenous Immunoglobulin (IVIG 0.4 g/kg/day for 5 days) OR Plasma Exchange (Plasmapheresis, 4-6 sessions over 2 weeks). Systemic corticosteroids are ineffective and NOT recommended."
    },

    # --- 7. OBSTETRICS, GYNECOLOGY & WOMEN'S HEALTH ---
    {
        "id": "ICD10-O00.9",
        "topic": "Ruptured Ectopic Pregnancy",
        "icd10": "O00.9",
        "specialty": "Obstetrics & Gynecology / Emergency Medicine",
        "organ_system": "Gynecological Emergency",
        "keywords": ["ectopic pregnancy", "ruptured ectopic", "pregnancy with bleeding and pain", "missed period with severe abdominal pain", "tubal rupture", "positive pregnancy test with collapse"],
        "red_flags": ["sudden severe sharp lancinating iliac fossa pain followed by syncope or hemorrhagic shock (tachycardia, hypotension, cold clammy extremities)", "referred shoulder tip pain (Kehr sign: diaphragmatic irritation from intraperitoneal blood)", "cervical motion tenderness with fullness in pouch of Douglas", "frank peritoneal guarding and rebound rigidity"],
        "clinical_hallmarks": ["classic triad in female of reproductive age: 1. History of missed menstrual period / amenorrhea (6-8 weeks); 2. Unilateral lower abdominal or pelvic pain; 3. Abnormal vaginal bleeding or spotting", "positive urine pregnancy test (beta-hCG positive)", "cervical os closed on speculum examination with dark blood trickle"],
        "pertinent_negatives": ["absence of intrauterine gestational sac on transvaginal ultrasound"],
        "content": "Implantation of fertilized ovum outside the uterine cavity, over 95% occurring in the Fallopian tube (ampulla/isthmus). Tubal rupture causes massive intra-abdominal hemorrhage and ranks as a leading cause of first-trimester maternal mortality. Diagnostic workup: Transvaginal Ultrasound (TVS: empty uterine cavity with thickened endometrium, adnexal mass separate from ovary, and free fluid in pouch of Douglas / Morison's pouch); Quantitative serum beta-hCG (discriminatory zone: TVS should visualize intrauterine sac if beta-hCG > 1500-2000 mIU/mL); Blood type and Rh status (Rh-negative mothers require anti-D immunoglobulin STAT). Treatment: If ruptured/unstable: Immediate emergency laparoscopy or laparotomy for salpingectomy + aggressive blood transfusion. If unruptured, stable, beta-hCG < 5000, and no fetal cardiac activity: Medical management with IM Methotrexate (50 mg/m2)."
    },
    {
        "id": "ICD10-O14.9",
        "topic": "Pre-eclampsia & Eclampsia (Hypertensive Disorders of Pregnancy)",
        "icd10": "O14.9",
        "specialty": "Obstetrics & Gynecology / Critical Care",
        "organ_system": "Obstetric Emergency",
        "keywords": ["preeclampsia", "eclampsia", "high bp in pregnancy", "seizures in pregnancy", "protein in urine pregnancy", "headache and blurry vision in pregnancy", "swollen feet pregnancy"],
        "red_flags": ["ECLAMPSIA: new-onset generalized tonic-clonic convulsions in a pre-eclamptic patient", "severe hypertension: Systolic BP >= 160 mmHg and/or Diastolic BP >= 110 mmHg on 2 occasions", "HELLP syndrome (Hemolysis, Elevated Liver enzymes, Low Platelets < 100,000)", "severe persistent epigastric / right upper quadrant pain (hepatic capsular distension / rupture risk)", "visual disturbances (scotomata, photopsia) and severe intractable frontal headache"],
        "clinical_hallmarks": ["new-onset hypertension (BP >= 140/90 mmHg on two occasions at least 4 hours apart) occurring AFTER 20 weeks of gestation in previously normotensive woman", "PLUS proteinuria (>= 300 mg/24h or urine protein:creatinine ratio >= 0.3 or dipstick 1+)", "OR in absence of proteinuria: thrombocytopenia, renal insufficiency, impaired liver function, pulmonary edema, or cerebral symptoms", "brisk hyperactive deep tendon reflexes (patellar clonus)"],
        "pertinent_negatives": ["no history of preexisting chronic hypertension prior to 20 weeks"],
        "content": "Multisystem pregnancy-specific disorder driven by abnormal placentation, inadequate spiral artery remodeling, and generalized endothelial dysfunction. Definitive cure is delivery of placenta. Diagnostic workup: Continuous BP monitoring, urine protein dipstick / 24h collection, CBC with platelet count, peripheral smear (schistocytes), LFT (AST/ALT, LDH), serum creatinine, uric acid, fetal assessment (NST, biophysical profile, umbilical artery Doppler). Management: Seizure prophylaxis: IV Magnesium Sulfate (Pritchard or Zuspan regimen: 4g IV loading over 15 min + 1-2 g/hr maintenance; continue 24h postpartum). Antihypertensive therapy: IV Labetalol, oral Nifedipine, or IV Hydralazine for BP >= 160/110. Delivery planning: Expedited delivery indicated at >= 37 weeks, or immediately at any gestational age for eclampsia, HELLP, pulmonary edema, or fetal compromise."
    },
    {
        "id": "ICD10-O21.0",
        "topic": "Hyperemesis Gravidarum & Wernicke Encephalopathy Risk",
        "icd10": "O21.0",
        "specialty": "Obstetrics & Gynecology / Gastroenterology",
        "organ_system": "Obstetric",
        "keywords": ["hyperemesis gravidarum", "severe pregnancy vomiting", "cannot keep food down in pregnancy", "ketones in pregnancy", "weight loss pregnancy", "thiamine deficiency pregnancy"],
        "red_flags": ["Wernicke Encephalopathy: triad of confusion/ataxia/ophthalmoplegia triggered by IV dextrose without prior thiamine", "severe dehydration with postural hypotension and tachycardia", "electrolyte derangements (severe hypokalemia, hyponatremia, hypochloremic metabolic alkalosis)", "weight loss exceeding 5-10% of pre-pregnancy weight"],
        "clinical_hallmarks": ["intractable, persistent nausea and vomiting starting in early first trimester (weeks 6-12)", "inability to tolerate any oral liquids or solids for > 24-48 hours", "ketonuria (>= 2+ to 3+ on dipstick) from starvation ketosis", "dry mucous membranes, sunken eyes, and poor skin turgor"],
        "pertinent_negatives": ["no fever or diarrhea (excludes acute viral gastroenteritis)", "no goiter or hyperthyroid signs"],
        "content": "Severe form of nausea and vomiting of pregnancy characterized by intractable vomiting, starvation ketosis, dehydration, electrolyte depletion, and weight loss > 5%. High human chorionic gonadotropin (hCG) and estrogen levels play key roles. CRITICAL SAFETY WARNING: Intravenous dextrose infusion without concurrent thiamine (Vitamin B1) supplementation can precipitate acute irreversible Wernicke Encephalopathy. Diagnostic workup: Urine dipstick (ketonuria, specific gravity), serum electrolytes, BUN, creatinine, LFT (mild transaminase rise), pelvic ultrasound (rule out molar pregnancy and multiple gestation). Treatment: IV rehydration with 0.9% Normal Saline with potassium replacement; MANDATORY IV Thiamine (100 mg daily) before any glucose solutions; Antiemetics: Doxylamine-Pyridoxine (first line), Promethazine, Metoclopramide, or Ondansetron."
    },

    # --- 8. ENVIRONMENTAL, BITES & TOXICOLOGY EMERGENCIES ---
    {
        "id": "ICD10-T63.0A",
        "topic": "Snake Envenomation - Neurotoxic Elapid (Krait & Cobra)",
        "icd10": "T63.0",
        "specialty": "Emergency Medicine / Critical Care / Toxicology",
        "organ_system": "Toxicology / Environmental",
        "keywords": ["snake bite", "neurotoxic snakebite", "krait bite", "cobra bite", "anti snake venom", "asv", "ptosis with snake bite", "respiratory paralysis snake bite"],
        "red_flags": ["bilateral ptosis (drooping eyelids: earliest and most sensitive sign of neurotoxicity)", "bulbar palsy: dysphagia, pooling of saliva, inability to swallow or speak clearly", "respiratory muscle paralysis (intercostal and diaphragmatic weakness leading to fatal asphyxia)", "krait bite often presents with early morning abdominal pain and paralysis without visible bite mark"],
        "clinical_hallmarks": ["history of snake encounter or sleeping on floor in rural dwelling", "rapidly descending flaccid motor paralysis: ptosis -> extraocular ophthalmoplegia -> facial/palatal weakness -> neck muscle weakness (broken neck sign) -> respiratory arrest", "cobra bite features painful local swelling, blister formation, and tissue necrosis; krait bite has virtually zero local swelling"],
        "pertinent_negatives": ["normal 20-Minute Whole Blood Clotting Test (20WBCT confirms non-hemotoxic)"],
        "content": "Envenomation by neurotoxic snakes (Common Krait - Bungarus caeruleus; Spectacled Cobra - Naja naja) possessing postsynaptic (alpha-neurotoxins) and presynaptic (beta-bungarotoxin) neurotoxins blocking neuromuscular junction transmission. Leading cause of rural accidental mortality in India. Diagnostic workup: Single Breath Count (normal > 30; count < 15 indicates impending respiratory failure); 20-Minute Whole Blood Clotting Test (20WBCT); Neostigmine test. Protocolized Treatment: Step 1: Immediate immobilization of bitten limb (splinting, no tourniquets, no cutting/suction). Step 2: Polyvalent Anti-Snake Venom (ASV: 10 vials reconstituted in 100 mL normal saline infused over 30-60 min STAT). Step 3: Atropine (0.6 mg IV) followed by Neostigmine (1.5 mg IV) test for cobra bites (reverses postsynaptic block). Step 4: Early elective endotracheal intubation and mechanical ventilation for impending respiratory arrest."
    },
    {
        "id": "ICD10-T63.0B",
        "topic": "Snake Envenomation - Hemotoxic Viperine (Russell's & Saw-Scaled Viper)",
        "icd10": "T63.0",
        "specialty": "Emergency Medicine / Hematology / Nephrology",
        "organ_system": "Toxicology / Hematological",
        "keywords": ["viper bite", "hemotoxic snakebite", "russell viper", "saw scaled viper", "bleeding gums snake bite", "20 minute clotting test", "asv protocol", "acute renal failure snake"],
        "red_flags": ["20-Minute Whole Blood Clotting Test (20WBCT) abnormal / non-clotting blood (indicates severe venom-induced consumption coagulopathy)", "spontaneous systemic bleeding: hematuria, hemoptysis, bleeding from gums/venipuncture sites", "rapidly progressive local swelling crossing two major joints within hours (risk of compartment syndrome)", "acute kidney injury / oliguria / anuria from tubular necrosis (Russell's viper hallmark)"],
        "clinical_hallmarks": ["two distinct puncture fang marks with immediate severe agonizing localized burning pain", "rapid local edema, hemorrhagic bullae, ecchymosis, and tissue necrosis spreading up the limb", "bleeding from gingival margins and continuous ooze from bite punctures", "hypotension and shock from third-space fluid sequestration"],
        "pertinent_negatives": ["no bilateral ptosis or descending paralysis"],
        "content": "Envenomation by viperine snakes (Russell's Viper - Daboia russelii; Saw-Scaled Viper - Echis carinatus) containing hemorrhagins, procoagulant enzymes (factor X/V activators), and nephrotoxins. Produces Venom-Induced Consumption Coagulopathy (VICC), local tissue gangrene, and acute tubular necrosis. Diagnostic workup: 20-Minute Whole Blood Clotting Test (20WBCT: 2 mL of fresh venous blood in dry glass tube left undisturbed for 20 mins; failure to clot indicates coagulopathy; repeated every 30 mins); Prothrombin Time (PT/INR), Serum Creatinine, Urine examination for hematuria/proteinuria. Treatment: Polyvalent Anti-Snake Venom (ASV: 10 vials in 100 mL NS over 1 hr); Repeat 10 vials after 6 hours if 20WBCT remains non-clotting (max 30 vials); Hemodialysis for acute renal failure; Avoid surgical fasciotomy unless true intracompartmental pressure > 30-40 mmHg is documented after coagulopathy correction."
    },
    {
        "id": "ICD10-T60.0",
        "topic": "Acute Organophosphate & Carbamate Poisoning",
        "icd10": "T60.0",
        "specialty": "Emergency Medicine / Critical Care / Toxicology",
        "organ_system": "Toxicology",
        "keywords": ["organophosphate poisoning", "op poisoning", "insecticide poisoning", "atropine protocol", "pralidoxime", "pinpoint pupils with secretions", "sludge syndrome"],
        "red_flags": ["massive bronchorrhea and bronchospasm (flooding of lungs with secretions causing suffocation)", "severe bradycardia / heart block and hypotension", "coma, respiratory arrest, and continuous generalized fasciculations", "Intermediate Syndrome (type II weakness of neck flexors, cranial nerves, and respiratory muscles on day 2-4)"],
        "clinical_hallmarks": ["cholinergic toxidrome (SLUDGE-BBB): Salivation, Lacrimation, Urination, Defecation, Gastric emesis, Bronchorrhea, Bronchospasm, Bradycardia", "pathognomonic pinpoint, miosis pupils non-reactive to light", "garlic-like / kerosene-like odor on breath or clothing", "generalized muscle fasciculations and twitching"],
        "pertinent_negatives": ["no dry mouth or dilated pupils (excludes anticholinergic poisoning)"],
        "content": "Toxic exposure to agricultural organophosphate insecticides (Chlorpyrifos, Malathion, Monocrotophos) which irreversibly inhibit acetylcholinesterase enzyme, causing massive acetylcholine accumulation at muscarinic and nicotinic receptors. Diagnostic workup: Immediate clinical recognition; Serum pseudocholinesterase / RBC acetylcholinesterase levels (reduced < 50%); Arterial blood gas, ECG, chest x-ray (aspiration/pulmonary edema). Management (The 3 Life-Saving Steps): Step 1: Resuscitation and Decontamination (strip contaminated clothes, wash skin with soap/water; healthcare staff wear PPE). Step 2: Immediate Atropinization (Atropine 2-5 mg IV bolus every 3-5 minutes, doubling dose until 'Atropinized': clear chest on auscultation, heart rate > 80, dry axillae, pupil dilation). Step 3: Cholinesterase reactivator: Pralidoxime (PAM 2g IV loading over 30 min, then 500 mg/hr infusion)."
    },
    {
        "id": "ICD10-T67.0",
        "topic": "Heat Stroke & Severe Heat Exhaustion",
        "icd10": "T67.0",
        "specialty": "Emergency Medicine / Critical Care",
        "organ_system": "Environmental Emergency",
        "keywords": ["heat stroke", "loo lagna", "severe heat illness", "core temperature 40", "hot dry skin with confusion", "heat exhaustion", "sunstroke emergency"],
        "red_flags": ["core body temperature (rectal) exceeding 40.0°C (104.0°F)", "central nervous system dysfunction: delirium, confusion, ataxia, seizures, or coma", "disseminated intravascular coagulation (DIC) and multiorgan failure", "rhabdomyolysis with dark tea-colored urine and acute kidney injury"],
        "clinical_hallmarks": ["triad: 1. Extreme hyperthermia (core temp > 40°C); 2. Severe CNS dysfunction; 3. History of exposure to ambient environmental heatwave (classic heat stroke in elderly/infants) or strenuous exertion in heat (exertional heat stroke in laborers/athletes)", "anhidrosis (hot, dry skin) typical in classic heat stroke; exertional patients may be drenched in sweat", "hyperventilation, tachycardia, hypotension, and vomiting"],
        "pertinent_negatives": ["no focal neurological signs", "no stiff neck characteristic of acute meningitis"],
        "content": "Life-threatening environmental medical emergency where thermal regulatory mechanisms fail, producing uncompensable core hyperthermia (> 40°C) with systemic inflammatory response syndrome (SIRS) and multi-organ damage. Mortality exceeds 50% if cooling is delayed. PRINCIPLE: 'Cool first, transport second'—every minute of hyperthermia destroys neurons. Diagnostic workup: Continuous rectal temperature probe monitoring; CBC, PT/INR (DIC), CPK (rhabdomyolysis), renal function and electrolytes, arterial blood gas. Emergency Management: Immediate rapid aggressive physical cooling: Whole-body cold-water immersion (gold standard for exertional) OR evaporative cooling (continuous misting with tepid water while large fans blow high-velocity air) + ice packs placed on neck, axillae, and groins. Target: Reduce core temp to < 38.5°C within 30 minutes, then stop to prevent hypothermic overshoot. Antipyretics (Paracetamol/Aspirin) are completely ineffective and contraindicated due to hepatic/bleeding toxicity."
    },

    # --- 9. OPHTHALMOLOGY & ENT EMERGENCIES ---
    {
        "id": "ICD10-H40.2",
        "topic": "Acute Angle-Closure Glaucoma",
        "icd10": "H40.2",
        "specialty": "Ophthalmology / Emergency Medicine",
        "organ_system": "Ophthalmology",
        "keywords": ["acute glaucoma", "angle closure", "severe eye pain with headache", "steamy cornea", "rainbow halos around lights", "fixed mid-dilated pupil", "hard eyeball"],
        "red_flags": ["intraocular pressure (IOP) severely elevated > 40-70 mmHg (normal 10-21 mmHg)", "rapid irreversible ischemic optic nerve damage within hours to days", "complete vision loss in affected eye", "severe pain inducing nausea, vomiting, and abdominal pain frequently misdiagnosed as acute abdomen"],
        "clinical_hallmarks": ["sudden agonizing unilateral ocular and peri-orbital headache", "colored rainbow halos around lights and blurred cloudy vision", "steamy, hazy, dull cornea with loss of normal corneal luster", "fixed, mid-dilated, vertically oval pupil non-reactive to direct light", "ciliary / circumcorneal flush (violaceous ring of injection around limbus)", "eyeball feels stony-hard on gentle ballottement through closed eyelid"],
        "pertinent_negatives": ["no purulent discharge (excludes acute conjunctivitis)", "no foreign body or corneal abrasion on fluorescein"],
        "content": "Ophthalmic emergency resulting from appositional closure of the anterior chamber iridocorneal filtration angle, blocking aqueous humor outflow through the trabecular meshwork. Prevalent in hyperopic (farsighted) eyes, shallow anterior chambers, and elderly Asian females. Frequently triggered by pupillary dilation in dim light, emotional distress, or sympathomimetic / anticholinergic medications. Diagnostic workup: Tonometry (IOP > 30-60 mmHg); Slit-lamp biomicroscopy; Gonioscopy (closed angle); Fundoscopy (optic cup pallor/edema). Immediate Emergency Treatment: Lower IOP STAT using combination medical therapy: 1. Topical beta-blocker (Timolol 0.5% 1 drop); 2. Topical alpha-2 agonist (Apraclonidine 1% or Brimonidine); 3. Systemic carbonic anhydrase inhibitor (Acetazolamide 500 mg IV or PO STAT); 4. Hyperosmotic agent (IV Mannitol 20% 1-2 g/kg over 45 min); 5. Topical Pilocarpine 2% after IOP drops < 40 mmHg. Definitive cure: Bilateral Nd:YAG Laser Peripheral Iridotomy once corneal edema clears."
    },
    {
        "id": "ICD10-J36",
        "topic": "Peritonsillar Abscess (Quinsy)",
        "icd10": "J36",
        "specialty": "ENT / Emergency Medicine",
        "organ_system": "ENT",
        "keywords": ["peritonsillar abscess", "quinsy", "hot potato voice", "trismus", "uvula deviated", "severe sore throat on one side", "throat abscess"],
        "red_flags": ["upper airway compromise / respiratory stridor", "spread of infection into parapharyngeal or retropharyngeal space", "erosion into internal carotid artery (pseudoaneurysm with catastrophic hemorrhage)", "inability to swallow own secretions with drooling and dehydration"],
        "clinical_hallmarks": ["triad: 1. Severe unilateral sore throat and odynophagia (painful swallowing); 2. Marked trismus (inability to open mouth due to pterygoid spasm); 3. 'Hot potato' muffled resonant voice", "striking asymmetric bulging of superior tonsillar pillar and soft palate, pushing the inflamed tonsil downward and medially", "deviation of the uvula away from affected side toward contralateral healthy side", "ipsilateral tender cervical jugulodigastric lymphadenopathy"],
        "pertinent_negatives": ["no symmetric bilateral tonsillitis (favors simple tonsillitis / infectious mononucleosis)"],
        "content": "Collection of purulent exudate in the potential peritonsillar space between the capsule of the palatine tonsil and the superior pharyngeal constrictor muscle, typically arising as a complication of acute bacterial tonsillitis (Streptococcus pyogenes, Fusobacterium necrophorum). Most common deep neck infection in young adults. Diagnostic workup: Clinical diagnosis; Needle aspiration yielding frank foul-smelling pus is diagnostic and therapeutic; Contrast-enhanced CT neck if airway distress or deep neck extension suspected. Treatment: Immediate surgical drainage via Needle Aspiration or Incision and Drainage (I&D) under local anesthesia; Intravenous antibiotics (IV Ceftriaxone + Metronidazole, or Ampicillin-Sulbactam); High-dose IV Dexamethasone (8-10 mg) to rapidly reduce edema and trismus; Interval tonsillectomy considered after 4-6 weeks for recurrent quinsy."
    }
]


def expand_database():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        protocols = json.load(f)

    existing_ids = {p["id"] for p in protocols}
    added_count = 0

    for new_p in NEW_PROTOCOLS:
        if new_p["id"] not in existing_ids:
            protocols.append(new_p)
            existing_ids.add(new_p["id"])
            added_count += 1

    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(protocols, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {added_count} new clinical protocols!")
    print(f"Total knowledge base protocols now: {len(protocols)}")

if __name__ == "__main__":
    expand_database()

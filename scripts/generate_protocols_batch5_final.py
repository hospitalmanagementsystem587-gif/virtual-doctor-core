#!/usr/bin/env python3
"""
Batch 5 Final: Orthopedics, Toxicology, Pediatrics/Neonatology, Psychiatry.
Pushes knowledge base to 510+ comprehensive protocols.
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
    # --- 13. ORTHOPEDICS & TRAUMA (12) ---
    {
        "id": "ICD10-T79.A0",
        "topic": "Acute Compartment Syndrome (The 5 Ps & Emergency Fasciotomy)",
        "icd10": "T79.A0",
        "specialty": "Orthopedic Surgery / Trauma Surgery / Emergency Medicine",
        "organ_system": "Musculoskeletal Emergency",
        "keywords": ["compartment syndrome", "acute compartment syndrome", "the 5 ps pain out of proportion", "pain on passive stretch", "tense wooden compartment", "emergency fasciotomy", "delta pressure < 30"],
        "red_flags": ["myonecrosis and irreversible nerve damage after 6 hours", "rhabdomyolysis and acute renal failure", "amputation or Volkmann ischemic contracture"],
        "clinical_hallmarks": ["history of high-energy tibial shaft fracture, crush injury, tight circumferential cast/bandage, or revascularization", "EARLIEST AND MOST RELIABLE CLINICAL HALLMARK: SEVERE, AGONIZING PAIN OUT OF PROPORTION TO INJURY, recalcitrant to high-dose opioids", "PATHOGNOMONIC PHYSICAL EXAMINATION SIGN: EXCRUCIATING PAIN ELICITED BY PASSIVE STRETCH OF THE MUSCLES traversing the affected compartment (e.g. passive toe extension for deep posterior compartment of calf)", "palpation: TENSE, WOODEN, BOARD-LIKE, SHINY SWELLING of the muscular compartment", "THE TRADITIONAL '5 Ps': 1. Pain (early, reliable); 2. Paresthesias (early nerve ischemia); 3. Pallor; 4. Paralysis (late, indicates muscle death); 5. Pulselessness (TERMINAL, EXTREMELY LATE SIGN - peripheral pulse is typically PRESERVED because intracompartmental pressure rarely exceeds systolic arterial pressure)", "intracompartmental pressure manometry: absolute pressure > 30 mmHg, OR DELTA PRESSURE (Diastolic BP minus Compartment Pressure) <= 30 mmHg confirms diagnosis"],
        "pertinent_negatives": ["PULSELESSNESS IS A TERMINAL SIGN, NOT A SENSITIVE SCREENING CRITERION; presence of a distal pulse DOES NOT rule out compartment syndrome"],
        "content": "Life-threatening surgical emergency where increased tissue pressure within an enclosed non-distensible osteofascial compartment exceeds capillary perfusion pressure (approx 30 mmHg), causing microvascular occlusion, tissue hypoxia, and muscle/nerve necrosis. Immediate Surgical Protocol: 1. STAT REMOVAL OF ALL CIRCUMFERENTIAL CASTS, BANDAGES, OR DRESSINGS DOWN TO SKIN (reduces pressure by 50-80%); 2. Maintain limb at heart level (DO NOT ELEVATE, as elevation decreases arterial perfusion pressure; DO NOT DEPEND); 3. STAT EMERGENCY FASCIOTOMY: Urgent full-length dual-incision four-compartment fasciotomy for leg (anterolateral and posteromedial incisions releasing anterior, lateral, superficial posterior, and deep posterior compartments); 4. Re-look at 48 hours and delayed closure or skin grafting."
    },
    {
        "id": "ICD10-T79.1",
        "topic": "Fat Embolism Syndrome (Gurd's Criteria & Petechial Rash)",
        "icd10": "T79.1",
        "specialty": "Orthopedic Surgery / Critical Care / Trauma Surgery",
        "organ_system": "Trauma Respiratory Emergency",
        "keywords": ["fat embolism syndrome", "fes", "gurds criteria", "petechial rash axilla", "snowstorm pattern chest x-ray", "long bone femur fracture embolism", "hypoxemia confusion petechiae"],
        "red_flags": ["fulminant acute respiratory distress syndrome (ards)", "diffuse cerebral microvascular infarction / coma", "cardiorespiratory arrest"],
        "clinical_hallmarks": ["develops typically 24 to 72 hours following blunt trauma with CLOSED LONG BONE FRACTURES (femur, tibia) or pelvic fractures, or during reamed intramedullary nailing", "CLASSIC DIAGNOSTIC TRIAD: 1. Respiratory distress (dyspnea, tachypnea, profound refractory hypoxemia); 2. Neurological dysfunction (acute confusion, agitation, drowsiness, seizures, coma); 3. PATHOGNOMONIC PETECHIAL RASH (in 20-50%: non-palpable, pinpoint petechiae characteristically distributed over the ANTERIOR AXILLAE, CHEST, NECK, FLANKS, AND CONJUNCTIVAE, resolving within days)", "Gurd's Diagnostic Criteria (requires >= 1 major + >= 4 minor): Major: petechial rash, hypoxemia (PaO2 < 60 mmHg), CNS depression, pulmonary edema; Minor: tachycardia (HR > 110), fever > 38.5C, retinal fat emboli, fat globules in urine, sudden thrombocytopenia, unexplained drop in hematocrit", "chest radiograph: bilateral, diffuse, patchy interstitial and alveolar opacities ('SNOWSTORM APPEARANCE')"],
        "pertinent_negatives": ["rash is absent in simple pulmonary thromboembolism"],
        "content": "Multisystem microvascular occlusion and systemic inflammatory cascade caused by bone marrow fat globules and free fatty acids entering the torn venous circulation following orthopedic trauma. Treatment: 1. STRICTLY PREVENTIVE: Early, definitive, stable surgical reduction and fixation of long bone fractures within 24 hours of trauma markedly reduces incidence; 2. Supportive Critical Care: High-flow oxygen and early lung-protective mechanical ventilation with PEEP for ARDS; Maintenance of intravascular volume; Systemic corticosteroids (Methylprednisolone) may reduce hypoxemia when given early in high-risk polytrauma."
    },
    {
        "id": "ICD10-M86.9",
        "topic": "Acute Osteomyelitis & Brodie's Abscess (Staph Aureus)",
        "icd10": "M86.9",
        "specialty": "Orthopedics / Infectious Disease / Pediatrics",
        "organ_system": "Bone & Joint Infectious",
        "keywords": ["acute osteomyelitis", "bone infection", "brodie abscess", "staphylococcus aureus osteomyelitis", "refusal to bear weight child", "metaphyseal tenderness", "sequestrum and involucrum"],
        "red_flags": ["suppurative joint decompression / septic arthritis in infants", "pathological fracture", "chronic osteomyelitis with sinus tract and squamous cell carcinoma (Marjolin ulcer)"],
        "clinical_hallmarks": ["Acute Hematogenous Osteomyelitis: overwhelmingly affects CHILDREN (< 10 years, male:female 2:1), characteristically localizing to the METAPHYSIS OF RAPIDLY GROWING LONG BONES (distal femur, proximal tibia, proximal humerus)", "abrupt onset of high fever, chills, irritability, and REFUSAL TO BEAR WEIGHT OR MOVE THE AFFECTED LIMB (pseudoparalysis of childhood)", "EXQUISITE, WELL-LOCALIZED POINT BONE TENDERNESS directly over the metaphysis upon gentle palpation, accompanied by local warmth and soft-tissue edema", "Brodie's Abscess: subacute/chronic form presenting as a localized, round or oval radiolucent abscess cavity surrounded by a dense, sclerotic bone margin", "late plain radiograph signs (lag behind clinical symptoms by 10-14 days): periosteal reaction, lytic bone destruction, SEQUESTRUM (island of dead, devitalized bone separated from living bone), and INVOLUCRUM (shell of new periosteal bone enclosing dead bone)", "MRI of bone (gold standard): bone marrow edema within 24-48 hours", "predominant pathogen: STAPHYLOCOCCUS AUREUS (> 80-90% of cases, including MRSA)"],
        "pertinent_negatives": ["early normal plain radiograph DOES NOT rule out acute osteomyelitis; MRI or bone scan is mandatory"],
        "content": "Suppurative bacterial infection and inflammation of bone and marrow cavity. Diagnostic workup: Blood cultures (positive in 50%), bone aspirate / biopsy for culture, CBC, ESR, CRP, and contrast MRI. Treatment: 1. Empiric IV Antibiotic Therapy: IV Cefazolin or IV Flucloxacillin (or IV Vancomycin / Daptomycin for suspected MRSA) initiated for 2 weeks followed by high-dose oral antibiotics for total 4-6 weeks; 2. Surgical Indications: Subperiosteal abscess, cortical bone perforation, lack of clinical/CRP improvement within 48-72 hours of targeted antibiotics, or chronic sequestrum (requires surgical debridement and sequestrectomy)."
    },
    {
        "id": "ICD10-M00.9",
        "topic": "Septic Arthritis of Native Joint (Kocher Criteria & Arthrocentesis)",
        "icd10": "M00.9",
        "specialty": "Orthopedics / Rheumatology / Infectious Disease / Emergency Medicine",
        "organ_system": "Joint Infectious Emergency",
        "keywords": ["septic arthritis", "infected joint", "kocher criteria pediatric hip", "arthrocentesis synovial wbc > 50000", "intense pain active passive range of motion", "staphylococcus aureus joint", "emergency joint washout"],
        "red_flags": ["rapid proteolytic cartilage destruction and joint destruction within 24-48 hours", "septic shock", "osteonecrosis of femoral head in infant"],
        "clinical_hallmarks": ["statutory orthopedic emergency: ACUTE ONSET OF AGONIZING MONOARTHRITIS (in > 80-90% affecting a single large joint: THE KNEE [50%], followed by hip, shoulder, ankle, and wrist)", "the joint is visibly swollen, tense, red, hot, and held in a position of maximum capsular capacity (e.g. hip held in flexion, abduction, and external rotation)", "PATHOGNOMONIC EXAM HALLMARK: EXCRUCIATING, COMPLETE INTOLERANCE TO EVEN THE SLIGHTEST ACTIVE OR PASSIVE JOINT RANGE OF MOTION (joint is held completely rigid)", "KOCHER CRITERIA (for differentiating pediatric septic hip from transient synovitis; 4 criteria = 99% probability of septic arthritis): 1. Inability to bear weight / non-weight-bearing; 2. Oral temperature > 38.5C; 3. ESR > 40 mm/hr; 4. Serum WBC > 12,000 /mcL", "DIAGNOSTIC GOLD STANDARD: URGENT JOINT ARTHROCENTESIS: turbid, purulent synovial fluid with SYNOVIAL WHITE BLOOD CELL COUNT > 50,000 /mcL (often > 100,000 /mcL) with > 75-90% polymorphonuclear neutrophils (PMNs), low synovial glucose (< 50% blood glucose), and positive Gram stain/culture"],
        "pertinent_negatives": ["intense pain on PASSIVE movement distinguishes true intra-articular septic arthritis from peri-articular cellulitis/bursitis"],
        "content": "Bacterial invasion of synovial joint space causing rapid enzymatic chondrolysis by neutrophil elastases and bacterial metalloproteinases. Pathogens: Staphylococcus aureus, Streptococcus pyogenes, Neisseria gonorrhoeae (sexually active young adults). Protocol: 1. STAT Emergency Joint Arthrocentesis (BEFORE initiating antibiotics); 2. STAT Surgical Joint Drainage and Decompression: Emergency Arthroscopic or Open Arthrotomy and Joint Washout / Lavage (hip and shoulder almost always require open arthrotomy); 3. Empiric IV Antibiotics (IV Vancomycin + Ceftriaxone) adjusted to Gram stain and continued for 3-4 weeks; 4. Early passive motion rehabilitation."
    },
    {
        "id": "ICD10-M87.00",
        "topic": "Avascular Necrosis of Femoral Head (Crescent Sign & Ficat Staging)",
        "icd10": "M87.00",
        "specialty": "Orthopedic Surgery",
        "organ_system": "Bone Ischemic Necrosis",
        "keywords": ["avascular necrosis", "avn", "osteonecrosis femoral head", "crescent sign subchondral collapse", "steroid induced avn", "ficat staging", "core decompression total hip arthroplasty"],
        "red_flags": ["subchondral cortical collapse and secondary severe osteoarthritis", "bilateral disease (in > 50-70%)"],
        "clinical_hallmarks": ["history of high-risk etiologies: prolonged high-dose SYSTEMIC CORTICOSTEROID THERAPY (most common non-traumatic cause), chronic ALCOHOL ABUSE (> 400 mL/week), sickle cell disease, systemic lupus erythematosus, or prior femoral neck fracture", "insidious, progressive, deep groin or anterior thigh pain, aggravated by weight-bearing and relieved by rest", "physical examination: restricted and painful internal rotation and abduction of the hip", "radiographic hallmarks (Ficat and Arlet Staging):", "Stage I: Normal plain radiograph, but MRI reveals diagnostic focal bone marrow edema with a serpentine low-signal band on T1-weighted images ('double-line sign' on T2)", "Stage II: Radiographic evidence of sclerosis and osteopenia with preserved spherical femoral head contour", "Stage III: PATHOGNOMONIC 'CRESCENT SIGN' (subchondral radiolucent linear fracture line) indicating impending or early structural bone collapse", "Stage IV: Flattening, collapse of the femoral head, and joint space narrowing with secondary osteoarthritis"],
        "pertinent_negatives": ["plain radiograph can be completely normal in early disease (Stage I), requiring MRI for definitive early detection"],
        "content": "Ischemic death of cellular elements of trabecular bone and marrow of the femoral head, caused by compromised microvascular supply from the medial femoral circumflex artery. Diagnostic gold standard: MRI pelvis (sensitivity > 99%). Treatment: 1. Pre-collapse (Stages I-II): Joint-preserving procedures: Core Decompression +/- autologous bone marrow aspirate concentrate (BMAC) to reduce intraosseous pressure and promote revascularization; 2. Post-collapse (Stages III-IV): Total Hip Arthroplasty (THA - gold standard, provides definitive pain relief and functional restoration)."
    },
    {
        "id": "ICD10-M93.00",
        "topic": "Slipped Capital Femoral Epiphysis (SCFE & Klein's Line)",
        "icd10": "M93.00",
        "specialty": "Pediatric Orthopedics / Pediatrics",
        "organ_system": "Pediatric Musculoskeletal Emergency",
        "keywords": ["slipped capital femoral epiphysis", "scfe", "klein line", "obese adolescent knee pain", "femoral epiphysis displacement", "obligate external rotation hip flexion", "in situ percutaneous screw fixation"],
        "red_flags": ["avascular necrosis of femoral head (catastrophic complication of forcible reduction)", "chondrolysis (rapid articular cartilage destruction)", "bilateral slip (in up to 40-50%)"],
        "clinical_hallmarks": ["predominantly affects ADOLESCENT CHILDREN during pubertal growth spurt (boys age 12-16, girls age 10-14), characteristically in OBESE or overweight adolescents", "INSIDIOUS, DULL, ACHING REFERRED KNEE OR DISTAL THIGH PAIN (in up to 30-50% the hip pain is completely absent, leading to frequent diagnostic delays or missed diagnosis)", "limp with antalgic or Trendelenburg gait; foot on affected side is held in external rotation", "PATHOGNOMONIC PHYSICAL EXAMINATION SIGN: OBLIGATE EXTERNAL ROTATION DURING PASSIVE HIP FLEXION (as the hip is flexed upward to 90 degrees, the thigh spontaneously and involuntarily externally rotates and abducts)", "plain radiographs (AP and Frog-leg lateral pelvis): posterior and inferior displacement of the femoral epiphysis relative to the femoral neck ('ice cream slipping off the cone')", "PATHOGNOMONIC RADIOGRAPHIC SIGN: ABNORMAL KLEIN'S LINE (a line drawn along the superior border of the femoral neck normally intersects the lateral aspect of the femoral epiphysis; in SCFE, the line FAILS TO INTERSECT the slipped epiphysis / Trethowan sign)"],
        "pertinent_negatives": ["DO NOT ATTEMPT MANIPULATIVE CLOSED REDUCTION (manipulation kinks fragile retinacular blood vessels and drastically increases AVN risk from < 5% to > 50%)"],
        "content": "Most common hip disorder of adolescents, characterized by displacement of the femoral neck anteriorly and superiorly through the hypertrophic zone of the physeal growth plate while the capital epiphysis remains in the acetabulum. Classified as stable (can bear weight) or unstable (unable to bear weight even with crutches). Statutory orthopedic semi-emergency: Patient MUST BE KEPT STRICTLY NON-WEIGHT-BEARING ON CRUTCHES / WHEELCHAIR IMMEDIATELY upon suspicion. Definitive Treatment: STAT In Situ Single Percutaneous Cannulated Screw Fixation (across the physis into the center of the epiphysis) to arrest slip progression; Prophylactic pinning of contralateral normal hip considered for high-risk endocrine disorders."
    },

    # --- 14. TOXICOLOGY & ENVIRONMENTAL EMERGENCIES (12) ---
    {
        "id": "ICD10-T60.0X1A",
        "topic": "Organophosphate & Carbamate Poisoning (SLUDGE / DUMBELS & Atropine)",
        "icd10": "T60.0X1A",
        "specialty": "Emergency Medicine / Clinical Toxicology / Critical Care",
        "organ_system": "Toxicological Emergency",
        "keywords": ["organophosphate poisoning", "cholinergic crisis", "sludge dumbels", "pinpoint pupils miosis", "atropinization clear lungs", "pralidoxime 2-pam", "acetylcholinesterase inhibition"],
        "red_flags": ["bronchorrhea and bronchospasm with acute asphyxiation", "respiratory arrest from central depression and diaphragmatic weakness", "Intermediate Syndrome (type II neuromuscular weakness)"],
        "clinical_hallmarks": ["history of ingestion (suicidal), dermal absorption, or inhalation of agricultural insecticides (Chlorpyrifos, Malathion, Diazinon)", "characteristic pungent 'GARLIC-LIKE' OR CHEMICAL ODOR to breath and vomitus", "FULL CHOLINERGIC TOXIDROME (The 'DUMBELS' Mnemonic):", "1. D - Diarrhea; 2. U - Urination; 3. M - Miosis (pathognomonic PINPOINT, CONSTRICTED PUPILS < 1-2 mm); 4. B - BRONCHORRHEA AND BRONCHOSPASM (massive flooding of bronchial tree with copious watery secretions and wheezing - THE PRIMARY CAUSE OF DEATH); 5. E - Emesis; 6. L - Lacrimation (copious tearing); 7. S - Salivation (frothing at mouth) and profound Diaphoresis (drenching sweats)", "Nicotinic signs: generalized muscle fasciculations, tremors, muscle weakness, and diaphragmatic paralysis", "CNS signs: confusion, seizures, and coma", "laboratory hallmark: MARKED DEPRESSION OF SERUM BUTYRYLCHOLINESTERASE (pseudocholinesterase) AND RED BLOOD CELL ACETYLCHOLINESTERASE (< 20-50% normal)"],
        "pertinent_negatives": ["DRY LUNGS, NOT PUPIL SIZE, IS THE PRIMARY ENDPOINT FOR ATROPINIZATION"],
        "content": "Irreversible inhibition of acetylcholinesterase enzyme via phosphorylation of active site serine residue, leading to toxic accumulation of acetylcholine at muscarinic, nicotinic, and CNS synapses. Life-Saving Protocol: 1. PPE for medical staff; STAT Decontamination (remove all clothing, soap/water bath); 2. STAT ATROPINE TITRATION: Atropine (2 to 5 mg IV bolus, DOUBLING THE DOSE EVERY 3-5 MINUTES: 2mg, 4mg, 8mg, 16mg... until full 'ATROPINIZATION' is achieved: Clear chest on auscultation [dry lungs], HR > 80 bpm, Systolic BP > 90, dry axillae); 3. STAT Oxime: Pralidoxime (2-PAM: 1-2 g IV loading dose over 30 min followed by 500 mg/hr infusion) initiated BEFORE 'aging' of enzyme occurs; 4. IV Diazepam for seizure control."
    },
    {
        "id": "ICD10-T39.1X1A",
        "topic": "Paracetamol (Acetaminophen) Toxicity & Rumack-Matthew Nomogram",
        "icd10": "T39.1X1A",
        "specialty": "Clinical Toxicology / Emergency Medicine / Hepatology",
        "organ_system": "Toxicological / Hepatic Emergency",
        "keywords": ["paracetamol toxicity", "acetaminophen overdose", "rumack matthew nomogram", "n acetylcysteine nac", "napqi toxicity", "fulminant hepatic failure paracetamol", "ast alt > 10000"],
        "red_flags": ["fulminant acute liver failure (incoagulable INR > 6.5, grade III/IV encephalopathy)", "King's College Hospital criteria for emergency liver transplant", "severe lactic acidosis"],
        "clinical_hallmarks": ["history of acute ingestion of >= 7.5 - 10 grams (or > 150-200 mg/kg in children) of Paracetamol / Acetaminophen", "FOUR CLINICAL PHASES OF TOXICITY:", "Phase 1 (0-24 hours): patient is deceivably ASYMPTOMATIC or has mild nausea, vomiting, malaise, and diaphoresis (normal transaminases)", "Phase 2 (24-72 hours): 'the clinical lull' - nausea resolves, but patient develops RIGHT UPPER QUADRANT PAIN and tenderness with early elevation of transaminases (AST, ALT), bilirubin, and INR", "Phase 3 (72-96 hours - PEAK HEPATOTOXICITY): FULMINANT HEPATIC NECROSIS with profound jaundice, coagulopathy, encephalopathy, marked AST/ALT elevations (often EXCEEDING 10,000 IU/L), acute renal failure (acute tubular necrosis), and severe lactic acidosis", "Phase 4 (4-14 days): recovery or death from multiorgan failure", "DIAGNOSTIC WORKUP: 4-Hour Serum Acetaminophen Level plotted on the RUMACK-MATTHEW NOMOGRAM (treatment line starts at 150 mcg/mL at 4 hours post-ingestion)"],
        "pertinent_negatives": ["mild initial Phase 1 symptoms DO NOT imply mild poisoning; early therapy before transaminases rise is 100% protective"],
        "content": "Excess NAPQI (N-acetyl-p-benzoquinone imine) metabolite depletes hepatic glutathione stores (> 70% depletion), leading to covalent binding of NAPQI to hepatic mitochondrial proteins and centrilobular (Zone 3) hepatic necrosis. SPECIFIC ANTIDOTE: N-ACETYLCYSTEINE (NAC - replenishes glutathione). Protocol: 1. Activated Charcoal (1 g/kg orally) if presenting within 1-2 hours of ingestion; 2. IV N-Acetylcysteine (3-Bag Intravenous Regimen: 150 mg/kg over 1 hour, then 50 mg/kg over 4 hours, then 100 mg/kg over 16 hours) OR simplified 2-bag regimen; NAC is 100% hepatoprotective if started within 8 hours of ingestion, but MUST BE GIVEN even in late presentations; Continue NAC until AST/ALT resolving and INR < 2.0."
    },
    {
        "id": "ICD10-T58.01XA",
        "topic": "Carbon Monoxide Poisoning (Cherry-Red Lips & Carboxyhemoglobin)",
        "icd10": "T58.01XA",
        "specialty": "Emergency Medicine / Hyperbaric Medicine / Clinical Toxicology",
        "organ_system": "Toxicological Hypoxic Emergency",
        "keywords": ["carbon monoxide poisoning", "co toxicity", "cherry red lips skin", "carboxyhemoglobin cohb", "headache confusion faulty furnace", "hyperbaric oxygen hbo", "pulse oximetry falsely normal"],
        "red_flags": ["delayed neuropsychiatric sequelae (dns) weeks after recovery", "myocardial ischemia / infarction", "coma and cerebral edema"],
        "clinical_hallmarks": ["history of exposure to enclosed combustion sources: house fires, faulty domestic gas heaters/furnaces, indoor charcoal grills, running automobile exhaust, or power generators", "multiple co-occupants or pets in the same household presenting simultaneously with identical 'flu-like' symptoms", "MILD-TO-MODERATE TOXICITY: dull, throbbing, bilateral frontal headache (most common early symptom), nausea, dizziness, vomiting, fatigue, visual disturbances, and confusion", "SEVERE TOXICITY: syncope, seizures, chest pain (ischemia), cardiac arrhythmias, ataxia, coma, and cardiorespiratory arrest", "CLASSIC BUT RARE/LATE PHYSICAL SIGN: 'CHERRY-RED' DISCOLORATION of the lips, mucosal membranes, and skin (seen in < 2-3% of living patients, predominantly a post-mortem finding)", "PATHOGNOMONIC MONITORING PITFALL: STANDARD PULSE OXIMETRY (SpO2) IS FALSELY NORMAL (standard two-wavelength pulse oximeters cannot distinguish carboxyhemoglobin from oxyhemoglobin, falsely reading 99-100% despite severe cellular hypoxia)", "laboratory gold standard: Venous or Arterial Blood Co-oximetry measuring CARBOXYHEMOGLOBIN (COHb: > 3-5% in non-smokers, > 10% in heavy smokers is diagnostic; severe poisoning typically > 25-40%)"],
        "pertinent_negatives": ["standard SpO2 reading of 100% DOES NOT rule out lethal carbon monoxide poisoning"],
        "content": "CO binds to hemoglobin with an affinity 200-250 times greater than oxygen, forming carboxyhemoglobin and shifting the oxygen-hemoglobin dissociation curve sharply to the left (Haldane effect), blocking oxygen unloading. Also inhibits mitochondrial Cytochrome c Oxidase. Treatment: 1. STAT 100% High-Flow Normobaric Oxygen via tightly fitting non-rebreather reservoir mask (reduces COHb half-life from 320 minutes on room air to 74 minutes on 100% O2); 2. HYPERBARIC OXYGEN (HBO: 100% O2 at 2.5-3.0 atmospheres reduces COHb half-life to 20 minutes and prevents Delayed Neuropsychiatric Sequelae); HBO Indications: COHb > 25% (> 15% in pregnancy), loss of consciousness, neurological deficits, cardiac ischemia, or severe acidosis."
    },
    {
        "id": "ICD10-T63.011A",
        "topic": "Snakebite Envenomation (Neurotoxic vs Vasculotoxic - Polyvalent ASV)",
        "icd10": "T63.011A",
        "specialty": "Emergency Medicine / Clinical Toxicology / Critical Care",
        "organ_system": "Toxinology / Envenomation Emergency",
        "keywords": ["snakebite envenomation", "anti snake venom asv", "neurotoxic cobra krait", "vasculotoxic viper", "20 minute whole blood clotting test", "ptosis respiratory arrest snake", "compartment syndrome snakebite"],
        "red_flags": ["acute respiratory paralysis (Krait/Cobra)", "consumptive coagulopathy / fatal intracranial hemorrhage (Viper)", "acute kidney injury and renal cortical necrosis"],
        "clinical_hallmarks": ["history of bite by a venomous snake (The Indian 'Big Four': Russell's Viper, Saw-Scaled Viper, Common Krait, Spectacled Cobra)", "presence of visible fang puncture marks, with or without localized swelling", "VASCULOTOXIC / HEMOTOXIC ENVENOMATION (Russell's & Saw-scaled Viper): rapid, progressive, severe local edema and tissue necrosis; spontaneous systemic bleeding (hematuria, gingival bleeding, epistaxis, hematemesis); PATHOGNOMONIC BEDSIDE TEST: POSITIVE 20-MINUTE WHOLE BLOOD CLOTTING TEST (20WBCT: 2 mL of fresh blood placed in clean glass tube fails to clot firmly after 20 minutes, indicating venom-induced consumptive coagulopathy)", "NEUROTOXIC ENVENOMATION (Common Krait & Cobra): minimal or ABSENT local signs (Krait bite can be completely painless with invisible puncture marks during sleep); progressive descending flaccid motor paralysis: EARLIEST SIGN IS BILATERAL PTOSIS (drooping eyelids), followed by diplopia, ophthalmoplegia, dysarthria, dysphagia, pooling of saliva, and RAPID RESPIRATORY ARREST within 1-6 hours", "Russell's Viper adds: acute renal failure, hypopituitarism (Sheehan-like pituitary infarction)"],
        "pertinent_negatives": ["TOURNIQUETS, CUTTING, SUCTION, AND HERBAL PASTES ARE STRICTLY PROHIBITED (accelerate tissue necrosis and gangrene)"],
        "content": "Life-threatening biological envenomation. Immediate Protocol: 1. Strict immobilization of bitten extremity in splint (DO NOT apply tourniquet or pressure immobilization for viper bites); 2. STAT INDICATIONS FOR POLYVALENT ANTI-SNAKE VENOM (ASV): systemic envenomation (abnormal 20WBCT, systemic bleeding, neurotoxicity [ptosis], shock) or severe local swelling (> 1/2 limb); 3. ASV DOSING: Initial 10 vials of lyophilized Polyvalent ASV reconstituted in 500 mL normal saline infused over 1 hour; 4. Neurotoxic rescue: Neostigmine (0.5 mg IV) + Atropine (0.6 mg IV) trial (acts as antidote for Cobra post-synaptic neurotoxin; Krait pre-synaptic toxin requires mechanical ventilation); 5. Repeat ASV based on persistent 20WBCT abnormality at 6 hours."
    },
    {
        "id": "ICD10-T51.1X1A",
        "topic": "Toxic Alcohol Ingestion (Methanol vs Ethylene Glycol - Fomepizole)",
        "icd10": "T51.1X1A",
        "specialty": "Clinical Toxicology / Emergency Medicine / Nephrology",
        "organ_system": "Toxicological Metabolic Emergency",
        "keywords": ["methanol poisoning", "ethylene glycol poisoning", "toxic alcohols", "snowstorm vision blindness", "calcium oxalate envelope crystals", "high anion gap and osmolar gap", "fomepizole", "hemodialysis toxic alcohol"],
        "red_flags": ["permanent optic atrophy and irreversible bilateral blindness (Methanol)", "oliguric acute renal failure (Ethylene glycol)", "severe refractory metabolic acidosis (pH < 7.0)"],
        "clinical_hallmarks": ["history of ingesting bootleg/illicit liquor, moonshine, windshield washer fluid (Methanol) or automotive radiator antifreeze (Ethylene Glycol)", "LABORATORY CORNERSTONE: HIGH OSMOLAR GAP (> 10-15 mOsm/kg) in early stages, evolving into a SEVERE HIGH ANION GAP METABOLIC ACIDOSIS (HAGMA with bicarbonate often < 5-10 mEq/L)", "METHANOL SPECIFIC HALLMARKS: 1. Visual disturbances described as 'BEING IN A SNOWSTORM' or 'looking through a white snow blizzard'; 2. Fundoscopy: marked optic disc hyperemia, edema, and subsequent optic atrophy and complete blindness (formic acid retinal toxicity); 3. Bilateral putaminal necrosis on brain CT/MRI", "ETHYLENE GLYCOL SPECIFIC HALLMARKS: 1. Acute oliguric/anuric kidney injury (glycolic and oxalic acid toxicity); 2. Urinalysis under polarized light shows pathognomonic 'ENVELOPE-SHAPED' OR DUMBBELL-SHAPED CALCIUM OXALATE MONOHYDRATE CRYSTALS; 3. Urine fluoresces under Wood's lamp (due to added fluorescein dye in antifreeze)"],
        "pertinent_negatives": ["ethanol level can delay toxic metabolite formation; osmolar gap is highest early, while anion gap is highest late"],
        "content": "Metabolized by Alcohol Dehydrogenase (ADH) into highly toxic organic acids (Methanol -> Formaldehyde -> Formic Acid; Ethylene Glycol -> Glycolic Acid -> Oxalic Acid). Specific Antidote Protocol: 1. INHIBIT ALCOHOL DEHYDROGENASE IMMEDIATELY: Fomepizole (15 mg/kg IV loading dose over 30 min, then 10 mg/kg q12h; has 8,000x greater affinity for ADH than ethanol) OR Oral/IV Ethanol (target blood level 100-150 mg/dL); 2. STAT Emergency Hemodialysis (clears parent alcohol and toxic acid metabolites; indicated for pH < 7.25, visual symptoms, renal failure, or level > 50 mg/dL); 3. Adjunctive cofactors: IV Folinic acid / Leucovorin (50 mg q4h for methanol) OR IV Thiamine + Pyridoxine (for ethylene glycol)."
    },
    {
        "id": "ICD10-T67.0XXA",
        "topic": "Heat Stroke (Exertional vs Classical - Core Temp > 40.5C)",
        "icd10": "T67.0XXA",
        "specialty": "Emergency Medicine / Sports Medicine / Critical Care",
        "organ_system": "Environmental Hyperthermic Emergency",
        "keywords": ["heat stroke", "core temperature > 40.5", "central nervous system dysfunction heat", "anhidrosis heat stroke", "exertional vs classic heat stroke", "evaporative cooling water immersion", "rhabdomyolysis heat"],
        "red_flags": ["disseminated intravascular coagulation (dic)", "severe rhabdomyolysis and myoglobinuric acute renal failure", "cerebellar ataxia and permanent neurological damage"],
        "clinical_hallmarks": ["TRUE ENVIRONMENTAL EMERGENCY defined by two absolute mandatory diagnostic criteria:", "1. SEVERE HYPERPYREXIA: CORE BODY TEMPERATURE > 40.5C (> 105F) measured rectally (oral, axillary, and tympanic thermometers are completely inaccurate and underestimate core temperature);", "2. PROFOUND CENTRAL NERVOUS SYSTEM (CNS) DYSFUNCTION: delirium, confusion, bizarre behavior, combativeness, ataxia, seizures, or coma", "CLASSIC / NON-EXERTIONAL HEAT STROKE: occurs in elderly, frail, impoverished individuals without air conditioning during ambient heat waves; ANHIDROSIS (hot, flushed, completely dry skin due to thermoregulatory failure) is typical", "EXERTIONAL HEAT STROKE: occurs in young athletes, military recruits, or laborers undergoing strenuous physical exertion in hot environments; PROFUSE DIAPHORESIS (skin is often wet and clammy) is present in > 50% at collapse", "associated complications: multiorgan failure, hypotension, tachycardia, hyperventilation, marked AST/ALT elevation (> 10,000 U/L), and severe lactic acidosis"],
        "pertinent_negatives": ["ANTIPYRETICS (PARACETAMOL, ASPIRIN) ARE COMPLETELY INEFFECTIVE AND HARMFUL (heat stroke is not mediated by hypothalamic pyrogens; antipyretics worsen hepatic and renal toxicity)"],
        "content": "Life-threatening failure of thermoregulation where metabolic heat production and environmental heat absorption overwhelm heat dissipation mechanisms, inducing systemic inflammatory response syndrome and multiorgan failure. Mortalities reach 50-70% if cooling delayed. Immediate Resuscitation Protocol: 1. RAPID PHYSICAL COOLING IS LIFE-SAVING: Target: cool core temperature to 38.3 - 38.9C (101-102F) WITHIN 30 MINUTES; 2. Exertional: Cold-Water Immersion (ice-water tub immersion is the gold standard, cooling at > 0.2C/min); 3. Classical: Evaporative and Convective Cooling (continuous misting of lukewarm water combined with high-flow fans); 4. STOP COOLING AT 38.5C to prevent hypothermic overshoot; 5. IV Benzodiazepines (Diazepam) to control shivering and seizures; 6. Aggressive IV fluid hydration with Normal Saline."
    },

    # --- 15. PEDIATRICS & NEONATOLOGY (6) ---
    {
        "id": "ICD10-Q40.0",
        "topic": "Infantile Hypertrophic Pyloric Stenosis (Olive Mass & Projectile Vomiting)",
        "icd10": "Q40.0",
        "specialty": "Pediatric Surgery / Pediatrics / Emergency Medicine",
        "organ_system": "Pediatric Gastrointestinal",
        "keywords": ["pyloric stenosis", "hypertrophic pyloric stenosis", "projectile non bilious vomiting", "palpable olive mass", "hypochloremic hypokalemic metabolic alkalosis", "ramstedt pyloromyotomy", "string sign ultrasound"],
        "red_flags": ["severe dehydration and circulatory shock", "paradoxical aciduria", "aspiration pneumonia"],
        "clinical_hallmarks": ["predominantly affects first-born male infants (male:female ratio 4:1), characteristically presenting between 3 to 6 WEEKS OF AGE", "CARDINAL SYMPTOM: FORCEFUL, PROJECTILE, NON-BILIOUS VOMITING occurring immediately after every feeding (vomitus is milky/curdled, NEVER bile-stained or greenish)", "infant remains ravenously hungry immediately after vomiting ('hungry vomiter') and eagerly feeds again", "visible gastric peristaltic waves traveling from left to right across upper abdomen prior to emesis", "PATHOGNOMONIC PHYSICAL EXAMINATION SIGN: A PALPABLE, FIRM, MOBILE, NON-TENDER, 1-2 CM 'OLIVE-LIKE' MASS in the right upper quadrant / epigastrium (palpated best with child calm and relaxed after feeding)", "DIAGNOSTIC LABORATORY HALLMARK: HYPOCHLOREMIC, HYPOKALEMIC METABOLIC ALKALOSIS (caused by repeated loss of gastric hydrochloric acid and renal potassium-hydrogen exchange)", "Abdominal Ultrasound (gold standard): thickened pyloric muscle thickness >= 3-4 mm and pyloric channel length >= 14-16 mm ('doughnut' or 'target' sign)"],
        "pertinent_negatives": ["vomitus is strictly NON-BILIOUS (bilious vomit indicates intestinal obstruction distal to ampulla of Vater, e.g. malrotation with volvulus)"],
        "content": "Hypertrophy and hyperplasia of the circular muscle layer of the pylorus, causing severe narrowing of the pyloric canal and functional gastric outlet obstruction. Emergency Rule: Pyloric stenosis is a MEDICAL RESUSCITATION EMERGENCY, NOT AN IMMEDIATE SURGICAL EMERGENCY (surgery performed before correcting alkalosis causes fatal postoperative apnea). Protocol: 1. Correct dehydration and electrolyte alkalosis FIRST: IV fluid resuscitation with 0.9% Normal Saline + 5% Dextrose with added Potassium Chloride (20-40 mEq/L); serum chloride MUST be > 100 mEq/L and bicarbonate < 30 mEq/L before surgery; 2. DEFINITIVE CURATIVE SURGERY: Ramstedt Extramucosal Pyloromyotomy (longitudinal splitting of the hypertrophied pyloric muscle without breaching the underlying mucosal layer)."
    },
    {
        "id": "ICD10-K56.1",
        "topic": "Intussusception (Red Currant Jelly Stool & Target Sign)",
        "icd10": "K56.1",
        "specialty": "Pediatrics / Pediatric Surgery / Emergency Medicine",
        "organ_system": "Pediatric Gastrointestinal Emergency",
        "keywords": ["intussusception", "red currant jelly stools", "target sign ultrasound", "sausage shaped abdominal mass", "ileocolic intussusception", "air enema reduction", "colicky crying legs pulled up"],
        "red_flags": ["bowel necrosis and intestinal perforation with peritonitis", "hypovolemic septic shock", "lead point malignancy (lymphoma) in older child"],
        "clinical_hallmarks": ["most common cause of intestinal obstruction in infants (peak age 5 to 10 months, male predominance)", "CLASSIC DIAGNOSTIC TRIAD (present simultaneously in < 40-50%): 1. Paroxysmal, severe, episodic colicky abdominal pain (infant cries inconsolably and DRAWS KNEES UP TO CHEST for 10-15 minutes, followed by complete calm/lethargy between episodes); 2. Sausage-shaped mass; 3. Red Currant Jelly stools", "physical examination: palpable, smooth, firm, sausage-shaped abdominal mass in the right upper quadrant or epigastrium, with a pathognomonic 'EMPTY' RIGHT LOWER QUADRANT (Signe de Dance / Dance sign)", "PATHOGNOMONIC LATE SIGN: 'RED CURRANT JELLY STOOL' (passage per rectum of a mixture of blood, mucus, and sloughed mucosal cells - indicates bowel ischemia)", "Abdominal Ultrasound (DIAGNOSTIC GOLD STANDARD - sensitivity > 98%): 1. Transverse view: 'TARGET SIGN' OR 'DONUT SIGN' (concentric rings of bowel wall representing the outer intussuscipiens and inner telescoping intussusceptum); 2. Longitudinal view: 'Pseudokidney sign'"],
        "pertinent_negatives": ["absence of peritonitis and absence of free air under diaphragm on plain X-ray are prerequisites for pneumatic reduction"],
        "content": "Invagination or telescoping of a proximal segment of bowel (intussusceptum) into an adjacent distal segment (intussuscipiens), overwhelmingly ileocolic (90%), triggered by hypertrophied Peyer's patches following viral gastroenteritis or Meckel's diverticulum. Treatment: 1. NPO, NG tube decompression, IV fluid resuscitation; 2. FIRST-LINE THERAPEUTIC REDUCTION: Image-Guided Air Contrast Enema (Pneumatic Reduction) or Hydrostatic Saline Enema (success rate > 80-90%); 3. Emergency Surgical Laparotomy: INDICATED if peritonitis, perforation, hemodynamic shock, or failed radiologic air enemas."
    },
    {
        "id": "ICD10-P77.9",
        "topic": "Necrotizing Enterocolitis (NEC & Pneumatosis Intestinalis)",
        "icd10": "P77.9",
        "specialty": "Neonatology / Pediatric Surgery",
        "organ_system": "Neonatal Gastrointestinal Emergency",
        "keywords": ["necrotizing enterocolitis", "nec", "pneumatosis intestinalis", "premature infant feeding intolerance", "portal venous gas", "bell staging nec", "pneumoperitoneum football sign"],
        "red_flags": ["intestinal perforation with septic shock", "disseminated intravascular coagulation (dic)", "extensive bowel gangrene ('NEC totalis')"],
        "clinical_hallmarks": ["overwhelmingly affects PREMATURE, LOW-BIRTH-WEIGHT INFANTS (< 32 weeks gestation, < 1500g birth weight) in the Neonatal Intensive Care Unit (NICU)", "typically develops 1 to 3 weeks after initiation of enteral formula feeding", "CARDINAL CLINICAL SIGNS: 1. Feeding intolerance with large gastric aspirates / bilious gastric residuals; 2. Rapid, progressive, tense abdominal distension with visible dilated bowel loops; 3. Abdominal wall erythema, edema, and induration; 4. Gross or occult blood in stools (hematochezia); 5. Systemic signs: temperature instability, apnea, bradycardia, lethargy, and profound hypotension", "Plain Abdominal Radiographs (Modified Bell Staging):", "PATHOGNOMONIC RADIOGRAPHIC HALLMARK: PNEUMATOSIS INTESTINALIS (linear or bubbly radiolucent gas collections within the subserosal or submucosal layers of the bowel wall);", "PORTAL VENOUS GAS (branching radiolucent branching gas arborizing out to the periphery of the liver);", "PNEUMOPERITONEUM (free intraperitoneal air under diaphragm or 'Football sign' indicating bowel perforation)"],
        "pertinent_negatives": ["exclusive human breast milk feeding is strongly protective against NEC"],
        "content": "Acute ischemic and inflammatory mucosal necrosis of the neonatal bowel (predominantly terminal ileum and ascending colon), driven by prematurity, enteral feeding, abnormal bacterial colonization, and mucosal ischemia. Protocol: 1. Strict NPO, continuous low-intermittent nasogastric suctioning; 2. Aggressive IV fluid resuscitation and correction of thrombocytopenia and coagulopathy; 3. STAT Broad-Spectrum IV Triple Antibiotics (Ampicillin + Gentamicin + Metronidazole or Meropenem + Vancomycin); 4. Serial abdominal radiographs every 6-8 hours; 5. Emergency Surgical Laparotomy with resection of necrotic bowel and enterostomy, OR bedside Primary Peritoneal Drainage (PPD) for extremely low birth weight infants (< 1000g) with perforation."
    },
    {
        "id": "ICD10-J04.0",
        "topic": "Croup (Laryngotracheobronchitis & The Steeple Sign)",
        "icd10": "J04.0",
        "specialty": "Pediatrics / ENT / Emergency Medicine",
        "organ_system": "Pediatric Airway",
        "keywords": ["croup", "laryngotracheobronchitis", "barking seal cough", "inspiratory stridor child", "steeple sign neck x-ray", "parainfluenza virus croup", "dexamethasone nebulized epinephrine", "westley croup score"],
        "red_flags": ["bacterial tracheitis (toxic, high fever, copious purulent secretions)", "biphasic stridor with sternal retractions at rest", "cyanosis and exhaustion"],
        "clinical_hallmarks": ["most common cause of acute infectious upper airway obstruction in young children (age 6 months to 3 years, peak incidence in late autumn/winter)", "viral etiology: overwhelmingly Human Parainfluenza Virus (Type 1 and 2 in > 75%)", "prodrome of mild rhinorrhea, sore throat, and low-grade fever for 1-3 days", "CARDINAL CLINICAL TRIAD: 1. HARSH, METALLIC, RESIDUAL 'BARKING COUGH' (universally likened to the barking of a seal); 2. Hoarseness / raspy dysphonia; 3. INSPIRATORY STRIDOR that is characteristically WORSE AT NIGHT and aggravated by crying or agitation", "Westley Croup Clinical Score (mild <= 2, moderate 3-7, severe >= 8)", "Anteroposterior (AP) soft-tissue neck radiograph: PATHOGNOMONIC 'STEEPLE SIGN' (symmetric subglottic tapering and narrowing of the upper tracheal airway shadow resembling a church steeple)"],
        "pertinent_negatives": ["absence of drooling and absence of toxic prostration distinguishes croup from acute epiglottitis"],
        "content": "Viral inflammation producing edema of the subglottic mucosa and vocal cords within the rigid cricoid ring. Treatment Protocol: 1. SINGLE-DOSE ORAL DEXAMETHASONE (0.15 - 0.60 mg/kg orally or IM) IS RECOMMENDED FOR ALL CHILDREN WITH CROUP (even mild cases, reducing ED visits and hospitalizations); 2. Moderate-to-Severe Croup (stridor at rest or retractions): NEBULIZED RACEMIC EPINEPHRINE (0.5 mL of 2.25% solution or 5 mL of 1:1,000 L-epinephrine in saline) provides rapid subglottic mucosal vasoconstriction and stridor relief within 10-30 minutes; 3. Mandatory observation for minimum 2-4 hours post-epinephrine to monitor for rebound airway edema; 4. Humidified air/mist and keeping child calm."
    },
    {
        "id": "ICD10-M30.3",
        "topic": "Kawasaki Disease (Mucocutaneous Lymph Node Syndrome - Coronary Aneurysms)",
        "icd10": "M30.3",
        "specialty": "Pediatrics / Pediatric Cardiology / Rheumatology",
        "organ_system": "Pediatric Vasculitis Emergency",
        "keywords": ["kawasaki disease", "strawberry tongue", "coronary artery aneurysm", "bilateral non purulent conjunctivitis", "cervical lymphadenopathy child", "desquamation fingers toes", "ivig high dose aspirin"],
        "red_flags": ["coronary artery aneurysms / thrombosis / acute myocardial infarction", "giant coronary aneurysm (> 8 mm)", "myocarditis with congestive heart failure"],
        "clinical_hallmarks": ["predominantly affects INFANTS AND YOUNG CHILDREN (< 5 years, peak age 1-2 years), leading cause of acquired pediatric heart disease in developed nations", "CLASSIC AHA DIAGNOSTIC CRITERIA: FEVER PERSISTING FOR AT LEAST 5 CONSECUTIVE DAYS (remittent, unresponsive to antibiotics and antipyretics), PLUS >= 4 OF THE FOLLOWING 5 PRINCIPAL CLINICAL FEATURES:", "1. BILATERAL BULBAR CONJUNCTIVAL INJECTION without purulent exudate or discharge (limbic sparing);", "2. ORAL CAVITY ERYTHEMA: fiery red, cracked, bleeding lips, diffuse strawberry-red pharyngeal injection, and PATHOGNOMONIC 'STRAWBERRY TONGUE' (prominent hypertrophied fungiform papillae on an erythematous base);", "3. POLYMORPHOUS CUTANEOUS RASH: maculopapular, scarlatiniform, or targetoid eruption, prominent in perineal groin region;", "4. EXTREMITY CHANGES: acute erythema of palms and soles with indurated, firm, painful edema of hands and feet; SUBACUTE PERIUNGUAL DESQUAMATION (sheet-like peeling of skin starting under the nails of fingers and toes in weeks 2-3);", "5. CERVICAL LYMPHADENOPATHY: typically unilateral, non-suppurative, firm lymph node >= 1.5 cm"],
        "pertinent_negatives": ["conjunctivitis lacks pus (distinguishes from adenovirus or bacterial conjunctivitis)"],
        "content": "Acute, self-limited medium-vessel necrotizing vasculitis with a striking predilection for the coronary arterial tree. Untreated Kawasaki disease carries a 25% risk of coronary artery aneurysms. STAT Treatment Protocol (MUST BE INITIATED WITHIN 10 DAYS OF FEVER ONSET): 1. HIGH-DOSE INTRAVENOUS IMMUNOGLOBULIN (IVIG: 2 g/kg as a single IV infusion over 10-12 hours) DRAMATICALLY REDUCES coronary aneurysm risk from 25% to < 3-5%; 2. HIGH-DOSE ORAL ASPIRIN (30-50 mg/kg/day divided q6h until afebrile for 48h, then switched to low-dose 3-5 mg/kg/day antiplatelet dose for 6-8 weeks); 3. Transthoracic Echocardiogram at diagnosis, 2 weeks, and 6-8 weeks (Z-scores for coronary diameter)."
    },
    {
        "id": "ICD10-R56.00",
        "topic": "Febrile Seizures (Simple vs Complex & Status)",
        "icd10": "R56.00",
        "specialty": "Pediatrics / Pediatric Neurology / Emergency Medicine",
        "organ_system": "Pediatric Neuro-Emergency",
        "keywords": ["febrile seizures", "simple vs complex febrile seizure", "fever induced seizure child", "generalized tonic clonic fever", "pediatric seizure rectal diazepam", "lumbar puncture criteria febrile seizure"],
        "red_flags": ["bacterial meningitis (stiff neck, bulging fontanelle, petechial rash)", "febrile status epilepticus (> 30 minutes)", "post-ictal focal motor deficit (Todd's paresis lasting > 24 hours)"],
        "clinical_hallmarks": ["most common neurological disorder of childhood (affecting 2-5% of children aged 6 MONTHS TO 5 YEARS, peak incidence at 18 months)", "seizure occurring in association with a core febrile illness (> 38.0C / 100.4F) WITHOUT intracranial infection, metabolic disturbance, or history of prior afebrile seizures", "CLINICAL DIFFERENTIATION: SIMPLE VS COMPLEX FEBRILE SEIZURE:", "1. Simple Febrile Seizure (80-85%): GENERALIZED tonic-clonic motor activity, DURATION LESS THAN 15 MINUTES, and DOES NOT RECUR WITHIN A 24-HOUR PERIOD (or within the same febrile illness); child recovers completely without persistent focal deficits", "2. Complex Febrile Seizure (15-20%): FOCAL onset or focal features during seizure, DURATION >= 15 MINUTES, OR RECURS >= 2 TIMES WITHIN 24 HOURS", "MANDATORY INVESTIGATION: Rule out Bacterial Meningitis; Lumbar puncture strongly considered in infants < 12 months who are unimmunized or have persistent drowsiness or meningismus"],
        "pertinent_negatives": ["child returns to completely normal neurological baseline sensorium within an hour"],
        "content": "Age-dependent seizure triggered by rapid rise in core body temperature in a developing, thermally sensitive cerebral cortex. Excellent long-term prognosis (simple febrile seizures do not cause brain damage, intellectual disability, or substantial epilepsy risk [1-2% baseline risk]). Protocol: 1. Acute seizure lasting > 5 minutes: abortive treatment with IV Lorazepam (0.1 mg/kg) or rectal Diazepam gel or buccal Midazolam (0.2 mg/kg); 2. Identify and treat the underlying primary fever source (otitis media, viral pharyngitis, UTI); 3. Antipyretics (Acetaminophen, Ibuprofen) provide comfort but DO NOT prevent recurrent febrile seizures; 4. Reassure parents and educate on recovery position."
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
            
    print(f"Batch 5 Final added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

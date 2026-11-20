#!/usr/bin/env python3
"""
Batch 7: Reaches 512 validated ICD-10 protocols.
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
        "id": "ICD10-A80.9",
        "topic": "Acute Poliomyelitis (Enterovirus & Asymmetric Flaccid Paralysis)",
        "icd10": "A80.9",
        "specialty": "Infectious Disease / Pediatrics / Neurology",
        "organ_system": "Neuro-Infectious",
        "keywords": ["poliomyelitis", "polio", "acute flaccid paralysis", "asymmetric flaccid paralysis", "anterior horn cell destruction", "opv ipv vaccine", "tripod sign polio"],
        "red_flags": ["bulbar polio with respiratory arrest", "dysphagia and vocal cord paralysis", "autonomic dysfunction"],
        "clinical_hallmarks": ["history of incomplete immunization in an endemic or outbreak region, spread via fecal-oral transmission", "minor illness: non-specific prodrome of fever, headache, pharyngitis, nausea, and vomiting for 1-3 days", "major illness: abrupt resurgence of high fever followed by severe muscle myalgias, spasms, and ASYMMETRIC, PROXIMAL-PREDOMINANT LOWER EXTREMITY WEAKNESS", "CARDINAL PHYSICAL EXAMINATION SIGNS: 1. PURE LOWER MOTOR NEURON (LMN) WEAKNESS (flaccidity, hypotonia, and total loss of deep tendon reflexes / areflexia); 2. ASYMMETRIC DISTRIBUTION (typically one leg or one arm, proximal muscles weaker than distal); 3. COMPLETE PRESERVATION OF SENSATION (normal light touch and pinprick sensation); 4. Tripod sign (child sits with hands braced behind on bed for spinal support); 5. Positive kiss-the-knee sign (inability to flex neck to touch knee)", "stool viral culture (gold standard): isolation of poliovirus from 2 stool specimens collected 24 hours apart"],
        "pertinent_negatives": ["completely normal sensory examination confirms pure anterior horn cell motor lesion"],
        "content": "Poliovirus infection (Enterovirus C family) with selective tropism for the anterior horn motor neurons of the spinal cord and motor nuclei of the brainstem. Treatment: No curative antiviral therapy exists; Supportive care: Bed rest, gentle analgesia, hot moist packs for muscle spasms, tracheostomy and mechanical ventilation for bulbar respiratory failure; Orthopedic splinting and long-term physiotherapy to minimize contractures; Universal Prevention: Inactivated Poliovirus Vaccine (IPV - Salk) and Bivalent Oral Poliovirus Vaccine (bOPV - Sabin)."
    },
    {
        "id": "ICD10-A05.1",
        "topic": "Botulism (Clostridium Botulinum & Symmetrical Descending Paralysis)",
        "icd10": "A05.1",
        "specialty": "Infectious Disease / Neurology / Critical Care / Toxicology",
        "organ_system": "Neuro-Infectious Toxin Emergency",
        "keywords": ["botulism", "clostridium botulinum", "symmetric descending paralysis", "the 4 ds diplopia dysarthria dysphonia dysphagia", "dilated unreactive pupils", "canned food botulism", "infant honey botulism floppiness"],
        "red_flags": ["acute respiratory failure from diaphragmatic paralysis", "complete paralysis with fully preserved consciousness", "cardiac arrest"],
        "clinical_hallmarks": ["history of consuming home-canned vegetables, cured meats, or fermented fish (Foodborne Botulism) OR infant under 12 months fed raw honey (Infant Botulism / 'floppy baby syndrome')", "CARDINAL PATHOGNOMONIC MOTOR SEQUENCE: SYMMETRICAL, DESCENDING, FLACCID MOTOR PARALYSIS AFFECTING BULBAR MUSCLES FIRST", "THE '4 Ds' OF CRANIAL NERVE BULBAR PALSY: 1. DIPLOPIA (double vision) and ptosis; 2. DYSARTHRIA (slurred speech); 3. DYSPHONIA (hoarse or absent voice); 4. DYSPHAGIA (inability to swallow saliva, choking)", "PATHOGNOMONIC PUPILLARY AND AUTONOMIC FINDING: BILATERALLY FIXED, DILATED PUPILS UNRESPONSIVE TO LIGHT (in > 50-70% of foodborne cases - cholinergic blockade of pupillary sphincter); severe dry mouth (xerostomia), paralytic ileus, and urinary retention", "weakness advances sequentially downward from head/neck -> upper extremities -> respiratory diaphragm -> lower extremities", "ALERT, CLEAR SENSORIUM MAINTAINED THROUGHOUT (patient remains completely awake and mentally intact inside a paralyzed body)"],
        "pertinent_negatives": ["normal sensory examination and preserved consciousness confirm neuromuscular junction toxin"],
        "content": "Most lethal biological toxin known, produced by anaerobic spore-forming Clostridium botulinum. Botulinum neurotoxin is a zinc metalloprotease that cleaves SNARE proteins (SNAP-25, Syntaxin, Synaptobrevin), irreversibly blocking presynaptic acetylcholine exocytosis at neuromuscular junctions. Statutory emergency. Protocol: 1. STAT Emergency Airway Protection and ICU mechanical ventilation based on serial vital capacity; 2. STAT BOTULINUM ANTITOXIN ADMINISTRATION: Equine Heptavalent Botulinum Antitoxin (HBAT: serotypes A-G) for adults OR Botulism Immune Globulin Intravenous (BabyBIG / BIG-IV) for infants (neutralizes circulating free toxin before it binds; does not reverse existing paralysis); 3. Wound debridement + IV Penicillin G for wound botulism; AVOID aminoglycosides."
    },
    {
        "id": "ICD10-B57.0",
        "topic": "Chagas Disease (Trypanosoma Cruzi - Romaña Sign & Megadisease)",
        "icd10": "B57.0",
        "specialty": "Infectious Disease / Cardiology / Gastroenterology",
        "organ_system": "Protozoal Zoonosis",
        "keywords": ["chagas disease", "trypanosoma cruzi", "romana sign", "kissing bug triatomine", "dilated cardiomyopathy chagas", "apical aneurysm chagas", "megaesophagus megacolon", "benznidazole"],
        "red_flags": ["apical left ventricular aneurysm rupture / fatal ventricular tachycardia", "congestive biventricular heart failure", "sigmoid volvulus secondary to megacolon"],
        "clinical_hallmarks": ["transmission via feces of infected triatomine bugs ('kissing bugs' / reduviid bugs) in endemic regions (Latin America) or congenital/transfusion spread", "ACUTE CHAGAS (in 5%): PATHOGNOMONIC ROMAÑA'S SIGN (unilateral, painless, brawny, purplish periorbital edema with conjunctivitis and preauricular lymphadenopathy developing when bug feces is rubbed into eye) OR Chagoma (erythematous subcutaneous skin nodule at bite site)", "CHRONIC CHAGAS (develops decades after initial silent infection in 20-30%):", "1. CARDIAC CHAGAS: progressive Dilated Cardiomyopathy with biventricular heart failure, Right Bundle Branch Block (RBBB) + Left Anterior Fascicular Block (LAFB) on ECG, malignant ventricular arrhythmias, and PATHOGNOMONIC THIN-WALLED APICAL LEFT VENTRICULAR ANEURYSM (apical thinning with mural thrombus formation and high stroke risk);", "2. GASTROINTESTINAL CHAGAS: progressive destruction of the enteric myenteric plexus of Auerbach leading to 'MEGADISEASE': MEGAESOPHAGUS (severe progressive dysphagia and regurgitation mimicking achalasia) and MEGACOLON (intractable severe constipation, fecaloma, and sigmoid volvulus)"],
        "pertinent_negatives": ["apical LV aneurysm with RBBB is the classic signature of Chagasic cardiomyopathy"],
        "content": "Zoonotic protozoan infection caused by Trypanosoma cruzi. Diagnostic workup: Acute: Direct blood smear (motile trypomastigotes); Chronic: Two distinct positive serological assays (ELISA + indirect immunofluorescence). Treatment: 1. Anti-parasitic pharmacotherapy: Benznidazole (5-7 mg/kg/day for 60 days) OR Nifurtimox (8-10 mg/kg/day for 60-90 days) - highly effective in acute, congenital, and early chronic infection; 2. Cardiac: Guideline-directed heart failure therapy, ICD for ventricular tachycardia, anticoagulation for apical aneurysm; 3. GI: Endoscopic pneumatic dilatation / laparoscopic Heller myotomy for megaesophagus; Sigmoidectomy for megacolon."
    },
    {
        "id": "ICD10-B74.9",
        "topic": "Lymphatic Filariasis (Wuchereria Bancrofti - Elephantiasis & DEC)",
        "icd10": "B74.9",
        "specialty": "Infectious Disease / Tropical Medicine / Urology",
        "organ_system": "Lymphatic Parasitic",
        "keywords": ["lymphatic filariasis", "elephantiasis", "wuchereria bancrofti", "hydrocele filarial", "microfilariae nocturnal blood smear", "filarial dance sign", "diethylcarbamazine dec"],
        "red_flags": ["severe secondary bacterial dermatolymphangioadenitis (acute attacks)", "massive disfiguring scrotal elephantiasis", "chyluria (milky white urine) with profound malnutrition"],
        "clinical_hallmarks": ["transmitted by mosquitoes (Culex quinquefasciatus in urban endemic areas, Anopheles in rural zones); endemic in tropical India, Africa, Southeast Asia", "ADULT WORMS LODGE IN THE LYMPHATIC VESSELS, predominantly in the inguinal, scrotal, and lower extremity lymphatic channels", "ACUTE ATTACKS (Dermatolymphangioadenitis - ADLA): high spiking fever, shaking chills, and retrograde lymphangitis (warm, tender red streaks extending DOWN the limb from inflamed regional lymph nodes)", "CHRONIC IRREVERSIBLE PATHOLOGY (THE ELEPHANTIASIS STAGES):", "1. FILARIAL HYDROCELE (most common manifestation in men: massive, chronic, non-transilluminating fluid accumulation within the tunica vaginalis);", "2. ELEPHANTIASIS (massive, grotesque, irreversible brawny non-pitting lymphedema, dermal thickening, hyperkeratosis, verrucous papules, and deep skin folds of the legs, arms, scrotum, or vulva);", "3. CHYLURIA: intermittent passage of milky-white, lipid-rich urine due to rupture of retroperitoneal lymphatic varices into the urinary tract", "diagnostic gold standard: MIDNIGHT / NOCTURNAL PERIPHERAL BLOOD SMEAR (10 PM to 2 AM: microfilariae demonstrate nocturnal periodicity, matching mosquito feeding habits) or Filarial Antigen test (Alere strip); Ultrasound of scrotum shows pathognomonic 'FILARIAL DANCE SIGN' (active motile live adult worms undulating in dilated lymphatics)"],
        "pertinent_negatives": ["blood smear must be collected at night (daytime blood smears have > 90% false negative rate due to microfilarial lung sequestration)"],
        "content": "Tissue nematode infection caused by Wuchereria bancrofti (90%) or Brugia malayi. Pathophysiology involves lymphatic endothelial damage and secondary bacterial streptococcal infections. Protocol: 1. Triple-Drug Mass Drug Administration (IDA regimen): Single-dose oral Ivermectin (200 mcg/kg) + Diethylcarbamazine (DEC: 6 mg/kg) + Albendazole (400 mg) clears microfilariae for > 1 year (CRITICAL: DEC is STRICTLY CONTRAINDICATED in onchocerciasis co-infection due to fatal Mazzotti ocular reaction); 2. Meticulous local limb hygiene (washing with soap/water BID, skin fold care) prevents acute bacterial attacks and halts elephantiasis progression; 3. Surgical hydrocelectomy."
    },
    {
        "id": "ICD10-B16.9",
        "topic": "Acute Hepatitis B Virus Infection (HBsAg, IgM anti-HBc & Serology)",
        "icd10": "B16.9",
        "specialty": "Gastroenterology / Hepatology / Infectious Disease",
        "organ_system": "Viral Hepatic",
        "keywords": ["hepatitis b", "acute hepatitis b", "hbsag positive", "igm anti hbc", "hbeag high infectivity", "anti hbs immunity", "fulminant hepatic failure hbv"],
        "red_flags": ["acute fulminant hepatic failure (coagulopathy INR > 1.5, encephalopathy)", "submassive hepatic necrosis", "progression to chronic hepatitis B with cirrhosis/HCC risk"],
        "clinical_hallmarks": ["transmitted parenterally, sexually, or vertically via blood and bodily fluids; incubation period 30 to 180 days (mean 75 days)", "prodromal serum-sickness-like syndrome (in 10-20%): fever, transient urticarial rash, and symmetrical polyarthralgias (immune complex deposition)", "ICTERIC PHASE: insidious onset of deep fatigue, malaise, anorexia, nausea, dull right upper quadrant discomfort, dark tea-colored urine, and frank scleral/cutaneous icterus", "physical examination: smooth, tender, enlarged liver margin and mild splenomegaly", "laboratory hallmarks: MASSIVE TRANSAMINASE ELEVATION (serum ALT and AST typically > 1,000 - 3,000 IU/L, with ALT > AST)", "PATHOGNOMONIC SEROLOGICAL PROFILE OF ACUTE HEPATITIS B:", "1. Hepatitis B Surface Antigen (HBsAg): FIRST serological marker to appear, indicating active infection;", "2. IgM Antibody to Hepatitis B Core Antigen (IgM anti-HBc): THE ABSOLUTE DIAGNOSTIC MARKER OF ACUTE HBV INFECTION (present in high titer during acute phase and sole marker present during the 'WINDOW PERIOD' when HBsAg has cleared but anti-HBs has not yet appeared);", "3. Hepatitis B e-Antigen (HBeAg): indicates active high-level viral replication and extreme infectivity;", "4. Hepatitis B Surface Antibody (anti-HBs): indicates recovery, clinical cure, and protective lifelong immunity (also sole marker positive after recombinant vaccination)"],
        "pertinent_negatives": ["IgM anti-HBc distinguishes acute hepatitis B from acute flare of chronic hepatitis B (where IgG anti-HBc is present)"],
        "content": "Partially double-stranded DNA virus of the family Hepadnaviridae. Greater than 95% of immunocompetent adults achieve spontaneous clearance and lifelong immunity (by contrast, > 90% of perinatally infected neonates develop chronic HBV). Management: 1. Uncomplicated Acute HBV: Supportive care, rest, adequate hydration, avoidance of alcohol and hepatotoxic drugs; 2. Severe Acute / Fulminant HBV (INR > 1.5, encephalopathy, or protracted course): STAT Oral Nucleoside/Nucleotide Analogue (Entecavir 0.5 mg daily OR Tenofovir alafenamide / TDF) initiated immediately to reduce mortality and need for liver transplant; 3. Universal Prevention: 3-dose recombinant Hepatitis B vaccine + Hepatitis B Immune Globulin (HBIG) administered within 12 hours of birth to infants of HBsAg-positive mothers."
    },
    {
        "id": "ICD10-B17.10",
        "topic": "Acute Hepatitis C Virus Infection (HCV RNA & DAA Cure)",
        "icd10": "B17.10",
        "specialty": "Gastroenterology / Hepatology / Infectious Disease",
        "organ_system": "Viral Hepatic",
        "keywords": ["hepatitis c", "acute hepatitis c", "hcv rna pcr", "anti hcv antibody", "direct acting antivirals daa", "sofosbuvir velpatasvir", "chronic hepatitis c progression"],
        "red_flags": ["high rate of chronicity (75-85% progress to chronic hepatitis C)", "cirrhosis / portal hypertension over 20-30 years", "hepatocellular carcinoma (HCC)"],
        "clinical_hallmarks": ["predominantly transmitted via percutaneous blood exposure: injection drug use (sharing needles/syringes in > 70%), contaminated medical injections, occupational needle-stick injury, or unscreened blood transfusions", "ACUTE INFECTION IS ASYMPTOMATIC IN > 75-80% OF CASES ('the silent epidemic')", "symptomatic acute hepatitis C (20-25%): mild fatigue, low-grade fever, nausea, abdominal discomfort, and jaundice developing 2 to 12 weeks post-exposure", "LABORATORY AND DIAGNOSTIC ALGORITHM:", "1. Hepatitis C Viral RNA by quantitative RT-PCR (HCV RNA): THE EARLIEST AND MOST SENSITIVE DIAGNOSTIC MARKER, detectable in serum within 1 to 2 weeks post-exposure (well before anti-HCV antibodies develop);", "2. Anti-HCV Antibody (ELISA): becomes positive 4 to 12 weeks post-exposure; a positive anti-HCV antibody WITH a positive HCV RNA confirms active viremic infection; a positive antibody with NEGATIVE HCV RNA indicates resolved/cured prior infection;", "serum ALT fluctuates characteristically with episodic spikes", "unlike Hepatitis B, SPONTANEOUS CLEARANCE OCCURS IN ONLY 15-25%; THE REMAINING 75-85% DEVELOP CHRONIC HEPATITIS C"],
        "pertinent_negatives": ["negative anti-HCV antibody DOES NOT rule out acute infection during the first 4-8 weeks; HCV RNA PCR is mandatory for acute diagnosis"],
        "content": "Positive-sense single-stranded enveloped RNA virus of the Flaviviridae family. Modern Revolution in HCV Therapy: Direct-Acting Antivirals (DAAs) achieve Sustained Virologic Response (SVR12 - undetectable HCV RNA 12 weeks post-therapy, representing a COMPLETE CLINICAL AND VIROLOGICAL CURE in > 95-98% of patients across all genotypes). Pan-Genotypic DAA Regimens (First-Line): Oral Sofosbuvir / Velpatasvir (Epclusa: 400/100 mg one tablet daily for 12 weeks) OR Glecaprevir / Pibrentasvir (Mavyret: 3 tablets daily for 8 weeks). No vaccine exists; post-exposure prophylaxis with DAAs is not currently recommended; test HCV RNA at 4 weeks post-exposure."
    },
    {
        "id": "ICD10-B17.2",
        "topic": "Acute Hepatitis E Virus (Waterborne Epidemic & Pregnancy Mortality)",
        "icd10": "B17.2",
        "specialty": "Gastroenterology / Hepatology / Obstetrics / Infectious Disease",
        "organ_system": "Viral Enteric Hepatic",
        "keywords": ["hepatitis e", "acute hepatitis e", "waterborne hepatitis epidemic", "pregnancy high mortality hepatitis e", "fulminant hepatic failure third trimester", "anti hev igm", "fecal oral sewage contamination"],
        "red_flags": ["FULMINANT HEPATIC FAILURE IN PREGNANCY (case fatality rate 20-25% in third trimester)", "obstetric catastrophe: DIC, eclampsia, massive PPH, and intrauterine fetal demise", "chronic HEV in solid-organ transplant recipients"],
        "clinical_hallmarks": ["epidemiological hallmark: LARGE WATERBORNE EPIDEMICS in developing countries (Indian subcontinent, Africa) resulting from fecal contamination of municipal drinking water supplies during monsoon seasons or floodings", "transmission is primarily fecal-oral (Genotypes 1 and 2 in humans); zoonotic transmission via undercooked pork/game meat (Genotypes 3 and 4 in industrialized nations)", "incubation period 2 to 10 weeks (mean 40 days)", "clinical presentation in general population: self-limiting acute icteric hepatitis (fatigue, anorexia, nausea, fever, dark urine, and jaundice with elevated transaminases) with low overall mortality (< 0.5-1%)", "CATASTROPHIC PATHOGNOMONIC VULNERABILITY: EXTREME, UNEXPLAINED HIGH MORTALITY IN PREGNANT WOMEN (approaching 20-25% case fatality rate, peaking in the THIRD TRIMESTER)", "pregnant women experience rapid, catastrophic progression from mild jaundice to FULMINANT HEPATIC FAILURE within days, accompanied by massive hepatic encephalopathy, severe coagulopathy, DIC, and spontaneous abortion / stillbirth", "diagnostic hallmark: Serum anti-HEV IgM antibodies (high specificity) or HEV RNA in stool/serum"],
        "pertinent_negatives": ["does NOT progress to chronic carrier state or cirrhosis in immunocompetent individuals (unlike HBV and HCV)"],
        "content": "Non-enveloped positive-sense RNA virus of the Hepeviridae family. High pregnancy mortality is linked to high viral loads, hormonal changes (progesterone/estrogen downregulating cell-mediated immunity), and altered cytokine profiles. Management: 1. Strict supportive care in ICU for pregnant women with acute HEV; 2. Monitoring of coagulation profile, transaminases, and neurological sensorium; 3. Prompt management of cerebral edema, hypoglycemia, and coagulopathy; 4. Ribavirin (oral 600-1000 mg daily for 12 weeks) is effective for chronic HEV in immunocompromised patients (STRICTLY TERATOGENIC, CONTRAINDICATED IN PREGNANCY); 5. Prevention: Clean drinking water sanitation, boiling water, and recombinant HEV vaccine (Hecolin - approved in China)."
    },
    {
        "id": "ICD10-B05.9",
        "topic": "Measles (Rubeola - Koplik's Spots & The 3 Cs)",
        "icd10": "B05.9",
        "specialty": "Pediatrics / Infectious Disease / Dermatology",
        "organ_system": "Viral Exanthematous Emergency",
        "keywords": ["measles", "rubeola", "the 3 cs cough coryza conjunctivitis", "koplik spots buccal mucosa", "morbilliform rash hairline", "subacute sclerosing panencephalitis sspe", "vitamin a for measles", "mmr vaccine"],
        "red_flags": ["giant cell pneumonia (Hecht pneumonia) and acute respiratory failure", "acute post-measles encephalitis", "Subacute Sclerosing Panencephalitis (SSPE - fatal neurodegeneration years later)"],
        "clinical_hallmarks": ["one of the most highly contagious human infectious diseases known (basic reproduction number R0 = 12-18), spread via aerosolized respiratory droplets", "incubation period 10-14 days", "PRODROMAL CATARRHAL PHASE (3-5 days): high spiking remittent fever (often > 40C / 104F), severe prostration, and THE PATHOGNOMONIC '3 Cs':", "1. COUGH (harsh, dry, hacking brassy cough);", "2. CORYZA (profuse, watery rhinorrhea and nasal congestion);", "3. CONJUNCTIVITIS (intense bilateral conjunctival injection, lacrimation, and marked photophobia)", "PATHOGNOMONIC ENANTHEM: KOPLIK'S SPOTS (appear on days 3-4, 24-48 hours BEFORE the skin rash: tiny, 1-2 mm, pinpoint, bluish-white or gray specks surrounded by an erythematous halo, clustered on the BUCCAL MUCOSA OPPOSITE THE LOWER MOLAR TEETH - likened to 'grains of white salt sprinkled on a red background'; fade within 48 hours)", "EXANTHEM PHASE: a dark red, maculopapular, confluent 'morbilliform' rash that BEGINS AT THE FOREHEAD AND HAIRLINE / BEHIND THE EARS, spreading downward cephalocaudally over 3 days to neck, trunk, and extremities (including palms and soles); fades in same sequence leaving fine branny desquamation and brownish hyperpigmentation"],
        "pertinent_negatives": ["Koplik's spots are 100% pathognomonic for measles (absent in rubella, roseola, or scarlet fever)"],
        "content": "Single-stranded negative-sense RNA virus of the Paramyxoviridae family (Morbillivirus). Diagnostic workup: Measles-specific IgM capture ELISA (detectable within 3 days of rash), throat/nasopharyngeal swab for measles RT-PCR. Treatment Protocol: 1. Strict airborne isolation; Supportive hydration and antipyretics; 2. WHO MANDATORY VITAMIN A PROTOCOL: High-dose oral Vitamin A (50,000 IU for < 6 months; 100,000 IU for 6-11 months; 200,000 IU for >= 12 months, administered IMMEDIATELY ON DIAGNOSIS and repeated the next day) HALVES MEASLES MORTALITY by restoring mucosal integrity and preventing blinding corneal ulceration; 3. Prevention: 2 doses of live attenuated MMR vaccine."
    },
    {
        "id": "ICD10-B26.9",
        "topic": "Mumps (Epidemic Parotitis & Orchitis - Infertility Risk)",
        "icd10": "B26.9",
        "specialty": "Pediatrics / Infectious Disease / Urology",
        "organ_system": "Viral Parotid / Genitourinary",
        "keywords": ["mumps", "epidemic parotitis", "painful parotid swelling", "earlobe pushed upward outward", "mumps orchitis testicular atrophy", "elevated serum amylase mumps", "aseptic meningitis mumps"],
        "red_flags": ["mumps orchitis with testicular atrophy and impaired spermatogenesis / subfertility", "acute mumps pancreatitis (epigastric pain, vomiting)", "sudden permanent sensorineural deafness (unilateral)"],
        "clinical_hallmarks": ["transmitted by direct contact with respiratory droplets or saliva; incubation period 16 to 18 days", "prodrome: low-grade fever, malaise, headache, anorexia, and earache on chewing", "PATHOGNOMONIC SIGN: ACUTE PAINFUL SWELLING OF THE PAROTID GLANDS (PAROTITIS - in > 95% of symptomatic cases, bilateral in 75%, characteristically asymmetric onset)", "physical examination: tender, tense, firm, non-erythematous swelling that obliterates the retromandibular sulcus and PUSHES THE EARLOBE UPWARD AND OUTWARD", "pathognomonic oral sign: erythema, edema, and pouting of STENSEN'S DUCT ORIFICE (on the buccal mucosa opposite the upper second molar tooth)", "exquisite pain triggered by ingesting sour, acidic, or tart foods (lemons) which stimulates salivation against obstructed ducts", "EXTRAPAROTID COMPLICATIONS (predominantly in post-pubertal adolescent/adult males):", "1. MUMPS ORCHITIS (in 20-30% of post-pubertal males): abrupt onset of high fever, chills, and EXCRUCIATING UNILATERAL (or bilateral in 15%) SCROTAL PAIN AND MASSIVE TESTICULAR SWELLING, developing 4-8 days after parotitis; leads to testicular atrophy in 30-50% of affected testes (permanent sterility is rare unless severe bilateral atrophy occurs);", "2. Aseptic Meningitis (in 10-15%);", "3. Acute Pancreatitis (elevated serum lipase confirms pancreatitis; serum amylase is elevated from parotitis alone)"],
        "pertinent_negatives": ["absence of purulent discharge expressed from Stensen's duct upon gentle parotid pressure distinguishes mumps from suppurative bacterial parotitis"],
        "content": "Single-stranded negative-sense RNA virus of the Paramyxoviridae family (Rubulavirus). Diagnostic workup: Mumps IgM ELISA, RT-PCR from buccal swab/saliva, serum amylase and lipase. Treatment: Strictly supportive: 1. Parotitis: Warm or cold compresses, soft diet, avoidance of sour citrus foods, analgesia (Acetaminophen/Ibuprofen); 2. Orchitis: Strict bed rest, snug scrotal support (jockstrap / scrotal sling), ice packs applied for 15-20 min q2h, NSAIDs or short-course oral corticosteroids for severe excruciating swelling; 3. Universal Prevention: 2 doses of live attenuated MMR vaccine."
    },
    {
        "id": "ICD10-B01.9",
        "topic": "Varicella (Chickenpox - Dewdrops on a Rose Petal)",
        "icd10": "B01.9",
        "specialty": "Pediatrics / Infectious Disease / Dermatology",
        "organ_system": "Viral Exanthematous",
        "keywords": ["varicella", "chickenpox", "dewdrops on a rose petal", "pleomorphic rash all stages present", "centripetal rash trunk to face", "intense itching varicella", "varicella pneumonia pregnancy", "varicella zoster immune globulin"],
        "red_flags": ["varicella pneumonia (hypoxemic respiratory failure, especially in adults and pregnancy)", "secondary invasive Group A Streptococcal necrotizing fasciitis", "cerebellar ataxia / post-infectious encephalitis"],
        "clinical_hallmarks": ["primary infection with Varicella-Zoster Virus (VZV / Human Herpesvirus 3), spread via aerosolized respiratory droplets and direct contact with blister fluid; extremely contagious (secondary attack rate > 90%)", "incubation period 10-21 days", "PATHOGNOMONIC MORPHOLOGICAL SIGN: 'DEWDROPS ON A ROSE PETAL' (clear, thin-walled, fragile vesicles resting on an intensely erythematous maculopapular base)", "PATHOGNOMONIC PROGRESSION AND DISTRIBUTION:", "1. PLEOMORPHISM: LESIONS IN ALL STAGES OF DEVELOPMENT ARE PRESENT SIMULTANEOUSLY IN THE SAME ANATOMICAL AREA (macules, papules, clear vesicles, pustules, umbilicated lesions, and crusts seen side-by-side at any given time, arising in recurrent crops over 3-5 days);", "2. CENTRIPETAL DISTRIBUTION: rash begins on the TRUNK AND SCALP, rapidly spreading outward to the face and proximal limbs (in sharp contrast to smallpox which is centrifugal, affecting face and distal limbs);", "intense, troublesome pruritus; lesions frequently involve oral and genital mucous membranes", "contagious window: 1-2 days BEFORE rash onset until ALL VESICLES HAVE COMPLETELY CRUSTED OVER"],
        "pertinent_negatives": ["pleomorphic crops (all stages present simultaneously) definitively rule out smallpox (where all lesions are at the identical stage)"],
        "content": "Double-stranded DNA alphaherpesvirus. Diagnostic workup: Clinical diagnosis, Tzanck smear (multinucleated giant cells), VZV PCR. Treatment: 1. Healthy children < 12 years: Strictly symptomatic (Calamine lotion, oral antihistamines [Diphenhydramine/Cetirizine], cool colloidal oatmeal baths, trimming fingernails to prevent excoriation and secondary staphylococcal/streptococcal impetigo); STRICT AVOIDANCE OF ASPIRIN (precipitates fatal Reye syndrome: encephalopathy and fatty liver); 2. Adolescents, adults, pregnant women, or immunocompromised: Oral Valacyclovir (1000 mg TID for 7 days) OR oral/IV Acyclovir initiated within 24 hours of rash onset; 3. Post-exposure prophylaxis: Varicella Vaccine within 3-5 days or Varicella-Zoster Immune Globulin (VariZIG) within 10 days for high-risk exposed individuals."
    },
    {
        "id": "ICD10-K22.0",
        "topic": "Achalasia Cardia (Bird's-Beak Esophagram & High-Resolution Manometry)",
        "icd10": "K22.0",
        "specialty": "Gastroenterology / Thoracic Surgery",
        "organ_system": "Esophageal Motility Disorder",
        "keywords": ["achalasia", "achalasia cardia", "birds beak sign barium swallow", "high resolution manometry chicago classification", "dysphagia to both solids and liquids", "loss of myenteric plexus nitrergic", "pneumatic dilation hellers myotomy poem"],
        "red_flags": ["pseudoachalasia (gastroesophageal junction adenocarcinoma mimicking achalasia)", "aspiration pneumonia from nocturnal regurgitation", "massive megaesophagus / sigmoid esophagus"],
        "clinical_hallmarks": ["insidious, progressive DYSPHAGIA TO BOTH SOLIDS AND LIQUIDS SIMULTANEOUSLY from symptom onset (in sharp, fundamental contrast to mechanical esophageal obstruction/cancer which begins with solids and only later advances to liquids)", "nocturnal regurgitation of undigested, foul, non-acidic food consumed hours earlier (often soiling the pillow, causing nighttime coughing or choking)", "substernal chest pressure and gradual unintentional weight loss", "Eckardt Clinical Symptom Score (weight loss, dysphagia, retrosternal pain, regurgitation: 0-12)", "Barium Esophagram (PATHOGNOMONIC RADIOGRAPHIC SIGN): dilated, tortuous, aperistaltic esophagus tapering smoothly at the gastroesophageal junction into a sharp, symmetrical 'BIRD'S-BEAK' OR 'RAT-TAIL' APPEARANCE, with delayed emptying into stomach", "HIGH-RESOLUTION ESOPHAGEAL MANOMETRY (DIAGNOSTIC GOLD STANDARD - Chicago Classification v4.0):", "1. Elevated Integrated Relaxation Pressure (IRP > 15 mmHg) indicating failure of Lower Esophageal Sphincter (LES) relaxation; 2. Complete absence of normal coordinated peristalsis in the esophageal body (100% failed peristalsis)"],
        "pertinent_negatives": ["dysphagia to liquids from day one rules out simple peptic esophageal stricture"],
        "content": "Primary esophageal motor disorder characterized by loss of inhibitory nitrergic ganglion cells in the myenteric plexus (Auerbach's plexus) of the distal esophagus and LES, leading to uninhibited cholinergic tone, failure of LES relaxation, and loss of peristalsis. UPPER ENDOSCOPY IS MANDATORY IN ALL PATIENTS to exclude pseudoachalasia (malignancy at GE junction). Definitive Treatment Options: 1. Endoscopic Pneumatic Balloon Dilatation (graded 30, 35, 40 mm balloons disrupting circular LES muscle fibers); 2. Laparoscopic Heller Myotomy (surgical division of LES circular muscle down to mucosa combined with Dor/Toupet partial fundoplication); 3. Per-Oral Endoscopic Myotomy (POEM - endoscopic submucosal tunneling and myotomy); 4. Botulinum toxin injection into LES (reserved for elderly/frail patients unfit for surgery)."
    },
    {
        "id": "ICD10-T40.1X1A",
        "topic": "Acute Opioid Overdose (The Opioid Toxidrome & Naloxone Titration)",
        "icd10": "T40.1X1A",
        "specialty": "Emergency Medicine / Clinical Toxicology / Critical Care",
        "organ_system": "Toxicological Respiratory Emergency",
        "keywords": ["opioid overdose", "heroin fentanyl overdose", "the opioid triad", "pinpoint pupils respiratory depression coma", "naloxone narcan titration", "bag valve mask ventilation", "non cardiogenic pulmonary edema opioid"],
        "red_flags": ["apneic hypoxemic cardiac arrest within minutes", "severe anoxic brain injury", "acute non-cardiogenic pulmonary edema post-resuscitation"],
        "clinical_hallmarks": ["history of recreational illicit opioid abuse (Heroin, Fentanyl, Oxycodone, Methadone, Morphine) or iatrogenic postoperative opioid oversedation", "THE CLASSIC DIAGNOSTIC 'OPIOID TRIAD':", "1. SEVERE RESPIRATORY DEPRESSION (slow, shallow, irregular, or agonal breathing with respiratory rate typically < 8-10 breaths/min, progressing to complete apnea and profound cyanosis);", "2. CNS DEPRESSION (unconsciousness, stupor, or deep unarousable coma);", "3. PINPOINT PUPILS (marked, bilateral, symmetrical, extreme MIOSIS: pupils constricted to < 1-2 mm, responding poorly to light)", "physical examination: cold, clammy skin, profound muscle flaccidity, bradycardia, hypotension, and hypothermia", "PATHOGNOMONIC MONITORING PITFALL: Fentanyl and high-potency synthetic fentanyl analogues can induce acute 'WOODEN CHEST SYNDROME' (severe, rigid chest wall muscle rigidity preventing manual bag-valve-mask ventilation)", "PATHOGNOMONIC THERAPEUTIC RESPONSE: RAPID, COMPLETE REVERSAL OF COMA AND RESUMPTION OF NORMAL SPONTANEOUS RESPIRATION WITHIN 1-3 MINUTES OF INTRAVENOUS OR INTRANASAL NALOXONE"],
        "pertinent_negatives": ["pupils may be normal or dilated if concomitant severe cerebral hypoxia, hypothermia, or co-ingestion with sympathomimetics/anticholinergics"],
        "content": "Agonism of central mu-opioid receptors in the brainstem medullary respiratory center, blunting normal hypercapnic and hypoxemic ventilatory drives. Statutory life-saving emergency. STAT Treatment Protocol: 1. AIRWAY AND VENTILATION FIRST: Immediate Bag-Valve-Mask (BVM) ventilatory support with 100% high-flow oxygen; 2. SPECIFIC COMPETITIVE OPIOID ANTAGONIST: NALOXONE (Narcan): IV/IM/SC/Intranasal (Titrated Dosing Protocol: begin with 0.04 - 0.4 mg IV in non-arrested patients, titrating upward every 2-3 minutes to RESTORE ADEQUATE SPONTANEOUS BREATHING [RR > 10-12/min] WITHOUT precipitating severe, violent acute opioid withdrawal and sympathetic surge; Intranasal Narcan: 4 mg single nasal spray into one nostril for community bystanders); 3. CRITICAL OBSERVATION MANDATE: Naloxone half-life is short (30-90 minutes); long-acting opioids (Methadone, extended-release Oxycodone) frequently outlast naloxone, causing RECURRENT APNEA AND RESEDATION requiring continuous IV Naloxone infusion."
    },
    {
        "id": "ICD10-T39.011A",
        "topic": "Salicylate (Aspirin) Toxicity (Mixed Respiratory Alkalosis & Metabolic Acidosis)",
        "icd10": "T39.011A",
        "specialty": "Clinical Toxicology / Emergency Medicine / Critical Care",
        "organ_system": "Toxicological Metabolic Emergency",
        "keywords": ["salicylate toxicity", "aspirin overdose", "tinnitus deafness nausea", "mixed respiratory alkalosis metabolic acidosis", "urine alkalinization sodium bicarbonate", "hemodialysis for aspirin", "hyperthermia tachypnea"],
        "red_flags": ["cerebral edema and coma (indicates neuroglycopenia and CNS acid toxicity)", "non-cardiogenic pulmonary edema", "severe refractory metabolic acidosis and hyperpyrexia"],
        "clinical_hallmarks": ["history of acute ingestion of > 150 mg/kg of Acetylsalicylic Acid (Aspirin) or chronic ingestion in elderly with renal impairment", "EARLIEST AND MOST COMMON SYMPTOM: TINNITUS (ringing or buzzing in the ears) and subjective mild sensorineural hearing impairment, accompanied by nausea, vomiting, dizziness, and diaphoresis", "PATHOGNOMONIC ARTERIAL BLOOD GAS (ABG) SIGNATURE: MIXED ACID-BASE DISORDER:", "1. Primary RESPIRATORY ALKALOSIS (direct salicylate stimulation of the medullary respiratory center producing rapid, deep hyperventilation / tachypnea, low PaCO2, and early high pH);", "2. Concomitant Primary HIGH ANION GAP METABOLIC ACIDOSIS (HAGMA: uncoupling of oxidative phosphorylation leading to anaerobic glycolysis, accumulation of lactic acid, ketoacids, and salicylate organic acid ions, depressing serum bicarbonate);", "late and severe toxicity signs: hyperpyrexia / hyperthermia (due to uncoupled oxidative phosphorylation dissipating energy as raw heat), marked dehydration, delirium, hallucinations, pulmonary edema, and coma", "laboratory hallmarks: Serum Salicylate Level > 30-40 mg/dL (severe toxicity typically > 80-100 mg/dL); Positive Ferric Chloride urine test (purple color)"],
        "pertinent_negatives": ["normal or near-normal pH on ABG with simultaneously low PaCO2 and low HCO3 confirms a classic mixed respiratory alkalosis / metabolic acidosis"],
        "content": "Salicylate uncouples mitochondrial oxidative phosphorylation, impairs Krebs cycle enzymes, and causes lipid and carbohydrate catabolism. Emergency Treatment Protocol: 1. STAT Gastric Decontamination: Activated Charcoal (1 g/kg orally, repeated in 2-4 hours); 2. URINE ALKALINIZATION (THE MAINSTAY OF MEDICAL MANAGEMENT): IV Sodium Bicarbonate infusion (100-150 mEq NaHCO3 in 1 L D5W at 150-250 mL/hr, maintaining urine pH >= 7.5 - 8.0 and blood pH < 7.55; 'ion-trapping' ionizes salicylate into lipid-insoluble form, preventing CNS entry and accelerating renal clearance by tenfold); 3. MANDATORY Potassium Repletion (hypokalemia prevents urine alkalinization because kidneys exchange H+ for Na+); 4. STAT EMERGENCY HEMODIALYSIS INDICATIONS: Serum salicylate > 90-100 mg/dL acute (> 60 mg/dL chronic), severe acidosis (pH < 7.20), neurological impairment/coma, pulmonary edema, or renal failure."
    },
    {
        "id": "ICD10-T57.8X1A",
        "topic": "Acute Cyanide Poisoning (Bitter Almond Breath & Hydroxocobalamin)",
        "icd10": "T57.8X1A",
        "specialty": "Clinical Toxicology / Emergency Medicine / Critical Care",
        "organ_system": "Cellular Asphyxiant Emergency",
        "keywords": ["cyanide poisoning", "bitter almond breath", "cellular hypoxia normal spo2", "markedly elevated lactic acidosis > 8-10", "hydroxocobalamin cyanokit", "smoke inhalation enclosed fire", "bright red venous blood"],
        "red_flags": ["rapid cardiorespiratory collapse and death within 5-15 minutes", "refractory metabolic acidosis", "seizures and anoxic coma"],
        "clinical_hallmarks": ["history of exposure to smoke inhalation from enclosed structure fires (combustion of polyurethane, synthetic wool, plastics), industrial electroplating, jewelry manufacturing, or ingestion of cyanogenic plants (cassava, apricot kernels / amygdalin)", "abrupt onset within seconds to minutes of inhalation: flushing, rapid tachypnea, severe headache, dizziness, nausea, followed rapidly by convulsions, coma, severe hypotension, and respiratory arrest", "PATHOGNOMONIC CLINICAL ODOR: FAINT 'BITTER ALMOND' ODOR to breath or gastric contents (genetically detectable by only 40-60% of people)", "PATHOGNOMONIC LABORATORY AND METABOLIC HALLMARKS:", "1. SEVERE, EXPLOSIVE ANION GAP LACTIC ACIDOSIS (serum lactate typically > 8-10 mmol/L in smoke inhalation victims is highly sensitive and specific for cyanide toxicity);", "2. NORMAL OR HIGH ARTERIAL PO2 WITH NARROWED ARTERIOVENOUS OXYGEN DIFFERENCE (cells are completely unable to extract oxygen from blood; venous blood remains fully oxygenated, producing bright pink skin and retinal veins appearing as bright red as retinal arteries on fundoscopy)"],
        "pertinent_negatives": ["pulse oximetry and arterial PaO2 remain normal (cellular asphyxiation, NOT arterial hypoxemia)"],
        "content": "Cyanide binds with extreme affinity to the ferric (Fe3+) iron atom of mitochondrial Cytochrome c Oxidase (Complex IV of electron transport chain), completely halting cellular aerobic respiration and ATP production, triggering catastrophic anaerobic metabolism. Statutory emergency. Life-Saving Protocol: 1. STAT 100% High-Flow Oxygen via non-rebreather mask; 2. FIRST-LINE SPECIFIC ANTIDOTE OF CHOICE: HYDROXOCOBALAMIN (Cyanokit: 5 grams IV infusion over 15 minutes; binds cyanide directly to form non-toxic Cyanocobalamin / Vitamin B12, safely excreted in urine; causes harmless transient red discoloration of skin and urine); 3. Alternative Cyanide Antidote Kit (if Cyanokit unavailable): Sodium Nitrite (induces methemoglobinemia which binds cyanide - CONTRAINDICATED in smoke inhalation with carbon monoxide) followed by IV Sodium Thiosulfate."
    },
    {
        "id": "ICD10-T75.00XA",
        "topic": "Lightning Strike Injury (Lichtenberg Figures & Keraunoparalysis)",
        "icd10": "T75.00XA",
        "specialty": "Emergency Medicine / Trauma Surgery / Critical Care",
        "organ_system": "Environmental High-Energy Electrical Emergency",
        "keywords": ["lightning strike", "lichtenberg figures ferning pattern", "keraunoparalysis transient paralysis", "tympanic membrane rupture lightning", "cataracts lightning", "reverse triage lightning", "asystolic cardiac arrest"],
        "red_flags": ["immediate asystolic cardiac arrest", "ventricular fibrillation from R-on-T shock", "hypoxic brain injury"],
        "clinical_hallmarks": ["history of sudden collapse during an outdoor thunderstorm (direct strike, side flash, ground current / step voltage, or contact)", "PATHOGNOMONIC DERMATOLOGICAL SIGN: LICHTENBERG FIGURES (FERN-LIKE / FEATHER-LIKE ARBORESCENT PATTERN: transient, non-palpable, reddish-brown, branching, dendritic cutaneous arborization patterns resembling a fern plant or tree; caused by electron showering along dermal pathways, appearing within 1 hour and completely fading within 24-48 hours)", "PATHOGNOMONIC NEUROLOGICAL SIGN: KERAUNOPARALYSIS (transient, temporary, flaccid paralysis and sensory loss with pale, cold, pulseless extremities, predominantly affecting the lower limbs; caused by extreme autonomic vasospasm, resolving spontaneously within hours)", "BLAST TRAUMA SIGNS: BILATERAL TYMPANIC MEMBRANE RUPTURE (in > 50-80% due to acoustic shock wave) and melted metallic jewelry or scorched clothing", "late ocular complication: BILATERAL LIGHTNING CATARACTS developing months after injury", "REVERSE TRIAGE PROTOCOL: In mass-casualty lightning strikes, VICTIMS WHO APPEAR DEAD (APNEIC AND PULSELESS) RECEIVE PRIORITY RESUSCITATION FIRST ('REVERSE TRIAGE'), because the heart's intrinsic automaticity can spontaneously restart, but persistent diaphragmatic spasm/apnea leads to secondary fatal anoxic arrest unless ventilated immediately"],
        "pertinent_negatives": ["Lichtenberg figures are not true thermal burns and require no surgical debridement"],
        "content": "Massive, instantaneous, direct-current electrical discharge (up to 10-100 million volts, delivering 30,000 amperes in 1/10,000 of a second). Emergency Protocol: 1. IMMEDIATE CPR AND VENTILATION: Aggressive resuscitation of apneic and pulseless victims (high survival rates > 70-80% with immediate CPR); 2. Full Trauma Protocol: Cervical spine immobilization, FAST exam, secondary survey for blast injuries, intracranial hemorrhages, and fractures from violent tetanic muscular contractions; 3. Baseline 12-lead ECG, cardiac enzymes, urinalysis for myoglobinuria; 4. Comprehensive burn care and ophthalmology follow-up."
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
            
    print(f"Batch 7 added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

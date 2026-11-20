#!/usr/bin/env python3
"""
Batch 4B: Obstetrics & Gynecology, Dermatology & STDs, Ophthalmology & ENT.
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
    # --- 10. OBSTETRICS & GYNECOLOGY (14) ---
    {
        "id": "ICD10-O14.90",
        "topic": "Severe Preeclampsia & HELLP Syndrome (Magnesium Sulfate Protocol)",
        "icd10": "O14.90",
        "specialty": "Obstetrics & Gynecology / Maternal-Fetal Medicine",
        "organ_system": "Obstetric Emergency",
        "keywords": ["preeclampsia", "severe preeclampsia", "hellp syndrome", "magnesium sulfate seizure prophylaxis", "proteinuria hypertension pregnancy", "right upper quadrant pain pregnancy", "hyperreflexia clonus pregnancy"],
        "red_flags": ["eclampsia (generalized tonic-clonic convulsions)", "intracranial hemorrhage", "subcapsular liver hematoma rupture", "placental abruption"],
        "clinical_hallmarks": ["new-onset hypertension (Systolic BP >= 140 mmHg or Diastolic BP >= 90 mmHg on two occasions at least 4 hours apart) occurring AFTER 20 WEEKS GESTATION in a previously normotensive woman, with Proteinuria (>= 300 mg/24h or protein-to-creatinine ratio >= 0.3)", "Severe Features: Systolic BP >= 160 mmHg or Diastolic BP >= 110 mmHg, persistent severe frontal headache unresponsive to analgesics, scotomas or visual blurring, intractable right upper quadrant / epigastric pain (hepatic capsule stretch), pulmonary edema, thrombocytopenia (< 100,000 /mcL), serum creatinine > 1.1 mg/dL", "brisk hyperreflexia with sustained patellar/ankle clonus (heralds impending eclamptic seizure)", "HELLP SYNDROME TRIAD: 1. Hemolysis (schistocytes on smear, LDH > 600 U/L, indirect bilirubin > 1.2 mg/dL); 2. Elevated Liver enzymes (AST/ALT >= 2x ULN); 3. Low Platelets (< 100,000 /mcL)"],
        "pertinent_negatives": ["absence of chronic hypertension preceding 20 weeks gestation"],
        "content": "Multisystem disorder of pregnancy characterized by defective spiral artery remodeling leading to placental hypoperfusion, endothelial dysfunction, and widespread vasospasm. Definitive cure is delivery. Emergency Protocol: 1. SEIZURE PROPHYLAXIS: IV Magnesium Sulfate (Zuspan regimen: 4-6 g IV loading dose over 20 min, followed by 1-2 g/hr continuous IV maintenance; monitor patellar reflexes, respiratory rate > 12/min, and urine output > 30 mL/hr; Calcium Gluconate 1g IV is antidote for Mg toxicity); 2. STAT ANTIHYPERTENSIVE THERAPY for BP >= 160/110 mmHg (IV Labetalol 20 mg bolus, IV Hydralazine 5-10 mg, or oral immediate-release Nifedipine 10-20 mg); 3. Delivery indicated at >= 34 weeks, or immediately at any gestational age if maternal/fetal compromise or HELLP syndrome."
    },
    {
        "id": "ICD10-O00.9",
        "topic": "Ruptured Ectopic Pregnancy (Hemoperitoneum & Methotrexate Criteria)",
        "icd10": "O00.9",
        "specialty": "Obstetrics & Gynecology / Emergency Medicine",
        "organ_system": "Gynecologic Emergency",
        "keywords": ["ectopic pregnancy", "ruptured ectopic", "amenorrhea vaginal bleeding belly pain", "cervical motion tenderness", "adnexal mass empty uterus", "beta hcg discriminatory zone", "methotrexate ectopic"],
        "red_flags": ["exsanguinating hemorrhagic shock (hypotension, tachycardia)", "peritoneal peritonism / rigid abdomen", "referred shoulder tip pain (Kehr sign)"],
        "clinical_hallmarks": ["classic clinical triad: 1. Amenorrhea (6-8 weeks of missed period); 2. Vaginal bleeding (often dark brown, spotting, or scant); 3. Unilateral lower abdominal or pelvic pain (sharp, stabbing)", "physical examination: exquisite CERVICAL MOTION TENDERNESS ('chandelier sign') and unilateral tender adnexal mass", "Rupture Signs: sudden tearing abdominal agony, syncope, dizziness, subdiaphragmatic blood irritating phrenic nerve causing REFERRED SHOULDER TIP PAIN (Kehr's sign), abdominal guarding, rebound tenderness, and hypovolemic shock", "Transvaginal Ultrasound (TVUS) + Serum Beta-hCG: ABSENCE OF AN INTRAUTERINE GESTATIONAL SAC when quantitative serum Beta-hCG EXCEEDS THE DISCRIMINATORY ZONE (typically 1,500 - 2,000 mIU/mL), accompanied by a complex extra-uterine adnexal mass with 'ring of fire' Doppler flow and echogenic free fluid in pouch of Douglas"],
        "pertinent_negatives": ["no intrauterine double decidual sac"],
        "content": "Implantation of blastocyst outside the endometrial cavity (> 95% in fallopian tube, commonly ampulla). Statutory gynecological emergency. Protocol: 1. Hemodynamically Unstable or Ruptured: STAT Emergency Laparoscopy or Laparotomy with Salpingectomy + massive transfusion protocol; 2. Hemodynamically Stable Unruptured (Eligible for Medical Management with IM Methotrexate 50 mg/m2 BSA single-dose protocol if: Beta-hCG < 5,000 mIU/mL, unruptured mass < 3.5-4 cm, absence of fetal cardiac activity, and normal renal/liver function); Check hCG on day 4 and 7 (hCG should drop >= 15% between day 4 and 7)."
    },
    {
        "id": "ICD10-O44.00",
        "topic": "Placenta Previa (Painless Third-Trimester Vaginal Bleeding)",
        "icd10": "O44.00",
        "specialty": "Obstetrics & Gynecology / Maternal-Fetal Medicine",
        "organ_system": "Obstetric Bleeding Emergency",
        "keywords": ["placenta previa", "painless vaginal bleeding third trimester", "soft non tender uterus", "marginal complete previa", "no digital pelvic exam", "cesarean delivery previa"],
        "red_flags": ["catastrophic hemorrhagic maternal shock", "fetal bradycardia / exsanguination", "placenta accreta spectrum invasion"],
        "clinical_hallmarks": ["pathognomonic clinical presentation: SUDDEN, UNPROVOKED, PROFUSE, BRIGHT RED VAGINAL BLEEDING occurring in the third trimester (typically after 28 weeks gestation) that is ENTIRELY PAINLESS", "bleeding characteristically starts without warning, often waking the patient from sleep ('sentinel bleed')", "physical examination: UTERUS IS SOFT, RELAXED, AND NON-TENDER (in sharp, fundamental contrast to the rigid, wood-hard, agonizingly tender uterus of placental abruption)", "fetal heart rate pattern is initially reassuring unless maternal hemorrhagic shock supervenes", "high incidence of abnormal fetal lie (transverse, oblique) or floating high unengaged presenting part", "imaging gold standard: Transvaginal Ultrasound (TVUS - completely safe when transducer introduced gently) demonstrates placental tissue overlying or abutting the internal cervical os"],
        "pertinent_negatives": ["DIGITAL VAGINAL EXAMINATION IS STRICTLY CONTRAINDICATED (can dislodge placental cotyledon and provoke catastrophic, fatal hemorrhage) until ultrasound has ruled out previa"],
        "content": "Abnormal implantation of the placenta over or near the internal cervical os. Risk factors: prior cesarean delivery, multiparity, advanced maternal age, prior uterine curettage. Classification: complete (covers internal os), marginal (edge <= 2 cm from os). Management: NPO, large-bore IV access (16G x 2), crossmatch packed red blood cells, continuous fetal monitoring, maternal resuscitation; Corticosteroids (Betamethasone) for fetal lung maturity if < 37 weeks; Delivery: Scheduled Cesarean section at 36-37 weeks (or emergent Cesarean delivery at any gestation for severe intractable hemorrhage); Vigilance for Placenta Accreta Spectrum (PAS)."
    },
    {
        "id": "ICD10-O45.90",
        "topic": "Placental Abruption (Abruptio Placentae & Couvelaire Uterus)",
        "icd10": "O45.90",
        "specialty": "Obstetrics & Gynecology / Emergency Medicine",
        "organ_system": "Obstetric Bleeding Emergency",
        "keywords": ["placental abruption", "abruptio placentae", "painful vaginal bleeding dark blood", "woody hard uterus", "couvelaire uterus", "uterine hypertonus", "dic in abruption"],
        "red_flags": ["catastrophic Disseminated Intravascular Coagulation (DIC)", "fetal demise / severe prolonged fetal bradycardia", "maternal hypovolemic shock out of proportion to visible bleeding"],
        "clinical_hallmarks": ["sudden onset of CONSTANT, SEVERE, AGONIZING ABDOMINAL AND BACK PAIN in the third trimester", "vaginal bleeding with DARK, PORT-WINE OR CLOTTED BLOOD (though 20% of abruptions are 'concealed' where blood is trapped behind placenta without external bleeding)", "pathognomonic physical examination: UTERUS IS EXQUISITELY TENDER, RIGID, HYPERTONIC, AND 'WOOD-LIKE' OR 'BOARD-LIKE' ('WOODY HARD UTERUS')", "uterine tachysystole (frequent, high-frequency, low-amplitude contractions on tocodynamometry)", "fetal distress: severe persistent fetal bradycardia, late decelerations, or intrauterine fetal demise", "maternal shock that is COMPLETELY OUT OF PROPORTION TO VISIBLE EXTERNAL BLEEDING (due to massive concealed retroplacental hematoma)", "Couvelaire uterus (intraoperative finding): widespread myometrial extravasation of blood giving the uterus a purple, bruised, mottled ecchymotic appearance"],
        "pertinent_negatives": ["uterus is rigid and agonizingly tender (distinguishes decisively from painless soft uterus of placenta previa)"],
        "content": "Premature separation of a normally implanted placenta from the uterine myometrial wall before delivery, initiated by hemorrhage into the decidua basalis. Major risk factors: maternal chronic hypertension, preeclampsia, cocaine use, abdominal trauma, rapid uterine decompression. Complications: Consumptive coagulopathy (DIC in 30% of severe abruptions), renal failure, maternal and fetal mortality. Management: STAT emergent resuscitation (large-bore IV access, aggressive fluids, crossmatch 4-6 units PRBCs, FFP, cryoprecipitate for fibrinogen < 150 mg/dL); IMMEDIATE EMERGENCY CESAREAN DELIVERY for viable fetus with fetal distress or maternal instability; Vaginal delivery permitted only if fetal demise has occurred and mother is hemodynamically stable."
    },
    {
        "id": "ICD10-O72.0",
        "topic": "Postpartum Hemorrhage (PPH & The 4 Ts Management)",
        "icd10": "O72.0",
        "specialty": "Obstetrics & Gynecology / Emergency Medicine",
        "organ_system": "Obstetric Hemorrhage Emergency",
        "keywords": ["postpartum hemorrhage", "pph", "the 4 ts tone trauma tissue thrombin", "uterine atony boggy uterus", "oxytocin pph", "bimanual uterine compression", "bakri balloon tamponade"],
        "red_flags": ["exsanguinating maternal hemorrhagic shock", "consumptive coagulopathy / acidosis / hypothermia triad", "peripartum emergency hysterectomy"],
        "clinical_hallmarks": ["ACOG Definition: cumulative blood loss >= 1,000 mL OR blood loss accompanied by signs or symptoms of hypovolemia within 24 hours following delivery (regardless of delivery route)", "THE 4 Ts ETIOLOGICAL MNEMONIC: 1. TONE (Uterine Atony - accounts for 70-80% of PPH: uterus is soft, flaccid, enlarged, poorly contracted, and 'BOGGY' upon fundal palpation); 2. TRAUMA (20%: lacerations of cervix, vagina, perineum, or uterine rupture); 3. TISSUE (10%: retained placental fragments or succenturiate lobe); 4. THROMBIN (1%: coagulopathy, DIC)", "profuse, continuous vaginal blood loss with large clots, accompanied by maternal tachycardia (pulse > 110), hypotension, pallor, cold extremities, and oliguria"],
        "pertinent_negatives": ["firm, well-contracted fundus rules out uterine atony (mandates immediate visual inspection for genital tract lacerations)"],
        "content": "Leading cause of maternal mortality worldwide. Stepwise Management Protocol: 1. Call for multidisciplinary obstetric emergency help STAT; 2. Vigorous Continuous Bimanual Uterine Compression and Fundal Massage; 3. First-line Uterotonic: IV Oxytocin (10-40 units in 500-1000 mL crystalloid infusion at 250-500 mL/hr or 10 units IM); 4. Second-line Uterotonics: Methylergonovine (Methergine 0.2 mg IM - CONTRAINDICATED in hypertension/preeclampsia), Carboprost (Hemabate 15-methyl PGF2-alpha 250 mcg IM - CONTRAINDICATED in asthma), and rectal/sublingual Misoprostol (800-1000 mcg); 5. STAT Tranexamic Acid (TXA: 1g IV within 3 hours); 6. Intrauterine Balloon Tamponade (Bakri balloon filled with 300-500 mL warm saline); 7. Surgical laparotomy: B-Lynch uterine compression sutures, bilateral uterine artery ligation, or emergent Peripartum Hysterectomy."
    },
    {
        "id": "ICD10-E28.2",
        "topic": "Polycystic Ovary Syndrome (PCOS - Rotterdam Diagnostic Criteria)",
        "icd10": "E28.2",
        "specialty": "Obstetrics & Gynecology / Endocrinology",
        "organ_system": "Reproductive Endocrine",
        "keywords": ["polycystic ovary syndrome", "pcos", "rotterdam criteria", "oligomenorrhea hirsutism acne", "string of pearls ovaries", "insulin resistance pcos", "lh fsh ratio 2:1", "metformin pcos"],
        "red_flags": ["endometrial hyperplasia / endometrial adenocarcinoma (from unopposed chronic estrogen)", "metabolic syndrome and Type 2 diabetes mellitus", "gestational diabetes and preeclampsia"],
        "clinical_hallmarks": ["ROTTERDAM CONSENSUS CRITERIA (requires >= 2 of the following 3 features after excluding other etiologies):", "1. Oligo- or Anovulation: irregular, infrequent menstrual cycles (cycles > 35 days or < 8 cycles/year) or secondary amenorrhea", "2. Clinical and/or Biochemical Hyperandrogenism: hirsutism (excessive terminal hair growth in male-pattern distribution: chin, upper lip, chest, linea alba - Ferriman-Gallwey score >= 4-8), severe persistent nodulocystic acne, androgenic alopecia (crown thinning), and elevated serum total or free testosterone", "3. Polycystic Ovarian Morphology on Ultrasound: >= 20 follicles per ovary (measuring 2-9 mm in diameter) and/or increased ovarian volume (>= 10 mL) with characteristic peripheral 'STRING OF PEARLS' distribution surrounding a hyperechoic dense central stroma", "associated metabolic features: central abdominal obesity, Acanthosis Nigricans (velvety hyperpigmented skin tags in neck/axillary folds), and severe insulin resistance"],
        "pertinent_negatives": ["normal 17-OH progesterone (rules out non-classic congenital adrenal hyperplasia) and normal prolactin"],
        "content": "Most common endocrine disorder in women of reproductive age (prevalence 8-13%). Pathophysiology involves neuroendocrine GnRH pulsatility alterations (elevated LH:FSH ratio > 2:1), ovarian theca cell androgen hypersecretion, and hyperinsulinemia. Diagnostic workup: Pelvic ultrasound, total testosterone, DHEA-S, 17-OHP, TSH, Prolactin, 75g 2-hour OGTT, fasting lipid profile. Treatment: 1. Lifestyle modification (5-10% weight loss restores spontaneous ovulation in > 50%); 2. Regulate menses / reduce endometrial cancer risk: Combined Oral Contraceptives (COCs - first-line); 3. Hirsutism: COCs + Spironolactone (anti-androgen); 4. Metabolic: Metformin (insulin sensitizer); 5. Ovulation induction for fertility: Letrozole (aromatase inhibitor - first-line, superior to Clomiphene)."
    },
    {
        "id": "ICD10-N80.9",
        "topic": "Endometriosis & Ovarian Endometrioma (Chocolate Cyst)",
        "icd10": "N80.9",
        "specialty": "Obstetrics & Gynecology / Reproductive Surgery",
        "organ_system": "Gynecologic Proliferative",
        "keywords": ["endometriosis", "chocolate cyst", "ovarian endometrioma", "the 4 ds dysmenorrhea dyspareunia dyschezia dysuria", "infertility endometriosis", "ground glass ovarian cyst", "powder burn lesions"],
        "red_flags": ["ovarian endometrioma rupture with acute chemical peritonitis", "ureteral obstruction and hydronephrosis", "malignant transformation (clear cell/endometrioid ovarian carcinoma)"],
        "clinical_hallmarks": ["CARDINAL SYMPTOM COMPLEX - THE '4 Ds': 1. Severe secondary DYSMENORRHEA (deep pelvic cramping pain that starts 1-2 days before menses, lasts throughout menstruation, and worsens progressively over time); 2. Deep DYSPAREUNIA (sharp, excruciating pain with deep sexual penetration); 3. DYSCHEZIA (painful defecation, rectal tenesmus, or hematochezia during menstruation); 4. DYSURIA (cyclical painful urination or hematuria)", "subfertility / unexplained infertility (in 30-50% of affected women)", "bimanual pelvic examination: tender, fixed, retroverted uterus; exquisite tenderness and nodularity in the pouch of Douglas and uterosacral ligaments; fixed tender adnexal masses", "Pelvic Ultrasound / MRI: Ovarian Endometrioma ('Chocolate Cyst') showing a unilocular, homogenous cyst with LOW-LEVEL INTERNAL 'GROUND-GLASS' ECHOES and absence of internal vascularity on Doppler", "laparoscopy (pathognomonic visual findings): 'powder-burn' or 'gunmetal' bluish-black peritoneal lesions, red flame-like lesions, white fibrous plaques, and dense adhesions obliterating the cul-de-sac"],
        "pertinent_negatives": ["symptoms characteristically fluctuate synchronously with the menstrual cycle"],
        "content": "Presence of functional endometrial glands and stroma outside the uterine cavity, overwhelmingly in dependent pelvic sites (ovaries, uterosacral ligaments, pouch of Douglas). Sampson's retrograde menstruation theory. Treatment: 1. First-line Medical Suppression: Combined Oral Contraceptives or Progestins (oral Dienogest 2 mg daily, depot medroxyprogesterone, or Levonorgestrel-IUD [Mirena]) induce decidualization and atrophy of ectopic implants; 2. Second-line: GnRH agonists/antagonists (Elagolix, Leuprolide) + add-back hormonal therapy; 3. Conservative Laparoscopic Excision / Ablation of endometriotic implants and cystectomy of endometriomas (improves spontaneous fertility and relieves pain); 4. Definitive surgery: Total Hysterectomy with Bilateral Salpingo-Oophorectomy."
    },
    {
        "id": "ICD10-N73.9",
        "topic": "Pelvic Inflammatory Disease (PID & Fitz-Hugh-Curtis Syndrome)",
        "icd10": "N73.9",
        "specialty": "Obstetrics & Gynecology / Infectious Disease",
        "organ_system": "Gynecologic Infectious",
        "keywords": ["pelvic inflammatory disease", "pid", "cervical motion tenderness", "uterine tenderness adnexal tenderness", "purulent cervical discharge", "fitz hugh curtis syndrome", "violin string adhesions"],
        "red_flags": ["tubo-ovarian abscess (toa) rupture with septic peritonitis", "ectopic pregnancy risk increased 7- to 10-fold", "chronic pelvic pain and tubal-factor infertility"],
        "clinical_hallmarks": ["CDC EMPIRIC MINIMAL DIAGNOSTIC CRITERIA (therapy should be initiated in sexually active young women if lower abdominal/pelvic pain is present with >= 1 of the following on bimanual pelvic exam):", "1. CERVICAL MOTION TENDERNESS ('Chandelier sign' - exquisite pain upon lateral manual deflection of cervix); 2. UTERINE TENDERNESS; 3. ADNEXAL TENDERNESS", "additional supporting criteria: purulent or mucopurulent endocervical discharge, friable cervix that bleeds easily with cotton swab, oral temperature > 38.3C, abundant WBCs on saline wet mount of vaginal fluid, and laboratory documentation of cervical Neisseria gonorrhoeae or Chlamydia trachomatis", "FITZ-HUGH-CURTIS SYNDROME (Gonococcal or Chlamydial Perihepatitis): acute onset of sharp, severe RIGHT UPPER QUADRANT (RUQ) pleuritic pain radiating to right shoulder (mimicking acute cholecystitis); Laparoscopy reveals pathognomonic 'VIOLIN-STRING' FIBROUS ADHESIONS connecting the anterior liver capsule to the abdominal wall"],
        "pertinent_negatives": ["negative urine pregnancy test is mandatory to exclude ectopic pregnancy"],
        "content": "Infectious and inflammatory spectrum affecting upper female genital tract (endometritis, salpingitis, tubo-ovarian abscess, pelvic peritonitis), predominantly caused by sexually transmitted pathogens (Chlamydia trachomatis, Neisseria gonorrhoeae) and vaginal anaerobes. Outpatient Regimen: Ceftriaxone 500 mg IM single dose PLUS Doxycycline 100 mg BID for 14 days PLUS Metronidazole 500 mg BID for 14 days; Inpatient Regimen (for TOA, pregnancy, severe vomiting): IV Cefotetan 2g q12h OR IV Cefoxitin 2g q6h PLUS IV Doxycycline 100 mg q12h; MANDATORY examination and treatment of male sexual partners."
    },
    {
        "id": "ICD10-O01.9",
        "topic": "Hydatidiform Mole (Molar Pregnancy & Snowstorm Ultrasound)",
        "icd10": "O01.9",
        "specialty": "Obstetrics & Gynecology / Gynecologic Oncology",
        "organ_system": "Gestational Trophoblastic Disease",
        "keywords": ["hydatidiform mole", "molar pregnancy", "complete vs partial mole", "snowstorm pattern ultrasound", "grape like vesicles vaginal bleeding", "extremely high beta hcg", "theca lutein cysts"],
        "red_flags": ["choriocarcinoma / invasive mole transformation", "maternal thyroid storm (due to massive hCG cross-reacting with TSH receptors)", "early preeclampsia (< 20 weeks)"],
        "clinical_hallmarks": ["abnormal, irregular, painless or crampy vaginal bleeding in first trimester (in > 80% of complete moles)", "pathognomonic macroscopic sign: passage of clear, swollen, fluid-filled, translucent 'GRAPE-LIKE VESICLES' per vaginam", "UTERINE SIZE IS DISPROPORTIONATELY LARGE FOR GESTATIONAL AGE (e.g. fundal height at umbilicus at 10 weeks gestation in complete mole)", "severe, intractable hyperemesis gravidarum (intense vomiting requiring IV fluids)", "early-onset Preeclampsia developing BEFORE 20 WEEKS GESTATION (highly pathognomonic for hydatidiform mole)", "bilateral, massively enlarged, multilocular ovarian THECA LUTEIN CYSTS (due to massive hCG luteinizing ovarian stroma)", "laboratory hallmark: ASTRONOMICALLY HIGH QUANTITATIVE SERUM BETA-hCG (frequently > 100,000 mIU/mL, often reaching 500,000 - 1,000,000 mIU/mL)", "Pelvic Ultrasound (pathognomonic): 'SNOWSTORM' or 'BUNCH OF GRAPES' appearance (diffuse, echogenic intrauterine mass with innumerable microcystic spaces, with COMPLETE ABSENCE OF FETAL PARTS or amniotic sac in complete mole)"],
        "pertinent_negatives": ["absence of fetal heartbeat and absence of fetal skeleton in complete hydatidiform mole"],
        "content": "Gestational trophoblastic disease characterized by abnormal fertilization and hydropic villous hyperplasia. Complete Mole (46,XX diploid, all paternal chromosomes from single sperm duplicating in enucleated ovum); Partial Mole (69,XXY triploid, fertilization of normal ovum by two sperm). Treatment Protocol: 1. STAT Suction Curettage (Suction Dilation and Evacuation - D&E) under ultrasound guidance; 2. Post-evacuation Surveillance: Weekly quantitative serum Beta-hCG monitoring until normal for 3 consecutive weeks, then monthly for 6 months; 3. Strict contraception for 6 months; 4. Rising or plateauing hCG indicates Gestational Trophoblastic Neoplasia (GTN / choriocarcinoma) requiring Single-agent Methotrexate or multi-agent EMA-CO chemotherapy."
    },
    {
        "id": "ICD10-N83.511",
        "topic": "Ovarian Torsion (Adnexal Twisting & Whirlpool Sign)",
        "icd10": "N83.511",
        "specialty": "Obstetrics & Gynecology / Emergency Medicine",
        "organ_system": "Gynecologic Emergency",
        "keywords": ["ovarian torsion", "adnexal torsion", "sudden pelvic pain vomiting", "ovarian whirlpool sign", "enlarged ovary doppler", "detorsion ovary laparoscopy", "dermoid cyst torsion"],
        "red_flags": ["ovarian gangrene and ischemic necrosis if surgical detorsion delayed", "peritonitis and pelvic abscess", "loss of ovary and future fertility"],
        "clinical_hallmarks": ["sudden, acute, excruciating, sharp, unilateral lower quadrant abdominal and pelvic pain, frequently triggered by sudden postural movement, exercise, or coitus", "paroxysmal pain: pain waxes and wanes or occurs in waves as the ovary transiently twists and partially untwists", "PROFOUND, INTRACTABLE NAUSEA AND REPEATED VOMITING present in > 70-85% of cases (due to autonomic visceral stimulation from twisted infundibulopelvic ligament)", "pre-existing ovarian enlargement: > 80% have a benign ovarian cyst or mass measuring >= 5 cm (most frequently a Mature Cystic Teratoma / Dermoid Cyst)", "physical exam: unilateral adnexal tenderness and a palpable tender adnexal mass", "Pelvic Color Doppler Ultrasound: markedly ENLARGED, EDEMATOUS OVARY (volume > 3x contralateral normal ovary) with peripherally displaced antral follicles ('string of pearls' in stroma) and pathognomonic 'WHIRLPOOL SIGN' (twisting of the vascular pedicle in cross-section)"],
        "pertinent_negatives": ["PRESENCE OF NORMAL DOPPLER BLOOD FLOW DOES NOT RULE OUT TORSION (venous occlusion occurs first; arterial flow can remain preserved intermittently)"],
        "content": "Complete or partial rotation of the ovary and fallopian tube on its ligamentous vascular axis (infundibulopelvic and utero-ovarian ligaments), obstructing venous and lymphatic outflow followed by arterial thrombosis and hemorrhagic infarction. Statutory gynecological surgical emergency. Diagnostic Mandate: High clinical suspicion warrants emergent diagnostic laparoscopy even if ultrasound appears equivocal. Management: STAT Emergency Laparoscopy with Ovarian Detorsion (unwinding the twisted vascular pedicle); conservative detorsion and ovarian preservation is indicated REGARDLESS OF OVARY APPEARANCE (even dusky blue/black ovaries often recover endocrine and follicular function); Cystectomy is performed electively after detorsion to prevent recurrence."
    },
    {
        "id": "ICD10-C53.9",
        "topic": "Cervical Carcinoma (High-Risk HPV & Postcoital Bleeding)",
        "icd10": "C53.9",
        "specialty": "Obstetrics & Gynecology / Gynecologic Oncology",
        "organ_system": "Gynecologic Oncology",
        "keywords": ["cervical cancer", "human papillomavirus hpv 16 18", "postcoital bleeding", "pap smear colposcopy", "exophytic cervical mass", "foul smelling vaginal discharge", "radical hysterectomy chemoradiation"],
        "red_flags": ["bilateral hydronephrosis / uremia from ureteral encasement (leading cause of death)", "profuse arterial vaginal hemorrhage", "vesicovaginal or rectovaginal fistula"],
        "clinical_hallmarks": ["early stage disease is frequently asymptomatic (highlighting the critical imperative for regular screening)", "cardinal early symptom: POSTCOITAL VAGINAL BLEEDING (contact spotting or fresh bleeding immediately following sexual intercourse)", "intermenstrual bleeding, postmenopausal bleeding, and a persistent, malodorous, watery, blood-tinged vaginal discharge", "advanced stage: dull pelvic and deep sciatic back pain radiating down leg, lower extremity unilateral edema (lymphatic/venous compression), and hematuria/fecaluria from fistula", "speculum examination: visible exophytic (fungating, friable, cauliflower-like) or endophytic (ulcerative, indurated) lesion on the ectocervix that BLEEDS COPIOUSLY UPON TOUCH", "etiological hallmark: Persistent infection with HIGH-RISK HUMAN PAPILLOMAVIRUS (HPV Type 16 in > 50-60%, HPV Type 18 in 10-15%, expressing oncoproteins E6 [degrades p53] and E7 [inactivates pRb])"],
        "pertinent_negatives": ["normal Pap smear cytology without HPV co-testing has up to 30-40% false negative rate; biopsy of any visible suspicious lesion is MANDATORY regardless of Pap result"],
        "content": "Malignant neoplasm arising from the transformation zone of the cervix, predominantly Squamous Cell Carcinoma (75-80%) or Adenocarcinoma (20-25%). Staging: FIGO Clinical/Pathological Staging (Stage I-IV). Diagnostic workup: Cervical punch biopsy, Colposcopy, Pelvic MRI, PET-CT. Treatment: Early Stage (FIGO IA-IB2): Radical Hysterectomy with Bilateral Pelvic Lymphadenectomy (Wertheim operation); Locally Advanced Stage (FIGO IB3 - IVA): Definitive Concurrent Chemoradiotherapy (CCRT: External Beam Radiotherapy + Intracavitary Brachytherapy + weekly IV Cisplatin); Primary Prevention: 9-valent HPV Vaccine (Gardasil 9) given at age 9-14 years."
    },
    {
        "id": "ICD10-N92.0",
        "topic": "Abnormal Uterine Bleeding (FIGO PALM-COEIN Classification)",
        "icd10": "N92.0",
        "specialty": "Obstetrics & Gynecology / Primary Care",
        "organ_system": "Gynecologic Bleeding",
        "keywords": ["abnormal uterine bleeding", "aub", "palm coein", "menorrhagia heavy menstrual bleeding", "uterine fibroids leiomyoma", "endometrial biopsy pipelle", "tranexamic acid for bleeding"],
        "red_flags": ["endometrial adenocarcinoma in postmenopausal bleeding", "severe symptomatic microcytic anemia (Hb < 6-7 g/dL)", "hemodynamic instability from acute hemorrhage"],
        "clinical_hallmarks": ["FIGO PALM-COEIN ETIOLOGICAL CLASSIFICATION SYSTEM for Abnormal Uterine Bleeding:", "Structural Causes (PALM): 1. POLYP (endometrial/cervical polyps); 2. ADENOMYOSIS (globular enlarged, uniformly tender, 'boggy' uterus); 3. LEIOMYOMA (uterine fibroids - submucosal causing heavy prolonged bleeding, intramural, subserosal); 4. MALIGNANCY and Hyperplasia (endometrial carcinoma - any postmenopausal bleeding is cancer until proven otherwise)", "Non-Structural Causes (COEIN): 1. COAGULOPATHY (Von Willebrand disease in adolescents); 2. OVULATORY Dysfunction (PCOS, thyroid disorders, perimenopause); 3. ENDOMETRIAL (primary hemostatic defect); 4. IATROGENIC (IUDs, anticoagulants); 5. NOT yet classified", "clinical evaluation: soaking through >= 1 sanitary pad/tampon every 1-2 hours for consecutive hours, passage of large blood clots (> 2.5 cm / quarter size), bleeding lasting > 7-8 days, or intermenstrual spotting"],
        "pertinent_negatives": ["pregnancy test MUST ALWAYS BE PERFORMED FIRST to exclude obstetric complications"],
        "content": "Bleeding from the uterine corpus that is abnormal in frequency, regularity, duration, or volume outside of pregnancy. Diagnostic workup: Urine pregnancy test, CBC, ferritin, TSH, Transvaginal ultrasound, Saline Infusion Sonohysterography (SIS), and Pipelle Endometrial Biopsy (mandatory in women >= 45 years, or < 45 years with risk factors like obesity or chronic unopposed estrogen). Treatment: Acute Severe Bleeding: High-dose oral Tranexamic Acid (1.3 g TID) OR high-dose IV conjugated estrogens OR oral medroxyprogesterone; Chronic Long-term: Levonorgestrel-releasing IUD (Mirena - reduces blood loss by > 90%), Combined Oral Contraceptives, Tranexamic acid during menses; Surgical: Hysteroscopic polypectomy/myomectomy, Endometrial Ablation, or Hysterectomy."
    },
    {
        "id": "ICD10-N76.0",
        "topic": "Infectious Vaginitis (Bacterial Vaginosis vs Trichomoniasis vs Candida)",
        "icd10": "N76.0",
        "specialty": "Obstetrics & Gynecology / Primary Care / Infectious Disease",
        "organ_system": "Gynecologic Infectious",
        "keywords": ["vaginitis", "bacterial vaginosis", "clue cells", "trichomoniasis strawberry cervix", "candida vulvovaginitis cottage cheese discharge", "whiff test amine odor", "vaginal ph"],
        "red_flags": ["recurrent intractable candidiasis (screen for diabetes mellitus or HIV)", "bacterial vaginosis in pregnancy (increases risk of preterm labor and prom)", "pelvic inflammatory disease progression"],
        "clinical_hallmarks": ["CLINICAL AND MICROSCOPIC TRIAD DIFFERENTIATION OF INFECTIOUS VAGINITIS:", "1. Bacterial Vaginosis (BV - Gardnerella vaginalis & anaerobes): thin, homogeneous, off-white/gray discharge that smoothly coats vaginal walls; prominent foul 'FISHY' AMINE ODOR accentuated after intercourse; POSITIVE WHIFF TEST (fishy odor on adding 10% KOH); Vaginal pH > 4.5; Saline wet mount shows pathognomonic CLUE CELLS (vaginal squamous epithelial cells studded with adherent bacteria, obscuring cell borders in > 20% of cells) and absent PMNs (Amsel criteria)", "2. Trichomoniasis (Trichomonas vaginalis): profuse, thin, FROTHY, greenish-yellow, malodorous discharge; intense vulvar itching and dysuria; pathognomonic 'STRAWBERRY CERVIX' (colpitis macularis: punctate red cervical petechial hemorrhages); Vaginal pH > 4.5; Wet mount shows MOTILE FLAGELLATED OVAL PROTOZOA and sheets of neutrophils", "3. Candida Vulvovaginitis (Candida albicans): thick, white, curdy, 'COTTAGE CHEESE-LIKE' adherent vaginal discharge; severe, intense vulvar pruritus, burning, and marked vulvar erythema and edema; NORMAL Vaginal pH (< 4.5); Negative Whiff test; 10% KOH prep reveals budding yeast and PSEUDOHYPHAE"],
        "pertinent_negatives": ["normal vaginal pH (< 4.5) points directly to Candida (rules out BV and Trichomonas)"],
        "content": "Most common gynecological diagnosis in primary care. Differential Diagnostic Workup: Vaginal pH paper (litmus), Whiff test, saline wet mount, 10% KOH preparation. Treatment: 1. Bacterial Vaginosis: Oral Metronidazole (500 mg BID for 7 days) OR topical 0.75% Metronidazole gel intravaginally daily for 5 days; 2. Trichomoniasis: Oral Metronidazole (500 mg BID for 7 days - MANDATORY concurrent treatment of male sexual partner, sexual abstinence until treatment completed); 3. Candida: Single-dose Oral Fluconazole (150 mg single dose) or topical Clotrimazole/Miconazole cream."
    },
    {
        "id": "ICD10-N81.4",
        "topic": "Pelvic Organ Prolapse (Cystocele, Rectocele & Uterine Procidentia)",
        "icd10": "N81.4",
        "specialty": "Obstetrics & Gynecology / Urogynecology",
        "organ_system": "Gynecologic Pelvic Floor",
        "keywords": ["pelvic organ prolapse", "pop", "cystocele", "rectocele", "uterine procidentia", "pelvic heaviness bulging mass", "splinting for defecation", "pessary for prolapse"],
        "red_flags": ["complete procidentia with decubitus ulceration and bleeding", "bilateral hydronephrosis from ureteral kinking", "acute urinary retention"],
        "clinical_hallmarks": ["sensation of a vaginal bulge, lump, protrusion, or 'something falling out of the vagina'", "chronic pelvic heaviness, dragging sensation, and lower back pressure that worsens towards the end of the day or after prolonged standing, and relieves upon lying down", "Cystocele (Anterior compartment): urinary hesitancy, slow stream, incomplete emptying, and recurrent cystitis; stress urinary incontinence (or 'masked' incontinence unmasked upon reduction of prolapse)", "Rectocele (Posterior compartment): constipation, difficult defecation, and pathognomonic 'SPLINTING' (patient must use fingers to press against the posterior vaginal wall or perineum to successfully evacuate stool)", "Uterine Procidentia: complete herniation and exteriorization of the entire uterus outside the introitus, showing dry, keratinized, ulcerated vaginal epithelium (decubitus ulcers)", "quantified objectively using the Pelvic Organ Prolapse Quantification (POP-Q) staging system (Stages 0 to IV)"],
        "pertinent_negatives": ["prolapse reduces or softens in supine non-straining position"],
        "content": "Herniation of pelvic organs through the vaginal canal resulting from relaxation and damage to the levator ani muscle complex, endopelvic fascia, and uterosacral/cardinal ligament supports. Risk factors: multiparity, vaginal deliveries, operative deliveries (forceps), obesity, chronic coughing/straining, menopause (loss of estrogen). Management: Mild/asymptomatic: Pelvic floor muscle training (Kegel exercises) and lifestyle modifications; Symptomatic Moderate-Severe: 1. Non-surgical: Vaginal Pessary (ring, Gellhorn, shelf pessary fitted individually) + topical vaginal estrogen cream for mucosal health; 2. Surgical: Anterior/posterior colporrhaphy, Sacrocolpopexy (gold standard for apical prolapse), Sacrospinous ligament fixation, or Colpocleisis (obliterative surgery for frail elderly)."
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
            
    print(f"Batch 4B added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

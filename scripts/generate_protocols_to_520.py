#!/usr/bin/env python3
"""
Generate protocols to expand clinical knowledge base to > 500 validated ICD-10 protocols.
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
    # --- 1. CARDIOVASCULAR & VASCULAR (15) ---
    {
        "id": "ICD10-I71.0",
        "topic": "Acute Aortic Dissection (Stanford Type A / B)",
        "icd10": "I71.0",
        "specialty": "Cardiology / Cardiothoracic Surgery / Emergency Medicine",
        "organ_system": "Cardiovascular Emergency",
        "keywords": ["aortic dissection", "tearing chest pain", "ripping chest pain radiating to back", "unequal blood pressure in arms", "widened mediastinum", "acute aortic syndrome"],
        "red_flags": ["cardiac tamponade", "acute aortic regurgitation murmur", "pulse deficit across extremities", "syncope / paraplegia / stroke"],
        "clinical_hallmarks": ["abrupt onset of excruciating, sharp, 'tearing' or 'ripping' substernal chest pain radiating between shoulder blades into interscapular back", "marked blood pressure differential (> 20 mmHg systolic) between left and right arms", "new diastolic decrescendo murmur of aortic insufficiency", "radio-femoral pulse delay or absent radial/femoral pulses"],
        "pertinent_negatives": ["no st-elevation on ecg typical of transmural myocardial infarction", "no response to sublingual nitroglycerin"],
        "content": "Intimal tear allowing high-pressure arterial blood to cleave aortic media. Stanford Type A involves ascending aorta (surgical emergency); Type B is confined to descending aorta. Diagnosis: Emergent CT Aortogram with contrast (CT Angiography thorax/abdomen) is gold standard; Transesophageal Echocardiogram (TEE) if unstable. Management: Type A requires STAT emergent open surgical repair (graft replacement). Type B: aggressive medical BP and shear stress control with IV beta-blockers (Esmolol / Labetalol targeting systolic BP 100-120 mmHg and HR < 60 bpm) +/- vasodilators (Nitroprusside) and TEVAR for complicated cases."
    },
    {
        "id": "ICD10-I73.9",
        "topic": "Peripheral Artery Disease & Leriche Syndrome",
        "icd10": "I73.9",
        "specialty": "Vascular Surgery / Cardiology",
        "organ_system": "Vascular",
        "keywords": ["peripheral artery disease", "pad", "intermittent claudication", "leg pain walking", "leriche syndrome", "diminished pedal pulses", "ankle brachial index"],
        "red_flags": ["critical limb ischemia (rest pain, gangrene)", "absent pedal pulses with pale cold foot", "non-healing arterial ulcer"],
        "clinical_hallmarks": ["intermittent claudication: reproducible cramping, ache, or fatigue in calves/thighs triggered by walking a set distance and relieved within 2-5 minutes of standing still", "cool, pale, shiny skin on feet with loss of hair and thick brittle toenails", "diminished or absent dorsalis pedis and posterior tibial pulses with delayed capillary refill (> 3s)", "Leriche syndrome triad: bilateral buttock claudication, absent femoral pulses, and erectile dysfunction from aortoiliac occlusion"],
        "pertinent_negatives": ["no venous stasis dermatitis or medial malleolar hyperpigmentation", "no lumbar nerve root radiation (pseudoclaudication)"],
        "content": "Atherosclerotic narrowing of peripheral arteries causing reduced perfusion to extremities. Diagnosis: Resting Ankle-Brachial Index (ABI <= 0.90 confirms PAD; < 0.4 indicates critical limb ischemia); Arterial Duplex Doppler ultrasound and CT Angiography of lower limbs. Treatment: Supervised exercise walking program, Smoking cessation, high-intensity Statin, antiplatelet therapy (Aspirin 75-100 mg or Clopidogrel 75 mg), Cilostazol (100 mg BID for claudication relief); Endovascular angioplasty/stenting or surgical bypass for lifestyle-limiting or limb-threatening ischemia."
    },
    {
        "id": "ICD10-I45.81",
        "topic": "Brugada Syndrome (Sodium Channelopathy - Sudden Cardiac Death)",
        "icd10": "I45.81",
        "specialty": "Cardiology / Electrophysiology",
        "organ_system": "Cardiovascular Arrhythmia",
        "keywords": ["brugada syndrome", "brugada sign", "coved st elevation v1 v2", "sudden cardiac death family history", "syncope during rest or sleep"],
        "red_flags": ["nocturnal agonal respiration / cardiac arrest", "unexplained syncope without prodrome", "polymorphic ventricular tachycardia / vf"],
        "clinical_hallmarks": ["coved-type ST segment elevation (>= 2 mm / 0.2 mV) followed by a negative T wave in >= 1 right precordial leads (V1-V2) positioned in 2nd, 3rd, or 4th intercostal spaces (Type 1 Brugada pattern)", "episodes of unexplained syncope or nocturnal agonal gasping in young, otherwise structurally healthy individuals", "family history of sudden unexplained nocturnal death in young relatives (< 45 years)"],
        "pertinent_negatives": ["no structural heart disease on echocardiogram", "normal coronary arteries on angiography"],
        "content": "Autosomal dominant cardiac channelopathy (most commonly loss-of-function SCN5A mutation encoding Nav1.5 cardiac sodium channel) predisposing to malignant ventricular arrhythmias and sudden cardiac death during sleep or fever. ECG diagnosis: Type 1 coved ST-segment elevation in V1-V2 (spontaneous or unmasked by fever or sodium channel blockers like Ajmaline/Flecainide). Management: Implantable Cardioverter-Defibrillator (ICD) is the only proven preventive therapy for high-risk patients. Strict avoidance of Brugada-triggering drugs (BrugadaDrugs.org), prompt antipyretic treatment of fever, Quinidine for electrical storms."
    },
    {
        "id": "ICD10-I47.1",
        "topic": "Supraventricular Tachycardia (Paroxysmal SVT / AVNRT)",
        "icd10": "I47.1",
        "specialty": "Cardiology / Emergency Medicine",
        "organ_system": "Cardiovascular Arrhythmia",
        "keywords": ["supraventricular tachycardia", "psvt", "avnrt", "sudden fast heart rate", "racing heart 180 bpm", "palpitations with sudden stop", "adenosine for svt"],
        "red_flags": ["hemodynamic instability (hypotension, altered mental status)", "ischemic chest pain during tachycardia", "acute pulmonary edema"],
        "clinical_hallmarks": ["sudden abrupt onset and termination of rapid, regular, intense palpitation ('flip-flop' switch sensation in chest)", "heart rate typically 150-250 bpm with regular rhythm", "narrow QRS complex (< 120 ms) with absent or retrograde P waves buried within or immediately after QRS (pseudo-r' in V1)", "polyuria following attack due to atrial natriuretic peptide (ANP) release"],
        "pertinent_negatives": ["regular rhythm differentiates from atrial fibrillation", "narrow QRS differentiates from ventricular tachycardia"],
        "content": "Re-entrant supraventricular tachyarrhythmia, most commonly AV Nodal Re-entrant Tachycardia (AVNRT 60%) involving dual AV nodal pathways (slow and fast), or AV Reciprocating Tachycardia (AVRT 30% via accessory pathway). Acute management: 1. Hemodynamically unstable: Synchronized DC cardioversion (50-100 J); 2. Hemodynamically stable: Vagal maneuvers (Modified Valsalva maneuver with leg elevation achieves > 40% reversion); if unsuccessful: Rapid IV Adenosine (6 mg rapid IV push followed by 20 mL saline flush; repeat 12 mg if no response); second-line: IV Verapamil or Diltiazem. Long-term definitive cure: Electrophysiology study (EPS) and catheter ablation of slow pathway (> 95% curative)."
    },
    {
        "id": "ICD10-I47.2",
        "topic": "Ventricular Tachycardia (Monomorphic & Polymorphic / Torsades)",
        "icd10": "I47.2",
        "specialty": "Cardiology / Critical Care",
        "organ_system": "Cardiovascular Emergency",
        "keywords": ["ventricular tachycardia", "wide complex tachycardia", "vtach", "torsades de pointes", "av dissociation", "fusion and capture beats"],
        "red_flags": ["pulseless cardiac arrest", "hypotension / cardiogenic shock", "loss of consciousness / syncope", "ischemic chest pain"],
        "clinical_hallmarks": ["regular, rapid wide complex tachycardia (QRS > 120-140 ms, rate 140-250 bpm)", "pathognomonic ECG signs: AV dissociation (P waves marching independently through QRS), capture beats, and fusion beats (Dressler beats)", "extreme axis deviation ('northwest axis'), concordance of QRS polarity across all precordial leads V1-V6", "Torsades de Pointes: polymorphic VT with twisting of QRS peaks around the isoelectric line in patients with prolonged QT interval"],
        "pertinent_negatives": ["absence of typical bundle branch block morphology favors VT over SVT with aberrancy"],
        "content": "Potentially lethal ventricular tachyarrhythmia originating distal to the bundle of His, most frequently secondary to prior myocardial infarction scar, cardiomyopathy, channelopathy, or QT prolongation. Protocol: 1. Pulseless VT: Immediate unsynchronized defibrillation (200 J biphasic) + ACLS; 2. Unstable with pulse: Immediate synchronized cardioversion (100 J); 3. Stable monomorphic VT: IV Amiodarone (150 mg IV over 10 min, then 1 mg/min for 6 hours) or IV Procainamide; 4. Torsades de Pointes: IV Magnesium Sulfate (2 g IV bolus), correct hypokalemia, overdrive pacing/Isoproterenol. Long-term: ICD implantation and antiarrhythmic therapy."
    },
    {
        "id": "ICD10-I31.3",
        "topic": "Pericardial Tamponade (Beck's Triad & Pulsus Paradoxus)",
        "icd10": "I31.3",
        "specialty": "Cardiology / Emergency Medicine / Critical Care",
        "organ_system": "Cardiovascular Emergency",
        "keywords": ["pericardial tamponade", "cardiac tamponade", "becks triad", "pulsus paradoxus", "electrical alternans", "muffled heart sounds"],
        "red_flags": ["obstructive shock with severe hypotension", "cyanosis and altered mental status", "PEA cardiac arrest"],
        "clinical_hallmarks": ["classic Beck's triad: 1. Hypotension with narrowed pulse pressure; 2. Jugular venous distension (elevated JVP with prominent x descent and absent y descent); 3. Muffled, distant heart sounds", "pulsus paradoxus: an abnormally large drop in systolic blood pressure (> 10 mmHg) during inspiration", "ECG shows low-voltage QRS complexes and electrical alternans (beat-to-beat alternation of QRS amplitude due to heart swinging within fluid)", "bedside ultrasound/echo: large pericardial effusion with right ventricular diastolic collapse and dilated IVC without respiratory collapse"],
        "pertinent_negatives": ["no lung crackles/edema (distinguishes from cardiogenic shock caused by LV failure)"],
        "content": "Life-threatening mechanical compression of the heart chambers caused by rapid accumulation of pericardial fluid, impairing diastolic filling and reducing stroke volume. Diagnostic workup: Bedside focused cardiac ultrasound (POCUS) confirms pericardial effusion and chamber collapse. Treatment: Immediate emergency Pericardiocentesis (subxiphoid needle decompression with catheter drainage) or emergent surgical subxiphoid pericardial window. Aggressive volume loading with IV normal saline bolus as temporary temporizing measure to augment preload."
    },
    {
        "id": "ICD10-I33.0",
        "topic": "Infective Endocarditis (Modified Duke Criteria)",
        "icd10": "I33.0",
        "specialty": "Cardiology / Infectious Disease",
        "organ_system": "Cardiovascular Infectious",
        "keywords": ["infective endocarditis", "endocarditis", "duke criteria", "splinter hemorrhages", "osler nodes", "janeway lesions", "new heart murmur with fever"],
        "red_flags": ["acute valvular rupture causing acute pulmonary edema", "septic embolic stroke", "myocardial ring abscess with complete heart block"],
        "clinical_hallmarks": ["persistent unexplained fever in a patient with a prosthetic valve, congenital heart lesion, or history of IV drug use", "new or worsening regurgitant heart murmur (aortic or mitral regurgitation)", "pathognomonic peripheral stigmata: Janeway lesions (painless erythematous macules on palms/soles), Osler nodes (painful violaceous subcutaneous nodules on finger pads), Roth spots (retinal hemorrhages with pale centers), and subungual splinter hemorrhages", "microscopic hematuria and glomerulonephritis from immune complex deposition"],
        "pertinent_negatives": ["no response to brief empiric outpatient oral antibiotic courses"],
        "content": "Microbial infection of endocardial surface, primarily affecting heart valves (native or prosthetic). Modified Duke Criteria: Major (positive blood cultures for typical organisms [S. aureus, Viridans strep, Enterococcus] x 2; positive echo showing oscillating vegetation, abscess, or new dehiscence); Minor (predisposition, fever >= 38.0C, vascular phenomena, immunologic phenomena, microbiologic evidence). Treatment: Prolonged high-dose bactericidal IV antibiotic therapy (Ampicillin/Ceftriaxone + Gentamicin or Vancomycin) for 4-6 weeks; Urgent valve replacement surgery for intractable heart failure, uncontrollable infection, or recurrent embolic events."
    },
    {
        "id": "ICD10-I51.81",
        "topic": "Takotsubo Cardiomyopathy (Stress-Induced Apical Ballooning)",
        "icd10": "I51.81",
        "specialty": "Cardiology",
        "organ_system": "Cardiovascular",
        "keywords": ["takotsubo cardiomyopathy", "broken heart syndrome", "stress cardiomyopathy", "apical ballooning", "catecholamine cardiomyopathy", "chest pain after grief"],
        "red_flags": ["cardiogenic shock", "left ventricular outflow tract (lvot) obstruction", "ventricular free wall rupture"],
        "clinical_hallmarks": ["acute onset ischemic chest pain, dyspnea, and syncope immediately preceded by profound emotional distress (grief, divorce, panic) or severe physical trauma/surgery", "ECG mimicking acute STEMI: anterior ST-segment elevation, subsequent deep symmetrical T-wave inversions, and prolonged QT interval", "echocardiogram reveals pathognomonic apical ballooning with hypercontractile basal segments and akinesia of the mid and apical left ventricle", "absence of obstructive coronary artery disease on urgent coronary angiography"],
        "pertinent_negatives": ["angiography shows clear coronary arteries with no plaque rupture or acute thrombus"],
        "content": "Transient systolic dysfunction of apical and mid-ventricular myocardial segments mimicking acute myocardial infarction, triggered by massive catecholamine surge and microvascular spasm. Predominantly affects postmenopausal women (> 90%). Diagnosis: Mayo Clinic Criteria (transient LV hypokinesis, absence of angiographic obstructive CAD, new ECG changes, modest troponin rise disproportionately low for extent of wall motion abnormality). Management: Supportive hemodynamics, beta-blockers, ACE inhibitors; avoid inotropes if LVOT obstruction is present. Prognosis is generally excellent with recovery of LV function within 4-8 weeks."
    },
    {
        "id": "ICD10-I05.0",
        "topic": "Rheumatic Mitral Stenosis & Atrial Fibrillation",
        "icd10": "I05.0",
        "specialty": "Cardiology",
        "organ_system": "Cardiovascular Valvular",
        "keywords": ["mitral stenosis", "rheumatic heart disease", "opening snap", "mid diastolic murmur", "malar flush", "hemoptysis in mitral stenosis", "left atrial enlargement"],
        "red_flags": ["massive pulmonary hemorrhage from bronchial vein rupture (apoplexy)", "acute thromboembolic stroke from left atrial thrombus", "pulmonary edema triggered by tachycardia"],
        "clinical_hallmarks": ["opening snap (OS) followed by a low-pitched, rumbling mid-diastolic murmur with presystolic accentuation, best heard at apex in left lateral decubitus position with the bell of stethoscope", "loud first heart sound (S1)", "malar flush (pinkish-purple plum discoloration over malar prominences from cutaneous vasoconstriction and cyanosis)", "exertional dyspnea, orthopnea, nocturnal cough, and pink frothy hemoptysis", "frequently complicated by new-onset irregular pulse of Atrial Fibrillation"],
        "pertinent_negatives": ["no systolic ejection murmur or carotid thrill typical of aortic stenosis"],
        "content": "Progressive mechanical narrowing of the mitral valve orifice, overwhelmingly caused by post-streptococcal Rheumatic Heart Disease (RHD) resulting in commissural fusion and calcification. Diagnostic workup: Transthoracic and Transesophageal Echocardiography with Wilkins score (valve area < 1.5 cm2 indicates clinically significant stenosis; < 1.0 cm2 severe). Management: Rate control (Beta-blockers, Digoxin) to prolong diastolic filling time; Anticoagulation (Warfarin, INR 2-3) MANDATORY if atrial fibrillation or prior embolic event; Percutaneous Transvenous Mitral Commissurotomy (PTMC / balloon valvuloplasty) if favorable valve anatomy, or surgical mitral valve replacement."
    },
    {
        "id": "ICD10-I73.00",
        "topic": "Raynaud's Phenomenon (Primary vs Secondary Vasospasm)",
        "icd10": "I73.00",
        "specialty": "Rheumatology / Vascular Medicine",
        "organ_system": "Vascular",
        "keywords": ["raynauds phenomenon", "white blue red fingers", "cold sensitive fingers", "digital vasospasm", "secondary raynauds"],
        "red_flags": ["digital gangrene / tissue necrosis", "digital tip pitted ulcerations", "rapid asymmetric onset in elderly"],
        "clinical_hallmarks": ["classic episodic triphasic digital color changes triggered by cold exposure or emotional stress: 1. Pallor / white (severe arteriolar vasospasm and ischemia); 2. Cyanosis / blue (tissue hypoxia and deoxygenated venous pooling); 3. Rubor / red (reactive hyperemia with throbbing pain and tingling on rewarming)", "sharply demarcated blanching of distal digits of hands and feet", "primary Raynaud (Raynaud disease): symmetric, adolescent onset, normal nailfold capillaroscopy, negative ANA", "secondary Raynaud (Raynaud syndrome): older onset, asymmetric, digital ulcers, abnormal nailfold capillary drop-out, positive ANA (suggests Scleroderma or SLE)"],
        "pertinent_negatives": ["absence of persistent ischemic pain between attacks in primary Raynaud"],
        "content": "Reversible paroxysmal digital vasospasm of small muscular arteries and arterioles. Diagnosis: Clinical diagnosis; Nailfold video-capillaroscopy and autoimmune serology (ANA, Anti-Scl-70, Anti-Centromere) to distinguish primary from secondary Raynaud. Treatment: Lifestyle measures (thermal insulation, hand warmers, avoidance of smoking and sympathomimetics); First-line pharmacotherapy: Dihydropyridine Calcium Channel Blockers (oral Nifedipine 30-60 mg daily or Amlodipine); Topical nitroglycerin; Phosphodiesterase-5 inhibitors (Sildenafil) or IV Iloprost for refractory or ulcerating secondary Raynaud."
    },
    {
        "id": "ICD10-I80.2",
        "topic": "Deep Vein Thrombosis & Phlegmasia Cerulea Dolens",
        "icd10": "I80.2",
        "specialty": "Vascular Surgery / Hematology / Emergency Medicine",
        "organ_system": "Vascular Emergency",
        "keywords": ["deep vein thrombosis", "dvt", "swollen calf", "unilateral leg swelling", "wells score for dvt", "phlegmasia cerulea dolens", "calf tenderness"],
        "red_flags": ["phlegmasia cerulea dolens (massive cyanotic edema with threatened arterial perfusion)", "acute shortness of breath indicating pulmonary embolism", "compartment syndrome"],
        "clinical_hallmarks": ["acute, unilateral, painful calf or entire lower extremity swelling (> 3 cm difference in calf circumference measured 10 cm below tibial tuberosity)", "erythema, warmth, and localized tenderness along deep venous system distribution", "pitting edema restricted to affected extremity", "Phlegmasia Cerulea Dolens: catastrophic fulminant ileofemoral venous thrombosis presenting with massive taut edema, profound violaceous cyanosis, agonizing pain, and impending venous gangrene"],
        "pertinent_negatives": ["absence of bilateral symmetric ankle edema typical of congestive heart failure"],
        "content": "Thrombus formation in deep veins of lower extremity (popliteal, femoral, iliac), governed by Virchow's triad (stasis, endothelial injury, hypercoagulability). Clinical stratification via Wells Score for DVT. Diagnostic workup: High-sensitivity D-Dimer (rules out DVT if low risk); Compression Duplex Venous Ultrasonography (loss of vein compressibility confirms DVT). Treatment: Direct Oral Anticoagulants (DOACs: Apixaban, Rivaroxaban) or LMWH bridged to Warfarin for minimum 3-6 months; Emergent catheter-directed thrombolysis or surgical thrombectomy for Phlegmasia Cerulea Dolens."
    },
    {
        "id": "ICD10-I83.9",
        "topic": "Chronic Venous Insufficiency & Venous Stasis Ulcer",
        "icd10": "I83.9",
        "specialty": "Vascular Surgery / Dermatology",
        "organ_system": "Vascular",
        "keywords": ["chronic venous insufficiency", "varicose veins", "venous stasis ulcer", "stasis dermatitis", "hemosiderin staining", "lipodermatosclerosis", "medial malleolus ulcer"],
        "red_flags": ["secondary bacterial cellulitis", "rapidly enlarging ulcer", "profuse varicose hemorrhage"],
        "clinical_hallmarks": ["chronic bilateral lower extremity heaviness, dull ache, and dependent edema worsening at end of day and relieved by elevation", "dilated, tortuous superficial varicose veins in saphenous distribution", "cutaneous changes: hemosiderin hyperpigmentation (brownish discoloration of lower third of leg), stasis dermatitis (erythematous pruritic scale), and 'champagne bottle' leg (lipodermatosclerosis with wooden induration)", "Venous stasis ulcer: large, shallow, irregular-bordered, exudative ulcer located OVER THE MEDIAL MALLEOLUS with granulating base"],
        "pertinent_negatives": ["punched-out, deep, painful lateral foot ulcer suggests arterial ulcer, not venous"],
        "content": "Venous hypertension and reflux resulting from incompetent valves in superficial, perforator, or deep leg veins. CEAP classification (C1-C6). Diagnostic workup: Duplex Doppler ultrasound mapping of lower extremity venous reflux (> 0.5 sec reflux in superficial veins). Treatment: Graduated compression stockings (30-40 mmHg) is the cornerstone; Leg elevation; Moist wound dressings; Endovenous thermal ablation (EVLA / RFA) or foam sclerotherapy of incompetent saphenous trunks."
    },
    {
        "id": "ICD10-I42.0",
        "topic": "Dilated Cardiomyopathy & Biventricular Systolic Failure",
        "icd10": "I42.0",
        "specialty": "Cardiology",
        "organ_system": "Cardiovascular",
        "keywords": ["dilated cardiomyopathy", "dcm", "systolic heart failure", "reduced ejection fraction", "hfref", "displaced apex beat", "s3 gallop"],
        "red_flags": ["cardiogenic shock", "intractable ventricular arrhythmias", "left ventricular apical mural thrombus with stroke"],
        "clinical_hallmarks": ["progressive exertional dyspnea, orthopnea (pillow elevation needed to sleep), and paroxysmal nocturnal dyspnea (PND)", "laterally and inferiorly displaced diffuse apex beat (hyperdynamic or sustained PMI)", "pathognomonic S3 ventricular filling gallop ('Kentucky' cadence)", "bilateral basal lung crackles, elevated JVP with hepatojugular reflux, and bilateral dependent pitting pedal edema", "echocardiogram reveals four-chamber cardiac enlargement with severe diffuse left ventricular systolic hypokinesis (LVEF < 40%)"],
        "pertinent_negatives": ["no significant coronary artery stenosis on angiography (non-ischemic etiology)"],
        "content": "Myocardial disorder characterized by left ventricular or biventricular enlargement and impaired systolic contractile function not explained by abnormal loading conditions or CAD. Etiologies: genetic (titin/TTN), viral myocarditis, alcohol, peripartum, chemotherapy (doxorubicin). Diagnostic workup: Echocardiography, cardiac MRI (late gadolinium enhancement for fibrosis), BNP/NT-proBNP. Guideline-Directed Medical Therapy (GDMT - The 4 Pillars): 1. ARNI (Sacubitril-Valsartan) or ACEi; 2. Evidence-based Beta-blocker (Carvedilol, Bisoprolol, Metoprolol succinate); 3. Mineralocorticoid Receptor Antagonist (Spironolactone); 4. SGLT2 inhibitor (Dapagliflozin/Empagliflozin); Loop diuretics for congestion; Primary prevention ICD."
    },
    {
        "id": "ICD10-I42.1",
        "topic": "Hypertrophic Cardiomyopathy (HOCM & Dynamic LVOT Obstruction)",
        "icd10": "I42.1",
        "specialty": "Cardiology",
        "organ_system": "Cardiovascular Genetic",
        "keywords": ["hypertrophic cardiomyopathy", "hocm", "asymmetric septal hypertrophy", "systolic anterior motion", "sam mitral valve", "murmur louder with valsalva"],
        "red_flags": ["exertional syncope in young athlete", "family history of premature sudden cardiac death", "non-sustained ventricular tachycardia on holter"],
        "clinical_hallmarks": ["harsh crescendo-decrescendo systolic murmur at left sternal border that INTENSIFIES WITH VALSALVA MANEUVER and standing (decreased preload), and SOFTENS WITH SQUATTING or handgrip (increased preload/afterload)", "bifid carotid pulse (pulsus bisferiens) and prominent 'a' wave in jugular venous pulse", "echocardiogram demonstrates asymmetric septal hypertrophy (interventricular septum to posterior wall ratio > 1.3-1.5) and Systolic Anterior Motion (SAM) of the anterior mitral leaflet producing dynamic LVOT gradient"],
        "pertinent_negatives": ["murmur differs from aortic stenosis which softens with Valsalva and radiates to carotids"],
        "content": "Autosomal dominant genetic cardiac disease caused by sarcomeric protein mutations (MYH7, MYBPC3) causing marked, unexplained myocardial hypertrophy and myofibrillar disarray. Leading cause of sudden cardiac death in young competitive athletes. Treatment: First-line medical: Non-vasodilating Beta-blockers (Metoprolol, Atenolol) or non-dihydropyridine CCBs (Verapamil) to prolong diastole and decrease gradient; Novel cardiac myosin inhibitor (Mavacamten); Surgical septal myectomy or alcohol septal ablation for drug-refractory gradients >= 50 mmHg; ICD for high-risk sudden death prevention."
    },
    {
        "id": "ICD10-I44.2",
        "topic": "Complete Heart Block (Third-Degree Atrioventricular Block)",
        "icd10": "I44.2",
        "specialty": "Cardiology / Emergency Medicine",
        "organ_system": "Cardiovascular Emergency",
        "keywords": ["complete heart block", "third degree av block", "av dissociation", "cannon a waves", "stokes adams attacks", "bradycardia 30 bpm"],
        "red_flags": ["Stokes-Adams syncope / sudden collapse", "hemodynamic collapse / cardiogenic shock", "asystolic ventricular pause > 3 seconds"],
        "clinical_hallmarks": ["profound, fixed bradycardia (typically heart rate 25-45 bpm) refractory to atropine", "intermittent pathognomonic 'cannon a waves' in the jugular venous pulse occurring when atrium contracts against closed tricuspid valve", "varying intensity of the first heart sound (S1) and fluctuating systolic blood pressure", "ECG shows complete AV dissociation: regular P waves marching at one rate, and independent regular wide or narrow QRS complexes marching at a much slower escape rate with NO relationship between P waves and QRS"],
        "pertinent_negatives": ["no constant PR interval (distinguishes from first or second degree block)"],
        "content": "Complete electrical disruption of impulse conduction from atria to ventricles, caused by degenerative conduction disease (Lenegre-Lev disease), acute inferior or anterior MI, hyperkalemia, or drug toxicity (Digoxin, Beta-blockers). Acute emergency management: STAT transcutaneous pacing pads applied; IV Atropine (0.5 mg - 1 mg; often ineffective in infra-nodal block); IV Isoproterenol or Dopamine infusion; Emergency temporary transvenous pacemaker insertion. Definitive long-term treatment: Permanent dual-chamber (DDD) pacemaker implantation."
    },

    # --- 2. PULMONOLOGY & THORACIC (12) ---
    {
        "id": "ICD10-J84.112",
        "topic": "Idiopathic Pulmonary Fibrosis (Usual Interstitial Pneumonia - UIP)",
        "icd10": "J84.112",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "keywords": ["idiopathic pulmonary fibrosis", "ipf", "usual interstitial pneumonia", "uip", "honeycombing lung", "velcro crackles", "dry cough clubbing"],
        "red_flags": ["acute exacerbation of ipf (rapid respiratory failure over days)", "pulmonary hypertension / cor pulmonale"],
        "clinical_hallmarks": ["insidious, progressive exertional breathlessness and chronic non-productive dry hacking cough lasting > 6 months in an older adult (> 60 years)", "bilateral, bibasilar, fine end-inspiratory 'Velcro-like' crackles on auscultation that do not clear with coughing", "prominent digital clubbing (watchglass nails) in > 50% of patients", "High-Resolution CT (HRCT) of thorax demonstrates UIP pattern: subpleural, basilar-predominant reticular opacities with traction bronchiectasis and pathognomonic subpleural honeycombing"],
        "pertinent_negatives": ["no systemic autoimmune features, environmental mold/bird exposure, or drug toxicity"],
        "content": "Specific form of chronic, progressive, fibrosing interstitial pneumonia of unknown cause, limited to lungs. Pulmonary Function Tests (PFTs): Restrictive defect with reduced FVC, preserved FEV1/FVC ratio (> 0.70), and markedly reduced DLCO. Treatment: Antifibrotic pharmacotherapy (Pirfenidone or Nintedanib) slows the rate of FVC decline; Supplemental ambulatory oxygen therapy; Pulmonary rehabilitation; Evaluation for single or bilateral Lung Transplantation."
    },
    {
        "id": "ICD10-D86.0",
        "topic": "Pulmonary Sarcoidosis & Löfgren Syndrome",
        "icd10": "D86.0",
        "specialty": "Pulmonology / Rheumatology",
        "organ_system": "Respiratory / Multisystem Granulomatous",
        "keywords": ["sarcoidosis", "lofgren syndrome", "bilateral hilar lymphadenopathy", "non caseating granulomas", "erythema nodosum ankles", "elevated ace level"],
        "red_flags": ["cardiac sarcoidosis (vt, complete heart block)", "neurosarcoidosis (cranial nerve vii palsy)", "hypercalcemic nephropathy"],
        "clinical_hallmarks": ["Löfgren syndrome acute triad: 1. Bilateral hilar lymphadenopathy on chest radiograph; 2. Erythema nodosum (painful red tender subcutaneous pretibial nodules); 3. Migratory periarthritis/arthritis primarily affecting ankles", "chronic sarcoidosis: insidious dry cough, exertional dyspnea, fatigue, uveitis, and lupus pernio (violaceous indurated plaques on nose/cheeks)", "histopathology reveals non-caseating epithelioid cell granulomas", "elevated serum Angiotensin-Converting Enzyme (ACE) and 1,25-dihydroxyvitamin D causing hypercalcemia"],
        "pertinent_negatives": ["absence of caseous necrosis (distinguishes decisively from tuberculosis)"],
        "content": "Multisystem inflammatory disease characterized by accumulation of non-caseating granulomas composed of CD4+ T-cells and macrophages. Staging by chest radiograph (Stage 0-IV). Diagnostic workup: HRCT chest, Bronchoscopy with endobronchial ultrasound-guided transbronchial needle aspiration (EBUS-TBNA) or lung biopsy, serum ACE, calcium, ECG/cardiac MRI. Treatment: Löfgren syndrome has high spontaneous remission (> 80%) treated with NSAIDs; Progressive symptomatic pulmonary or organ-threatening disease: Oral Prednisone (20-40 mg daily) tapered over 6-12 months; Methotrexate as steroid-sparing agent."
    },
    {
        "id": "ICD10-J47.9",
        "topic": "Bronchiectasis & Cystic Bronchiectasis",
        "icd10": "J47.9",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "keywords": ["bronchiectasis", "tram track sign", "signet ring sign", "copious purulent sputum", "daily sputum production", "hemoptysis in bronchiectasis"],
        "red_flags": ["massive hemoptysis (> 300-500 mL/day)", "respiratory failure with co2 retention", "pseudomonas aeruginosa colonization"],
        "clinical_hallmarks": ["chronic, daily production of copious amounts of foul, purulent, three-layered sputum (top frothy, middle turbid serous, bottom dense purulent sediment)", "recurrent lower respiratory tract infections and recurrent bouts of hemoptysis", "coarse crackles, wheezes, and rhonchi heard predominantly at lung bases", "High-Resolution CT (HRCT) thorax confirms diagnosis: internal bronchoarterial diameter ratio > 1 ('signet ring sign'), lack of bronchial tapering, and parallel line densities ('tram-track sign')"],
        "pertinent_negatives": ["sputum volume and chronicity differentiates from simple acute bronchitis"],
        "content": "Permanent abnormal dilation and destruction of major elastic and muscular bronchi resulting from vicious cycle of chronic infection, impaired mucociliary clearance, and inflammation. Etiologies: post-infectious (measles, pertussis, severe pneumonia, tuberculosis), cystic fibrosis, ciliary dyskinesia, hypogammaglobulinemia. Treatment: Airway clearance techniques (chest physiotherapy, oscillatory positive expiratory pressure devices, hypertonic saline nebulization); Prompt targeted antibiotics for acute exacerbations (guided by sputum culture); Long-term Macrolide (Azithromycin 250 mg 3x/week) for frequent exacerbators; Bronchial artery embolization for massive hemoptysis."
    },
    {
        "id": "ICD10-J93.0",
        "topic": "Tension Pneumothorax (Acute Thoracic Decompression)",
        "icd10": "J93.0",
        "specialty": "Emergency Medicine / Trauma Surgery / Critical Care",
        "organ_system": "Thoracic Emergency",
        "keywords": ["tension pneumothorax", "tracheal deviation", "hyperresonance unilateral", "absent breath sounds", "needle thoracostomy", "distended neck veins chest trauma"],
        "red_flags": ["obstructive shock / cardiac arrest", "severe cyanosis and agonal respirations", "tracheal deviation away from affected side"],
        "clinical_hallmarks": ["sudden onset severe sharp unilateral pleuritic chest pain and rapidly worsening dyspnea in setting of trauma or positive pressure mechanical ventilation", "hyperresonance to percussion and total absence of vesicular breath sounds over affected hemithorax", "tracheal deviation to the CONTRALATERAL (opposite) side", "distended jugular neck veins, tachycardia, severe hypotension, and cyanosis caused by vena caval compression"],
        "pertinent_negatives": ["CLINICAL DIAGNOSIS: DO NOT DELAY LIFE-SAVING TREATMENT TO OBTAIN CHEST RADIOGRAPH"],
        "content": "One-way valve mechanism allowing air into the pleural space during inspiration without escape during expiration, producing progressive intrapleural pressure rise, lung collapse, mediastinal shift, and inferior vena cava compression leading to fatal obstructive shock. Immediate Life-Saving Action: Emergency Needle Decompression (14-16G large-bore cannula inserted into 2nd intercostal space mid-clavicular line, or 5th intercostal space anterior-axillary line) STAT, instantly converting tension into open pneumothorax. Follow immediately by definitive tube thoracostomy (Chest Tube / Intercostal Drain in 5th intercostal space anterior to mid-axillary line connected to underwater seal)."
    },
    {
        "id": "ICD10-J62.8",
        "topic": "Silicosis & Coal Workers' Pneumoconiosis (CWP)",
        "icd10": "J62.8",
        "specialty": "Pulmonology / Occupational Medicine",
        "organ_system": "Respiratory Occupational",
        "keywords": ["silicosis", "pneumoconiosis", "eggshell calcification", "quarry worker lung", "stone cutter cough", "progressive massive fibrosis", "black lung disease"],
        "red_flags": ["silicotuberculosis (active mycobacterial infection)", "progressive massive fibrosis (pmf) with acute respiratory failure"],
        "clinical_hallmarks": ["long occupational history of crystalline silica exposure (sandblasting, quarrying, stonecutting, foundry work, coal mining) typically > 10-20 years", "progressive exertional dyspnea, chronic productive cough, and chest tightness", "chest radiograph: multiple small, rounded opacities (1-3 mm) predominantly distributed in UPPER lung lobes", "pathognomonic 'eggshell calcification' of hilar and mediastinal lymph nodes (calcification rimming node periphery)"],
        "pertinent_negatives": ["absence of acute fever (unless superimposed silicotuberculosis is present)"],
        "content": "Fibronodular lung disease resulting from inhalation and alveolar retention of crystalline silicon dioxide (silica) particles, inducing alveolar macrophage phagocytosis, cytokine storm (IL-1, TNF-alpha), and progressive fibrogenesis. Critical association: Silicosis confers a 30-fold increased risk of Pulmonary Tuberculosis (Silicotuberculosis). Diagnostic workup: Occupational exposure history, Chest X-ray / HRCT, baseline PFTs, annual tuberculin skin test (Mantoux) / IGRA. Treatment: No curative therapy; Complete removal from silica exposure; Preventive therapy for latent TB; Smoking cessation; Pulmonary rehabilitation; Lung transplant evaluation for end-stage PMF."
    },
    {
        "id": "ICD10-J67.0",
        "topic": "Farmer's Lung & Hypersensitivity Pneumonitis (Extrinsic Allergic Alveolitis)",
        "icd10": "J67.0",
        "specialty": "Pulmonology / Allergy & Immunology",
        "organ_system": "Immunologic Respiratory",
        "keywords": ["farmers lung", "hypersensitivity pneumonitis", "extrinsic allergic alveolitis", "moldy hay cough", "bird fanciers lung", "ground glass with air trapping"],
        "red_flags": ["acute hypoxemic respiratory failure", "irreversible honeycombing fibrosis"],
        "clinical_hallmarks": ["acute form: abrupt onset of fever, chills, malaise, dry cough, and dyspnea developing 4-8 hours following intense exposure to organic antigens (moldy hay [thermophilic actinomycetes], bird droppings [avian antigens])", "symptoms resolve spontaneously over 24-48 hours upon removal from exposure, but recur upon re-exposure", "chest auscultation reveals diffuse fine bibasilar inspiratory crackles and mid-inspiratory squeaks", "HRCT thorax: diffuse centrilobular ground-glass opacities, mosaic attenuation, and pathognomonic 'headcheese sign' (combination of ground-glass, normal lung, and air trapping on expiratory CT)"],
        "pertinent_negatives": ["no wheezing or eosinophilia (differentiates from IgE-mediated asthma)"],
        "content": "Immunologically mediated lung disease caused by repetitive inhalation of specific organic aeroantigens in sensitized individuals, involving Type III (immune-complex) and Type IV (cell-mediated) hypersensitivity. Diagnostic workup: Antigen exposure history, serum precipitating IgG antibodies, HRCT, Bronchoalveolar lavage (BAL) showing marked lymphocytosis (often > 50% with low CD4/CD8 ratio). Treatment: Complete and strict antigen avoidance is paramount and often curative in early stages; Oral Corticosteroids (Prednisone 0.5 mg/kg/day tapered over 4-8 weeks) for severe acute/subacute disease to accelerate symptom and physiologic recovery."
    },
    {
        "id": "ICD10-G47.33",
        "topic": "Obstructive Sleep Apnea (OSA & Obesity Hypoventilation)",
        "icd10": "G47.33",
        "specialty": "Pulmonology / Sleep Medicine",
        "organ_system": "Respiratory / Neuro-Sleep",
        "keywords": ["obstructive sleep apnea", "osa", "loud snoring", "choking in sleep", "daytime sleepiness", "epworth sleepiness scale", "apnea hypopnea index"],
        "red_flags": ["motor vehicle accidents due to falling asleep at wheel", "resistant hypertension", "pulmonary hypertension and polycythemia"],
        "clinical_hallmarks": ["partner-reported loud, disruptive, habitual snoring punctuated by observed breathing pauses, gasping, snorting, or choking arousals during sleep", "excessive, unrefreshing daytime sleepiness (falling asleep during driving, meetings, reading) with high Epworth Sleepiness Scale (> 10)", "morning dull frontal headaches, dry mouth, irritability, and cognitive impairment", "physical examination: obesity (BMI > 30), thick neck circumference (> 17 inches in men, > 16 inches in women), crowded oropharynx (Mallampati Class III or IV), and retrognathia"],
        "pertinent_negatives": ["absence of cataplexy or hypnagogic hallucinations (excludes narcolepsy)"],
        "content": "Repetitive episodes of partial (hypopnea) or complete (apnea) upper airway collapse during sleep, resulting in intermittent hypoxemia, hypercapnia, and cortical micro-arousals. Diagnostic gold standard: In-lab Overnight Polysomnography (PSG) measuring Apnea-Hypopnea Index (AHI: mild 5-14, moderate 15-29, severe >= 30 events/hour). Treatment: Continuous Positive Airway Pressure (CPAP) during sleep is the gold standard therapy; Mandibular advancement oral appliances for mild-moderate OSA; Weight reduction (diet, GLP-1 agonists, bariatric surgery); Avoidance of alcohol and sedatives before bed."
    },
    {
        "id": "ICD10-J69.0",
        "topic": "Aspiration Pneumonia & Mendelson Syndrome",
        "icd10": "J69.0",
        "specialty": "Pulmonology / Critical Care / Geriatrics",
        "organ_system": "Respiratory",
        "keywords": ["aspiration pneumonia", "mendelson syndrome", "aspiration pneumonitis", "swallowing difficulty coughing while eating", "foul sputum aspiration", "superior segment lower lobe infiltrate"],
        "red_flags": ["acute respiratory distress syndrome (ards)", "lung abscess formation with putrid sputum", "empyema thoracis"],
        "clinical_hallmarks": ["acute cough, fever, dyspnea, and hypoxemia in a patient with impaired consciousness (alcohol intoxication, stroke, seizures, general anesthesia) or chronic neurogenic dysphagia", "chest radiography: focal infiltrates located classically in the dependent bronchopulmonary segments (superior segment of lower lobes or posterior segment of upper lobes in recumbent patients; right lower lobe basilar segments in upright patients)", "putrid, foul-smelling sputum strongly indicates secondary anaerobic bacterial pulmonary gangrene or abscess", "Mendelson syndrome: acute chemical pneumonitis from massive acidic gastric juice aspiration producing abrupt bronchospasm, cyanosis, and pulmonary edema within 2-4 hours"],
        "pertinent_negatives": ["no anterior upper lobe predominance (atypical for simple gravity-dependent aspiration)"],
        "content": "Pulmonary consequence resulting from inhalation of colonized oropharyngeal secretions (aspiration pneumonia) or sterile acidic gastric contents (chemical pneumonitis / Mendelson syndrome). Polymicrobial etiology including oral streptococci and anaerobes (Peptostreptococcus, Fusobacterium, Prevotella). Treatment: Chemical pneumonitis: supportive oxygen and suctioning (prophylactic antibiotics NOT indicated immediately); Aspiration pneumonia: IV Ampicillin-Sulbactam (1.5-3g q6h) or Amoxicillin-Clavulanate, or Ceftriaxone + Metronidazole (or Clindamycin); Swallowing assessment and speech therapy."
    },
    {
        "id": "ICD10-J86.9",
        "topic": "Empyema Thoracis & Complicated Parapneumonic Effusion",
        "icd10": "J86.9",
        "specialty": "Pulmonology / Thoracic Surgery",
        "organ_system": "Respiratory Infectious",
        "keywords": ["empyema", "complicated parapneumonic effusion", "pus in chest", "loculated pleural effusion", "lights criteria exudate", "pleural fluid ph low"],
        "red_flags": ["septic shock", "trapped lung / fibrothorax", "bronchopleural fistula"],
        "clinical_hallmarks": ["persistent or recrudescent high fever, night sweats, pleuritic chest pain, and failing clinical improvement despite standard pneumonia antibiotic therapy", "dullness to percussion and absent vocal resonance over base of affected hemithorax", "diagnostic thoracentesis reveals frank macroscopic pus or turbid fluid", "pleural fluid biochemical analysis (Light's criteria): pH < 7.20, low glucose (< 40-60 mg/dL), markedly elevated LDH (> 1000 IU/L), and positive Gram stain or culture", "thoracic ultrasound / CT: thick pleural enhancement (split pleura sign) and complex multi-loculations"],
        "pertinent_negatives": ["transudative fluid (normal ph, low ldh) rules out empyema"],
        "content": "Progression of parapneumonic pleural fluid accumulation into an infected, fibrinopurulent collection (complicated parapneumonic effusion) or frank intrapleural pus (empyema). Protocol: 1. Prompt, complete pleural space evacuation via large-bore chest tube thoracostomy (intercostal drain); 2. Empiric IV broad-spectrum antibiotics covering Strep pneumoniae, Staph aureus, and anaerobes (IV Piperacillin-Tazobactam or Ceftriaxone + Metronidazole); 3. Intrapleural fibrinolytic and mucolytic therapy (Tissue Plasminogen Activator [tPA] + rhDNase); 4. Early Video-Assisted Thoracoscopic Surgery (VATS) decortication for loculated or organized empyema."
    },
    {
        "id": "ICD10-A48.1",
        "topic": "Legionnaires' Disease (Legionella Pneumophila - Severe Atypical Pneumonia)",
        "icd10": "A48.1",
        "specialty": "Infectious Disease / Pulmonology",
        "organ_system": "Respiratory Infectious",
        "keywords": ["legionnaires disease", "legionella pneumophila", "pneumonia with diarrhea and confusion", "hyponatremia pneumonia", "fever with relative bradycardia", "hotel air conditioning pneumonia"],
        "red_flags": ["rapidly progressive respiratory failure / ards", "acute renal failure", "delirium / coma"],
        "clinical_hallmarks": ["history of exposure to aerosolized mist from contaminated water reservoirs: hotel cooling towers, air-conditioning systems, hot tubs, or cruise ships", "high remittent fever with relative bradycardia (Faget sign: pulse rate slower than expected for the degree of hyperpyrexia)", "striking extrapulmonary manifestations: prominent watery diarrhea, nausea, vomiting, abdominal pain, and early neurological confusion or encephalopathy out of proportion to fever", "characteristic laboratory abnormalities: profound hyponatremia (serum Na+ < 130 mEq/L from SIADH), elevated transaminases, microhematuria, and marked hypophosphatemia"],
        "pertinent_negatives": ["sputum Gram stain reveals numerous neutrophils but NO predominant bacterial organisms (poorly staining intracellular bacillus)"],
        "content": "Severe form of atypical pneumonia caused by Legionella pneumophila, an intracellular Gram-negative flagellated bacterium. Diagnostic workup: Urine Legionella Antigen test (rapid, detects serogroup 1 with > 95% specificity), sputum Legionella PCR or BCYE agar culture, CBC, electrolytes. Treatment: First-line pharmacotherapy: Fluoroquinolones (IV/oral Levofloxacin 750 mg daily) or Macrolides (IV/oral Azithromycin 500 mg daily) for 7-14 days (21 days in immunocompromised patients). Beta-lactam antibiotics are completely ineffective."
    },
    {
        "id": "ICD10-J43.9",
        "topic": "Alpha-1 Antitrypsin Deficiency & Early-Onset Panacinar Emphysema",
        "icd10": "J43.9",
        "specialty": "Pulmonology / Medical Genetics",
        "organ_system": "Respiratory / Hepatic",
        "keywords": ["alpha 1 antitrypsin deficiency", "aatd", "panacinar emphysema", "early copd non smoker", "basilar emphysema", "pi zz phenotype"],
        "red_flags": ["rapidly declining fev1", "decompensated cirrhosis / portal hypertension", "hepatocellular carcinoma"],
        "clinical_hallmarks": ["early-onset chronic obstructive pulmonary disease (COPD / emphysema) presenting in young patients (< 40-45 years) or in non-smokers or minimal smokers", "progressive exertional dyspnea, wheezing, and hyperinflated barrel chest", "chest radiograph and HRCT thorax demonstrate severe panacinar (panlobular) emphysematous destruction with marked PREDILECTION FOR LOWER LUNG BASES (in contrast to upper-lobe centrilobular emphysema of cigarette smoking)", "concomitant unexplained chronic liver disease, neonatal cholestasis, or cryptogenic cirrhosis"],
        "pertinent_negatives": ["absence of heavy smoking history or advanced age typical of standard copd"],
        "content": "Autosomal co-dominant genetic disorder caused by mutations in the SERPINA1 gene, resulting in deficiency of the protease inhibitor Alpha-1 Antitrypsin (AAT). Uninhibited neutrophil elastase degrades alveolar elastin, destroying alveolar architecture. Phenotypes: PiMM (normal), PiMZ (carrier), PiZZ (severe deficiency). Diagnostic workup: Serum AAT quantitative level (< 11 mcmol/L or < 57 mg/dL confirms deficiency), SERPINA1 genotype/phenotype testing. Treatment: Standard COPD bronchodilators, smoking cessation (smoking drastically accelerates lung destruction); Weekly IV augmentation therapy with human pooled Alpha-1 Proteinase Inhibitor for patients with FEV1 35-65%."
    },
    {
        "id": "ICD10-J98.4",
        "topic": "Bronchopulmonary Aspergillosis (ABPA & Aspergilloma)",
        "icd10": "J98.4",
        "specialty": "Pulmonology / Allergy & Immunology",
        "organ_system": "Respiratory Fungal",
        "keywords": ["allergic bronchopulmonary aspergillosis", "abpa", "aspergilloma", "fungus ball", "brown mucus plugs", "high ige asthma", "monod sign"],
        "red_flags": ["massive life-threatening hemoptysis from aspergilloma", "central bronchiectasis progression"],
        "clinical_hallmarks": ["Allergic Bronchopulmonary Aspergillosis (ABPA): poorly controlled, steroid-dependent severe asthma or cystic fibrosis with recurrent episodic wheezing, fever, fleeting pulmonary infiltrates, and expectoration of brownish mucus plugs", "marked peripheral blood eosinophilia (> 500-1000 cells/mcL) and massively elevated total serum IgE (typically > 1000 IU/mL)", "Aspergilloma (Fungus Ball): preexisting tuberculosis or sarcoid cavity colonized by Aspergillus fumigatus, presenting with recurrent hemoptysis and pathognomonic chest radiograph/CT showing a mobile, rounded intracavitary mass surrounded by a crescent of air ('Monod sign' or 'Air-crescent sign')"],
        "pertinent_negatives": ["no invasive tissue necrosis in immunocompetent host"],
        "content": "Hypersensitivity reaction to Aspergillus colonization (ABPA) or saprophytic growth within pre-existing pulmonary cavities (Aspergilloma). Diagnostic workup: Total serum IgE, Aspergillus-specific IgE/IgG, serum galactomannan, HRCT thorax (central bronchiectasis). Treatment: ABPA: Oral Systemic Corticosteroids (Prednisone 0.5 mg/kg/day tapered over 3-6 months) + Oral Itraconazole (200 mg BID for 16 weeks); Aspergilloma: Surgical cavity resection (lobectomy) for recurrent severe hemoptysis, or bronchial artery embolization."
    },

    # --- 3. GASTROENTEROLOGY & HEPATOBILIARY (16) ---
    {
        "id": "ICD10-K55.0",
        "topic": "Acute Mesenteric Ischemia (Superior Mesenteric Artery Embolism)",
        "icd10": "K55.0",
        "specialty": "Gastroenterology / Vascular Surgery / Emergency Medicine",
        "organ_system": "Gastrointestinal Emergency",
        "keywords": ["acute mesenteric ischemia", "mesenteric infarction", "pain out of proportion to exam", "sma embolism", "gut ischemia", "elevated lactate with belly pain"],
        "red_flags": ["bowel gangrene with peritonitis", "profound lactic acidosis", "septic shock and death"],
        "clinical_hallmarks": ["catastrophic, agonizing, severe diffuse abdominal pain that is STRIKINGLY OUT OF PROPORTION TO PHYSICAL EXAMINATION FINDINGS (abdomen remains soft and non-tender initially despite agonizing distress)", "patient is typically elderly with atrial fibrillation, recent myocardial infarction, or vascular disease", "sudden urgent bowel evacuation ('gut emptying': vomiting and explosive diarrhea) at symptom onset", "late signs (indicating bowel infarction): abdominal distension, rebound peritonitis, bloody diarrhea ('currant jelly' stool), and marked anion gap metabolic acidosis with elevated serum lactate"],
        "pertinent_negatives": ["initially soft abdomen without guarding distinguishes early ischemia from perforated viscus"],
        "content": "Sudden reduction in intestinal blood flow, most commonly (> 50%) due to an embolus lodging in the Superior Mesenteric Artery (SMA) originating from the left atrium in atrial fibrillation. Diagnostic gold standard: Emergency Multidetector CT Angiography (CTA) of the abdomen without oral contrast (shows SMA filling defect, lack of bowel wall enhancement, pneumatosis intestinalis, or mesenteric venous gas). Management: STAT IV resuscitation, broad-spectrum antibiotics, IV Heparin infusion; Emergent surgical laparotomy with embolectomy and resection of non-viable gangrenous bowel, or endovascular revascularization."
    },
    {
        "id": "ICD10-K22.3",
        "topic": "Boerhaave Syndrome (Spontaneous Esophageal Perforation - Mackler Triad)",
        "icd10": "K22.3",
        "specialty": "Gastroenterology / Cardiothoracic Surgery / Emergency Medicine",
        "organ_system": "Thoracogastrointestinal Emergency",
        "keywords": ["boerhaave syndrome", "esophageal perforation", "mackler triad", "vomiting followed by severe chest pain", "subcutaneous emphysema neck", "hamman sign"],
        "red_flags": ["fulminant mediastinitis and septic shock", "tension hydropneumothorax", "cardiorespiratory collapse"],
        "clinical_hallmarks": ["classic Mackler triad: 1. Repeated violent vomiting / retching; 2. Sudden, catastrophic, excruciating retrosternal or epigastric tearing pain; 3. Cervical or thoracic subcutaneous emphysema (crepitus on palpation of neck)", "Hamman sign: crunching, rasping sound synchronous with the heartbeat heard on precordial auscultation due to mediastinal emphysema", "left-sided pleural effusion (frequently showing low pH < 6.0 and high salivary amylase on thoracentesis)", "chest CT with oral contrast: pneumomediastinum, extravasation of water-soluble contrast (Gastrografin) from distal esophagus"],
        "pertinent_negatives": ["Mackler triad distinguishes Boerhaave from simple myocardial infarction or Mallory-Weiss tear"],
        "content": "Spontaneous full-thickness transmural rupture of the esophagus, most frequently occurring in the left posterolateral wall of the distal intrathoracic esophagus, caused by a sudden massive increase in intraluminal pressure against a closed glottis during violent retching. Statutory surgical emergency with mortality approaching 50% if treatment delayed > 24 hours. Diagnosis: Water-soluble Gastrografin swallow or Contrast CT chest. Protocol: NPO, STAT IV broad-spectrum antibiotics, ICU resuscitation; Emergent open thoracotomy or VATS with primary esophageal repair and mediastinal debridement/drainage within 24 hours."
    },
    {
        "id": "ICD10-K22.6",
        "topic": "Mallory-Weiss Syndrome (Mucosal Laceration at Gastroesophageal Junction)",
        "icd10": "K22.6",
        "specialty": "Gastroenterology / Emergency Medicine",
        "organ_system": "Gastrointestinal",
        "keywords": ["mallory weiss tear", "hematemesis after vomiting", "vomiting blood after alcohol binge", "gastroesophageal mucosal tear"],
        "red_flags": ["hypovolemic shock from massive upper gi bleeding", "syncope / orthostasis", "active arterial spurting on endoscopy"],
        "clinical_hallmarks": ["acute onset of painless hematemesis (bright red fresh blood or coffee-ground vomitus) preceded immediately by repeated bouts of non-bloody retching or forceful vomiting", "strongly associated with acute alcohol binge drinking, severe gastroenteritis, or hyperemesis gravidarum", "vital signs: tachycardia or orthostatic hypotension depending on the volume of blood lost", "absence of severe substernal chest pain or mediastinal air (distinguishes decisively from transmural Boerhaave syndrome)"],
        "pertinent_negatives": ["no subcutaneous crepitus, no pneumomediastinum, no peritonitis"],
        "content": "Non-transmural, longitudinal mucosal and submucosal lacerations occurring predominantly at the gastroesophageal junction or gastric cardia, caused by sudden rise in intragastric pressure during violent retching. Accounts for 5-10% of upper GI bleeding cases. Diagnostic workup: Urgent Upper GI Endoscopy (EGD) reveals single or multiple linear mucosal tears with or without active bleeding. Management: Over 80-90% of tears heal spontaneously without intervention; High-dose IV Proton Pump Inhibitor (Pantoprazole 80 mg bolus + 8 mg/hr infusion); Endoscopic intervention (hemoclip placement, multipolar electrocoagulation, or band ligation) for active spurting."
    },
    {
        "id": "ICD10-K74.3",
        "topic": "Primary Biliary Cholangitis (PBC - Anti-Mitochondrial Antibodies)",
        "icd10": "K74.3",
        "specialty": "Gastroenterology / Hepatology",
        "organ_system": "Hepatobiliary Autoimmune",
        "keywords": ["primary biliary cholangitis", "pbc", "antimitochondrial antibodies", "ama positive", "pruritus and jaundice", "elevated alkaline phosphatase female", "xanthomas"],
        "red_flags": ["decompensated biliary cirrhosis (variceal bleed, ascites)", "severe osteoporosis with pathological fractures"],
        "clinical_hallmarks": ["striking female predominance (female-to-male ratio 9:1), characteristically presenting in middle-aged women (40-60 years)", "insidious, debilitating pruritus (intense itching, often worst at night on palms and soles) and profound chronic fatigue", "cutaneous signs of chronic cholestasis: xanthelasma around eyelids, palmar/plantar planar xanthomas, and excoriations from scratching", "laboratory hallmark: isolated, marked elevation of serum Alkaline Phosphatase (ALP) and Gamma-Glutamyl Transferase (GGT) with normal or mildly elevated transaminases", "serological hallmark: Anti-Mitochondrial Antibodies (AMA - M2 subtype) positive in > 95% of patients"],
        "pertinent_negatives": ["normal extrahepatic bile ducts on ultrasound / MRCP rules out gallstone obstruction"],
        "content": "Chronic, progressive autoimmune cholestatic liver disease characterized by T-lymphocyte-mediated destruction of small interlobular bile ducts, leading to cholestasis, progressive fibrosis, and cirrhosis. Diagnostic criteria (2 of 3 needed): 1. Biochemical evidence of cholestasis (elevated ALP); 2. Positive AMA titre >= 1:40; 3. Compatible liver histology (florid duct lesions). Treatment: Ursodeoxycholic Acid (UDCA: 13-15 mg/kg/day) is the first-line therapy (delays progression and prolongs transplant-free survival); Obeticholic acid or Bezafibrate for UDCA non-responders; Liver transplantation for end-stage cirrhosis."
    },
    {
        "id": "ICD10-K83.01",
        "topic": "Primary Sclerosing Cholangitis (PSC & Ulcerative Colitis)",
        "icd10": "K83.01",
        "specialty": "Gastroenterology / Hepatology",
        "organ_system": "Hepatobiliary Autoimmune",
        "keywords": ["primary sclerosing cholangitis", "psc", "beaded bile ducts on mrcp", "ulcerative colitis liver", "cholangiocarcinoma risk", "p-anca cholestasis"],
        "red_flags": ["cholangiocarcinoma (malignant bile duct obstruction)", "bacterial ascending cholangitis", "variceal hemorrhage"],
        "clinical_hallmarks": ["strong male predominance (male-to-female ratio 2:1), presenting between ages 30-50", "overwhelming association with Inflammatory Bowel Disease (> 70-80% have concomitant Ulcerative Colitis)", "insidious onset of fatigue, intermittent jaundice, right upper quadrant pain, pruritus, and recurrent episodes of ascending bacterial cholangitis", "Magnetic Resonance Cholangiopancreatography (MRCP) reveals pathognomonic 'string-of-beads' or 'beaded' appearance: multifocal, segmental, annular stricturing and dilations involving BOTH intrahepatic and extrahepatic bile ducts", "serology: atypical p-ANCA positive in up to 80%"],
        "pertinent_negatives": ["negative AMA distinguishes decisively from Primary Biliary Cholangitis"],
        "content": "Chronic, progressive cholestatic liver disease characterized by diffuse fibrosing inflammation and obliterative obliteration of intrahepatic and extrahepatic biliary tree, progressing to biliary cirrhosis and end-stage liver failure. High lifetime risk of Cholangiocarcinoma (10-15%) and Colorectal Carcinoma. Diagnostic gold standard: MRCP or ERCP showing multifocal strictures and beading; Liver biopsy shows pathognomonic periductal 'onion-skin' fibrosis. Treatment: Endoscopic balloon dilatation of dominant strictures; Annual colonoscopy surveillance for CRC; Annual CA 19-9 and imaging for cholangiocarcinoma; Liver transplantation is the only curative intervention."
    },
    {
        "id": "ICD10-E83.01",
        "topic": "Wilson's Disease (Hepatolenticular Degeneration - Copper Overload)",
        "icd10": "E83.01",
        "specialty": "Gastroenterology / Neurology / Medical Genetics",
        "organ_system": "Metabolic / Hepato-Neuro",
        "keywords": ["wilson disease", "hepatolenticular degeneration", "kayser fleischer rings", "low ceruloplasmin", "copper toxicity", "wing beating tremor", "coombs negative hemolytic anemia"],
        "red_flags": ["acute fulminant hepatic failure with coombs-negative hemolytic anemia", "severe dystonia and pseudo-bulbar palsy"],
        "clinical_hallmarks": ["bimodal presentation: hepatic disease in children/adolescents (unexplained acute hepatitis, cirrhosis) vs neuropsychiatric manifestations in young adults (tremor, dystonia, parkinsonism, dysarthria, behavioral changes)", "pathognomonic Kayser-Fleischer (KF) rings: golden-brown or greenish copper pigmentation in the Descemet membrane of the corneal limbus on slit-lamp examination (present in > 95% with neurological symptoms)", "'wing-beating' coarse postural tremor of upper limbs", "laboratory tetrad: 1. Low serum ceruloplasmin (< 20 mg/dL); 2. Markedly elevated 24-hour urinary copper excretion (> 100 mcg/day); 3. High free serum copper; 4. Coombs-negative hemolytic anemia with acute liver failure"],
        "pertinent_negatives": ["negative autoimmune markers and viral hepatitis serologies"],
        "content": "Autosomal recessive inborn error of copper metabolism caused by mutations in the ATP7B gene on chromosome 13, impairing biliary copper excretion and incorporation of copper into ceruloplasmin, causing toxic accumulation in liver, basal ganglia, and cornea. Diagnostic workup: Slit-lamp examination, serum ceruloplasmin, 24-hour urinary copper, liver biopsy for quantitative dry-weight copper. Treatment: Copper chelating agents: D-Penicillamine or Trientine hydrochloride (taken away from meals); Oral Zinc acetate (blocks intestinal copper absorption via metallothionein induction) for maintenance; Liver transplantation is curative for fulminant liver failure."
    },
    {
        "id": "ICD10-E83.110",
        "topic": "Hereditary Hemochromatosis (HFE Gene & Bronze Diabetes)",
        "icd10": "E83.110",
        "specialty": "Gastroenterology / Hematology / Endocrinology",
        "organ_system": "Metabolic Iron Overload",
        "keywords": ["hemochromatosis", "bronze diabetes", "iron overload", "high ferritin high transferrin saturation", "hfe c282y", "chondrocalcinosis pseudogout", "dilated cardiomyopathy iron"],
        "red_flags": ["hepatocellular carcinoma (200-fold increased risk)", "dilated cardiomyopathy / intractable arrhythmias", "decompensated cirrhosis"],
        "clinical_hallmarks": ["the classic triad (advanced disease): 1. Bronze cutaneous hyperpigmentation ('slate-grey' or bronze metallic skin); 2. Diabetes mellitus ('bronze diabetes' due to pancreatic islet iron deposition); 3. Cirrhosis / hepatomegaly", "severe chronic fatigue, loss of libido, and erectile dysfunction (due to pituitary iron accumulation causing secondary hypogonadotropic hypogonadism)", "arthropathy characteristically targeting 2nd and 3rd metacarpophalangeal (MCP) joints with chondrocalcinosis (pseudogout)", "laboratory hallmarks: Transferrin Saturation > 45-50% (earliest and most sensitive screening test) and Markedly elevated serum Ferritin (> 1000 ng/mL indicates risk of cirrhosis)"],
        "pertinent_negatives": ["absence of secondary iron overload (no multiple blood transfusions)"],
        "content": "Autosomal recessive iron overload disorder caused by mutations in the HFE gene (most commonly homozygous C282Y or compound heterozygous C282Y/H63D) causing inappropriately low hepcidin production and unregulated excessive intestinal iron absorption. Diagnostic workup: Fasting transferrin saturation, serum ferritin, HFE gene mutation analysis, Liver MRI (T2* sequence for quantitative iron quantification). Treatment: Therapeutic Phlebotomy (removal of 500 mL blood weekly or biweekly until serum ferritin reaches 50-100 ng/mL); Iron-chelation therapy (Deferasirox) if phlebotomy contraindicated; Dietary iron restriction."
    },
    {
        "id": "ICD10-K90.0",
        "topic": "Celiac Disease (Gluten-Sensitive Enteropathy & Dermatitis Herpetiformis)",
        "icd10": "K90.0",
        "specialty": "Gastroenterology / Dermatology",
        "organ_system": "Gastrointestinal Autoimmune",
        "keywords": ["celiac disease", "gluten enteropathy", "anti ttg iga", "dermatitis herpetiformis", "villous atrophy", "chronic diarrhea bloating gluten", "malabsorption iron deficiency"],
        "red_flags": ["enteropathy-associated t-cell lymphoma (eatcl)", "refractory celiac disease", "severe osteomalacia with pathological fractures"],
        "clinical_hallmarks": ["chronic pale, voluminous, foul-smelling diarrhea, steatorrhea, abdominal flatulence, and bloating provoked by gluten ingestion (wheat, rye, barley)", "features of multi-nutrient malabsorption: refractory microcytic iron deficiency anemia, weight loss, fat-soluble vitamin deficiencies (A, D, E, K), and hypocalcemia", "Dermatitis Herpetiformis: pathognomonic, intensely pruritic, symmetrical papulovesicular eruption over extensor surfaces (elbows, knees, buttocks, scalp)", "serological hallmark: Anti-Tissue Transglutaminase (tTG) IgA antibodies (with concurrent normal total IgA) and Anti-Endomysial (EMA) IgA", "duodenal endoscopy and biopsy: Marsh classification showing blunting/total villous atrophy, crypt hyperplasia, and intraepithelial lymphocytosis"],
        "pertinent_negatives": ["symptoms resolve completely on strict gluten elimination"],
        "content": "Immune-mediated systemic enteropathy triggered by ingestion of dietary gluten in genetically susceptible individuals carrying HLA-DQ2 or HLA-DQ8 haplotypes. Diagnostic workup: Serum total IgA + tTG-IgA (first-line serology while patient is on gluten-containing diet); Confirmation via Upper Endoscopy with multiple oriented duodenal biopsies. Treatment: Strict, lifelong, 100% Gluten-Free Diet (GFD) excluding wheat, barley, rye, and contaminated oats; Micronutrient supplementation (iron, folate, calcium, vitamin D); Oral Dapsone provides rapid relief for Dermatitis Herpetiformis skin lesions."
    },
    {
        "id": "ICD10-E16.4",
        "topic": "Zollinger-Ellison Syndrome (Gastrinoma & MEN-1)",
        "icd10": "E16.4",
        "specialty": "Gastroenterology / Endocrinology / Surgical Oncology",
        "organ_system": "Gastrointestinal / Neuroendocrine",
        "keywords": ["zollinger ellison syndrome", "gastrinoma", "recurrent peptic ulcer disease", "jejuna ulcers", "secretory diarrhea with ulcers", "high fasting gastrin", "men1 syndrome"],
        "red_flags": ["peptic ulcer perforation", "massive upper gi hemorrhage", "hepatic metastatic neuroendocrine disease"],
        "clinical_hallmarks": ["multiple, recurrent, severe, refractory peptic ulcers occurring in unusual locations (distal duodenum or jejunum)", "ulcers recur immediately despite high-dose PPI or H2-blocker therapy or after surgical ulcer repair", "chronic watery, secretory diarrhea that improves with high-dose acid suppression (diarrhea caused by massive acid volume overloading intestine and inactivating pancreatic lipase)", "25% of cases occur as part of Multiple Endocrine Neoplasia Type 1 (MEN-1: Parathyroid, Pancreas/Gastrinoma, Pituitary)", "laboratory hallmark: Fasting serum gastrin markedly elevated (> 1000 pg/mL in presence of gastric pH < 2.0)"],
        "pertinent_negatives": ["absence of h. pylori infection and negative nsaid use"],
        "content": "Gastrin-secreting neuroendocrine tumor (gastrinoma), typically located within the 'gastrinoma triangle' (confluence of cystic/common bile ducts, 2nd/3rd duodenum, and neck/body of pancreas), driving autonomous hypersecretion of gastric hydrochloric acid. Diagnostic workup: Fasting serum gastrin, gastric pH, Secretin stimulation test (paradoxical rise in gastrin > 120 pg/mL confirms gastrinoma), Somatostatin Receptor Scintigraphy (68Ga-DOTATATE PET-CT). Treatment: High-dose oral PPIs (Omeprazole 60-120 mg daily) to control acid secretion; Surgical exploratory laparotomy and oncological enucleation/resection of gastrinoma."
    },
    {
        "id": "ICD10-K57.32",
        "topic": "Acute Colonic Diverticulitis (Hinchey Staging)",
        "icd10": "K57.32",
        "specialty": "Gastroenterology / General Surgery / Emergency Medicine",
        "organ_system": "Gastrointestinal",
        "keywords": ["diverticulitis", "left lower quadrant pain", "fever with llq tenderness", "sigmoid diverticulitis", "hinchey classification", "pericolic abscess"],
        "red_flags": ["generalized feculent peritonitis (hinchey iv)", "colovesical fistula (pneumaturia, fecaluria)", "complete large bowel obstruction"],
        "clinical_hallmarks": ["constant, severe, aching pain localized to the LEFT LOWER QUADRANT (LLQ) of the abdomen (the 'left-sided appendicitis')", "fever, localized tenderness, muscular guarding, and sometimes a tender palpable inflammatory mass in left iliac fossa", "nausea, anorexia, constipation (50%) or diarrhea (30%), and dysuria/frequency if inflamed sigmoid abuts the bladder", "Contrast-enhanced CT of abdomen/pelvis (gold standard): colonic diverticula with sigmoid wall thickening (> 4 mm), pericolic fat stranding, and absence or presence of extraluminal air/abscess"],
        "pertinent_negatives": ["COLONOSCOPY IS STRICTLY CONTRAINDICATED in acute episode due to high risk of bowel perforation"],
        "content": "Micro- or macro-perforation of a colonic diverticulum (most commonly sigmoid colon) leading to localized inflammation, pericolic abscess, or generalized peritonitis. Classified by modified Hinchey criteria (Stage I pericolic abscess to Stage IV feculent peritonitis). Diagnostic test of choice: Contrast CT abdomen/pelvis. Management: Uncomplicated: bowel rest, oral/IV antibiotics covering Gram-negatives and anaerobes (Ciprofloxacin + Metronidazole or Amoxicillin-Clavulanate); Complicated: CT-guided percutaneous drainage for abscess > 3-4 cm (Hinchey II); Emergent Hartmann's procedure or primary resection with anastomosis for generalized peritonitis (Hinchey III/IV); Elective colonoscopy recommended 6-8 weeks after recovery to exclude malignancy."
    },
    {
        "id": "ICD10-I82.0",
        "topic": "Budd-Chiari Syndrome (Hepatic Venous Outflow Obstruction)",
        "icd10": "I82.0",
        "specialty": "Gastroenterology / Hepatology / Vascular Surgery",
        "organ_system": "Hepatobiliary Emergency",
        "keywords": ["budd chiari syndrome", "hepatic vein thrombosis", "acute painful hepatomegaly", "refractory ascites", "caudate lobe hypertrophy", "polycythemia vera liver"],
        "red_flags": ["acute fulminant hepatic failure (coagulopathy, encephalopathy)", "spontaneous bacterial peritonitis", "variceal rupture"],
        "clinical_hallmarks": ["classic clinical triad: 1. Acute or subacute severe abdominal pain (right upper quadrant); 2. Tender, smooth, marked hepatomegaly; 3. Rapidly accumulating, intractable, high-protein ascites", "frequently occurs on background of underlying myeloproliferative neoplasm (Polycythemia Vera with JAK2 V617F mutation), antiphospholipid syndrome, PNH, or oral contraceptive use", "Doppler ultrasound of hepatic veins: absence of flow, reversed flow, or thrombus in hepatic veins or IVC", "CT/MRI abdomen: pathognomonic hypertrophied caudate lobe (spared due to independent venous drainage directly into IVC) with inhomogeneous patchy enhancement of liver parenchyma"],
        "pertinent_negatives": ["ascites has high serum-ascites albumin gradient (SAAG >= 1.1) and high total protein (> 2.5 g/dL) distinguishing from cirrhosis"],
        "content": "Obstruction of hepatic venous outflow tract anywhere from small hepatic venules to entry of Inferior Vena Cava into right atrium. Diagnostic workup: Hepatic Doppler Ultrasound (first-line), Triphasic Contrast CT / MRI liver, JAK2 V617F mutation screen, thrombophilia profile. Management: Stepwise therapeutic algorithm: 1. Medical anticoagulation (LMWH bridged to Warfarin or DOAC) + diuretics (Spironolactone + Furosemide); 2. Catheter-directed thrombolysis / angioplasty and stenting for short segmental stenosis; 3. Transjugular Intrahepatic Portosystemic Shunt (TIPS) for refractory ascites or liver failure; 4. Orthotopic liver transplantation for fulminant necrosis."
    },
    {
        "id": "ICD10-K65.2",
        "topic": "Spontaneous Bacterial Peritonitis (SBP in Cirrhotic Ascites)",
        "icd10": "K65.2",
        "specialty": "Gastroenterology / Hepatology / Emergency Medicine",
        "organ_system": "Hepatobiliary Infectious",
        "keywords": ["spontaneous bacterial peritonitis", "sbp", "infected ascites", "neutrophils in ascitic fluid > 250", "ceftriaxone for sbp", "albumin for sbp", "worsening encephalopathy cirrhotic"],
        "red_flags": ["hepatorenal syndrome (rapidly rising creatinine)", "refractory septic shock", "rapid progression to hepatic coma"],
        "clinical_hallmarks": ["insidious or subtle clinical presentation in a patient with decompensated cirrhosis and pre-existing ascites", "diffuse mild abdominal pain, tenderness, rebound tenderness, or absent bowel sounds", "unexplained clinical deterioration: new-onset or worsening hepatic encephalopathy, acute kidney injury, hypothermia, or failure to thrive without obvious peritonitis signs", "diagnostic paracentesis hallmark: ascitic fluid absolute Polymorphonuclear (PMN) neutrophil count >= 250 cells/mm3 (>= 0.25 x 10^9/L)"],
        "pertinent_negatives": ["ascitic fluid polymicrobial growth, gross air, or protein > 1 g/dL suggests secondary surgical peritonitis, NOT SBP"],
        "content": "Bacterial infection of ascitic fluid occurring in the absence of any surgically treatable intra-abdominal source, caused by bacterial translocation from the gut (Escherichia coli, Klebsiella pneumoniae, Streptococci). Diagnostic gold standard: Immediate diagnostic paracentesis before antibiotic administration (PMN >= 250/mm3 is diagnostic). Protocol: 1. STAT IV Third-Generation Cephalosporin (Ceftriaxone 2g IV q24h or Cefotaxime 2g q8h for 5 days); 2. IV Albumin (1.5 g/kg on day 1, followed by 1.0 g/kg on day 3) DRAMATICALLY REDUCES renal impairment and mortality (from 30% to 10%); 3. Long-term secondary prophylaxis with oral Norfloxacin or Rifaximin."
    },
    {
        "id": "ICD10-K60.2",
        "topic": "Anal Fissure (Acute vs Chronic - Sphincter Hypertonicity)",
        "icd10": "K60.2",
        "specialty": "General Surgery / Colorectal Surgery / Primary Care",
        "organ_system": "Gastrointestinal Proctology",
        "keywords": ["anal fissure", "glass cutting anal pain", "painful defecation with blood", "sentinel skin tag", "posterior midline fissure", "sphincter spasm"],
        "red_flags": ["off-midline lateral fissure (raises suspicion of Crohn's, TB, HIV, or anal carcinoma)", "fecal impaction with overflow incontinence"],
        "clinical_hallmarks": ["excruciating, sharp, tearing, burning anal pain during defecation, described as 'passing shards of broken glass'", "pain persists as an intense, throbbing spasm for several minutes to hours after defecation due to internal anal sphincter hypertonicity", "scant, bright red blood on toilet paper or streaking the outside of hard stool", "physical examination (gentle parting of buttocks): visible longitudinal tear located in the POSTERIOR MIDLINE (> 90%) or anterior midline (10%)", "chronic fissure triad: visible fissure base showing circular internal sphincter fibers, an external 'sentinel' skin tag at anal verge, and an enlarged hypertrophied anal papilla at proximal apex"],
        "pertinent_negatives": ["DIGITAL RECTAL EXAMINATION (DRE) SHOULD NOT BE FORCED acutely due to intolerable sphincter spasm"],
        "content": "Longitudinal tear in the anoderm distal to the dentate line, overwhelmingly caused by trauma from passage of hard, dry stool combined with localized microvascular ischemia from internal anal sphincter hypertonicity. Treatment: 1. Conservative (high-fiber diet, stool softeners, warm sitz baths); 2. Chemical Sphincterotomy (first-line medical): Topical 0.2-0.4% Glyceryl Trinitrate (GTN) ointment or topical 2% Diltiazem cream applied BID for 6-8 weeks (promotes healing in 60-70%); 3. Botulinum toxin injection into internal sphincter; 4. Lateral Internal Sphincterotomy (LIS surgery - gold standard cure > 95% for refractory chronic fissures)."
    },
    {
        "id": "ICD10-K60.3",
        "topic": "Perianal Fistula-in-Ano (Goodsall's Rule & Cryptoglandular Origin)",
        "icd10": "K60.3",
        "specialty": "Colorectal Surgery / General Surgery",
        "organ_system": "Gastrointestinal Proctology",
        "keywords": ["fistula in ano", "perianal fistula", "goodsalls rule", "pus discharge near anus", "recurrent perianal abscess", "crohns perianal disease"],
        "red_flags": ["high transsphincteric / suprasphincteric fistula (risk of fecal incontinence with surgery)", "multiple complex fistulae indicating Crohn's disease"],
        "clinical_hallmarks": ["persistent or intermittent, malodorous, purulent, serosanguinous discharge from an external opening on the perineal skin around the anus", "history of previous acute perianal abscess that was either surgically drained or ruptured spontaneously", "perianal pruritus, excoriation, and recurrent painful swelling that is temporarily relieved when pus bursts and drains", "Goodsall's Rule: fistulae with external openings POSTERIOR to the transverse anal line follow a curved path to the posterior midline crypt; anterior openings <= 3 cm from verge follow a straight radial tract to the nearest crypt", "palpable fibrous, cord-like tract extending from external skin opening toward anal canal"],
        "pertinent_negatives": ["no deep rectal mass or pelvic bone erosion on MRI"],
        "content": "Hollow, chronic, epithelialized fibrous tract connecting an internal opening in the anal canal (arising from infected anal cryptoglandular glands) to an external opening on the perianal skin. Park's classification (intersphincteric, transsphincteric, suprasphincteric, extrasphincteric). Diagnostic gold standard: Pelvic MRI with endoanal coil for complex or recurrent fistulae. Treatment: Low intersphincteric/subcutaneous fistulae: Fistulotomy (laying open the tract); High or complex fistulae involving significant sphincter muscle: Loose Seton placement, LIFT procedure (Ligation of Intersphincteric Fistula Tract), mucosal advancement flap, or VAAFT to preserve fecal continence."
    },
    {
        "id": "ICD10-K85.1",
        "topic": "Biliary Acute Pancreatitis & Gallstone Obstruction",
        "icd10": "K85.1",
        "specialty": "Gastroenterology / General Surgery",
        "organ_system": "Gastrointestinal Emergency",
        "keywords": ["biliary pancreatitis", "gallstone pancreatitis", "epigastric pain radiating to back", "elevated lipase 3x", "choledocholithiasis pancreatitis", "ranson criteria"],
        "red_flags": ["necrotizing pancreatitis with infection", "organ failure (shock, aki, ards) lasting > 48 hours", "concomitant ascending cholangitis (charcot triad)"],
        "clinical_hallmarks": ["acute onset of constant, agonizing, boring epigastric pain that RADIATES DIRECTLY THROUGH TO THE MID-BACK, partially eased by sitting forward or assuming fetal knee-chest position", "severe nausea, intractable retching, and bilious vomiting that fails to relieve pain", "epigastric tenderness and abdominal guarding with diminished or absent bowel sounds (paralytic ileus)", "laboratory hallmark: serum Lipase or Amylase elevated to >= 3 TIMES THE UPPER LIMIT OF NORMAL (Lipase is more specific and remains elevated longer)", "concurrent elevation of ALT (> 150 IU/L) strongly predicts gallstone etiology (> 95% positive predictive value)"],
        "pertinent_negatives": ["normal erect chest x-ray rules out perforated peptic ulcer free air under diaphragm"],
        "content": "Acute inflammation of the pancreas initiated when a gallstone or biliary sludge transiently lodges in or traverses the ampulla of Vater, causing biliary-pancreatic duct reflux and premature intraparenchymal trypsinogen activation. Atlanta Classification (mild, moderately severe, severe). Diagnostic criteria (2 of 3 needed): 1. Characteristic epigastric pain; 2. Lipase >= 3x ULN; 3. Typical imaging findings (CT/MRI/US). Protocol: Aggressive goal-directed IV fluid hydration (Ringer's Lactate 200-500 mL/hr guided by urine output and hematocrit); Multimodal analgesia (IV Opioids); Early enteral oral feeding as tolerated; Urgent ERCP within 24 hours indicated ONLY if concomitant acute cholangitis or persistent biliary obstruction; Index admission cholecystectomy to prevent recurrence."
    },
    {
        "id": "ICD10-K31.84",
        "topic": "Gastroparesis (Diabetic Autonomic Neuropathy & Post-Surgical)",
        "icd10": "K31.84",
        "specialty": "Gastroenterology / Endocrinology",
        "organ_system": "Gastrointestinal Motility",
        "keywords": ["gastroparesis", "delayed gastric emptying", "diabetic gastroparesis", "early satiety vomiting undigested food", "gastric scintigraphy", "erratic blood glucose"],
        "red_flags": ["severe dehydration and electrolyte derangements (hypokalemic alkalosis)", "gastric bezoar with mechanical obstruction", "profound malnutrition"],
        "clinical_hallmarks": ["persistent postprandial fullness, early satiety (inability to finish normal-sized meal), nausea, and bloating", "vomiting of recognizable, undigested food consumed many hours or even days earlier", "history of long-standing diabetes mellitus with microvascular complications (retinopathy, nephropathy, peripheral neuropathy) or prior vagotomy/gastric surgery", "unexplained erratic, brittle blood glucose fluctuations with frequent unpredictable postprandial hypoglycemia (insulin peaks before food is emptied and absorbed from stomach)", "succussion splash audible over epigastrium > 3-4 hours after food intake"],
        "pertinent_negatives": ["upper endoscopy reveals NO mechanical gastric outlet obstruction or peptic stenosis"],
        "content": "Symptomatic delayed gastric emptying of solid food in the absence of mechanical gastric outlet obstruction, caused by autonomic neuropathy, loss of interstitial cells of Cajal, or enteric neural nitric oxide synthase deficiency. Diagnostic gold standard: 4-Hour Solid-Phase Gastric Emptying Scintigraphy (retention of > 10% of radiolabeled meal at 4 hours is diagnostic). Treatment: Dietary modification (small, frequent, low-fat, low-insoluble-fiber meals); Optimization of glycemic control; Prokinetic pharmacotherapy: Oral Metoclopramide (10 mg 30 min before meals - limited to 12 weeks due to tardive dyskinesia risk) or oral Erythromycin (motilin receptor agonist) or Domperidone; Gastric electrical stimulation (Enterra) for refractory cases."
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
            
    print(f"Batch 1 added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""
Batch 6 Finish: Psychiatry, Acute Surgery, Tropical/Infectious, Orthopedics/Trauma.
Pushes knowledge base comfortably past 500 validated clinical protocols.
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
    # --- 16. PSYCHIATRY & BEHAVIORAL EMERGENCIES (10) ---
    {
        "id": "ICD10-G21.0",
        "topic": "Neuroleptic Malignant Syndrome (Lead-Pipe Rigidity & Dantrolene)",
        "icd10": "G21.0",
        "specialty": "Psychiatry / Critical Care / Emergency Medicine",
        "organ_system": "Psychopharmacological Emergency",
        "keywords": ["neuroleptic malignant syndrome", "nms", "lead pipe rigidity", "haloperidol hyperthermia", "dopamine receptor blockade", "dantrolene bromocriptine", "elevated ck > 10000"],
        "red_flags": ["hyperpyrexia > 41C / 106F with multiorgan failure", "rhabdomyolysis and acute tubular necrosis", "cardiovascular collapse / malignant arrhythmias"],
        "clinical_hallmarks": ["history of initiating, titrating, or taking high-potency first-generation antipsychotics (Haloperidol, Fluphenazine) or atypical antipsychotics, OR abrupt withdrawal of dopamine agonists (Levodopa)", "THE CARDINAL TETRAD: 1. HYPERTHERMIA (severe fever typically > 38.0 - 40.0C); 2. EXTREME 'LEAD-PIPE' MUSCLE RIGIDITY (generalized, uniform resistance to passive joint movement throughout range of motion); 3. AUTONOMIC INSTABILITY (profuse diaphoresis, tachycardia, labile fluctuating blood pressure, tachypnea, urinary incontinence); 4. ALTERED MENTAL STATUS (confusion, delirium, mutism, stupor, coma)", "LABORATORY HALLMARK: MASSIVE ELEVATION OF SERUM CREATINE KINASE (CK typically > 1,000 - 100,000 IU/L) and leukocytosis (WBC 10,000-40,000 /mcL)", "hyporeflexia or normal reflexes (fundamental contrast to hyperreflexia and clonus of Serotonin Syndrome)"],
        "pertinent_negatives": ["absence of hyperreflexia, ocular clonus, or shivering distinguishes NMS from Serotonin Syndrome"],
        "content": "Life-threatening idiosyncratic reaction to central dopamine D2 receptor blockade in the corpus striatum and hypothalamus. Immediate Protocol: 1. STAT DISCONTINUATION OF ALL ANTIPSYCHOTIC MEDICATIONS; 2. Aggressive physical cooling and IV hydration (Normal Saline 200-300 mL/hr to prevent myoglobinuric renal failure); 3. STAT SPECIFIC PHARMACOTHERAPY: Dantrolene Sodium (1-2.5 mg/kg IV push, repeated up to 10 mg/kg/day - direct skeletal muscle relaxant) PLUS Bromocriptine (2.5-5 mg orally TID - dopamine agonist) OR Amantadine; 4. IV Lorazepam for agitation and catatonic rigidity; 5. Electroconvulsive Therapy (ECT) for refractory NMS."
    },
    {
        "id": "ICD10-T43.221A",
        "topic": "Serotonin Syndrome (Hunter Criteria & Ocular Clonus)",
        "icd10": "T43.221A",
        "specialty": "Psychiatry / Clinical Toxicology / Emergency Medicine",
        "organ_system": "Toxicological / Neuropsychiatric Emergency",
        "keywords": ["serotonin syndrome", "serotonin toxicity", "hunter toxicity criteria", "ocular clonus", "spontaneous clonus hyperreflexia", "shivering tremor hyperthermia", "cyproheptadine ssri"],
        "red_flags": ["severe hyperthermia > 41.1C with metabolic acidosis", "disseminated intravascular coagulation (dic)", "rhabdomyolysis and multiorgan failure"],
        "clinical_hallmarks": ["history of co-administration of >= 2 pro-serotonergic agents (SSRIs, SNRIs, MAO inhibitors, Tramadol, Linezolid, MDMA/Ecstasy, Triptans, St. John's Wort) or overdose", "HUNTER TOXICITY CRITERIA (patient must have taken a serotonergic agent PLUS >= 1 of the following):", "1. SPONTANEOUS CLONUS (rhythmic, involuntary muscular contractions);", "2. INDUCIBLE CLONUS PLUS AGITATION OR PROFUSE DIAPHORESIS;", "3. OCULAR CLONUS (slow, rhythmic, involuntary horizontal oscillatory eye movements) PLUS AGITATION OR DIAPHORESIS;", "4. TREMOR PLUS HYPERREFLEXIA;", "5. HYPERTONIA PLUS HYPERTHERMIA (> 38C) PLUS OCULAR OR INDUCIBLE CLONUS;", "prominent NEUROMUSCULAR ABNORMALITIES ARE STRIKINGLY MORE PRONOUNCED IN LOWER EXTREMITIES (brisk ankle clonus, patellar hyperreflexia, and lower limb rigidity) than upper extremities", "autonomic hyperactivity: hyperactive 'rumbling' bowel sounds (borborygmi) and watery diarrhea"],
        "pertinent_negatives": ["hyperreflexia, clonus, and diarrhea distinguish Serotonin Syndrome from lead-pipe hyporeflexic NMS"],
        "content": "Life-threatening excess intrasynaptic serotonin activating 5-HT1A and 5-HT2A receptors. Protocol: 1. STAT CESSATION OF ALL SEROTONERGIC AGENTS; 2. IV Benzodiazepines (Lorazepam 2-4 mg IV) to control agitation and muscle hyperactivity; 3. STAT SPECIFIC 5-HT2A ANTAGONIST: Cyproheptadine (12 mg orally/NG initial dose, followed by 2 mg q2h if symptoms persist); 4. Severe Hyperthermia (> 41.1C): STAT Endotracheal Intubation, Neuromuscular Paralysis with Vecuronium (NON-DEPOLARIZING blocker - Succinylcholine strictly contraindicated), and ICU cooling."
    },
    {
        "id": "ICD10-T43.501A",
        "topic": "Lithium Toxicity (Coarse Tremor, Ataxia & Hemodialysis)",
        "icd10": "T43.501A",
        "specialty": "Psychiatry / Nephrology / Clinical Toxicology",
        "organ_system": "Toxicological / Neuro-Renal Emergency",
        "keywords": ["lithium toxicity", "lithium level > 1.5", "coarse hand tremor lithium", "ataxia dysarthria nystagmus", "hemodialysis for lithium", "nephrogenic diabetes insipidus lithium", "nsaids thiazides lithium"],
        "red_flags": ["permanent cerebellar and neurological damage (SILENT syndrome)", "generalized convulsions / status epilepticus", "cardiac arrhythmias and sinus node arrest"],
        "clinical_hallmarks": ["narrow therapeutic index of Lithium (normal maintenance therapeutic range: 0.6 - 1.2 mEq/L)", "frequently precipitated by VOLUME DEPLETION OR DRUG INTERACTIONS that reduce renal lithium excretion (NSAIDs, Thiazide diuretics, ACE inhibitors, dehydration, febrile illness)", "MILD TOXICITY (1.5 - 2.0 mEq/L): nausea, vomiting, watery diarrhea, lethargy, muscle weakness, and progression from fine tremor to a PROMINENT COARSE HAND TREMOR", "MODERATE TOXICITY (2.0 - 2.5 mEq/L): marked cerebellar signs (ataxia, unsteady stumbling gait, dysarthria, nystagmus), hyperreflexia, and diffuse fasciculations", "SEVERE TOXICITY (> 2.5 mEq/L): delirium, generalized tonic-clonic seizures, non-convulsive status epilepticus, coma, and cardiorespiratory arrest", "laboratory hallmark: SERUM LITHIUM LEVEL > 1.5 mEq/L"],
        "pertinent_negatives": ["activated charcoal DOES NOT bind lithium (ineffective)"],
        "content": "Toxic intracellular accumulation of monovalent lithium cations replacing sodium and inhibiting cellular inositol monophosphatase. Management: 1. STAT IV Fluid Resuscitation: 0.9% Normal Saline at 200-250 mL/hr (sodium-rich hydration restores volume and promotes renal lithium excretion); 2. Whole Bowel Irrigation with PEG for sustained-release formulations; 3. DEFINITIVE ELIMINATION: STAT EMERGENCY HEMODIALYSIS (Indications: Lithium level > 4.0 mEq/L regardless of symptoms; Level > 2.5 mEq/L with severe neurological symptoms or renal failure); 4. Post-dialysis rebound monitoring (lithium slowly redistributes from intracellular stores, often requiring repeated hemodialysis)."
    },
    {
        "id": "ICD10-F10.231",
        "topic": "Delirium Tremens & Severe Alcohol Withdrawal (CIWA-Ar Protocol)",
        "icd10": "F10.231",
        "specialty": "Psychiatry / Critical Care / Addiction Medicine",
        "organ_system": "Neuropsychiatric Withdrawal Emergency",
        "keywords": ["delirium tremens", "dt", "alcohol withdrawal delirium", "ciwa ar protocol", "formication tactile hallucinations", "autonomic storm tachycardia fever", "high dose diazepam iv"],
        "red_flags": ["fatal circulatory collapse / malignant ventricular arrhythmias", "hyperthermia and severe dehydration", "aspiration pneumonia"],
        "clinical_hallmarks": ["history of chronic, heavy, continuous alcohol dependence followed by abrupt cessation or marked reduction in drinking (e.g. hospitalized surgical or trauma patient)", "TIMELINE OF ALCOHOL WITHDRAWAL:", "1. Minor Withdrawal (6-12 hours): fine tremor ('the shakes'), insomnia, anxiety, diaphoresis, palpitations, GI upset;", "2. Withdrawal Seizures (12-48 hours): generalized tonic-clonic convulsions (typically 1-3 seizures, non-focal);", "3. Alcoholic Hallucinosis (12-48 hours): visual, auditory, or tactile hallucinations (FORMICATION: sensation of insects crawling on skin) with PRESERVED CLEAR SENSORIUM;", "4. DELIRIUM TREMENS (DTs - develops 48 to 96 hours post-cessation):", "THE FULL DELIRIUM TREMENS SYNDROME: PROFOUND CLOUDING OF CONSCIOUSNESS (fluctuating disorientation, confusion, agitation) COMBINED WITH A MASSIVE AUTONOMIC STORM (high fever, severe tachycardia > 120 bpm, marked hypertension, profuse drenching diaphoresis, and severe coarse tremor)"],
        "pertinent_negatives": ["clear orientation distinguishes simple alcoholic hallucinosis from delirium tremens (where orientation is profoundly shattered)"],
        "content": "Life-threatening rebound hyperexcitability of the central nervous system resulting from sudden removal of chronic GABA-A receptor facilitation and uninhibited NMDA/glutamate receptor activation. Untreated mortality is 15-20%. Emergency Protocol: 1. STAT High-Dose IV Benzodiazepines (SYMPTOM-TRIGGERED CIWA-Ar DOSING: IV Diazepam 10-20 mg IV every 10-15 minutes OR IV Lorazepam 2-4 mg until patient is calm, lightly sleeping, but easily arousable); 2. IV Thiamine (500 mg IV TID for 3-5 days) BEFORE ANY GLUCOSE to prevent Wernicke's encephalopathy; 3. Aggressive fluid and electrolyte replacement (correct hypomagnesemia, hypokalemia, hypophosphatemia); 4. IV Phenobarbital or Dexmedetomidine infusion for refractory DTs."
    },
    {
        "id": "ICD10-F31.9",
        "topic": "Bipolar I Disorder (Acute Manic Episode & DIG FAST Mnemonic)",
        "icd10": "F31.9",
        "specialty": "Psychiatry / Emergency Medicine",
        "organ_system": "Psychiatric Mood Disorder",
        "keywords": ["bipolar 1 disorder", "acute mania", "dig fast mnemonic", "decreased need for sleep mania", "grandiosity flight of ideas", "pressured speech spending sprees", "atypical antipsychotic mood stabilizer"],
        "red_flags": ["exhaustion and cardiovascular collapse from severe hyperactivity", "reckless dangerous behavior / high risk taking", "manic psychosis with command auditory hallucinations"],
        "clinical_hallmarks": ["DSM-5 CRITERIA: A distinct period of abnormally and persistently elevated, expansive, or irritable mood and abnormally and persistently increased goal-directed activity or energy, lasting AT LEAST 1 WEEK (or any duration if hospitalization is necessary)", "CARDINAL 'DIG FAST' MNEMONIC (requires >= 3 symptoms, or >= 4 if mood is irritable):", "1. D - DISTRACTIBILITY (attention easily drawn to unimportant external stimuli);", "2. I - INDISCRETION / IMPULSIVITY (excessive involvement in activities with high potential for painful consequences: unrestrained shopping sprees, sexual indiscretions, foolish business investments);", "3. G - GRANDIOSITY or inflated self-esteem (unrealistic beliefs of possessing special divine powers, fame, or millions of dollars);", "4. F - FLIGHT OF IDEAS or subjective racing thoughts;", "5. A - ACTIVITY INCREASE (psychomotor agitation or multi-tasking frantic project starting at 3 AM);", "6. S - SLEEP DECREASE (DECREASED NEED FOR SLEEP: patient feels completely energetic, refreshed, and rested after only 2-3 hours of sleep - pathognomonic feature);", "7. T - TALKATIVENESS (rapid, loud, unstoppable, pressured speech that is impossible to interrupt)"],
        "pertinent_negatives": ["decreased NEED for sleep (feels fully rested on 2 hours) distinguishes mania from insomnia (wants to sleep but cannot)"],
        "content": "Severe cyclic mood disorder characterized by at least one lifetime manic episode. Emergency Management: 1. Acute Agitated Mania: Oral or IM Second-Generation Antipsychotic (Olanzapine 10-20 mg/day, Aripiprazole, or Quetiapine) combined with oral Lorazepam for rapid behavioral control; 2. First-line Mood Stabilizers: Oral Lithium Carbonate (target serum level 0.8-1.2 mEq/L for acute mania) OR Oral Divalproex Sodium / Valproate (loading dose 20-30 mg/kg/day); 3. STRICT AVOIDANCE OF ANTIDEPRESSANTS (precipitate rapid switching into mixed/manic states and cycle acceleration); 4. Safe inpatient hospitalization to protect from financial, social, and physical self-harm."
    },
    {
        "id": "ICD10-F32.9",
        "topic": "Major Depressive Disorder with High Suicide Risk (SIG E CAPS)",
        "icd10": "F32.9",
        "specialty": "Psychiatry / Primary Care / Emergency Medicine",
        "organ_system": "Psychiatric Mood Disorder",
        "keywords": ["major depressive disorder", "mdd", "sig e caps mnemonic", "anhedonia suicidal ideation", "early morning awakening depression", "ssri escitalopram sertraline", "sad persons scale"],
        "red_flags": ["active suicidal ideation with concrete plan and intent", "psychotic depression (delusions of guilt, poverty, or somatic decay)", "complete food and fluid refusal (catatonic stupor)"],
        "clinical_hallmarks": ["DSM-5 CRITERIA: At least 5 of the 9 symptoms present nearly every day during the same 2-WEEK PERIOD, representing a change from previous functioning, where AT LEAST ONE SYMPTOM IS DEPRESSED MOOD OR LOSS OF INTEREST/PLEASURE (ANHEDONIA):", "CARDINAL 'SIG E CAPS' MNEMONIC:", "1. S - SLEEP disturbance (insomnia with characteristically PATHOGNOMONIC TERMINAL INSOMNIA / EARLY MORNING AWAKENING 2 hours before alarm; or hypersomnia);", "2. I - INTEREST loss (profound anhedonia: inability to experience joy from hobbies, sex, or family);", "3. G - GUILT (excessive, inappropriate feelings of worthlessness or guilt);", "4. E - ENERGY loss (chronic debilitating fatigue, leaden paralysis);", "5. C - CONCENTRATION impairment (indecisiveness, memory complaints);", "6. A - APPETITE change (unintentional weight loss > 5% or weight gain);", "7. P - PSYCHOMOTOR agitation or retardation (observable physical slowing of speech and movement);", "8. S - SUICIDAL IDEATION (recurrent thoughts of death, suicidal ideation, or suicide attempts)"],
        "pertinent_negatives": ["no history of manic or hypomanic episodes (rules out bipolar depression)"],
        "content": "Major unipolar psychiatric mood disorder. Suicidal Risk Assessment: Evaluate intent, plan, lethality of means, access to firearms/pills, prior attempts, and protective factors (Columbia Suicide Severity Rating Scale). Management: 1. High Suicide Risk: Immediate voluntary or involuntary psychiatric inpatient admission with 1-to-1 constant observation; 2. Pharmacotherapy: Selective Serotonin Reuptake Inhibitors (SSRIs: Escitalopram 10-20 mg, Sertraline 50-200 mg) or SNRIs (Venlafaxine); educate patient that therapeutic onset takes 2-4 weeks; 3. Psychotherapy: Cognitive Behavioral Therapy (CBT); 4. STAT Rapid Interventions: IV Ketamine / Intranasal Esketamine OR Electroconvulsive Therapy (ECT - gold standard for psychotic depression, severe suicidality, or refusal of food/fluids)."
    },
    {
        "id": "ICD10-F20.9",
        "topic": "Schizophrenia (Schneiderian First-Rank Symptoms & Antipsychotics)",
        "icd10": "F20.9",
        "specialty": "Psychiatry",
        "organ_system": "Psychiatric Psychotic Disorder",
        "keywords": ["schizophrenia", "first rank symptoms schneider", "auditory hallucinations third person", "delusions of control thought insertion", "negative symptoms schizophrenia", "clozapine treatment resistant"],
        "red_flags": ["command auditory hallucinations directing violence or self-harm", "severe self-neglect and water intoxication (psychogenic polydipsia)", "suicide (10% lifetime risk)"],
        "clinical_hallmarks": ["DSM-5 CRITERIA: >= 2 of the following present for significant portion of time during a 1-MONTH PERIOD (with continuous disturbance lasting >= 6 months), where AT LEAST ONE must be Delusions, Hallucinations, or Disorganized Speech:", "1. DELUSIONS: fixed, false, idiosyncratic beliefs impervious to contradictory logic (persecutory, referential [news anchor is sending coded messages], or somatic);", "2. HALLUCINATIONS: perception in the absence of external stimulus, overwhelmingly AUDITORY (hearing distinct voices talking to or about the patient);", "SCHNEIDER'S FIRST-RANK PATHOGNOMONIC SYMPTOMS:", "1. Auditory hallucinations: Voices discussing or arguing about the patient in the THIRD PERSON; Voices commenting continuously on the patient's thoughts or actions (running commentary); Thought echo (thoughts spoken aloud);", "2. Delusions of Passivity and Control: feeling bodily movements, sensations, or impulses are completely controlled by an outside alien force;", "3. Thought Alienation: THOUGHT WITHDRAWAL (alien agency pulling thoughts out), THOUGHT INSERTION (outside thoughts placed in mind), and THOUGHT BROADCASTING (thoughts radiating openly to others);", "Negative Symptoms (The '5 As'): Affective flattening, Alogia (poverty of speech), Avolition, Anhedonia, and Asociality"],
        "pertinent_negatives": ["absence of prominent primary mood episode concurrent with active psychosis (distinguishes from schizoaffective disorder)"],
        "content": "Chronic, disabling neuropsychiatric brain disorder with neurodevelopmental and neurochemical origins (excess mesolimbic dopamine D2 activity causing positive symptoms; mesocortical dopamine deficit causing negative symptoms). Treatment: 1. First-line: Second-Generation (Atypical) Antipsychotics (Risperidone 2-6 mg, Olanzapine 10-20 mg, Aripiprazole) have lower extrapyramidal side-effect risk; 2. Treatment-Resistant Schizophrenia (failed >= 2 adequate antipsychotic trials): CLOZAPINE (the only antipsychotic proven superior for refractory illness and suicide reduction; MANDATORY weekly/monthly CBC monitoring for agranulocytosis and absolute neutrophil count [ANC]); 3. Long-Acting Injectable Antipsychotics (LAIs) for non-adherence; 4. Assertive Community Treatment."
    },
    {
        "id": "ICD10-F41.0",
        "topic": "Panic Disorder & Agoraphobia (Catastrophic Misinterpretation)",
        "icd10": "F41.0",
        "specialty": "Psychiatry / Primary Care / Cardiology",
        "organ_system": "Psychiatric Anxiety Disorder",
        "keywords": ["panic disorder", "panic attack", "fear of impending doom heart attack", "hyperventilation carpopedal spasm", "agoraphobia", "cbt for panic disorder", "ssri for panic"],
        "red_flags": ["severe agoraphobia causing complete home confinement", "recurrent emergency room visits for presumed MI / coronary angiograms", "secondary alcoholism / substance abuse"],
        "clinical_hallmarks": ["DSM-5 CRITERIA: Recurrent UNEXPECTED PANIC ATTACKS (abrupt surge of intense fear or intense discomfort that REACHES A PEAK WITHIN MINUTES), followed by AT LEAST 1 MONTH of persistent worry about having additional attacks or their consequences ('fear of the fear')", "CARDINAL SYMPTOMS OF A PANIC ATTACK (requires >= 4 of 13 symptoms):", "1. Palpitations, pounding heart, or tachycardia; 2. Profuse sweating; 3. Trembling or shaking; 4. Sensation of shortness of breath, smothering, or choking; 5. Chest pain or discomfort (frequently mimicking acute myocardial infarction); 6. Nausea or abdominal distress; 7. Dizziness, unsteadiness, lightheadedness, or feeling faint; 8. Chills or heat sensations; 9. Paresthesias (numbness or tingling sensations, especially circumoral and fingers from hyperventilation-induced respiratory alkalosis); 10. Derealization (feelings of unreality) or Depersonalization (being detached from oneself); 11. Fear of losing control or 'going crazy'; 12. SENSATION OF IMPENDING DOOM OR FEAR OF DYING", "Agoraphobia (in > 50%): marked fear or avoidance of situations where escape might be difficult or help unavailable in the event of a panic attack (public transport, open spaces, enclosed places, lines, crowds)"],
        "pertinent_negatives": ["normal ECG, normal high-sensitivity troponins, and normal D-Dimer rule out organic cardiopulmonary disease"],
        "content": "Anxiety disorder driven by catastrophic misinterpretation of normal somatic arousal sensations mediated by a hypersensitive amygdala and 'fear network'. Treatment: 1. FIRST-LINE PHARMACOTHERAPY: Selective Serotonin Reuptake Inhibitors (SSRIs: Sertraline, Paroxetine, Escitalopram) or SNRIs (Venlafaxine) started at HALF the usual initial dose to avoid paradoxical initial activation/anxiety; 2. Short-term bridging: Low-dose Benzodiazepines (Clonazepam, Alprazolam) for acute severe attacks (limit to 2-4 weeks to prevent dependence); 3. FIRST-LINE PSYCHOTHERAPY: Cognitive Behavioral Therapy (CBT: interoceptive exposure exercises, cognitive restructuring, and diaphragmatic breathing retraining has > 75-80% durable cure rate)."
    },
    {
        "id": "ICD10-F50.00",
        "topic": "Anorexia Nervosa (Severe Emaciation & Refeeding Syndrome)",
        "icd10": "F50.00",
        "specialty": "Psychiatry / Adolescent Medicine / Endocrinology",
        "organ_system": "Eating Disorder / Metabolic Emergency",
        "keywords": ["anorexia nervosa", "severe emaciation bmi < 15", "lanugo hair", "fear of gaining weight", "refeeding syndrome hypophosphatemia", "carotenemia yellow palms", "prolonged qt anorexia"],
        "red_flags": ["fatal Refeeding Syndrome (hypophosphatemic cardiac arrest upon rapid refeeding)", "malignant arrhythmias from severe hypokalemia and prolonged QTc", "suicide (second leading cause of death in anorexia)"],
        "clinical_hallmarks": ["DSM-5 CRITERIA: 1. Restriction of energy intake relative to requirements leading to a SIGNIFICANTLY LOW BODY WEIGHT in context of age, sex, and developmental trajectory; 2. Intense, irrational fear of gaining weight or becoming fat; 3. Disturbance in the way body weight/shape is experienced, with undue influence on self-evaluation or denial of the seriousness of current low weight", "severity by Body Mass Index (BMI in adults): Mild (>= 17), Moderate (16-16.99), Severe (15-15.99), Extreme (< 15 kg/m2)", "CARDINAL PHYSICAL SIGNS OF PROFOUND EMACIATION: 1. LANUGO (fine, soft, downy hair growing on back, arms, and cheeks); 2. Profound sinus bradycardia (resting HR < 40-50 bpm), hypothermia (< 35.5C), and hypotension; 3. Carotenemia (yellow-orange pigmentation of palms and soles due to impaired hepatic conversion of carotene); 4. Secondary amenorrhea and loss of axillary/pubic hair; 5. Parotid gland enlargement and Russell sign (knuckle calluses in purging subtype)", "REFEEDING SYNDROME RISK: rapid carbohydrate refeeding causes massive insulin surge, driving phosphate, potassium, and magnesium into cells, precipitating FATAL HYPOPHOSPHATEMIA, heart failure, and arrhythmias"],
        "pertinent_negatives": ["patient perceives themselves as 'overweight' despite objective extreme emaciation"],
        "content": "Psychiatric eating disorder with highest mortality of any psychiatric illness (5-10% per decade). Inpatient Hospitalization Indications: BMI < 13-14, HR < 40 bpm, BP < 80/50, QTc > 460 ms, K+ < 3.0 mEq/L, or acute refusal to eat. Management: 1. CAREFUL, GRADUAL NUTRITIONAL REHABILITATION: 'Start low and advance slow' (begin feeds at 1,000-1,200 kcal/day, increasing by 200 kcal every 2-3 days); 2. Daily monitoring of serum PHOSPHATE, potassium, and magnesium for first 1-2 weeks; oral/IV phosphate repletion is mandatory; 3. Psychotherapy: Family-Based Treatment (FBT / Maudsley approach) for adolescents; Specialist Supportive Clinical Management (SSCM) or CBT-E for adults; 4. Atypical antipsychotic (Olanzapine 2.5-10 mg) facilitates weight gain and reduces obsessive eating rumination."
    },
    {
        "id": "ICD10-F06.1",
        "topic": "Catatonia (Bush-Francis Rating Scale & Lorazepam Challenge)",
        "icd10": "F06.1",
        "specialty": "Psychiatry / Neurology / Emergency Medicine",
        "organ_system": "Neuropsychiatric Motor Syndrome",
        "keywords": ["catatonia", "bush francis scale", "waxy flexibility catalepsy", "mutism stupor negativism", "lorazepam challenge test", "echolalia echopraxia", "malignant catatonia ect"],
        "red_flags": ["Malignant Catatonia (hyperthermia, autonomic storm, cardiovascular collapse - lethal if untreated)", "pulmonary embolism from prolonged complete immobility", "severe dehydration / malnutrition"],
        "clinical_hallmarks": ["neuropsychiatric motor syndrome occurring secondary to mood disorders (bipolar mania/depression in 60%), schizophrenia, or general medical/neurological conditions", "DSM-5 requires >= 3 of 12 cardinal signs (quantified by Bush-Francis Catatonia Rating Scale):", "1. STUPOR (complete immobility and unresponsiveness with preserved awareness of environment);", "2. MUTISM (complete absence or minimal verbal output);", "3. CATALEPSY (passive induction of a posture held against gravity for extended periods);", "4. WAXY FLEXIBILITY (slight, even resistance to positioning by examiner, resembling the bending of a warm candle);", "5. NEGATIVISM (motiveless resistance or opposition to instructions or passive movements, or doing the exact opposite);", "6. POSTURING (spontaneous, active maintenance of a bizarre, uncomfortable posture against gravity, such as the 'psychological pillow' - head held 2 inches above bed for hours);", "7. ECHOLALIA (mimicking examiner's words) and ECHOPRAXIA (mimicking examiner's movements);", "8. Stereotypy, Mannerisms, Grimacing, and Agitation", "DIAGNOSTIC AND THERAPEUTIC TEST: THE LORAZEPAM CHALLENGE TEST (administration of IV Lorazepam 1-2 mg produces DRAMATIC, NEAR-COMPLETE TEMPORARY RESOLUTION OF CATATONIC MUTISM AND STUPOR WITHIN 10-15 MINUTES, with patient sitting up and speaking normally)"],
        "pertinent_negatives": ["response to lorazepam confirms catatonia and decisively rules out coma"],
        "content": "Neurochemical motor dysregulation characterized by top-down cortical GABA-A hypoactivity and dopamine-glutamate imbalance. STAT Protocol: 1. STAT LORAZEPAM CHALLENGE AND TITRATION: IV Lorazepam (2 mg IV bolus; if partial response, repeat 2 mg in 30 min; titrated up to 8-16 mg/day in divided doses); 2. Malignant Catatonia (fever, autonomic instability) or Lorazepam-Refractory Catatonia (after 48-72 hours): STAT EMERGENCY ELECTROCONVULSIVE THERAPY (Bilateral ECT is life-saving, achieving > 85-95% remission); 3. Prophylactic LMWH anticoagulation to prevent DVT/PE; 4. Strictly AVOID all antipsychotic medications (precipitate fatal malignant catatonia)."
    },

    # --- 17. ACUTE SURGERY & EMERGENCY MEDICINE (6) ---
    {
        "id": "ICD10-K40.90",
        "topic": "Incarcerated & Strangulated Inguinal Hernia (Taxis vs Surgery)",
        "icd10": "K40.90",
        "specialty": "General Surgery / Emergency Medicine",
        "organ_system": "Abdominal Wall Surgical Emergency",
        "keywords": ["incarcerated hernia", "strangulated inguinal hernia", "irreducible groin lump", "erythematous tender hernia", "taxis contraindication strangulation", "emergency groin exploration"],
        "red_flags": ["bowel gangrene and ischemic perforation within 4-6 hours", "generalized feculent peritonitis", "septic shock"],
        "clinical_hallmarks": ["history of a pre-existing groin lump or bulge (indirect, direct, or femoral hernia) that previously reduced spontaneously or with gentle manual pressure", "acute presentation: SUDDEN, AGONIZING, SEVERE PAIN IN THE GROIN BULGE that has become COMPLETELY IRREDUCIBLE / INCARCERATED", "CARDINAL DIFFERENTIATION: INCARCERATION VS STRANGULATION:", "1. Incarceration: non-reducible groin mass with local discomfort; overlying skin is normal and non-tender; patient may develop mechanical small bowel obstruction (vomiting, distension, obstipation)", "2. STRANGULATION (ISCHEMIC TISSUE NECROSIS - STAT SURGICAL EMERGENCY): groin mass becomes EXQUISITELY TENDER, TENSE, FIRM, ERYTHEMATOUS, DUSKY, PURPLISH, OR HOT; systemic signs of toxicity (high fever, marked tachycardia, leukocytosis, and peritonitis)", "MANDATORY CLINICAL RULE: MANUAL REDUCTION (TAXIS) IS STRICTLY CONTRAINDICATED IF STRANGULATION IS SUSPECTED (reducing gangrenous, non-viable, necrotic bowel into the peritoneal cavity causes catastrophic generalized peritonitis and septic shock / 'reduction en masse')"],
        "pertinent_negatives": ["erythema, warmth, and exquisite tenderness confirm strangulation (taxis is strictly prohibited)"],
        "content": "Entrapment of herniated abdominal contents (omentum, small bowel) through the internal or external inguinal ring or femoral canal, with subsequent vascular compromise. Femoral hernias have highest rate of strangulation (up to 40%). Emergency Protocol: 1. Strangulated Hernia: NPO, large-bore IV resuscitation, broad-spectrum IV antibiotics (Ceftriaxone + Metronidazole), STAT Emergency Surgical Exploration (groin incision, inspection of bowel viability before and after releasing constriction ring, bowel resection and anastomosis if non-viable, hernia repair without synthetic mesh if infected); 2. Simple Incarceration (< 2 hours, no signs of strangulation): gentle manual reduction (taxis) under IV analgesia and Trendelenburg position."
    },
    {
        "id": "ICD10-K56.60",
        "topic": "Acute Mechanical Small Bowel Obstruction (Adhesive SBO & Air-Fluid Levels)",
        "icd10": "K56.60",
        "specialty": "General Surgery / Emergency Medicine",
        "organ_system": "Gastrointestinal Surgical Emergency",
        "keywords": ["small bowel obstruction", "sbo", "adhesive bowel obstruction", "air fluid levels string of pearls", "bilious vomiting abdominal distension", "obstipation high pitched bowel sounds", "gastrografin challenge sbo"],
        "red_flags": ["closed-loop obstruction / strangulation (continuous localized pain, fever, peritonitis)", "bowel ischemia and perforation", "septic shock with lactic acidosis"],
        "clinical_hallmarks": ["history of previous abdominal surgery or pelvic laparotomy (INTRA-ABDOMINAL ADHESIONS account for > 65-75% of all SBO cases)", "CARDINAL '4-SYMPTOM' COMPLEX OF SBO: 1. Colicky, crampy periumbilical abdominal pain occurring in paroxysms every few minutes; 2. PROFUSE, EARLY VOMITING (progressing from clear gastric to bilious green and finally foul, feculent-smelling vomitus); 3. Progressive abdominal distension; 4. OBSTIPATION (complete failure to pass both flatus and feces)", "auscultation: EARLY: HIGH-PITCHED, TINKLING, METALLIC BOWEL SOUNDS with hyperactive rushes; LATE: absent, silent abdomen", "Erect Abdominal Radiograph / Contrast CT Abdomen (gold standard):", "PATHOGNOMONIC RADIOGRAPHIC HALLMARKS: 1. MULTIPLE DILATED SMALL BOWEL LOOPS (> 3 cm diameter) centrally located; 2. MULTIPLE AIR-FLUID LEVELS arranged in a stepped 'stepladder' pattern on erect film; 3. 'STRING OF PEARLS' OR 'STRING OF BEADS' SIGN (tiny bubbles of air trapped between valvulae conniventes in fluid-filled bowel); 4. Complete absence of air in the colon and rectum"],
        "pertinent_negatives": ["valvulae conniventes (plicae circulares) traverse the ENTIRE width of the small bowel lumen (distinguishes from colonic haustra which only cross part-way)"],
        "content": "Mechanical blockage of the passage of intestinal contents through the small intestine. Closed-loop obstruction (e.g. volvulus) carries extreme risk of rapid strangulation. Diagnostic gold standard: Multidetector Contrast CT Abdomen/Pelvis (transition point, bowel ischemia, closed-loop). Management Protocol: 1. Initial Non-Operative Management for Uncomplicated Adhesive SBO: NPO, Nasogastric (NG) Tube Decompression, aggressive IV Crystalloid Resuscitation, urinary catheter; 2. Water-Soluble Contrast (Gastrografin) Challenge: 100 mL oral Gastrografin; if contrast reaches colon on 4-24 hour X-ray, SBO resolves non-operatively in > 90%; 3. Emergency Exploratory Laparotomy/Laparoscopy: MANDATORY if peritonitis, closed-loop, bowel ischemia (fever, localized tenderness, WBC > 15,000, elevated lactate), or failure of Gastrografin challenge after 48-72 hours."
    },
    {
        "id": "ICD10-K56.2",
        "topic": "Sigmoid Volvulus (Coffee-Bean Sign & Endoscopic Detorsion)",
        "icd10": "K56.2",
        "specialty": "General Surgery / Colorectal Surgery / Emergency Medicine",
        "organ_system": "Colorectal Surgical Emergency",
        "keywords": ["sigmoid volvulus", "coffee bean sign x-ray", "bent inner tube sign", "massive asymmetric abdominal distension", "rigid sigmoidoscopy decompression", "flatus tube detorsion", "high fiber diet elderly"],
        "red_flags": ["sigmoid gangrene and perforation with feculent peritonitis", "hypovolemic septic shock", "endoscopic detorsion contraindicated if mucosal ischemia present"],
        "clinical_hallmarks": ["predominantly affects ELDERLY, BEDRIDDEN, INSTITUTIONALIZED PATIENTS or those with chronic constipation, neuropsychiatric disease (Parkinson's, schizophrenia on psychotropics), or high-fiber diets", "MASSIVE, ENORMOUS, ASYMMETRICAL ABDOMINAL DISTENSION (often described as a 'tympanitic balloon' filling the entire abdomen, predominantly on the right and upper abdomen)", "severe constipation and complete obstipation for several days, accompanied by dull colicky lower abdominal pain and late vomiting", "percussion: universal loud, drum-like TYMPANY over the distended sigmoid loop", "Plain Abdominal Radiograph (PATHOGNOMONIC): 'COFFEE-BEAN SIGN' OR 'BENT INNER TUBE SIGN' (a massively distended, smooth, ahaustral loop of sigmoid colon originating from the left pelvis and curving upwards towards the right upper quadrant, with its two medial walls apposed to form a central thick radiodense cleft resembling the seam of a coffee bean)", "barium/Gastrografin enema: pathognomonic smooth tapered 'BIRD'S-BEAK' appearance at the site of twist"],
        "pertinent_negatives": ["absence of signs of gangrene (peritonitis, bloody rectal discharge, fever, leukocytosis) is a mandatory prerequisite for non-operative detorsion"],
        "content": "Twisting of a redundant, mobile sigmoid colon on its elongated, narrow-based mesentery through >= 180-360 degrees, producing a closed-loop large bowel obstruction. Treatment Protocol: 1. First-line Emergency Decompression (for uncomplicated volvulus without gangrene/peritonitis): BEDSIDE RIGID SIGMOIDOSCOPY OR COLONOSCOPY WITH INSERTION OF A FLATUS TUBE (soft rectal tube passed gently under direct vision beyond the twist into the distended loop, producing an EXPLOSIVE EVACUATION OF PENT-UP GAS AND LIQUID FECES with instant abdominal deflation and decompression in > 80-90%); 2. Leave flatus tube in place for 24-48 hours; 3. Definitive Cure: Elective Semi-Urgent Sigmoid Colectomy (Hartmann or primary anastomosis) during the same hospital admission (because recurrence rate after detorsion alone exceeds 50-70%); 4. Emergency Laparotomy with Hartmann's Procedure for frank gangrene or peritonitis."
    },
    {
        "id": "ICD10-T68.XXXA",
        "topic": "Accidental Hypothermia & The Osborn J-Wave",
        "icd10": "T68.XXXA",
        "specialty": "Emergency Medicine / Critical Care",
        "organ_system": "Environmental Hypothermic Emergency",
        "keywords": ["hypothermia", "accidental hypothermia", "core temp < 35c", "osborn j wave ecg", "ventricular fibrillation hypothermia", "active internal rewarming", "no one is dead until warm and dead"],
        "red_flags": ["ventricular fibrillation / asystole provoked by rough handling or endotracheal suction", "rewarming shock and afterdrop", "refractory cardiac arrest"],
        "clinical_hallmarks": ["history of cold weather exposure, cold-water immersion, elderly fall on cold floor, or severe malnutrition/intoxication", "Swiss Staging System based on Core Temperature (measured with low-reading esophageal or bladder thermistor):", "Stage I (Mild: 32 - 35C): conscious, vigorous intense shivering, tachycardia, ataxia, cold pale skin;", "Stage II (Moderate: 28 - 32C): impaired consciousness, apathy, dilated sluggish pupils, CESSATION OF SHIVERING (body exhausts metabolic shivering at < 30-32C), progressive bradycardia;", "Stage III (Severe: 24 - 28C): unconscious, comatose, profound bradycardia (HR < 30), severe hypotension, barely detectable respirations;", "Stage IV (Apparent Death: < 24C): absent vital signs, asystole or ventricular fibrillation, fixed dilated pupils, cold stiff body mimicking rigor mortis;", "PATHOGNOMONIC ECG HALLMARK: THE OSBORN J-WAVE (a prominent, dome-shaped positive deflection at the J-point [junction of QRS complex and ST segment], amplitude directly proportional to depth of hypothermia), accompanied by PR/QT prolongation and baseline shivering artifact"],
        "pertinent_negatives": ["RESUSCITATION MANDATE: 'NO ONE IS DEAD UNTIL WARM AND DEAD' (resuscitative CPR must be continued until core temperature is rewarmed to >= 32-35C)"],
        "content": "Drop in involuntary core body temperature below 35.0C (95.0F). Rewarming Protocol: 1. Extreme gentle handling (rough movements easily trigger intractable Ventricular Fibrillation in the irritable, cold myocardium); 2. Stage I: Passive External Rewarming (dry clothes, warm blankets, warm sweet drinks); 3. Stage II: Active External Rewarming (forced-air warming blankets [Bair Hugger], radiant heat applied to trunk/core); 4. Stage III/IV: Active Internal Core Rewarming: Humidified warm O2 (40-42C), IV fluids warmed to 42C, warm pleural or peritoneal lavage, and ECMO / Cardiopulmonary Bypass (gold standard for hypothermic cardiac arrest); 5. Withhold IV epinephrine and defibrillation attempts if core temp < 30C."
    },
    {
        "id": "ICD10-L03.90",
        "topic": "Acute Erysipelas vs Cellulitis (Milian's Ear Sign & Peau d'Orange)",
        "icd10": "L03.90",
        "specialty": "Dermatology / Infectious Disease / Primary Care",
        "organ_system": "Bacterial Soft Tissue Infection",
        "keywords": ["erysipelas", "cellulitis", "milians ear sign", "sharply demarcated raised border", "peau d orange skin", "streptococcus pyogenes cellulitis", "flucloxacillin cefazolin"],
        "red_flags": ["necrotizing fasciitis (pain out of proportion, bullae, crepitus, skin anesthesia)", "orbital cellulitis with ophthalmoplegia", "bacteremic sepsis"],
        "clinical_hallmarks": ["CLINICAL AND ANATOMICAL DIFFERENTIATION: ERYSIPELAS VS CELLULITIS:", "1. ERYSIPELAS (Superficial Dermis & Lymphatics - Streptococcus pyogenes / Group A Strep): abrupt onset of high fever and chills followed by a FIERY RED, GLISTENING, SHINY, TENSE, INDURATED PLAQUE with SHARPLY DEMARCATED, DISTINCT, ELEVATED BORDERS; rapidly advancing; PATHOGNOMONIC MILIAN'S EAR SIGN (involvement of the ear pinna confirms erysipelas, because the earlobe has skin and dermis but NO deep subcutaneous tissue, making deep cellulitis impossible);", "2. CELLULITIS (Deep Dermis & Subcutaneous Fat - Strep pyogenes & Staphylococcus aureus): gradual onset of erythema, edema, warmth, and tenderness with POORLY DEMARCATED, INDISTINCT, DIFFUSE BORDERS that blend gradually into surrounding normal skin; PATHOGNOMONIC PEAU D'ORANGE APPEARANCE (dimpled, orange-peel cutaneous pitting caused by cutaneous lymphatic obstruction around hair follicles)", "predominantly affects lower extremities (> 80%), followed by face, arms, and surgical sites", "unilateral presentation; associated with tinea pedis (cracked toe webs as entry portal) or chronic lymphedema"],
        "pertinent_negatives": ["sharply demarcated raised margin and ear involvement confirm superficial erysipelas (distinguishes from indistinct deep cellulitis)"],
        "content": "Acute bacterial infection of dermis and subcutaneous tissues. Diagnostic workup: Clinical diagnosis; outline advancing border with skin marker to track therapy. Protocol: 1. Elevate the affected limb continuously (accelerates resolution of edema); 2. Treat portal of entry (antifungal cream for tinea pedis); 3. Antimicrobial Therapy: Erysipelas (Group A Strep): Oral Penicillin V (500 mg QID) OR Amoxicillin OR IV Aqueous Penicillin G; Cellulitis (covering Strep + MSSA): Oral Flucloxacillin (500 mg QID for 5-7 days) OR Cephalexin (500 mg QID) OR IV Cefazolin; Add Vancomycin or Linezolid if MRSA suspected or purulent drainage present."
    },
    {
        "id": "ICD10-T57.0X1A",
        "topic": "Acute & Chronic Arsenic Toxicity (Raindrop Pigmentation & Mees Lines)",
        "icd10": "T57.0X1A",
        "specialty": "Clinical Toxicology / Occupational Medicine / Dermatology",
        "organ_system": "Environmental Heavy Metal Toxicology",
        "keywords": ["arsenic poisoning", "arsenicosis", "raindrop pigmentation", "arsenical keratosis palms soles", "mees lines nails", "garlic breath arsenic", "dimercaprol bal", "contaminated tube well water"],
        "red_flags": ["malignancy: Squamous Cell Carcinoma of skin, bladder cancer, lung cancer", "acute circulatory collapse / hemorrhagic gastroenteritis", "severe sensory neuropathy"],
        "clinical_hallmarks": ["chronic ingestion of arsenic-contaminated groundwater from shallow tube-wells (widespread in Ganga-Brahmaputra delta: West Bengal, Bangladesh, Bihar) or occupational exposure", "ACUTE POISONING: Pungent 'GARLIC-LIKE' ODOR to breath; severe, agonizing burning abdominal pain, profuse 'rice-water' bloody diarrhea, vomiting, dehydration, and QTc prolongation (Torsades de Pointes)", "CHRONIC ARSENICOSIS (PATHOGNOMONIC CUTANEOUS HALLMARKS):", "1. 'RAINDROP' HYPERPIGMENTATION: mottled, diffuse, dark brown hyperpigmentation interspersed with small, pale, macules of normal/depigmented skin resembling 'raindrops on a dusty road', characteristically on trunk, chest, and abdomen;", "2. ARSENICAL PALMOPLANTAR KERATOSIS: rough, hard, punctate, corn-like hyperkeratotic papules and plaques over the PALMS AND SOLES (high propensity for transformation into invasive Bowen's disease and Squamous Cell Carcinoma);", "3. MEES' LINES: transverse, non-palpable, white, parallel bands across the entire width of all fingernails and toenails", "chronic peripheral sensorimotor 'glove-and-stocking' axonal neuropathy (painful burning dysesthesias in feet)"],
        "pertinent_negatives": ["24-hour urinary arsenic collection (> 50-100 mcg/L) confirms exposure (patient must avoid seafood for 48 hours prior to test to exclude non-toxic organic arsenobetaine)"],
        "content": "Toxic cellular poisoning by trivalent arsenite (As3+) which binds lipoic acid sulfhydryl groups, inhibiting pyruvate dehydrogenase and Krebs cycle ATP synthesis. Diagnostic gold standard: 24-hour urinary arsenic excretion, hair and nail arsenic levels. Treatment Protocol: 1. STAT PROVISION OF ARSENIC-FREE DRINKING WATER (filters, deep aquifers); 2. Acute Poisoning Chelation: STAT Intramuscular Dimercaprol (BAL - British Anti-Lewisite: 3-5 mg/kg IM q4h in peanut oil) OR oral Succimer (DMSA: 10 mg/kg TID for 5 days, then BID for 14 days); 3. Chronic Keratoses: Topical keratolytics (20% urea cream, topical retinoic acid); 4. Strict lifelong surveillance for cutaneous, bladder, and pulmonary malignancies."
    },

    # --- 18. ORTHOPEDICS & TRAUMA (6) ---
    {
        "id": "ICD10-G56.00",
        "topic": "Carpal Tunnel Syndrome (Phalen Sign, Tinel Sign & Median Neuropathy)",
        "icd10": "G56.00",
        "specialty": "Orthopedics / Neurology / Hand Surgery",
        "organ_system": "Peripheral Compressive Neuropathy",
        "keywords": ["carpal tunnel syndrome", "cts", "median nerve compression", "phalen test tinel sign", "thenar muscle atrophy", "numbness thumb index middle finger", "flick sign", "carpal tunnel release"],
        "red_flags": ["irreversible thenar motor atrophy and loss of thumb opposition", "permanent sensory anesthesia of fingertips"],
        "clinical_hallmarks": ["most common compressive focal mononeuropathy of the human body, with strong female predilection (female:male 3:1)", "burning pain, tingling paresthesias, and numbness strictly confined to the MEDIAN NERVE SENSORY DISTRIBUTION (palmar aspect of THUMB, INDEX FINGER, MIDDLE FINGER, and radial half of RING FINGER, with STRICT SPARING of the little finger)", "symptoms are CHARACTERISTICALLY WORST AT NIGHT, waking the patient from sleep with agonizing numbness; PATHOGNOMONIC 'FLICK SIGN' (patient vigorously shakes, flicks, or wrings their hand to relieve symptoms, like shaking down a thermometer)", "PROVOCATIVE PHYSICAL EXAMINATION SIGNS:", "1. PHALEN'S TEST (positive: complete flexion of wrists at 90 degrees for 60 seconds reproduces paresthesias in median distribution);", "2. TINEL'S SIGN (positive: light percussion over the volar carpal tunnel produces electric-shock sensations radiating into the fingers);", "3. DURKAN'S TEST (Carpal Compression Test - most sensitive: direct thumb pressure over carpal tunnel reproduces tingling within 30 seconds);", "severe chronic disease: VISIBLE ATROPHY AND FLATTENING OF THE THENAR EMINENCE (abductor pollicis brevis weakness with weak thumb opposition / 'ape-hand' deformity)"],
        "pertinent_negatives": ["palmar cutaneous branch spares the proximal palm (dermatome over thenar base is normal because nerve branches proximal to carpal tunnel)"],
        "content": "Increased pressure within the unyielding fibro-osseous carpal tunnel leading to ischemia and demyelination of the median nerve. Predisposing factors: repetitive wrist flexion, pregnancy, hypothyroidism, diabetes, rheumatoid arthritis. Diagnostic confirmation: Nerve Conduction Studies (NCS: prolonged median distal motor and sensory latencies). Treatment: 1. Conservative (mild-moderate): Volar neutral wrist splinting worn strictly at NIGHT for 6-8 weeks + ergonomic modification; 2. Local Carpal Tunnel Corticosteroid Injection (Triamcinolone 20-40 mg) provides substantial temporary relief; 3. Definitive Surgical Cure: Carpal Tunnel Release (open or endoscopic division of the transverse carpal ligament / flexor retinaculum, achieving > 90-95% long-term cure)."
    },
    {
        "id": "ICD10-M72.2",
        "topic": "Plantar Fasciitis (First-Step Morning Heel Pain & Windlass Mechanism)",
        "icd10": "M72.2",
        "specialty": "Orthopedics / Podiatry / Sports Medicine",
        "organ_system": "Musculoskeletal Enthesopathy",
        "keywords": ["plantar fasciitis", "first step morning heel pain", "calcaneal spur", "windlass test positive", "medial calcaneal tuberosity tenderness", "plantar fascia stretching", "night splints"],
        "red_flags": ["rupture of plantar fascia (sudden pop with ecchymosis, often post-steroid injection)", "calcaneal stress fracture"],
        "clinical_hallmarks": ["most common cause of inferior heel pain in adults (affecting runners, dancers, obese individuals, and workers with prolonged standing on hard surfaces)", "CARDINAL PATHOGNOMONIC SYMPTOM: EXCRUCIATING, SHARP, STABBING HEEL PAIN EXPERIENCED WITH THE VERY FIRST FEW STEPS OUT OF BED IN THE MORNING, or after prolonged periods of sitting and inactivity", "the pain gradually eases and warms up after walking for 5-10 minutes, but characteristically worsens again towards the end of the day or after prolonged standing", "PHYSICAL EXAMINATION HALLMARK: EXQUISITE, SHARPLY LOCALIZED POINT TENDERNESS OVER THE ANTEROMEDIAL ASPECT OF THE CALCANEAL TUBEROSITY (the origin of the plantar fascia)", "PATHOGNOMONIC BIOMECHANICAL SIGN: POSITIVE WINDLASS TEST (passive, forced dorsiflexion of the hallux / big toe stretches the plantar fascia over the metatarsal head, reproducing the sharp inferior heel pain)", "plain lateral foot radiographs: calcaneal traction spur present in 50% (spur is an incidental traction finding, NOT the cause of pain)"],
        "pertinent_negatives": ["absence of resting night pain (persistent night pain raises suspicion of calcaneal tumor or infection)"],
        "content": "Chronic degenerative micro-tearing and failed healing response (plantar fasciosis, rather than acute inflammation) at the enthesis of the plantar aponeurosis into the calcaneus. First-Line Conservative Protocol (effective in > 90-95% of patients over 6-12 months): 1. Plantar Fascia and Achilles Tendon Specific Stretching Exercises (performed multiple times daily, especially before the first morning step); 2. Footwear modifications: cushioned shoes with rigid arch support and silicone heel cups; 3. Night Splints (maintains foot in 5 degrees dorsiflexion overnight to prevent fascia shortening); 4. Short-course oral NSAIDs; 5. Extracorporeal Shock Wave Therapy (ESWT) for chronic refractory cases (> 6 months); 6. Plantar fascia release surgery reserved only for severe failed cases."
    },
    {
        "id": "ICD10-S83.511A",
        "topic": "Acute Anterior Cruciate Ligament Tear (Audible Pop & Lachman Test)",
        "icd10": "S83.511A",
        "specialty": "Orthopedic Sports Medicine / Trauma Surgery",
        "organ_system": "Knee Ligamentous Emergency",
        "keywords": ["acl tear", "anterior cruciate ligament", "audible pop knee", "lachman test", "pivot shift test", "acute hemarthrosis knee", "mri knee acl reconstruction"],
        "red_flags": ["the 'Unhappy Triad' of O'Donoghue (concurrent ACL tear, Medial Meniscus tear, and MCL tear)", "acute multiligamentous knee dislocation (popliteal artery injury)", "subchondral bone contusion"],
        "clinical_hallmarks": ["classic non-contact deceleration, cutting, pivoting, or hyperextension athletic injury (soccer, basketball, skiing)", "PATHOGNOMONIC PATIENT HISTORY: SENSATION OR AUDIBLE 'LOUD POP' OR 'CRACK' DEEP INSIDE THE KNEE AT THE MOMENT OF INJURY", "immediate, sudden collapse of the knee ('giving way') with complete inability to continue sports or bear weight", "PATHOGNOMONIC PHYSICAL EXAMINATION FINDING: RAPID, TENSE, MASSIVE HEMARTHROSIS (knee swells dramatically WITHIN 1 TO 4 HOURS of injury due to rupture of the middle genicular artery supplying the ACL - arthrocentesis yields frank blood with fat globules)", "DIAGNOSTIC CLINICAL TESTS:", "1. LACHMAN TEST (SINGLE MOST SENSITIVE CLINICAL TEST > 95%): with knee flexed to 20-30 degrees, anterior translation of the tibia demonstrates increased anterior excursion with a SOFT, MUSHY, ABSENT ENDPOINT;", "2. PIVOT SHIFT TEST (most specific for dynamic rotational instability): reproduces the athletic giving-way episode;", "3. Anterior Drawer Test (less sensitive due to hamstring spasm)", "MRI of Knee (gold standard, sensitivity > 95%): complete disruption of ACL fibers and pathognomonic 'kissing bone contusions' (bone marrow edema in lateral femoral condyle and posterior lateral tibial plateau)"],
        "pertinent_negatives": ["swelling developing rapidly within 1-4 hours indicates hemarthrosis (swelling developing > 24 hours suggests meniscal tear or reactive effusion)"],
        "content": "Full-thickness rupture of the anterior cruciate ligament, the primary restraint against anterior tibial translation and rotatory knee instability. Protocol: 1. Acute phase: RICE protocol (Rest, Ice, Compression, Elevation), knee immobilizer/brace, crutches, and aspiration of tense hemarthrosis for severe pain; 2. Preoperative 'Pre-habilitation' to regain full knee extension and quadriceps strength; 3. Surgical Reconstruction: Arthroscopic ACL Reconstruction using autologous graft (Bone-Patellar Tendon-Bone [BPTB] or Quadruple Hamstring or Quadriceps tendon autograft) indicated for active patients and cutting sports to restore knee stability and prevent secondary meniscal breakdown."
    },
    {
        "id": "ICD10-M65.4",
        "topic": "De Quervain's Tenosynovitis (Finkelstein Test & Radial Styloid)",
        "icd10": "M65.4",
        "specialty": "Orthopedics / Hand Surgery / Primary Care",
        "organ_system": "Musculoskeletal Tenosynovitis",
        "keywords": ["de quervain tenosynovitis", "finkelstein test", "first dorsal compartment wrist", "radial styloid pain", "extensor pollicis brevis abductor pollicis longus", "mothers wrist", "thumb spica splint"],
        "red_flags": ["superficial radial nerve injury from steroid injection or surgery", "severe chronic functional hand disability"],
        "clinical_hallmarks": ["stenosing tenosynovitis of the FIRST DORSAL EXTENSOR COMPARTMENT of the wrist, containing the tendons of the ABDUCTOR POLLICIS LONGUS (APL) and EXTENSOR POLLICIS BREVIS (EPB)", "predominantly affects women (female:male 6:1), classically NEW MOTHERS ('Mother's Wrist' - repeatedly lifting an infant with thumbs extended and wrists deviated) and individuals with repetitive thumb texting or forceful gripping", "constant, severe, aching pain localized directly over the RADIAL STYLOID PROCESS, radiating proximally into forearm or distally into thumb", "pain is aggravated by thumb extension, abduction, and pinching motions", "palpation: well-circumscribed tenderness and visible fusiform swelling over the first dorsal compartment at the radial styloid", "PATHOGNOMONIC DIAGNOSTIC MANEUVER: POSITIVE FINKELSTEIN'S TEST (the patient folds their thumb into the palm, clasps their fingers tightly over the thumb to make a fist, and the examiner gently ulnarly deviates the wrist: this reproduces EXCRUCIATING, SHARP PAIN over the radial styloid)"],
        "pertinent_negatives": ["pain is strictly over the radial styloid (pain at anatomical snuffbox indicates scaphoid pathology)"],
        "content": "Thickening and stenosing friction of the fibrous sheath enclosing the APL and EPB tendons over the radial styloid. Treatment Protocol: 1. First-line Conservative: Rigid THUMB SPICA SPLINT (immobilizing thumb IP and MCP joints and wrist) worn continuously for 4-6 weeks + oral NSAIDs + activity modification; 2. Local Corticosteroid Injection: Ultrasound-guided injection of Triamcinolone (20 mg) into the first dorsal extensor compartment sheath (success rate > 80-90% cure, take care to identify multiple sub-compartments); 3. Surgical Decompression: Surgical release of the first dorsal extensor retinaculum with identification of separate EPB slip and protection of superficial radial sensory nerve branches."
    },
    {
        "id": "ICD10-M48.061",
        "topic": "Lumbar Spinal Canal Stenosis (Neurogenic Claudication & Shopping Cart Sign)",
        "icd10": "M48.061",
        "specialty": "Orthopedic Spine Surgery / Neurosurgery / Neurology",
        "organ_system": "Spinal Degenerative",
        "keywords": ["lumbar spinal stenosis", "neurogenic claudication", "pseudoclaudication", "shopping cart sign", "relief bending forward", "ligamentum flavum hypertrophy", "decompressive lumbar laminectomy"],
        "red_flags": ["cauda equina syndrome (saddle anesthesia, bowel/bladder incontinence)", "rapidly progressing motor foot drop", "severe myelopathy"],
        "clinical_hallmarks": ["predominantly affects OLDER ADULTS (> 60-65 years of age) resulting from chronic degenerative spondylosis (facet joint osteoarthritis, disc bulging, and pathognomonic HYPERTROPHY OF THE LIGAMENTUM FLAVUM)", "CARDINAL PATHOGNOMONIC SYMPTOM: NEUROGENIC CLAUDICATION (PSEUDOCLAUDICATION):", "bilateral (or unilateral) dull ache, heaviness, numbness, tingling paresthesias, and weakness in the buttocks, thighs, and calves TRIGGERED BY WALKING OR PROLONGED STANDING", "PATHOGNOMONIC RELIEF MANEUVER: SYMPTOMS ARE PROMPTLY AND DRAMATICALLY RELIEVED BY BENDING FORWARD OR SITTING DOWN (flexing the lumbar spine widens the canal cross-sectional area by up to 25% and reduces venous congestion);", "THE 'SHOPPING CART SIGN': patients walk with a forward-stooped posture and can walk long distances without pain IF LEANING FORWARD OVER A GROCERY SHOPPING CART OR BICYCLE (in sharp contrast to vascular claudication where posture makes no difference)", "MRI of Lumbar Spine (gold standard): central canal cross-sectional area < 75-100 mm2, lateral recess narrowing, and ligamentum flavum thickening (characteristically L4-L5 and L3-L4)"],
        "pertinent_negatives": ["normal pedal pulses and absence of skin trophic changes distinguish neurogenic from vascular claudication"],
        "content": "Mechanical compression of lumbosacral nerve roots within the narrowed spinal canal. Treatment: 1. Conservative (mild-moderate): Physical therapy focusing on flexion-based core exercises, stationary cycling, NSAIDs, Gabapentin; 2. Epidural Corticosteroid Injections (interlaminar or transforaminal) provide intermediate-term symptomatic relief; 3. Definitive Surgical Treatment: Lumbar Decompressive Laminectomy (flavectomy and partial medial facetectomy +/- instrumented fusion if spondylolisthesis present) provides dramatic and durable walking endurance and pain relief."
    },
    {
        "id": "ICD10-M62.82",
        "topic": "Acute Rhabdomyolysis (Crush Injury & Serum Creatine Kinase > 5000)",
        "icd10": "M62.82",
        "specialty": "Nephrology / Critical Care / Emergency Medicine",
        "organ_system": "Musculoskeletal / Renal Emergency",
        "keywords": ["rhabdomyolysis", "crush syndrome", "tea colored urine myoglobinuria", "creatine kinase ck > 5000", "acute kidney injury rhabdomyolysis", "hyperkalemia rhabdomyolysis", "aggressive iv hydration"],
        "red_flags": ["fatal hyperkalemic cardiac arrest within hours of extrication", "oliguric acute tubular necrosis (acute renal failure)", "disseminated intravascular coagulation (dic)"],
        "clinical_hallmarks": ["precipitating causes: crush injuries / prolonged immobilization (elderly 'found down' on floor), strenuous unaccustomed exercise (marathon, crossfit), seizures, heat stroke, electrocution, or statin-fibrate interactions", "CLASSIC CLINICAL TRIAD (present in < 50%): 1. Severe muscle pain (myalgias); 2. Muscle weakness; 3. DARK, TEA-COLORED, COLA-COLORED, OR REDDISH-BROWN URINE (MYOGLOBINURIA)", "affected muscle groups (thighs, calves, lower back) are swollen, exquisitely tender, and indurated", "PATHOGNOMONIC URINALYSIS DISCREPANCY: URINE DIPSTICK POSITIVE FOR 'BLOOD', BUT URINE MICROSCOPY SHOWS VIRTUALLY NO RED BLOOD CELLS (the orthotolidine dipstick reagent cannot differentiate between hemoglobin and myoglobin; absence of intact RBCs confirms myoglobinuria)", "LABORATORY GOLD STANDARD: SERUM CREATINE KINASE (CK) ELEVATED TO >= 5 TIMES UPPER LIMIT OF NORMAL (typically > 5,000 - 50,000 IU/L, often exceeding 100,000 IU/L)", "early lethal metabolic derangements: HYPERKALEMIA (massive release of intracellular potassium from lysed myocytes), hyperphosphatemia, hyperuricemia, and early hypocalcemia followed by late hypercalcemia"],
        "pertinent_negatives": ["dipstick positive for blood with negative microscopic RBCs is the classic signature of myoglobinuria"],
        "content": "Rapid breakdown and necrosis of skeletal muscle tissue resulting in leakage of intracellular myocyte contents (myoglobin, CK, potassium, phosphate, aldolase) into the systemic circulation. Myoglobin causes acute tubular necrosis through renal vasoconstriction, tubular cast obstruction, and direct iron-catalyzed oxidative cytotoxicity. STAT Emergency Resuscitation Protocol: 1. IMMEDIATE AGGRESSIVE INTRAVENOUS FLUID RESUSCITATION: IV Crystalloids (0.9% Normal Saline or Ringer's Lactate initiated at 1.0 - 1.5 L/hr, maintaining a target urine output of 200 - 300 mL/hr until CK drops < 1,000-5,000 IU/L); 2. STAT TREATMENT OF HYPERKALEMIA (IV Calcium Gluconate for cardiac membrane stabilization, IV Insulin + Dextrose, nebulized Albuterol); 3. Urine alkalinization (IV Sodium Bicarbonate targeting urine pH > 6.5) prevents myoglobin cast precipitation; 4. Emergency Hemodialysis for refractory hyperkalemia or anuric renal failure."
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
            
    print(f"Batch 6 Finish added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

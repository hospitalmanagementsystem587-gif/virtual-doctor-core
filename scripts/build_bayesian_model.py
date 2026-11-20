#!/usr/bin/env python3
"""
Bayesian Diagnostic Model Compiler
Compiles the 4,920 Kaggle cases, 132 symptoms, and 41 diseases into an optimized,
precomputed Bayesian inference matrix with canonical ICD-10 protocols and precautions.
"""

import os
import csv
import json
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KAGGLE_DIR = os.path.join(BASE_DIR, "knowledge_base", "kaggle_data")
OUTPUT_PATH = os.path.join(KAGGLE_DIR, "bayesian_diagnostic_model.json")

# Canonical clinical mapping for all 41 Kaggle diseases
CANONICAL_CLINICAL_MAP = {
    "(vertigo) Paroymsal  Positional Vertigo": {
        "id": "ICD10-H81",
        "topic": "Benign Paroxysmal Positional Vertigo (BPPV)",
        "icd10": "H81.10",
        "specialty": "ENT / Neurology",
        "emergency": False,
        "workup": [
            {"test_name": "Dix-Hallpike Bedside Diagnostic Maneuver", "investigation_type": "Specialized Bedside", "urgency": "Routine", "clinical_purpose": "Confirm posterior canal canalithiasis nystagmus"},
            {"test_name": "Audiometry & Vestibular Function Testing", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Assess for coexisting inner ear pathology"}
        ]
    },
    "AIDS": {
        "id": "ICD10-B20",
        "topic": "Human Immunodeficiency Virus (HIV) Disease / AIDS",
        "icd10": "B20",
        "specialty": "Infectious Diseases / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "4th Generation HIV-1/2 Ag/Ab Immunoassay", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Detect HIV p24 antigen and specific antibodies"},
            {"test_name": "CD4+ T-Lymphocyte Count & Plasma HIV-1 RNA Viral Load", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Staging of immunosuppression and baseline viral replication"}
        ]
    },
    "Acne": {
        "id": "ICD10-L70.0",
        "topic": "Acne Vulgaris",
        "icd10": "L70.0",
        "specialty": "Dermatology",
        "emergency": False,
        "workup": [
            {"test_name": "Clinical Dermatological Lesion Grading", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Grade comedones, papules, pustules, and nodulocystic lesions"},
            {"test_name": "Serum Total/Free Testosterone & DHEAS (if hyperandrogenism signs)", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Evaluate endocrine hyperandrogenic etiology"}
        ]
    },
    "Alcoholic hepatitis": {
        "id": "ICD10-K70.1",
        "topic": "Alcoholic Hepatitis & Steatohepatitis",
        "icd10": "K70.1",
        "specialty": "Gastroenterology / Hepatology",
        "emergency": False,
        "workup": [
            {"test_name": "Comprehensive Liver Function Panel (AST/ALT ratio > 2:1, Bilirubin)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Quantify hepatocellular necrosis and calculate Maddrey's DF"},
            {"test_name": "Coagulation Profile (PT/INR) & Serum Albumin", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess hepatic synthetic capacity and coagulopathy"},
            {"test_name": "Abdominal Ultrasound with Doppler", "investigation_type": "Imaging", "urgency": "Priority", "clinical_purpose": "Rule out biliary obstruction, portal vein thrombosis, and ascites"}
        ]
    },
    "Allergy": {
        "id": "ICD10-T78.4",
        "topic": "Allergic Rhinitis & Hypersensitivity Reaction",
        "icd10": "T78.40",
        "specialty": "Allergy & Immunology / General Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Complete Blood Count (Absolute Eosinophil Count - AEC)", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Evaluate peripheral eosinophilia"},
            {"test_name": "Total Serum IgE & Allergen-Specific IgE", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Identify atopic predisposition and specific aeroallergen triggers"}
        ]
    },
    "Arthritis": {
        "id": "ICD10-M19.9",
        "topic": "Inflammatory Arthritis & Joint Effusion",
        "icd10": "M19.90",
        "specialty": "Rheumatology / Orthopedics",
        "emergency": False,
        "workup": [
            {"test_name": "Inflammatory Markers (ESR & High-Sensitivity CRP)", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Quantify systemic synovitis and inflammatory activity"},
            {"test_name": "Rheumatoid Factor (RF) & Anti-CCP Antibodies", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Differentiate autoimmune rheumatoid arthritis from degenerative arthropathy"},
            {"test_name": "Plain Radiograph (X-Ray) of Symptomatic Joints", "investigation_type": "Imaging", "urgency": "Routine", "clinical_purpose": "Detect erosions, joint space narrowing, and periarticular osteopenia"}
        ]
    },
    "Bronchial Asthma": {
        "id": "ICD10-J45",
        "topic": "Bronchial Asthma & Acute Bronchospasm",
        "icd10": "J45.901",
        "specialty": "Pulmonology / Respiratory Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Peak Expiratory Flow Rate (PEFR) & Pulse Oximetry (SpO2)", "investigation_type": "Point-of-Care Bedside", "urgency": "Stat", "clinical_purpose": "Assess airflow limitation and hypoxemia severity"},
            {"test_name": "Pre- and Post-Bronchodilator Spirometry (FEV1/FVC)", "investigation_type": "Specialized Bedside", "urgency": "Priority", "clinical_purpose": "Confirm reversible obstructive airway defect"},
            {"test_name": "Chest Radiograph (CXR PA View)", "investigation_type": "Imaging", "urgency": "Routine", "clinical_purpose": "Exclude pneumothorax, consolidation, or foreign body aspiration"}
        ]
    },
    "Cervical spondylosis": {
        "id": "ICD10-M47",
        "topic": "Cervical Spondylosis & Cervical Radiculopathy",
        "icd10": "M47.812",
        "specialty": "Orthopedics / Neurology",
        "emergency": False,
        "workup": [
            {"test_name": "Cervical Spine Plain Radiographs (AP, Lateral, Oblique views)", "investigation_type": "Imaging", "urgency": "Routine", "clinical_purpose": "Assess disc space narrowing, osteophytes, and neural foramen stenosis"},
            {"test_name": "Spurling's Bedside Test & Upper Limb Neurological Reflexes", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Evaluate cervical nerve root compression and myelopathic signs"}
        ]
    },
    "Chicken pox": {
        "id": "ICD10-B01.9",
        "topic": "Varicella Zoster Infection (Chickenpox)",
        "icd10": "B01.9",
        "specialty": "Infectious Diseases / Pediatrics",
        "emergency": False,
        "workup": [
            {"test_name": "Clinical Dermatological Pleomorphic Rash Assessment", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Verify simultaneous macules, papules, vesicles ('dewdrops on rose petal') and crusts"},
            {"test_name": "VZV PCR / Tzanck Smear from Unroofed Vesicle", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Microscopic and molecular confirmation in atypical cases"}
        ]
    },
    "Chronic cholestasis": {
        "id": "ICD10-K83.1",
        "topic": "Chronic Cholestasis & Biliary Stasis",
        "icd10": "K83.1",
        "specialty": "Gastroenterology / Hepatology",
        "emergency": False,
        "workup": [
            {"test_name": "Serum Alkaline Phosphatase (ALP) & GGT with Direct Bilirubin", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Confirm cholestatic enzymatic pattern and biliary excretion defect"},
            {"test_name": "High-Resolution Abdominal Ultrasound / MRCP", "investigation_type": "Imaging", "urgency": "Priority", "clinical_purpose": "Distinguish intrahepatic cholestasis from extrahepatic mechanical obstruction"}
        ]
    },
    "Common Cold": {
        "id": "ICD10-J00",
        "topic": "Acute Nasopharyngitis (Common Cold)",
        "icd10": "J00",
        "specialty": "General Medicine / Family Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Anterior Rhinoscopy & Oropharyngeal Examination", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Rule out acute streptococcal pharyngitis, sinusitis, or otitis media"}
        ]
    },
    "Dengue": {
        "id": "ICD10-A90",
        "topic": "Dengue Fever with Warning Signs Triage",
        "icd10": "A90",
        "specialty": "Infectious Diseases / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Dengue NS1 Antigen (Day 1-5) & Dengue IgM/IgG Serology", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Serological confirmation of acute flavivirus viremia"},
            {"test_name": "Serial Complete Blood Count (Hematocrit & Platelet Count)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Monitor hemoconcentration (>20% rise in Hct) and acute thrombocytopenia (<100,000)"},
            {"test_name": "Bedside Focused Ultrasound (FAST) for Plasma Leakage", "investigation_type": "Imaging", "urgency": "Priority", "clinical_purpose": "Detect subclinical ascites, gallbladder wall thickening, and pleural effusion"}
        ]
    },
    "Diabetes ": {
        "id": "ICD10-E11",
        "topic": "Type 2 Diabetes Mellitus & Hyperglycemic Triage",
        "icd10": "E11.9",
        "specialty": "Endocrinology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Glycated Hemoglobin (HbA1c) & Fasting Plasma Glucose (FPG)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Evaluate 3-month glycemic control and fasting hyperglycemia"},
            {"test_name": "Serum Creatinine, eGFR & Urine Albumin-to-Creatinine Ratio (UACR)", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Screen for diabetic nephropathy and microalbuminuria"},
            {"test_name": "Comprehensive Diabetic Foot & Monofilament Sensory Exam", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Screen for peripheral sensory neuropathy and vasculopathy"}
        ]
    },
    "Dimorphic hemmorhoids(piles)": {
        "id": "ICD10-K64",
        "topic": "Hemorrhoids (Piles) - Internal & External",
        "icd10": "K64.9",
        "specialty": "General Surgery / Proctology",
        "emergency": False,
        "workup": [
            {"test_name": "Digital Rectal Examination (DRE) & Anoscopy / Proctoscopy", "investigation_type": "Specialized Clinical", "urgency": "Priority", "clinical_purpose": "Grade internal piles (Grade I-IV) and evaluate for thrombosis/fissure"},
            {"test_name": "Complete Blood Count (Hemoglobin & Hematocrit)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess severity of iron deficiency anemia from chronic per-rectal bleeding"}
        ]
    },
    "Drug Reaction": {
        "id": "ICD10-L27.0",
        "topic": "Adverse Cutaneous Drug Reaction / Drug Eruption",
        "icd10": "L27.0",
        "specialty": "Dermatology / Clinical Pharmacology",
        "emergency": False,
        "workup": [
            {"test_name": "Medication Timeline & Dechallenge Chronology Audit", "investigation_type": "Specialized Clinical", "urgency": "Priority", "clinical_purpose": "Pinpoint offending causative pharmaceutical agent"},
            {"test_name": "Complete Blood Count with Absolute Eosinophil Count", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess eosinophilia and rule out DRESS syndrome"},
            {"test_name": "Comprehensive Metabolic Panel (Liver & Renal Function)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Detect occult visceral organ involvement"}
        ]
    },
    "Fungal infection": {
        "id": "ICD10-B35",
        "topic": "Superficial Fungal Infection (Tinea / Cutaneous Dermatophytosis)",
        "icd10": "B35.9",
        "specialty": "Dermatology",
        "emergency": False,
        "workup": [
            {"test_name": "10-20% Potassium Hydroxide (KOH) Mount of Active Margin Scrapings", "investigation_type": "Specialized Bedside", "urgency": "Routine", "clinical_purpose": "Demonstrate branching septate hyphae and arthroconidia"},
            {"test_name": "Wood's Lamp Ultraviolet Examination", "investigation_type": "Specialized Bedside", "urgency": "Routine", "clinical_purpose": "Rule out Corynebacterium erythrasma and tinea versicolor fluorescence"}
        ]
    },
    "GERD": {
        "id": "ICD10-K21",
        "topic": "Gastroesophageal Reflux Disease (GERD) & Reflux Esophagitis",
        "icd10": "K21.9",
        "specialty": "Gastroenterology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Diagnostic Upper GI Endoscopy (Esophagogastroduodenoscopy - EGD)", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Identify mucosal erosions, Los Angeles grade reflux, Barrett's esophagus"},
            {"test_name": "12-Lead Electrocardiogram (ECG) & Baseline Cardiac Check", "investigation_type": "Specialized Bedside", "urgency": "Priority", "clinical_purpose": "Unambiguously rule out acute ischemic heart disease presenting as heartburn"}
        ]
    },
    "Gastroenteritis": {
        "id": "ICD10-K52",
        "topic": "Acute Gastroenteritis & Foodborne Enteritis",
        "icd10": "K52.9",
        "specialty": "Gastroenterology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Stool Routine, Microscopy & Occult Blood", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Differentiate secretory viral watery diarrhea from invasive dysentery (pus cells, RBCs)"},
            {"test_name": "Serum Electrolytes (Sodium, Potassium, Bicarbonate) & Creatinine", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Quantify dehydration-induced hypokalemia, metabolic acidosis, and pre-renal AKI"}
        ]
    },
    "Heart attack": {
        "id": "ICD10-I21",
        "topic": "Acute Myocardial Infarction (STEMI / NSTEMI / ACS)",
        "icd10": "I21.9",
        "specialty": "Cardiology / Emergency Medicine",
        "emergency": True,
        "workup": [
            {"test_name": "Stat 12-Lead Electrocardiogram (ECG within 10 minutes of arrival)", "investigation_type": "Point-of-Care Bedside", "urgency": "Stat", "clinical_purpose": "Identify ST-segment elevation, pathological Q-waves, or new LBBB"},
            {"test_name": "High-Sensitivity Cardiac Troponin I/T (Serial 0h / 1h / 3h)", "investigation_type": "Laboratory", "urgency": "Stat", "clinical_purpose": "Confirm acute myocardial necrosis and dynamic rise/fall curve"},
            {"test_name": "Bedside Focused Transthoracic Echocardiogram (Echo)", "investigation_type": "Imaging", "urgency": "Stat", "clinical_purpose": "Evaluate regional wall motion abnormalities (RWMA) and ejection fraction"}
        ]
    },
    "Hepatitis B": {
        "id": "ICD10-B16",
        "topic": "Acute / Chronic Viral Hepatitis B",
        "icd10": "B16.9",
        "specialty": "Gastroenterology / Hepatology",
        "emergency": False,
        "workup": [
            {"test_name": "Hepatitis B Serology Panel (HBsAg, Anti-HBs, Anti-HBc IgM & Total)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Differentiate acute infection from chronic carrier state"},
            {"test_name": "Quantitative HBV DNA Viral Load (Real-Time PCR)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Quantify circulating viral burden for antiviral therapy eligibility"},
            {"test_name": "Comprehensive Liver Function Panel & Abdominal Sonogram", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess transaminase surge and structural parenchymal changes"}
        ]
    },
    "Hepatitis C": {
        "id": "ICD10-B18.2",
        "topic": "Viral Hepatitis C (HCV Infection)",
        "icd10": "B18.2",
        "specialty": "Gastroenterology / Hepatology",
        "emergency": False,
        "workup": [
            {"test_name": "Anti-HCV Antibody Screening Immunoassay", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Initial serological detection of exposure to Hepatitis C virus"},
            {"test_name": "Quantitative HCV RNA PCR (Viral Load & Genotyping)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Confirm active ongoing viral replication prior to Direct Acting Antivirals (DAAs)"},
            {"test_name": "Transient Elastography (FibroScan) / APRI Score", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Stage hepatic fibrosis and rule out established cirrhosis"}
        ]
    },
    "Hepatitis D": {
        "id": "ICD10-B17.0",
        "topic": "Hepatitis D (Delta Agent Superinfection)",
        "icd10": "B17.0",
        "specialty": "Gastroenterology / Hepatology",
        "emergency": False,
        "workup": [
            {"test_name": "Anti-HDV Total & IgM Antibodies with HBsAg", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Detect co-infection or superinfection in HBsAg-positive individuals"},
            {"test_name": "HDV RNA Quantitative Real-Time RT-PCR", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Quantify Delta virus viremia and disease activity"},
            {"test_name": "Coagulation Profile (PT/INR) & Serial Transaminases", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Monitor for fulminant hepatic failure"}
        ]
    },
    "Hepatitis E": {
        "id": "ICD10-B17.2",
        "topic": "Acute Enterically-Transmitted Hepatitis E",
        "icd10": "B17.2",
        "specialty": "Gastroenterology / Hepatology / Infectious Diseases",
        "emergency": False,
        "workup": [
            {"test_name": "Anti-HEV IgM Serology (ELISA)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Confirm acute waterborne Hepatitis E viral infection"},
            {"test_name": "Comprehensive Liver Function Tests (Total Bilirubin, AST, ALT, ALP)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess depth of cholestatic jaundice and hepatic inflammation"},
            {"test_name": "Obstetric & Fetal Well-being Ultrasound (if pregnant patient)", "investigation_type": "Imaging", "urgency": "Stat", "clinical_purpose": "HEV carries up to 25% maternal mortality in pregnancy; requires stat monitoring"}
        ]
    },
    "Hypertension ": {
        "id": "ICD10-I10",
        "topic": "Essential (Primary) Hypertension & Cardiovascular Risk",
        "icd10": "I10",
        "specialty": "Cardiology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Standardized Protocol Blood Pressure Measurement (both arms)", "investigation_type": "Point-of-Care Bedside", "urgency": "Priority", "clinical_purpose": "Stage hypertension per AHA/ESC guidelines (Stage 1 vs Stage 2 vs Crisis)"},
            {"test_name": "12-Lead Electrocardiogram (ECG)", "investigation_type": "Point-of-Care Bedside", "urgency": "Routine", "clinical_purpose": "Screen for left ventricular hypertrophy (Sokolow-Lyon voltage)"},
            {"test_name": "Serum Creatinine, eGFR, Fasting Lipid Panel & Urine Microalbumin", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Detect target organ damage and overall 10-year atherosclerotic risk"}
        ]
    },
    "Hyperthyroidism": {
        "id": "ICD10-E05",
        "topic": "Hyperthyroidism & Thyrotoxicosis",
        "icd10": "E05.9",
        "specialty": "Endocrinology",
        "emergency": False,
        "workup": [
            {"test_name": "Complete Thyroid Panel (Serum TSH, Free T3, Free T4)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Confirm thyrotoxicosis (suppressed TSH <0.01 with elevated FT3/FT4)"},
            {"test_name": "Anti-TSH Receptor Antibodies (TRAb) / Thyroid Ultrasound", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Differentiate Graves' disease from toxic multinodular goiter or thyroiditis"},
            {"test_name": "12-Lead ECG for Tachyarrhythmias", "investigation_type": "Point-of-Care Bedside", "urgency": "Priority", "clinical_purpose": "Detect sinus tachycardia or atrial fibrillation"}
        ]
    },
    "Hypoglycemia": {
        "id": "ICD10-E16.2",
        "topic": "Acute Hypoglycemia & Neuroglycopenic Triage",
        "icd10": "E16.2",
        "specialty": "Endocrinology / Emergency Medicine",
        "emergency": True,
        "workup": [
            {"test_name": "Stat Point-of-Care Capillary Blood Glucose (Fingerstick)", "investigation_type": "Point-of-Care Bedside", "urgency": "Stat", "clinical_purpose": "Immediate bedside confirmation of blood sugar < 70 mg/dL (< 3.9 mmol/L)"},
            {"test_name": "Laboratory Venous Plasma Glucose & Serum Electrolytes", "investigation_type": "Laboratory", "urgency": "Stat", "clinical_purpose": "Confirmatory venous quantification and rule out electrolyte imbalance"},
            {"test_name": "Plasma Insulin, C-Peptide, & Sulfonylurea Screen (if non-diabetic)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Evaluate for insulinoma, factitious hypoglycemia, or oral hypoglycemic overdose"}
        ]
    },
    "Hypothyroidism": {
        "id": "ICD10-E03",
        "topic": "Hypothyroidism & Myxedema Screening",
        "icd10": "E03.9",
        "specialty": "Endocrinology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Thyroid Stimulating Hormone (Serum TSH) & Free T4", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Confirm primary hypothyroidism (elevated TSH with low FT4)"},
            {"test_name": "Anti-Thyroid Peroxidase (Anti-TPO) Antibodies", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Confirm Hashimoto's autoimmune thyroiditis etiology"},
            {"test_name": "Fasting Lipid Profile & Complete Blood Count", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Screen for secondary dyslipidemia and normocytic/macrocytic anemia"}
        ]
    },
    "Impetigo": {
        "id": "ICD10-L01.0",
        "topic": "Impetigo Contagiosa (Non-bullous / Bullous)",
        "icd10": "L01.0",
        "specialty": "Dermatology / Pediatrics",
        "emergency": False,
        "workup": [
            {"test_name": "Clinical Dermatological Crusting & Lesion Assessment", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Identify pathognomonic honey-colored 'stuck-on' crusts"},
            {"test_name": "Bacterial Exudate Swab Gram Stain & Culture/Sensitivity", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Identify S. aureus or S. pyogenes and test methicillin resistance (MRSA)"}
        ]
    },
    "Jaundice": {
        "id": "ICD10-R17",
        "topic": "Jaundice & Acute Hyperbilirubinemia",
        "icd10": "R17",
        "specialty": "Gastroenterology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Fractionated Serum Bilirubin (Total, Direct/Conjugated, Indirect)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Classify pre-hepatic (hemolytic), hepatocellular, or post-hepatic (obstructive)"},
            {"test_name": "Comprehensive Liver Enzyme Panel (AST, ALT, ALP, GGT, Total Protein, Albumin)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Differentiate acute viral/toxic transaminitis from cholestasis"},
            {"test_name": "Abdominal Ultrasonography (Hepatobiliary Ultrasound)", "investigation_type": "Imaging", "urgency": "Priority", "clinical_purpose": "Evaluate common bile duct diameter, gallstones, and liver echogenicity"}
        ]
    },
    "Malaria": {
        "id": "ICD10-B54",
        "topic": "Malaria (Plasmodium Vivax / Falciparum / Mixed)",
        "icd10": "B54",
        "specialty": "Infectious Diseases / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Peripheral Blood Smear for Malaria Parasite (Thick & Thin Giemsa Stain)", "investigation_type": "Laboratory", "urgency": "Stat", "clinical_purpose": "Gold standard parasitemia identification and species differentiation (Pv vs Pf)"},
            {"test_name": "Rapid Diagnostic Test (Malaria RDT for Pf-HRP2 & Pan-pLDH)", "investigation_type": "Point-of-Care Bedside", "urgency": "Stat", "clinical_purpose": "Rapid point-of-care antigen detection within 15 minutes"},
            {"test_name": "Complete Blood Count with Platelet Count & Hemoglobin", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess severity of malarial hemolytic anemia and thrombocytopenia"}
        ]
    },
    "Migraine": {
        "id": "ICD10-G43",
        "topic": "Migraine Headache without / with Aura",
        "icd10": "G43.909",
        "specialty": "Neurology",
        "emergency": False,
        "workup": [
            {"test_name": "Detailed Neurological Cranial Nerve & Funduscopic Examination", "investigation_type": "Specialized Clinical", "urgency": "Priority", "clinical_purpose": "Rule out papilledema, focal neurological deficits, and secondary etiologies"},
            {"test_name": "Headache SNOOP4 Checklist & Migraine Severity Score (MIDAS)", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Classify episodic vs chronic migraine and assess functional disability"}
        ]
    },
    "Osteoarthristis": {
        "id": "ICD10-M19",
        "topic": "Osteoarthritis & Degenerative Joint Disease",
        "icd10": "M19.90",
        "specialty": "Orthopedics / Rheumatology",
        "emergency": False,
        "workup": [
            {"test_name": "Weight-Bearing Plain Radiography (X-Ray) of Affected Joints", "investigation_type": "Imaging", "urgency": "Routine", "clinical_purpose": "Kellgren-Lawrence grading (joint space narrowing, subchondral sclerosis, osteophytes)"},
            {"test_name": "Inflammatory Markers (ESR & CRP - typically normal in OA)", "investigation_type": "Laboratory", "urgency": "Routine", "clinical_purpose": "Rule out inflammatory autoimmune or infectious arthropathy"}
        ]
    },
    "Paralysis (brain hemorrhage)": {
        "id": "ICD10-I61",
        "topic": "Intracerebral Hemorrhage (ICH) / Acute Hemorrhagic Stroke",
        "icd10": "I61.9",
        "specialty": "Neurology / Neurosurgery / Emergency Medicine",
        "emergency": True,
        "workup": [
            {"test_name": "Stat Non-Contrast Computed Tomography of Brain (NCCT Head <20 mins)", "investigation_type": "Imaging", "urgency": "Stat", "clinical_purpose": "Distinguish hyperdense acute intracerebral hemorrhage from ischemic infarction"},
            {"test_name": "NIH Stroke Scale (NIHSS) & Continuous Neurological GCS Scoring", "investigation_type": "Point-of-Care Bedside", "urgency": "Stat", "clinical_purpose": "Quantify neurological deficit severity and track herniation risk"},
            {"test_name": "Coagulation Profile (PT/INR, aPTT, Platelets) & Type and Crossmatch", "investigation_type": "Laboratory", "urgency": "Stat", "clinical_purpose": "Guide urgent coagulopathy reversal (e.g. 4-factor PCC for warfarin/DOACs)"}
        ]
    },
    "Peptic ulcer diseae": {
        "id": "ICD10-K25",
        "topic": "Peptic Ulcer Disease (Gastric / Duodenal Ulcer)",
        "icd10": "K25.9",
        "specialty": "Gastroenterology",
        "emergency": False,
        "workup": [
            {"test_name": "Diagnostic Upper GI Endoscopy (EGD)", "investigation_type": "Specialized Clinical", "urgency": "Priority", "clinical_purpose": "Direct mucosal visualization, Forrest classification of bleeding, biopsy for malignancy"},
            {"test_name": "Helicobacter pylori Testing (Stool Antigen or 14C Urea Breath Test)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Identify active H. pylori infection requiring eradication therapy"},
            {"test_name": "Complete Blood Count (CBC) with Serum Ferritin", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Detect occult gastrointestinal blood loss and microcytic anemia"}
        ]
    },
    "Pneumonia": {
        "id": "ICD10-J18",
        "topic": "Community-Acquired Pneumonia (CAP)",
        "icd10": "J18.9",
        "specialty": "Pulmonology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Chest Radiograph (CXR PA & Lateral View)", "investigation_type": "Imaging", "urgency": "Priority", "clinical_purpose": "Demonstrate lobar or bronchopneumonic consolidation, cavitation, or pleural effusion"},
            {"test_name": "Complete Blood Count with Differential & Serum Procalcitonin/CRP", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Quantify bacterial leukocytosis and systemic inflammatory kinetics"},
            {"test_name": "Pulse Oximetry (Continuous SpO2) & CURB-65 Risk Stratification", "investigation_type": "Point-of-Care Bedside", "urgency": "Priority", "clinical_purpose": "Determine OPD vs ward vs ICU admission requirement"}
        ]
    },
    "Psoriasis": {
        "id": "ICD10-L40.0",
        "topic": "Psoriasis Vulgaris (Chronic Plaque Psoriasis)",
        "icd10": "L40.0",
        "specialty": "Dermatology",
        "emergency": False,
        "workup": [
            {"test_name": "Clinical Psoriasis Area and Severity Index (PASI) & Body Surface Area (BSA)", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Quantify plaque erythema, induration, scaling, and anatomic extent"},
            {"test_name": "Screening for Psoriatic Arthritis (PEST Questionnaire & Joint Exam)", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Detect enthesitis, dactylitis, and inflammatory axial/peripheral joint disease"}
        ]
    },
    "Tuberculosis": {
        "id": "ICD10-A15.0",
        "topic": "Pulmonary Tuberculosis (PTB / Koch's Disease)",
        "icd10": "A15.0",
        "specialty": "Pulmonology / Infectious Diseases",
        "emergency": False,
        "workup": [
            {"test_name": "Sputum GeneXpert MTB/RIF (CBNAAT - Molecular Assay)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Rapidly detect M. tuberculosis DNA and rifampicin resistance mutations"},
            {"test_name": "Sputum Smear Microscopy for Acid-Fast Bacilli (AFB - 2 samples)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Quantify mycobacterial load and assess infectiousness"},
            {"test_name": "Chest Radiograph (CXR PA View)", "investigation_type": "Imaging", "urgency": "Priority", "clinical_purpose": "Identify upper lobe apical/posterior infiltrates, cavitation, or fibrosis"}
        ]
    },
    "Typhoid": {
        "id": "ICD10-A01.0",
        "topic": "Enteric (Typhoid) Fever (Salmonella Typhi)",
        "icd10": "A01.0",
        "specialty": "Infectious Diseases / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Automated Blood Culture (BACTEC - 10-15 mL whole blood)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Diagnostic gold standard during 1st week of illness with antibiotic sensitivity"},
            {"test_name": "Typhidot Rapid IgM/IgG Serology & Complete Blood Count", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Detect acute outer membrane protein antibodies; CBC reveals relative leukopenia"},
            {"test_name": "Abdominal Ultrasonography (Hepatobiliary/Splenic)", "investigation_type": "Imaging", "urgency": "Routine", "clinical_purpose": "Evaluate splenomegaly and mesenteric lymphadenopathy"}
        ]
    },
    "Urinary tract infection": {
        "id": "ICD10-N39",
        "topic": "Acute Cystitis & Urinary Tract Infection (UTI)",
        "icd10": "N39.0",
        "specialty": "Urology / Internal Medicine",
        "emergency": False,
        "workup": [
            {"test_name": "Urine Routine & Microscopic Examination (Urine R/M)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Demonstrate pyuria (>5 WBCs/hpf), bacteriuria, and leukocyte esterase/nitrites"},
            {"test_name": "Clean Catch Midstream Urine Culture & Sensitivity (Urine C/S)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Isolate uropathogen (E. coli, Klebsiella) and guide targeted antimicrobial therapy"}
        ]
    },
    "Varicose veins": {
        "id": "ICD10-I83.9",
        "topic": "Varicose Veins of Lower Extremities & Venous Reflux",
        "icd10": "I83.9",
        "specialty": "Vascular Surgery / General Surgery",
        "emergency": False,
        "workup": [
            {"test_name": "Venous Duplex Ultrasound (Doppler) of Lower Extremities (Standing)", "investigation_type": "Imaging", "urgency": "Routine", "clinical_purpose": "Map saphenofemoral/saphenopopliteal junction reflux and perforator incompetence"},
            {"test_name": "Clinical CEAP Classification (C0-C6) & Ankle-Brachial Index (ABI)", "investigation_type": "Specialized Clinical", "urgency": "Routine", "clinical_purpose": "Grade disease severity and rule out coexisting arterial occlusive disease"}
        ]
    },
    "hepatitis A": {
        "id": "ICD10-B15",
        "topic": "Acute Viral Hepatitis A",
        "icd10": "B15.9",
        "specialty": "Gastroenterology / Hepatology / Infectious Diseases",
        "emergency": False,
        "workup": [
            {"test_name": "Anti-Hepatitis A Virus IgM Antibody (Anti-HAV IgM ELISA)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Definitive serological marker of acute viral hepatitis A infection"},
            {"test_name": "Complete Liver Function Panel (Total Bilirubin, AST, ALT, Alkaline Phosphatase)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Assess severity of acute hepatocellular injury (ALT/AST typically > 1000 IU/L)"},
            {"test_name": "Prothrombin Time / INR (PT/INR)", "investigation_type": "Laboratory", "urgency": "Priority", "clinical_purpose": "Screen for acute hepatic synthetic impairment and early acute liver failure"}
        ]
    }
}


def build_model():
    print("Building Bayesian Diagnostic Model from Kaggle CSVs...")
    
    # 1. Read Training.csv
    training_path = os.path.join(KAGGLE_DIR, "Training.csv")
    with open(training_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = [h.strip() for h in next(reader)]
        symptoms = headers[:-1]
        
        disease_counts = defaultdict(int)
        symptom_given_disease = defaultdict(lambda: defaultdict(int))
        total_samples = 0
        
        for row in reader:
            if not row:
                continue
            disease = row[-1].strip()
            disease_counts[disease] += 1
            total_samples += 1
            for i, val in enumerate(row[:-1]):
                if val.strip() == "1":
                    symptom_given_disease[disease][symptoms[i]] += 1

    diseases = sorted(list(disease_counts.keys()))
    print(f"Total training cases: {total_samples} across {len(diseases)} conditions.")

    # 2. Read Symptom-severity.csv
    symptom_weights = {}
    sev_path = os.path.join(KAGGLE_DIR, "Symptom-severity.csv")
    if os.path.exists(sev_path):
        with open(sev_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if r and len(r) >= 2:
                    symptom_weights[r[0].strip()] = int(r[1].strip())

    # 3. Read description.csv
    descriptions = {}
    desc_path = os.path.join(KAGGLE_DIR, "description.csv")
    if os.path.exists(desc_path):
        with open(desc_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if r and len(r) >= 2:
                    descriptions[r[0].strip()] = r[1].strip()

    # 4. Read precautions_df.csv
    precautions = {}
    prec_path = os.path.join(KAGGLE_DIR, "precautions_df.csv")
    if os.path.exists(prec_path):
        with open(prec_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if r and len(r) >= 6:
                    plist = [p.strip().capitalize() for p in r[2:6] if p.strip()]
                    precautions[r[1].strip()] = plist

    # 5. Read medications.csv
    medications = {}
    med_path = os.path.join(KAGGLE_DIR, "medications.csv")
    if os.path.exists(med_path):
        with open(med_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if r and len(r) >= 2:
                    val = eval(r[1]) if r[1].startswith("[") else [r[1].strip()]
                    medications[r[0].strip()] = val

    # 6. Read diets.csv
    diets = {}
    diet_path = os.path.join(KAGGLE_DIR, "diets.csv")
    if os.path.exists(diet_path):
        with open(diet_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if r and len(r) >= 2:
                    val = eval(r[1]) if r[1].startswith("[") else [r[1].strip()]
                    diets[r[0].strip()] = val

    # Calculate exact smoothed conditional probabilities
    # Laplace smoothed: P(s=1|d) = (count + alpha) / (n_d + 2*alpha)
    alpha = 1.0
    likelihoods = {}
    priors = {}

    for d in diseases:
        n_d = disease_counts[d]
        priors[d] = round(n_d / total_samples, 6)
        likelihoods[d] = {}
        for s in symptoms:
            cnt = symptom_given_disease[d][s]
            p_s1 = (cnt + alpha) / (n_d + 2.0 * alpha)
            likelihoods[d][s] = round(p_s1, 6)

    compiled_model = {
        "metadata": {
            "version": "2.0.0",
            "model_type": "Bernoulli_Naive_Bayes_Clinical_Classifier",
            "training_samples": total_samples,
            "disease_count": len(diseases),
            "symptom_count": len(symptoms),
            "smoothing_alpha": alpha
        },
        "symptoms": symptoms,
        "diseases": diseases,
        "priors": priors,
        "likelihoods": likelihoods,
        "symptom_weights": symptom_weights,
        "descriptions": descriptions,
        "precautions": precautions,
        "medications": medications,
        "diets": diets,
        "canonical_clinical_map": CANONICAL_CLINICAL_MAP
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(compiled_model, f, indent=2)

    print(f"Model successfully written to: {OUTPUT_PATH}")
    file_size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"Compiled model size: {file_size_kb:.2f} KB")


if __name__ == "__main__":
    build_model()

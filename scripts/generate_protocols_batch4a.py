#!/usr/bin/env python3
"""
Batch 4A: Rheumatology, Infectious Diseases/Tropical Medicine, Obstetrics & Gynecology.
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
    # --- 8. RHEUMATOLOGY & AUTOIMMUNE (14) ---
    {
        "id": "ICD10-M32.9",
        "topic": "Systemic Lupus Erythematosus (EULAR/ACR & Lupus Nephritis)",
        "icd10": "M32.9",
        "specialty": "Rheumatology / Nephrology",
        "organ_system": "Multisystem Autoimmune",
        "keywords": ["systemic lupus erythematosus", "sle", "malar rash butterfly rash", "discoid rash", "anti dsdna anti smith", "lupus nephritis", "photosensitivity rash"],
        "red_flags": ["diffuse proliferative lupus nephritis (class iv)", "lupus cerebritis / psychosis / seizures", "alveolar hemorrhage"],
        "clinical_hallmarks": ["predominantly affects young women of childbearing age (female:male ratio 9:1)", "pathognomonic cutaneous signs: MALAR RASH (erythematous 'butterfly' maculopapular eruption across bridge of nose and cheeks, characteristically SPARING THE NASOLABIAL FOLDS) and marked photosensitivity", "inflammatory, non-erosive polyarthritis primarily affecting hands and wrists (Jaccoud arthropathy with reversible joint deformities)", "serositis: pleurisy and pericarditis with friction rub", "Lupus Nephritis: persistent proteinuria (> 0.5 g/day) and active urinary sediment (RBC casts)", "laboratory hallmarks: ANA positive in > 98% (entry criterion); High specificity markers: Anti-dsDNA (correlates with disease activity and nephritis) and Anti-Smith (Sm) antibodies; Depressed serum complement levels (low C3 and C4 during active flare)"],
        "pertinent_negatives": ["malar rash strictly spares the nasolabial folds (distinguishes from seborrheic dermatitis or rosacea)"],
        "content": "Prototypic chronic multisystem autoimmune disease characterized by immune complex deposition, autoantibody production against nuclear antigens, and complement activation (EULAR/ACR 2019 criteria: ANA >= 1:80 plus >= 10 points). Protocol: 1. Hydroxychloroquine (HCQ: <= 5 mg/kg/day) is RECOMMENDED FOR ALL LUPUS PATIENTS (improves survival and prevents flares); 2. Systemic Corticosteroids for acute flares; 3. Lupus Nephritis: Renal biopsy mandatory for ISN/RPS classification; Induction: IV Methylprednisolone pulses + Mycophenolate Mofetil (MMF) or IV Cyclophosphamide; Belimumab or Voclosporin for refractory active nephritis."
    },
    {
        "id": "ICD10-M34.0",
        "topic": "Systemic Sclerosis (Scleroderma - Diffuse vs Limited CREST)",
        "icd10": "M34.0",
        "specialty": "Rheumatology / Pulmonology",
        "organ_system": "Multisystem Fibrosing Autoimmune",
        "keywords": ["scleroderma", "systemic sclerosis", "crest syndrome", "sclerodactyly", "salt and pepper skin", "scleroderma renal crisis", "anti scl 70 anti centromere"],
        "red_flags": ["scleroderma renal crisis (malignant hypertension, microangiopathic anemia)", "pulmonary arterial hypertension", "severe interstitial lung disease"],
        "clinical_hallmarks": ["Limited Cutaneous Scleroderma (CREST syndrome): 1. Calcinosis cutis (painful calcium deposits in finger pads); 2. Raynaud's phenomenon; 3. Esophageal dysmotility (reflux and dysphagia); 4. Sclerodactyly (tight, shiny, thickened skin of fingers distal to MCPs, loss of normal skin folds, flexion contractures); 5. Telangiectasias (mat-like red spots on face, lips, hands)", "Diffuse Cutaneous Scleroderma: rapid skin thickening extending PROXIMAL TO ELBOWS/KNEES and involving trunk, with early severe visceral fibrosis (ILD, renal crisis)", "facial changes: 'bird-like facies', pinched beaked nose, radial perioral furrows, and microstomia (restricted mouth opening)", "pathognomonic serology: Limited SSc: Anti-Centromere Antibodies (ACA in 70-80%); Diffuse SSc: Anti-Scl-70 (Anti-Topoisomerase I in 40%) and Anti-RNA Polymerase III (associated with high risk of Scleroderma Renal Crisis)"],
        "pertinent_negatives": ["ACE INHIBITORS (Captopril) are life-saving in Scleroderma Renal Crisis; HIGH-DOSE STEROIDS (> 15 mg/day) are strictly contraindicated because they precipitate renal crisis"],
        "content": "Systemic connective tissue disease characterized by immune dysregulation, microvascular obliterative vasculopathy, and progressive tissue fibrosis of skin and internal organs. Diagnostic workup: Nailfold capillaroscopy, ANA, Anti-Scl-70, Anti-Centromere, HRCT thorax, Echocardiogram with Doppler estimated PAP, PFTs. Treatment: Organ-specific: Raynaud: CCBs (Nifedipine); Scleroderma Renal Crisis: STAT immediate ACE inhibitor (Captopril); ILD: Mycophenolate Mofetil or Cyclophosphamide or Nintedanib; PAH: Endothelin receptor antagonists (Bosentan) + PDE-5 inhibitors (Sildenafil)."
    },
    {
        "id": "ICD10-M45.9",
        "topic": "Ankylosing Spondylitis (Axial Spondyloarthritis & Bamboo Spine)",
        "icd10": "M45.9",
        "specialty": "Rheumatology / Orthopedics",
        "organ_system": "Musculoskeletal Spondyloarthropathy",
        "keywords": ["ankylosing spondylitis", "axial spondyloarthritis", "bamboo spine", "hla b27", "sacroiliitis on mri", "inflammatory back pain", "morning stiffness back", "schober test"],
        "red_flags": ["acute anterior uveitis / iritis (painful red photophobic eye)", "aortic regurgitation and complete heart block", "cervical spine fracture from minor trauma"],
        "clinical_hallmarks": ["prototypic INFLAMMATORY BACK PAIN (Calin/ASAS criteria): insidious onset in young adults (< 40-45 years, male predominance), duration > 3 months, SEVERE MORNING STIFFNESS (> 30-60 minutes), pain that IMPROVES WITH EXERCISE/ACTIVITY and DOES NOT IMPROVE WITH REST, and nocturnal awakening during second half of night with buttock ache", "physical examination: limited spinal mobility in all planes; POSITIVE MODIFIED SCHOBER TEST (< 5 cm increase in lumbar flexion); decreased chest expansion (< 2.5 cm measured at 4th intercostal space)", "enthesitis: pain and tenderness at insertions of tendons into bone, characteristically Achilles tendinitis and plantar fasciitis", "radiographic hallmarks: bilateral symmetric sacroiliitis on pelvic X-ray or MRI (bone marrow edema on STIR sequences); late spine X-ray shows syndesmophytes with fusion producing classic 'BAMBOO SPINE'", "genetic hallmark: HLA-B27 positive in > 90-95% of patients"],
        "pertinent_negatives": ["absence of rheumatoid factor and anti-CCP (seronegative spondyloarthropathy)"],
        "content": "Chronic, systemic inflammatory disease of the axial skeleton, belonging to the seronegative spondyloarthropathy group. Assessment of SpondyloArthritis international Society (ASAS) classification. Treatment: 1. First-line therapy: Continuous non-steroidal anti-inflammatory drugs (NSAIDs: Celecoxib, Naproxen) at full anti-inflammatory doses + regular daily spinal physiotherapy; 2. Biologic Disease-Modifying Drugs (bDMARDs) for NSAID-refractory axial disease: TNF-alpha inhibitors (Infliximab, Adalimumab, Etanercept) or IL-17 inhibitors (Secukinumab) dramatically halt radiographic and clinical progression; Conventional synthetic DMARDs (Sulfasalazine) are effective ONLY for peripheral joint involvement, not axial disease."
    },
    {
        "id": "ICD10-L40.50",
        "topic": "Psoriatic Arthritis (CASPAR Criteria & Dactylitis)",
        "icd10": "L40.50",
        "specialty": "Rheumatology / Dermatology",
        "organ_system": "Musculoskeletal Spondyloarthropathy",
        "keywords": ["psoriatic arthritis", "psa", "dactylitis sausage digit", "pencil in cup deformity", "caspar criteria", "nail pitting psoriasis", "distal interphalangeal joint arthritis"],
        "red_flags": ["arthritis mutilans (telescoping fingers / opera-glass hand)", "rapid joint destruction"],
        "clinical_hallmarks": ["develops in up to 30% of patients with cutaneous psoriasis (cutaneous lesions precede joint disease by years in 70%, but can be concurrent or rarely postdate arthritis)", "cardinal clinical features: 1. DACTYLITIS ('sausage digit' - diffuse, uniform, painful erythematous swelling of an entire finger or toe from tenosynovitis); 2. Distinctive involvement of the DISTAL INTERPHALANGEAL (DIP) JOINTS; 3. Psoriatic nail dystrophy (nail pitting, onycholysis, subungual hyperkeratosis, and 'oil-drop' spots); 4. Enthesitis (Achilles tendon, plantar fascia)", "five clinical patterns (Moll and Wright): asymmetric oligoarthritis (most common 70%), symmetric polyarthritis (mimicking RA), DIP joint predominant, spondylitis, and Arthritis Mutilans (telescoping digits)", "plain X-ray (pathognomonic): 'PENCIL-IN-CUP' DEFORMITY (narrowing of the proximal articular bone entering the expanded cup-like base of the distal phalanx)"],
        "pertinent_negatives": ["seronegative: Rheumatoid Factor (RF) and Anti-CCP are negative"],
        "content": "Chronic inflammatory musculoskeletal disease associated with cutaneous psoriasis, classified using the CASPAR (ClASsification criteria for Psoriatic ARthritis: established inflammatory articular disease + >= 3 points from personal/family psoriasis, nail dystrophy, negative RF, dactylitis, and juxta-articular new bone formation). Treatment: Mild: NSAIDs; Peripheral arthritis: Conventional synthetic DMARDs (Methotrexate, Leflunomide); Moderate-severe, axial, or dactylitic disease: Biologic DMARDs (TNF inhibitors [Adalimumab], IL-17 inhibitors [Secukinumab, Ixekizumab], IL-23 inhibitors [Ustekinumab, Guselkumab]) or targeted synthetic JAK inhibitors (Tofacitinib)."
    },
    {
        "id": "ICD10-M02.9",
        "topic": "Reactive Arthritis (Reiter Syndrome Triad & Post-Infectious)",
        "icd10": "M02.9",
        "specialty": "Rheumatology / Infectious Disease / Urology",
        "organ_system": "Spondyloarthropathy Post-Infectious",
        "keywords": ["reactive arthritis", "reiter syndrome", "cant see cant pee cant climb a tree", "chlamydia reactive arthritis", "keratoderma blennorrhagica", "balanitis circinata", "asymmetric oligoarthritis"],
        "red_flags": ["severe carditis (aortic regurgitation, conduction blocks)", "destructive chronic arthropathy"],
        "clinical_hallmarks": ["classic clinical triad (the mnemonic 'CAN'T SEE, CAN'T PEE, CAN'T CLIMB A TREE'): 1. Conjunctivitis / anterior uveitis; 2. Urethritis or cervicitis; 3. Asymmetric, additive oligoarthritis primarily affecting large weight-bearing joints of lower limbs (knees and ankles)", "develops 1-4 weeks following a primary mucosal infection: either genitourinary (Chlamydia trachomatis, Ureaplasma) or gastrointestinal dysentery (Campylobacter jejuni, Salmonella, Shigella, Yersinia)", "pathognomonic mucocutaneous lesions: Keratoderma Blennorrhagica (hyperkeratotic, pustular, crusting, vesicular plaques on soles of feet and palms) and Circinate Balanitis (painless shallow serpiginous erosions on the glans penis)", "dactylitis ('sausage toes') and intense calcaneal heel pain (enthesitis)", "strongly linked to HLA-B27 (> 65-80%)"],
        "pertinent_negatives": ["synovial fluid is STERILE (sterile reactive inflammation, NOT septic arthritis)"],
        "content": "Sterile autoimmune inflammatory arthropathy developing secondary to an infectious trigger at a distant mucosal site in genetically predisposed individuals. Diagnostic workup: Joint arthrocentesis (rules out septic arthritis or crystals), First-void urine NAAT for Chlamydia trachomatis, stool cultures. Treatment: Acute phase: High-dose NSAIDs (Indomethacin 50-75 mg TID) is first-line; Intra-articular corticosteroid injections for monoarthritis; Antibiotic therapy is indicated ONLY to treat active persistent Chlamydia urethral infection (Doxycycline 100 mg BID for 10-14 days - treat partner!), antibiotics do NOT alter arthritis course once established; Sulfasalazine or Methotrexate for chronic persistent arthritis (> 3-6 months)."
    },
    {
        "id": "ICD10-M35.00",
        "topic": "Sjögren's Syndrome (Sicca Syndrome & Ro/SSA - La/SSB)",
        "icd10": "M35.00",
        "specialty": "Rheumatology / Ophthalmology / Oral Medicine",
        "organ_system": "Exocrine Gland Autoimmune",
        "keywords": ["sjogren syndrome", "sicca syndrome", "dry eyes dry mouth", "keratoconjunctivitis sicca", "xerostomia", "anti ro ssa anti la ssb", "schirmer test", "salivary gland biopsy"],
        "red_flags": ["non-hodgkin b-cell lymphoma (malt lymphoma - 44-fold increased risk)", "cryoglobulinemic vasculitis", "interstitial lung disease / renal tubular acidosis"],
        "clinical_hallmarks": ["cardinal 'Sicca complex': 1. Keratoconjunctivitis Sicca (severe dry eyes: persistent sandy, gritty, burning foreign-body sensation in eyes, photophobia, and inability to wear contact lenses); 2. Xerostomia (severe dry mouth: difficulty speaking or swallowing dry food without sipping water, rampant dental caries, and burning tongue)", "bilateral, non-tender or tender, recurrent parotid or major salivary gland enlargement ('chipmunk cheeks')", "extraglandular features: profound fatigue, non-erosive polyarthralgias, Raynaud phenomenon, and dry skin (xeroderma)", "diagnostic ocular test: POSITIVE SCHIRMER'S TEST (<= 5 mm wetting of filter paper strip placed in lower conjunctival sac after 5 minutes) and ocular surface Lissamine green staining", "serological hallmarks: Anti-Ro/SSA (positive in 70-80%) and Anti-La/SSB (positive in 40-50%); Minor Salivary Gland Biopsy (lip biopsy) reveals focal lymphocytic sialadenitis with Focus Score >= 1 (>= 50 mononuclear cells per 4 mm2)"],
        "pertinent_negatives": ["absence of medication-induced anticholinergic dryness (antihistamines, tricyclics)"],
        "content": "Chronic, slowly progressive autoimmune disorder characterized by lymphocytic infiltration of exocrine glands, predominantly the lacrimal and salivary glands, leading to glandular destruction and mucosal dryness. Diagnostic criteria: 2016 ACR/EULAR criteria (score >= 4). Treatment: Symptomatic sicca relief: Preservative-free artificial tears and ocular cyclosporine drops; Muscarinic agonists (Pilocarpine 5 mg TID/QID or Cevimeline) stimulate residual salivary secretion; Rigorous dental hygiene; Systemic extraglandular manifestations: Hydroxychloroquine (HCQ) for arthralgias; Systemic steroids and Rituximab (anti-CD20) for severe vasculitis or organ-threatening disease; Surveillance for B-cell MALT lymphoma."
    },
    {
        "id": "ICD10-M33.20",
        "topic": "Polymyositis & Dermatomyositis (Gottron Papules & Heliotrope Rash)",
        "icd10": "M33.20",
        "specialty": "Rheumatology / Dermatology / Neurology",
        "organ_system": "Inflammatory Muscle & Cutaneous",
        "keywords": ["dermatomyositis", "polymyositis", "gottron papules", "heliotrope rash", "shawl sign", "proximal muscle weakness", "anti jo-1 antisynthetase", "elevated creatine kinase"],
        "red_flags": ["occult underlying malignancy (ovarian, breast, lung, gastric - up to 30% paraneoplastic)", "interstitial lung disease (rapidly progressive ards)", "dysphagia with aspiration"],
        "clinical_hallmarks": ["cardinal motor presentation: PROGRESSIVE, SYMMETRIC, PAINLESS PROXIMAL MUSCLE WEAKNESS involving shoulder girdle (difficulty lifting arms to comb hair or reach high shelves) and pelvic girdle (difficulty rising from low chairs, climbing stairs, or getting out of bath)", "pathognomonic cutaneous signs in Dermatomyositis: 1. HELIOTROPE RASH (violaceous/purplish erythema of the upper eyelids, often accompanied by periorbital edema); 2. GOTTRON'S PAPULES (violaceous, flat-topped papules and plaques over the dorsal interphalangeal and MCP joints of hands); 3. Gottron sign (erythema over elbows and knees); 4. Shawl sign (erythema over upper back and shoulders) and V-sign (anterior chest)", "Mechanic's hands: hyperkeratotic, cracked, scaling skin along lateral aspect of digits (Antisynthetase syndrome: Anti-Jo-1)", "laboratory hallmarks: MASSIVELY ELEVATED SERUM CREATINE KINASE (CK - often 10-50x normal), elevated aldolase, LDH, and AST/ALT; Muscle biopsy shows CD4+ perivascular/perimysial inflammation in DM, CD8+ endomysial infiltration in PM"],
        "pertinent_negatives": ["normal sensory examination and preserved deep tendon reflexes"],
        "content": "Idiopathic inflammatory myopathies characterized by immune-mediated striated muscle injury. Crucial oncological association: Adults with Dermatomyositis have a 3- to 6-fold increased risk of underlying internal malignancy (MANDATORY age-appropriate cancer screening). Diagnostic workup: Serum CK, myositis-specific autoantibodies (Anti-Jo-1, Anti-Mi-2, Anti-TIF1-gamma), Electromyography (EMG), Muscle MRI (STIR shows muscle edema), and Muscle Biopsy. Treatment: First-line: High-dose oral Corticosteroids (Prednisone 1 mg/kg/day); Steroid-sparing immunosuppressants (Methotrexate or Azathioprine); IVIG for refractory weakness or severe dysphagia."
    },
    {
        "id": "ICD10-M31.30",
        "topic": "Granulomatosis with Polyangiitis (Wegener's - PR3-ANCA & Saddle Nose)",
        "icd10": "M31.30",
        "specialty": "Rheumatology / Pulmonology / Nephrology / ENT",
        "organ_system": "Systemic Necrotizing Vasculitis",
        "keywords": ["granulomatosis with polyangiitis", "gpa", "wegeners granulomatosis", "c-anca pr3", "saddle nose deformity", "cavitary lung lesions", "crescentic glomerulonephritis", "bloody rhinorrhea crusted nose"],
        "red_flags": ["diffuse alveolar hemorrhage (massive hemoptysis)", "rapidly progressive crescentic glomerulonephritis", "subglottic tracheal stenosis / airway obstruction"],
        "clinical_hallmarks": ["classic clinical triad of GPA: 1. Upper respiratory tract involvement; 2. Lower respiratory tract involvement; 3. Glomerulonephritis", "ENT hallmark: chronic, refractory sinusitis, recurrent bloody nasal discharge, severe nasal crusting, nasal septal perforation, and pathognomonic 'SADDLE-NOSE DEFORMITY' (collapse of nasal bridge from chondritis)", "Pulmonary hallmark: cough, hemoptysis, and chest imaging showing MULTIPLE BILATERAL CAVITARY NODULES and lung infiltrates", "Renal hallmark: Rapidly Progressive Glomerulonephritis (RPGN) with red blood cell casts and rising creatinine", "pathognomonic serological hallmark: Cytoplasmic ANCA (c-ANCA) targeting Proteinase-3 (PR3-ANCA) positive in > 85-95% of active disease"],
        "pertinent_negatives": ["absence of asthma or marked eosinophilia (distinguishes from EGPA / Churg-Strauss)"],
        "content": "Necrotizing granulomatous small- and medium-vessel vasculitis primarily targeting the respiratory tract and kidneys. Diagnostic gold standard: Biopsy of affected tissue (nasal mucosa, lung, or kidney showing necrotizing granulomas and pauci-immune glomerulonephritis) + PR3-ANCA positivity. Remission Induction Protocol (Organ/Life-Threatening): 1. Pulse IV Methylprednisolone (1 g daily for 3 days) + oral glucocorticoids; 2. Rituximab (anti-CD20: 375 mg/m2 weekly x 4 doses) OR IV Cyclophosphamide; 3. Avacopan (oral complement C5a receptor antagonist) as steroid-reducing therapy; 4. Maintenance: Rituximab or Azathioprine + Methotrexate."
    },
    {
        "id": "ICD10-M35.2",
        "topic": "Behçet's Disease (Recurrent Aphthous Ulcers & Pathergy Test)",
        "icd10": "M35.2",
        "specialty": "Rheumatology / Ophthalmology / Dermatology",
        "organ_system": "Systemic Variable Vessel Vasculitis",
        "keywords": ["behcet disease", "recurrent aphthous oral ulcers", "genital ulcers", "hypopyon uveitis", "pathergy test positive", "hla b51", "pulmonary artery aneurysm behcet"],
        "red_flags": ["rupture of pulmonary artery aneurysm (massive fatal hemoptysis)", "panuveitis leading to irreversible blindness", "neuro-behcet (brainstem encephalitis)"],
        "clinical_hallmarks": ["MANDATORY ENTRY CRITERION (International Study Group criteria): RECURRENT ORAL APHTHOUS ULCERATION (at least 3 episodes in a 12-month period: painful, round, sharply defined shallow ulcers with yellowish-gray necrotic base and erythematous halo on buccal mucosa, tongue, or lips)", "PLUS >= 2 of the following cardinal features: 1. Recurrent painful GENITAL ULCERS (scrotal or vulvar punched-out ulcers that heal with scarring); 2. Ocular inflammation (anterior uveitis with pathognomonic shifting HYPOPYON [sterile pus layering in anterior chamber], posterior uveitis, retinal vasculitis); 3. Cutaneous lesions (erythema nodosum-like nodules, pseudofolliculitis, acneiform lesions); 4. POSITIVE PATHERGY TEST (formation of an erythematous sterile papule or pustule >= 2 mm at site of 20-gauge sterile needle prick within 24-48 hours)", "strongly associated with HLA-B51 along the ancient Silk Road route"],
        "pertinent_negatives": ["negative ANA and negative ANCA (variable vessel vasculitis)"],
        "content": "Chronic, relapsing, systemic inflammatory disorder affecting blood vessels of all sizes (arteries and veins) with endothelial activation and neutrophil hyperreactivity. Treatment: Mucocutaneous disease: Topical steroids + oral Colchicine (0.5-1.5 mg daily) or Apremilast; Ocular / Visceral / Neurological disease: High-dose systemic Corticosteroids + Azathioprine; Anti-TNF agents (Infliximab, Adalimumab) are exceptionally effective for severe posterior uveitis and refractory vascular aneurysms. Anticoagulants are controversial in deep vein thrombosis due to high risk of bleeding from coexisting pulmonary aneurysms."
    },
    {
        "id": "ICD10-M30.0",
        "topic": "Polyarteritis Nodosa (PAN - HBV Association & Mononeuritis Multiplex)",
        "icd10": "M30.0",
        "specialty": "Rheumatology / Nephrology / Neurology",
        "organ_system": "Medium Vessel Necrotizing Vasculitis",
        "keywords": ["polyarteritis nodosa", "pan", "mononeuritis multiplex foot drop", "rosary beads microaneurysms", "hepatitis b vasculitis", "livedo reticularis", "testicular pain pan"],
        "red_flags": ["visceral infarction (bowel perforation, renal hematoma)", "malignant renovascular hypertension", "cardiac ischemia"],
        "clinical_hallmarks": ["systemic necrotizing vasculitis targeting medium-sized muscular arteries, with strong etiologic association with HEPATITIS B VIRUS (HBV) infection (in up to 30%)", "neurological hallmark: MONONEURITIS MULTIPLEX (asymmetric, painful, asynchronous involvement of non-contiguous peripheral nerves, characteristically presenting as acute foot drop [peroneal nerve] or wrist drop [radial nerve])", "cutaneous signs: Livedo Reticularis (purplish, mottled, reticular lace-like vascular skin discoloration), tender subcutaneous nodules along the course of arteries, and digital infarctions", "severe bilateral or unilateral TESTICULAR PAIN and tenderness in young men without infection", "renovascular hypertension (renal artery involvement causing ischemia and renin hypersecretion)", "angiography (mesenteric or renal): PATHOGNOMONIC MULTIPLE SEGMENTAL MICROANEURYSMS AND STENOSES resembling 'a string of beads' / rosary beads"],
        "pertinent_negatives": ["SPARES THE PULMONARY CIRCULATION (absence of pulmonary infiltrates distinguishes PAN from microscopic polyangiitis and GPA)", "ANCA NEGATIVE in classical PAN"],
        "content": "Systemic necrotizing medium-vessel vasculitis that spares arterioles, capillaries, and post-capillary venules, without glomerulonephritis. ACR 1990 criteria (needs >= 3 of 10 criteria). Diagnostic workup: Deep skin/muscle/sural nerve biopsy, Mesenteric/Renal Catheter Angiography (CT/conventional), Hepatitis B serologies (HBsAg, HBeAg, HBV DNA). Treatment: Idiopathic PAN: High-dose oral Prednisone (1 mg/kg/day) + Cyclophosphamide for severe organ-threatening disease (Five-Factor Score >= 1); HBV-associated PAN: Short course of corticosteroids + Plasma exchange + Antiviral therapy (Entecavir or Tenofovir) to clear viral replication."
    },
    {
        "id": "ICD10-M05.79",
        "topic": "Rheumatoid Arthritis (Anti-CCP & Extra-Articular Deformities)",
        "icd10": "M05.79",
        "specialty": "Rheumatology",
        "organ_system": "Synovial Autoimmune",
        "keywords": ["rheumatoid arthritis", "ra", "symmetric polyarthritis", "anti ccp antibodies", "morning stiffness > 1 hour", "swan neck boutonniere deformity", "methotrexate ra"],
        "red_flags": ["atlantoaxial subluxation with cervical cord compression", "rheumatoid vasculitis", "accelerated coronary artery disease"],
        "clinical_hallmarks": ["chronic, symmetric, inflammatory polyarthritis characteristically targeting the SMALL JOINTS OF HANDS AND FEET: Metacarpophalangeal (MCP), Proximal Interphalangeal (PIP), and wrist joints (STRICTLY SPARING THE DIP JOINTS)", "prolonged morning stiffness lasting GREATER THAN 60 MINUTES that improves with movement and warmth", "pathognomonic hand deformities in established disease: 1. Ulnar deviation of fingers at MCP joints; 2. Swan-neck deformity (hyperextension of PIP with flexion of DIP); 3. Boutonnière deformity (flexion of PIP with hyperextension of DIP); 4. Z-deformity of thumb", "subcutaneous firm, non-tender Rheumatoid Nodules over extensor surfaces (elbows)", "laboratory hallmarks: Anti-Citrullinated Protein Antibodies (Anti-CCP / ACPA: high specificity > 95-98%, correlates with aggressive erosive disease) and Rheumatoid Factor (RF 70-80%); Elevated ESR and CRP"],
        "pertinent_negatives": ["distal interphalangeal (DIP) joints are spared (involvement of DIP points to osteoarthritis or psoriatic arthritis)"],
        "content": "Systemic autoimmune inflammatory disease characterized by persistent synovial proliferation (pannus formation), leading to cartilage destruction and juxta-articular marginal bone erosions (2010 ACR/EULAR criteria). Treatment (Treat-to-Target Strategy): 1. FIRST-LINE ANCHOR DRUG: Oral Methotrexate (MTX: 15-25 mg once weekly + Folic acid 5 mg weekly); 2. Conventional synthetic DMARD combinations (Sulfasalazine, Leflunomide, Hydroxychloroquine); 3. Biologic DMARDs for inadequate response: TNF inhibitors (Adalimumab, Etanercept), IL-6 receptor antagonists (Tocilizumab), T-cell co-stimulation modulator (Abatacept), or JAK inhibitors (Tofacitinib, Upadacitinib)."
    },
    {
        "id": "ICD10-M35.3",
        "topic": "Polymyalgia Rheumatica (Bilateral Girdle Stiffness & Rapid Steroid Response)",
        "icd10": "M35.3",
        "specialty": "Rheumatology / Geriatrics",
        "organ_system": "Musculoskeletal Inflammatory",
        "keywords": ["polymyalgia rheumatica", "pmr", "bilateral shoulder aching", "morning stiffness hips shoulders", "rapid response low dose prednisone", "elevated esr elderly"],
        "red_flags": ["concurrent Giant Cell Arteritis (headache, jaw claudication, visual loss)", "malignancy mimicking polymyalgic onset"],
        "clinical_hallmarks": ["striking age predilection: exclusively occurs in patients OVER 50 YEARS OF AGE (mean onset 73 years)", "subacute, abrupt onset of severe aching and profound morning stiffness (> 45-60 minutes) symmetrically affecting BOTH SHOULDER GIRDLES and frequently the pelvic girdle/neck", "patients report severe difficulty raising arms to brush hair, put on a coat, or get up from a low chair", "physical exam: active range of motion of shoulders and hips is severely restricted by pain, but PASSIVE RANGE OF MOTION AND TRUE MUSCLE STRENGTH ARE NORMAL (normal manual muscle testing)", "laboratory hallmark: MARKED ELEVATION OF ESR (usually > 40-50 mm/hr, often > 80 mm/hr) and CRP, with normal serum Creatine Kinase (CK)", "pathognomonic therapeutic hallmark: DRAMATIC, NEAR-COMPLETE RESOLUTION OF PAIN AND STIFFNESS WITHIN 48-72 HOURS following initiation of low-dose oral prednisone (15 mg/day)"],
        "pertinent_negatives": ["normal Creatine Kinase (CK) decisively differentiates PMR from polymyositis"],
        "content": "Inflammatory rheumatic disorder of older adults characterized by bilateral bursitis and tenosynovitis of the subacromial/subdeltoid, trochanteric bursae, and biceps tendon sheaths (2012 ACR/EULAR provisional criteria). Over 15-20% of PMR patients develop Giant Cell Arteritis (GCA). Treatment: Low-dose Oral Prednisone (12.5 - 15 mg daily single morning dose); Symptoms typically improve by > 70-80% within 3 days; Maintain dose for 3-4 weeks, then slowly taper by 1-2.5 mg every 4 weeks over 12-18 months guided by clinical symptoms and ESR/CRP; IL-6 inhibitor (Sarilumab) approved for steroid-resistant or relapsing PMR."
    },
    {
        "id": "ICD10-M35.89",
        "topic": "Adult-Onset Still's Disease (Yamaguchi Criteria & Hyperferritinemia)",
        "icd10": "M35.89",
        "specialty": "Rheumatology / Hematology",
        "organ_system": "Systemic Autoinflammatory",
        "keywords": ["adult onset still disease", "aosd", "salmon colored evanescent rash", "quotidian fever", "extreme hyperferritinemia", "yamaguchi criteria", "sore throat arthralgia"],
        "red_flags": ["Macrophage Activation Syndrome (MAS / secondary HLH)", "fulminant hepatic failure", "disseminated intravascular coagulation"],
        "clinical_hallmarks": ["Yamaguchi Diagnostic Criteria (requires >= 5 features with >= 2 major):", "Major Criteria: 1. High spiking quotidian or double quotidian fever (>= 39C, typically peaking in evening and returning to baseline); 2. Arthralgias or arthritis lasting >= 2 weeks; 3. Evanescent, non-pruritic, macular or maculopapular SALMON-PINK / SALMON-COLORED CUTANEOUS RASH appearing synchronously with fever spikes and disappearing between spikes (Koebner phenomenon positive); 4. Leukocytosis (WBC >= 10,000 /mcL with >= 80% granulocytes)", "Minor Criteria: sore throat (pharyngitis without exudates), lymphadenopathy and/or splenomegaly, abnormal LFTs, and negative RF and negative ANA", "LABORATORY HALLMARK: EXTREME HYPERFERRITINEMIA (serum ferritin levels often > 3,000 - 10,000 ng/mL, occasionally > 50,000 ng/mL) accompanied by a low percentage of glycosylated ferritin (< 20%)"],
        "pertinent_negatives": ["strictly negative Rheumatoid Factor (RF) and negative ANA"],
        "content": "Rare, systemic autoinflammatory disorder characterized by neutrophil hyperactivation and uncontrolled cytokine storm (IL-1-beta, IL-6, IL-18, and ferritin). Statutory diagnosis of exclusion after ruling out occult infections and hematologic malignancies (lymphoma). Treatment: 1. First-line: High-dose oral Corticosteroids (Prednisone 0.5-1.0 mg/kg/day) or IV pulse Methylprednisolone; 2. Conventional DMARD: Methotrexate (15-25 mg/week); 3. Biologic therapy for steroid-refractory disease: IL-1 receptor antagonists (Anakinra, Canakinumab) or IL-6 antagonists (Tocilizumab) induce rapid clinical and biochemical remission."
    },
    {
        "id": "ICD10-M31.4",
        "topic": "Takayasu Arteritis (Pulseless Disease & Aortic Arch Syndrome)",
        "icd10": "M31.4",
        "specialty": "Rheumatology / Vascular Surgery / Cardiology",
        "organ_system": "Large Vessel Granulomatous Vasculitis",
        "keywords": ["takayasu arteritis", "pulseless disease", "absent radial pulse", "blood pressure discrepancy arms", "carotodynia", "aortic arch syndrome young woman", "claudication upper extremity"],
        "red_flags": ["aortic root aneurysm rupture", "cerebrovascular stroke in young female", "renovascular hypertensive crisis"],
        "clinical_hallmarks": ["predominantly affects YOUNG FEMALES (< 40 years of age, female:male ratio 8:1), historically high prevalence in Asia", "cardinal vascular signs: 1. MARKED BLOOD PRESSURE ASYMMETRY (> 10 mmHg systolic difference between arms); 2. DIMINISHED OR ABSENT UPPER EXTREMITY PULSES ('PULSELESS DISEASE' - impalpable radial or brachial pulses); 3. Arterial bruits audible over subclavian, carotid, or abdominal aorta; 4. Upper extremity claudication (arm fatigue and pain upon exertion)", "carotodynia: localized tenderness over the carotid arteries during active inflammatory phase", "systemic prodrome: low-grade fever, malaise, night sweats, arthralgias, and weight loss", "imaging gold standard: CT/MR Angiography or conventional catheter angiography showing smooth, tapered stenosis, occlusions, and aneurysms of the aorta and its primary branches"],
        "pertinent_negatives": ["age of onset < 40 years distinguishes decisively from Giant Cell Arteritis (> 50 years)"],
        "content": "Chronic, granulomatous, panarteritic large-vessel vasculitis predominantly affecting the aorta, its major primary branch vessels (subclavian, common carotid, renal arteries), and pulmonary arteries (ACR 1990 criteria). Diagnostic workup: MR Angiography (MRA) or CT Angiography of aorta and branches (concentric vessel wall thickening and luminal stenosis), ESR, CRP. Treatment: 1. High-dose oral Corticosteroids (Prednisone 1 mg/kg/day); 2. Steroid-sparing immunosuppressants (Methotrexate, Azathioprine, Mycophenolate); 3. Biologic anti-TNF agents (Infliximab) or Tocilizumab for refractory inflammation; 4. Surgical bypass grafting or endovascular angioplasty/stenting (PERFORMED ONLY WHEN VASCULAR INFLAMMATION IS IN QUIESCENT REMISSION)."
    },

    # --- 9. INFECTIOUS DISEASES & TROPICAL MEDICINE (16) ---
    {
        "id": "ICD10-A27.0",
        "topic": "Leptospirosis (Weil's Disease & Conjunctival Suffusion)",
        "icd10": "A27.0",
        "specialty": "Infectious Disease / Tropical Medicine / Nephrology",
        "organ_system": "Zoonotic Infectious Emergency",
        "keywords": ["leptospirosis", "weils disease", "conjunctival suffusion without purulence", "severe calf tenderness", "flood water fever rat urine", "jaundice with renal failure", "leptospira microscopic agglutination"],
        "red_flags": ["severe pulmonary hemorrhage syndrome (asphyxiating hemoptysis)", "acute anuric renal failure", "fulminant jaundice and coagulopathy (Weil disease)"],
        "clinical_hallmarks": ["history of exposure to freshwater, flooded streets, sewage, or soil contaminated with the urine of infected rodents (rats) or livestock", "abrupt onset of high spiking fever, rigors, and excruciating HEADACHE and MYALGIAS (with EXQUISITE PATHOGNOMONIC CALF MUSCLE TENDERNESS on gentle squeezing)", "pathognomonic physical sign: BILATERAL CONJUNCTIVAL SUFFUSION (diffuse redness and engorgement of bulbar conjunctiva WITHOUT purulent exudate, appearing on day 3-4)", "WEIL'S DISEASE (severe icteric leptospirosis triad): 1. Deep orange-colored jaundice; 2. Acute kidney injury (hypokalemic non-oliguric or oliguric renal failure with elevated creatinine); 3. Hemorrhagic diathesis (pulmonary hemorrhage, petechiae)", "serological gold standard: Microscopic Agglutination Test (MAT >= 1:400) or Leptospira IgM ELISA"],
        "pertinent_negatives": ["conjunctival suffusion lacks pus or crusting (rules out bacterial conjunctivitis)"],
        "content": "Zoonotic infection caused by pathogenic spirochetes of the genus Leptospira (Leptospira interrogans). Biphasic course (septicemic leptospiremic phase followed by immune leptospiruric phase). Diagnostic workup: Blood cultures (EMJH medium), MAT serology, Leptospira PCR. Treatment: Mild anicteric disease: Oral Doxycycline (100 mg BID for 7 days) or Azithromycin; Severe Weil's Disease: STAT IV Aqueous Penicillin G (1.5 million units IV q6h) OR IV Ceftriaxone (1-2 g IV daily for 7 days); Early lung-protective mechanical ventilation for pulmonary hemorrhage; Renal replacement therapy (hemodialysis) for severe AKI."
    },
    {
        "id": "ICD10-A92.0",
        "topic": "Chikungunya Fever (Crippling Arthralgia & Aedes Mosquito)",
        "icd10": "A92.0",
        "specialty": "Infectious Disease / Rheumatology",
        "organ_system": "Arboviral Infectious",
        "keywords": ["chikungunya", "crippling joint pain fever", "chikungunya bent posture", "aedes aegypti", "chikungunya igm", "chronic post chikungunya arthritis", "chikungunya hyperpigmentation nose"],
        "red_flags": ["meningoencephalitis in elderly/infants", "severe bullous cutaneous lesions", "fulminant hepatitis"],
        "clinical_hallmarks": ["transmitted by Aedes aegypti and Aedes albopictus mosquitoes; name derives from Makonde language meaning 'that which bends up' (reflecting the hunched, contorted posture of suffering patients)", "abrupt onset of high fever (> 39C / 102F) accompanied by SEVERE, CRIPPLING, DEBILITATING POLYARTHRALGIA AND POLYARTHRITIS", "joint involvement is bilateral and symmetric, characteristically affecting distal joints (wrists, hands, ankles, metatarsals) with visible periarticular swelling", "centrifugal maculopapular rash appearing 2-5 days after fever onset", "pathognomonic cutaneous pigmentation: Centrofacial brownish/black hyperpigmentation (Chik sign / 'brown nose sign')", "prolonged chronic phase: severe chronic inflammatory polyarthritis persisting for months to years in up to 30-40% of patients"],
        "pertinent_negatives": ["absence of severe retro-orbital pain and profound shock (differentiates from severe dengue, though co-infections occur)"],
        "content": "Arboviral alphavirus infection of the family Togaviridae. Diagnostic workup: RT-PCR for Chikungunya viral RNA (days 1-7 of illness), Chikungunya IgM capture ELISA (positive from day 5 onwards), CBC (lymphopenia, mild thrombocytopenia). Treatment: Acute phase: Strictly supportive: Adequate hydration; Analgesics: Acetaminophen / Paracetamol (avoid NSAIDs and Aspirin until Dengue is definitively excluded to prevent hemorrhage); Chronic persistent arthralgia: NSAIDs, short-course corticosteroids, or Methotrexate / Hydroxychloroquine for chronic destructive arthritis."
    },
    {
        "id": "ICD10-A82.9",
        "topic": "Rabies Encephalitis (Lyssavirus - Hydrophobia & Aerophobia)",
        "icd10": "A82.9",
        "specialty": "Infectious Disease / Emergency Medicine / Critical Care",
        "organ_system": "Neuro-Infectious Lethal Zoonosis",
        "keywords": ["rabies", "hydrophobia", "aerophobia", "dog bite rabies", "lyssavirus", "rabies post exposure prophylaxis", "furious rabies vs paralytic"],
        "red_flags": ["100% case-fatality rate once neurological symptoms appear", "violent inspiratory pharyngeal spasms", "autonomic hyperactivity"],
        "clinical_hallmarks": ["history of animal bite, scratch, or mucosal lick from a rabid mammal (dogs in > 95% in Asia/Africa; bats, raccoons, foxes in Americas)", "incubation period typically 1 to 3 months (ranges from 1 week to 1 year depending on bite distance from central nervous system)", "prodrome: paresthesias, pain, intense pruritus, or tingling at the site of the healed bite wound (in 50-80%)", "Furious Rabies (80%): hallmark HYDROPHOBIA (involuntary, excruciating, violent diaphragmatic and laryngeal spasms triggered by the sight, sound, or attempt to swallow water) and AEROPHOBIA (spasms triggered by a light breeze of air on the face); autonomic instability (hypersalivation / frothing at mouth, dilated pupils, piloerection), agitation, hallucination, and fluctuating lucidity", "Paralytic / Dumb Rabies (20%): ascending flaccid paralysis resembling GBS, progressing to quadriplegia and respiratory failure"],
        "pertinent_negatives": ["once clinical symptoms appear, death is virtually 100% inevitable; PREVENTION IS THE ONLY CURE"],
        "content": "Rhabdovirus neuro-invasive zoonosis caused by Rabies lyssavirus traveling retrogradely via peripheral nerves to the brain. Statutory Mandate - Post-Exposure Prophylaxis (PEP): 1. STAT IMMEDIATE WOUND WASHING: flush bite wound with running water and soap continuously for 15 MINUTES; 2. Rabies Vaccine (cell-culture: IM on days 0, 3, 7, and 14); 3. Human Rabies Immunoglobulin (HRIG: 20 IU/kg infiltrated locally into and around all bite wounds on day 0) MANDATORY for Category III exposures (transdermal bites, scratches, saliva on broken skin/mucosa)."
    },
    {
        "id": "ICD10-A00.9",
        "topic": "Cholera (Vibrio Cholerae - Rice-Water Diarrhea & Dehydration)",
        "icd10": "A00.9",
        "specialty": "Infectious Disease / Emergency Medicine / Gastroenterology",
        "organ_system": "Enteric Waterborne Emergency",
        "keywords": ["cholera", "vibrio cholerae", "rice water stools", "profuse watery diarrhea fishy odor", "washerwomans hands", "cholera cot", "ors fluid resuscitation"],
        "red_flags": ["hypovolemic shock / death within 2-4 hours ('cholera gravis')", "severe hypoglycemia in children", "anuric acute renal failure"],
        "clinical_hallmarks": ["ingestion of water or food contaminated with feces containing Vibrio cholerae (serogroups O1 and O139)", "abrupt onset of massive, effortless, painless, profuse watery diarrhea that rapidly loses all fecal character", "pathognomonic stool appearance: 'RICE-WATER STOOL' (pale, translucent, turbid grayish-white fluid containing flecks of mucus and intestinal epithelial cells, with a faint non-offensive fishy odor)", "volume of fluid loss can exceed 1 Liter per hour (up to 20-30 Liters/day in adults)", "profound signs of dehydration: sunken eyes, dry tongue, loss of skin pinch turgor (> 2-3 seconds), 'washerwoman's hands' (wrinkled shriveled skin on fingers), hoarse voice, absent radial pulses, and anuria"],
        "pertinent_negatives": ["absence of fever, absence of tenesmus, and absence of abdominal cramping (painless watery purged stools)"],
        "content": "Acute diarrheal illness caused by enterotoxigenic bacterium Vibrio cholerae. Cholera enterotoxin (choleragen) binds GM1 ganglioside, irreversibly activating adenylate cyclase, producing massive cAMP and hypersecretion of sodium, chloride, and water. Diagnostic workup: Stool darkfield microscopy (darting motility), Cary-Blair transport medium, TCBS agar culture, rapid dipstick. Emergency Treatment: 1. IMMEDIATE AGGRESSIVE REHYDRATION: IV Ringer's Lactate (100 mL/kg within 3 hours for severe dehydration: 30 mL/kg in first 30 min, then 70 mL/kg over 2.5 hours); 2. WHO Oral Rehydration Solution (ORS) as soon as patient can drink; 3. Single-dose oral antibiotic: Doxycycline (300 mg single dose) or Azithromycin (1 g single dose) reduces stool volume and shedding."
    },
    {
        "id": "ICD10-A03.9",
        "topic": "Shigellosis (Bacillary Dysentery & Hemolytic Uremic Syndrome)",
        "icd10": "A03.9",
        "specialty": "Infectious Disease / Pediatrics / Gastroenterology",
        "organ_system": "Enteric Invasive Infectious",
        "keywords": ["shigellosis", "bacillary dysentery", "bloody diarrhea with fever", "tenesmus severe", "shiga toxin", "hemolytic uremic syndrome shigella", "ciprofloxacin for shigella"],
        "red_flags": ["Hemolytic Uremic Syndrome (HUS: microangiopathic anemia, thrombocytopenia, AKI)", "toxic megacolon / colonic perforation", "pediatric encephalopathy / Ekiri syndrome"],
        "clinical_hallmarks": ["transmitted via fecal-oral route with an extremely low infectious dose (as few as 10-100 organisms can cause disease)", "abrupt onset of high fever, severe colicky lower abdominal pain, and initial watery diarrhea progressing within 24-48 hours to CLASSIC BACILLARY DYSENTERY", "frequent, scant-volume stools composed entirely of FRANK BLOOD, PUS, AND MUCUS (up to 20-30 times per day)", "severe, agonizing TENESMUS (painful, constant, ineffectual straining to defecate, with rectal burning)", "stool microscopy: sheets of Polymorphonuclear Leukocytes (WBCs > 50/hpf) and numerous RBCs", "caused by Shigella dysenteriae type 1 (produces Shiga toxin), Shigella flexneri, or Shigella sonnei"],
        "pertinent_negatives": ["high fever and rapid onset distinguish bacillary dysentery from amoebic dysentery (which is gradual with lower fever)"],
        "content": "Invasive acute bacterial enteritis characterized by mucosal invasion of colonic enterocytes, intracellular multiplication, cell-to-cell spread, and mucosal ulceration. Complications: HUS, toxic megacolon, reactive arthritis. Diagnostic workup: Stool culture (MacConkey or Hektoen enteric agar), stool PCR. Treatment: 1. Strict avoidance of antimotility agents (Loperamide is CONTRAINDICATED as it worsens toxic megacolon); 2. Rehydration therapy; 3. Targeted antimicrobial therapy: Oral Ciprofloxacin (500 mg BID for 3 days) or Azithromycin (500 mg day 1, 250 mg days 2-5) or Ceftriaxone for children."
    },
    {
        "id": "ICD10-A37.90",
        "topic": "Pertussis (Whooping Cough - Bordetella Pertussis Triad)",
        "icd10": "A37.90",
        "specialty": "Pediatrics / Pulmonology / Infectious Disease",
        "organ_system": "Respiratory Infectious",
        "keywords": ["pertussis", "whooping cough", "paroxysmal cough fits", "inspiratory whoop", "post tussive emesis", "bordetella pertussis", "marked absolute lymphocytosis"],
        "red_flags": ["apnea and sudden infant death in infants < 6 months", "refractory pulmonary hypertension and hyperleukocytosis", "seizures / encephalopathy from hypoxia"],
        "clinical_hallmarks": ["caused by Bordetella pertussis, presenting through three distinct sequential clinical phases:", "1. Catarrhal Phase (1-2 weeks): insidious onset of mild coryza, sneezing, low-grade fever, and mild occasional cough (most infectious stage, clinically indistinguishable from common cold)", "2. Paroxysmal Phase (2-6 weeks): violent, uncontrollable paroxysms of coughing (bursts of 5-15 rapid consecutive staccato coughs during a single expiration) culminating in a PATHOGNOMONIC HIGH-PITCHED INSPIRATORY 'WHOOP' as air is forcefully drawn through narrowed glottis", "3. POST-TUSSIVE EMESIS (vomiting immediately following a coughing fit) is highly specific for pertussis in adolescents/adults", "facial petechiae and subconjunctival hemorrhages from extreme venous pressure during coughing", "laboratory hallmark: MARKED ABSOLUTE LYMPHOCYTOSIS (WBC 20,000-50,000 /mcL with > 60-70% mature lymphocytes, driven by pertussis toxin inhibiting lymphocyte extravasation)"],
        "pertinent_negatives": ["infants < 6 months frequently lack the inspiratory whoop and present instead with life-threatening APNEA"],
        "content": "Highly contagious bacterial infection of the tracheobronchial tree. Diagnostic gold standard: Nasopharyngeal swab for Bordetella pertussis PCR (high sensitivity) or Regan-Lowe / Bordet-Gengou culture. Treatment: Macrolide antibiotic initiated early: Oral Azithromycin (10 mg/kg day 1, then 5 mg/kg days 2-5; or 500 mg daily for adults) or Clarithromycin; Antibiotics eliminate nasopharyngeal carriage and prevent secondary transmission within 5 days, though paroxysmal cough may persist for weeks ('the 100-day cough'); Mandatory chemoprophylaxis for all household close contacts."
    },
    {
        "id": "ICD10-A06.4",
        "topic": "Amoebic Liver Abscess (Entamoeba Histolytica & Anchovy Paste Pus)",
        "icd10": "A06.4",
        "specialty": "Gastroenterology / Infectious Disease / General Surgery",
        "organ_system": "Hepatobiliary Parasitic",
        "keywords": ["amoebic liver abscess", "anchovy sauce pus", "entamoeba histolytica", "right upper quadrant pain with fever", "right lobe liver abscess", "metronidazole for amoebic abscess"],
        "red_flags": ["intraperitoneal rupture with acute peritonitis", "rupture into pericardium (cardiac tamponade from left lobe abscess)", "pleuropulmonary rupture (bronchohepatic fistula with anchovy sputum)"],
        "clinical_hallmarks": ["striking male predominance (male:female ratio up to 10:1, peak age 20-50 years), frequently associated with chronic alcohol consumption", "constant, dull, aching RIGHT UPPER QUADRANT (RUQ) abdominal pain radiating to right shoulder or epigastrium", "high remittent fever with rigors, night sweats, and hepatomegaly with EXQUISITE POINT TENDERNESS over the liver (positive intercostal percussion tenderness in 8th/9th intercostal spaces)", "ultrasound / CT abdomen: solitary (80%), round or oval, hypoechoic cystic lesion located in the SUB-CAPSULAR REGION OF THE RIGHT HEPATIC LOBE (> 75-80%)", "diagnostic aspiration (pathognomonic): odorless, thick, reddish-brown fluid universally described as 'ANCHOVY PASTE' or 'CHOCOLATE SAUCE' pus (composed of necrotic hepatocytes and lysed erythrocytes, sterile on bacterial culture)", "serological hallmark: positive serum Entamoeba histolytica IgG ELISA (> 95% sensitivity)"],
        "pertinent_negatives": ["pus is odorless and sterile (foul-smelling pus indicates pyogenic bacterial liver abscess)"],
        "content": "Extra-intestinal complication of Entamoeba histolytica infection, where trophozoites invade colonic venules and travel via portal circulation to liver, causing focal enzymatic liquefactive necrosis. Protocol: 1. Systemic Tissue Amoebicide: Oral Metronidazole (750 mg TID for 10 days) or Tinidazole (2 g daily for 5 days) cures > 90-95% of cases without surgery; 2. MANDATORY Luminal Amoebicide: Oral Diloxanide Furoate (500 mg TID for 10 days) or Paromomycin to eradicate asymptomatic intestinal cyst carriage; 3. Percutaneous needle aspiration or catheter drainage indicated for large abscesses (> 5-10 cm), high risk of rupture, left lobe abscess, or failure to respond to metronidazole within 48-72 hours."
    },
    {
        "id": "ICD10-B55.0",
        "topic": "Visceral Leishmaniasis (Kala-Azar & Leishmania Donovani)",
        "icd10": "B55.0",
        "specialty": "Infectious Disease / Tropical Medicine / Hematology",
        "organ_system": "Reticuloendothelial Parasitic",
        "keywords": ["kala azar", "visceral leishmaniasis", "leishmania donovani", "amastigotes ld bodies", "massive splenomegaly with fever", "black sickness hyperpigmentation", "liposomal amphotericin b"],
        "red_flags": ["fatal secondary bacterial septicemia / pneumonia", "severe bleeding from profound thrombocytopenia", "hemophagocytic lymphohistiocytosis (hlh)"],
        "clinical_hallmarks": ["transmitted by the bite of infected female phlebotomine sandflies (Phlebotomus argentipes in Indian subcontinent); endemic in Bihar, Bengal, East Africa", "insidious onset of prolonged, persistent, irregular, double-spiking high fever lasting weeks to months", "MASSIVE, HUGE, NON-TENDER SPLENOMEGALY (often reaching right iliac fossa) and progressive hepatomegaly", "profound cachexia, muscle wasting, and pathognomonic slate-grey / dusky cutaneous hyperpigmentation of hands, feet, abdomen, and forehead (giving the Hindi name 'Kala-Azar' / Black Sickness)", "diagnostic laboratory triad: 1. PANCYTOPENIA (normocytic normochromic anemia, severe leukopenia/neutropenia < 2,000 /mcL, thrombocytopenia); 2. HYPERGAMMAGLOBULINEMIA with reversal of albumin-to-globulin (A:G) ratio; 3. Elevated transaminases", "diagnostic gold standard: Demonstration of intracellular AMASTIGOTES (Leishman-Donovan [LD] bodies) within macrophages on bone marrow aspirate or splenic aspirate (splenic aspirate sensitivity > 95%)"],
        "pertinent_negatives": ["positive rK39 rapid immunochromatographic dipstick test confirms diagnosis in endemic areas"],
        "content": "Severe parasitic infection of the reticuloendothelial system caused by the protozoan Leishmania donovani. Untreated visceral leishmaniasis is fatal in > 95% of cases within 2 years. WHO First-Line Treatment for Indian Subcontinent: Single-dose IV Liposomal Amphotericin B (AmBisome: 10 mg/kg IV infusion over 2 hours) achieves > 95-98% permanent cure rate with minimal toxicity; Alternative oral agent: Miltefosine (50 mg BID for 28 days - strictly teratogenic, contraindicated in pregnancy); Post-Kala-Azar Dermal Leishmaniasis (PKDL) requires extended treatment."
    },
    {
        "id": "ICD10-A51.0",
        "topic": "Syphilis (Treponema Pallidum - Primary Chancre to Neurosyphilis)",
        "icd10": "A51.0",
        "specialty": "Infectious Disease / Dermatology / Neurology",
        "organ_system": "Sexually Transmitted Multisystem",
        "keywords": ["syphilis", "treponema pallidum", "primary chancre painless ulcer", "secondary syphilis copper rash palms soles", "condylomata lata", "argyll robertson pupil", "vdrl rpr fta abs", "penicillin g benzathine"],
        "red_flags": ["Jarisch-Herxheimer reaction after penicillin", "tertiary neurosyphilis / tabes dorsalis / general paresis", "thoracic aortic aneurysm with tree-bark calcification"],
        "clinical_hallmarks": ["Primary Syphilis: HARD CHANCRE (solitary, painless, indurated, clean-based ulcer with raised, rolled borders on genitalia or oral mucosa) accompanied by painless regional lymphadenopathy; heals spontaneously in 3-6 weeks", "Secondary Syphilis (systemic dissemination): diffuse, non-pruritic, symmetrical, coppery-red / bronze maculopapular rash characteristically INVOLVING THE PALMS AND SOLES; CONDYLOMATA LATA (painless, highly infectious, broad, moist, wart-like plaques in intertriginous/perianal regions); mucous patches; 'moth-eaten' patchy alopecia", "Tertiary Syphilis: Gummas (destructive granulomatous lesions of skin/bone), cardiovascular syphilis (ascending aortitis), and Neurosyphilis: Tabes Dorsalis (sensory ataxia, lightning pains, Charcot joints) and ARGYLL ROBERTSON PUPILS ('prostitute's pupil': accommodates to near vision but does not react to light)", "serological algorithm: Non-treponemal screening tests (VDRL or RPR - titers monitor treatment response) confirmed by Treponemal-specific tests (FTA-ABS or TP-PA)"],
        "pertinent_negatives": ["painless clean base distinguishes primary chancre from painful necrotic chancroid or HSV"],
        "content": "Chronic, multistage systemic infection caused by the spirochete Treponema pallidum subsp. pallidum. Diagnostic workup: Darkfield microscopy of chancre exudate, nontreponemal (RPR/VDRL) and treponemal serology, CSF examination for neurosyphilis. Treatment: 1. Primary, Secondary, or Early Latent Syphilis: Benzathine Penicillin G (2.4 million units IM single dose); 2. Late Latent Syphilis or Latent of unknown duration: Benzathine Penicillin G (2.4 million units IM once weekly for 3 consecutive weeks, total 7.2 million units); 3. Neurosyphilis: Continuous IV Aqueous Crystalline Penicillin G (18-24 million units daily as 3-4 million units q4h for 10-14 days); Oral Doxycycline (100 mg BID for 14-28 days) for non-pregnant penicillin-allergic patients."
    },
    {
        "id": "ICD10-B02.30",
        "topic": "Herpes Zoster Ophthalmicus (VZV Reactivation & Hutchinson Sign)",
        "icd10": "B02.30",
        "specialty": "Ophthalmology / Dermatology / Infectious Disease / Neurology",
        "organ_system": "Cranial Neuropathic / Ocular Emergency",
        "keywords": ["herpes zoster ophthalmicus", "hzo", "hutchinson sign tip of nose", "dermatomal rash forehead", "varicella zoster reactivation", "dendritic pseudoulcer cornea", "postherpetic neuralgia"],
        "red_flags": ["corneal perforation / blindness", "acute retinal necrosis", "contralateral hemiplegia / post-herpetic stroke"],
        "clinical_hallmarks": ["reactivation of latent Varicella-Zoster Virus (VZV) within the Ophthalmic division of the Trigeminal Nerve (Cranial Nerve V1)", "prodromal severe unilateral burning, tingling, or lancinating forehead and scalp pain", "pain is followed by a classic unilateral, erythematous, vesicular, crusting dermatomal rash strictly respecting the midline of the forehead and upper eyelid", "PATHOGNOMONIC HUTCHINSON SIGN: presence of herpetic vesicles on the TIP, SIDE, OR ROOT OF THE NOSE (indicates involvement of the nasociliary branch of CN V1, carrying a > 75% risk of sight-threatening ocular complications)", "slit-lamp ocular manifestations: punctate epithelial keratitis, dendritic pseudoulcer (mucous plaque dendrite lacking terminal bulbs, distinct from HSV), anterior uveitis with raised intraocular pressure, and stromal keratitis"],
        "pertinent_negatives": ["rash strictly respects the vertical anatomical midline of face"],
        "content": "Sight-threatening ophthalmic emergency. Immediate Treatment Protocol: 1. Early Systemic Antiviral Therapy (MUST BE INITIATED WITHIN 72 HOURS OF RASH ONSET): Oral Valacyclovir (1,000 mg TID for 7-10 days) or Famciclovir (500 mg TID) or oral Acyclovir (800 mg 5x/day); 2. STAT Emergent Ophthalmologist Consultation; 3. Topical Corticosteroid drops (Prednisolone acetate 1%) indicated ONLY under ophthalmology supervision for stromal keratitis/uveitis; 4. Prevention: Recombinant Zoster Vaccine (Shingrix - 2 doses) for adults >= 50 years; 5. Postherpetic neuralgia management: Gabapentin, Pregabalin, or Amitriptyline."
    },
    {
        "id": "ICD10-A22.0",
        "topic": "Anthrax (Bacillus Anthracis - Cutaneous Malignant Pustule & Inhalation)",
        "icd10": "A22.0",
        "specialty": "Infectious Disease / Dermatology / Critical Care",
        "organ_system": "Bacterial Zoonosis / Biosecurity",
        "keywords": ["anthrax", "bacillus anthracis", "cutaneous anthrax black eschar", "malignant pustule", "inhalation anthrax widened mediastinum", "gelatinous non pitting edema", "ciprofloxacin for anthrax"],
        "red_flags": ["inhalation anthrax with acute respiratory failure (near 100% fatal without early therapy)", "anthrax meningoencephalitis with hemorrhagic CSF", "asphyxiation from massive cervical edema"],
        "clinical_hallmarks": ["history of exposure to infected herbivorous livestock (cattle, sheep, goats) or animal products (hides, wool, bone meal), or biosecurity aerosol threat", "Cutaneous Anthrax (95% of cases): painless pruritic papule developing 1-7 days post-exposure, rapidly enlarging into a vesicle surrounded by a ring of satellite vesicles; ruptures to form a characteristic PATHOGNOMONIC COAL-BLACK, DEPRESSED, PAINLESS NECROTIC ESCHAR ('MALIGNANT PUSTULE')", "surrounded by EXTENSIVE, GELATINOUS, NON-PITTING EDEMA that is striking and completely out of proportion to lesion size", "Inhalation Anthrax (Woolsorter's disease): biphasic illness (initial mild viral-like prodrome followed by abrupt acute dyspnea, cyanosis, stridor, and diaphoresis); Chest Radiograph: PATHOGNOMONIC MARKED WIDENING OF THE MEDIASTINUM and pleural effusions due to hemorrhagic mediastinitis without parenchymal bronchopneumonia"],
        "pertinent_negatives": ["lesion is PAINLESS and has absence of frank pus (distinguishes from staphylococcal carbuncle)"],
        "content": "Zoonotic infection caused by the spore-forming Gram-positive rod Bacillus anthracis. Virulence factors: Poly-D-glutamic acid antiphagocytic capsule and tripartite exotoxin (Protective Antigen [PA], Lethal Factor [LF], Edema Factor [EF]). Diagnostic workup: Gram stain and PCR of vesicle fluid, blood cultures, chest CT. Treatment: Cutaneous: Oral Ciprofloxacin (500 mg BID for 60 days) or Doxycycline (100 mg BID); Inhalation / Systemic: IV Triple Therapy (IV Ciprofloxacin + Clindamycin/Linezolid [protein synthesis inhibitor to halt toxin production] + Meropenem) + Monoclonal Antitoxin (Raxibacumab or Obiltoxaximab or Anthrax Immune Globulin)."
    },
    {
        "id": "ICD10-A23.9",
        "topic": "Brucellosis (Malta Fever - Undulant Fever & Sacroiliitis)",
        "icd10": "A23.9",
        "specialty": "Infectious Disease / Rheumatology / Orthopedics",
        "organ_system": "Zoonotic Infectious",
        "keywords": ["brucellosis", "malta fever", "undulant fever", "unpasteurized milk fever", "brucella sacroiliitis spondylodiscitis", "standard tube agglutination", "doxycycline rifampin"],
        "red_flags": ["brucella endocarditis (aortic valve destruction - leading cause of mortality)", "neurobrucellosis (meningoencephalitis)", "vertebral collapse with spinal cord compression"],
        "clinical_hallmarks": ["history of consuming unpasteurized raw dairy products (fresh goat/sheep milk, unpasteurized cheese) or direct contact with livestock tissues (farmers, slaughterhouse workers, veterinarians)", "classic 'UNDULANT FEVER': daily waxing and waning cyclical fevers rising in late afternoon/evening and falling towards morning, accompanied by PROFUSE, MALODOROUS DIAPHORESIS with a characteristic 'wet hay' or moldy odor", "ostearticular complications (most common 40%): unilateral SACROILIITIS, peripheral arthritis, and Lumbar Spondylodiscitis (characteristically affecting L4-L5 with anterior superior vertebral osteophytosis / 'Pedro Pons sign')", "hepatosplenomegaly and generalized lymphadenopathy", "diagnostic workup: prolonged blood culture (biphasic Castaneda medium kept for 4 weeks), Standard Tube Agglutination Test (STAT / Wright test >= 1:160) or Brucella Coombs test"],
        "pertinent_negatives": ["absence of acute leukocytosis (normal WBC or leukopenia with relative lymphocytosis)"],
        "content": "Zoonotic intracellular bacterial infection caused by Brucella species (Brucella melitensis [goats/sheep - most invasive], B. abortus [cattle], B. suis [swine]). First-line WHO Dual Antimicrobial Regimen: Oral Doxycycline (100 mg BID) PLUS Oral Rifampin (600-900 mg once daily fasting) FOR A MINIMUM OF 6 WEEKS (prolonged course mandatory to prevent relapse of intracellular bacteria); Alternative: Doxycycline for 6 weeks + IM Streptomycin (1g daily for first 14-21 days); Spondylodiscitis or neurobrucellosis requires triple therapy (Doxycycline + Rifampin + Ceftriaxone) for 3-6 months."
    },
    {
        "id": "ICD10-A15.0",
        "topic": "Multidrug-Resistant Tuberculosis (MDR-TB & GeneXpert MTB/RIF)",
        "icd10": "A15.0",
        "specialty": "Pulmonology / Infectious Disease",
        "organ_system": "Mycobacterial Respiratory",
        "keywords": ["mdr tb", "multidrug resistant tuberculosis", "genexpert rifampicin resistance", "isoniazid rifampicin resistant", "bedaquiline delamanid", "chronic cough hemoptysis cavity", "bpal regimen"],
        "red_flags": ["extensive drug-resistant tb (xdr-tb)", "respiratory failure with destroyed lung", "massive hemoptysis"],
        "clinical_hallmarks": ["chronic, progressive cough lasting > 3-4 weeks with purulent sputum, recurrent hemoptysis, pleuritic chest pain, and profound constitutional B-symptoms: drenching night sweats, persistent low-grade evening fever, anorexia, and severe wasting cachexia ('consumption')", "history of previous incomplete, interrupted, or irregular anti-tubercular therapy (ATT), or contact with a known drug-resistant TB patient", "chest radiograph: upper lobe cavitary lesions, extensive fibro-cavitary destruction, and bilateral bronchogenic endobronchial spread", "DEFINITIVE DEFINITION OF MDR-TB: Mycobacterium tuberculosis strain demonstrating RESISTANCE TO SIMULTANEOUSLY BOTH ISONIAZID (INH) AND RIFAMPICIN (RIF), the two most potent first-line anti-TB bactericidal agents", "molecular rapid diagnostic hallmark: GeneXpert MTB/RIF (Cartridge-Based Nucleic Acid Amplification Test - CBNAAT) detects MTB DNA and mutations in the rpoB gene (conferring Rifampicin resistance) within 2 hours"],
        "pertinent_negatives": ["GeneXpert positive for Rifampicin resistance acts as a reliable surrogate for MDR-TB (> 90% also INH resistant)"],
        "content": "Form of tuberculosis caused by Mycobacterium tuberculosis bacilli resistant to at least isoniazid and rifampicin. Diagnostic workup: GeneXpert MTB/RIF, Line Probe Assay (LPA: Hain test for first- and second-line drugs), Mycobacterial Liquid Culture (MGIT) with Phenotypic Drug Susceptibility Testing (DST). WHO Recommended All-Oral Treatment Regimens: 1. Novel 6-month BPaL/BPaLM regimen: Bedaquiline + Pretomanid + Linezolid (+/- Moxifloxacin); 2. All-oral longer regimen (18-20 months) grouped by WHO priority: Group A (Levofloxacin/Moxifloxacin, Bedaquiline, Linezolid) + Group B (Clofazimine, Cycloserine); Strict directly observed therapy (DOTS) and monthly sputum smear/culture monitoring."
    },
    {
        "id": "ICD10-B06.9",
        "topic": "Rubella (German Measles & Congenital Rubella Syndrome)",
        "icd10": "B06.9",
        "specialty": "Pediatrics / Obstetrics / Infectious Disease",
        "organ_system": "Viral Exanthem / Teratogenic",
        "keywords": ["rubella", "german measles", "congenital rubella syndrome", "forchheimer spots", "suboccipital lymphadenopathy", "patent ductus arteriosus cataracts deafness", "rubella igm"],
        "red_flags": ["congenital rubella syndrome (catastrophic multiorgan teratogenesis if acquired in first trimester)", "encephalitis", "thrombocytopenic purpura"],
        "clinical_hallmarks": ["Postnatal Rubella: mild viral illness with low-grade fever, mild conjunctivitis, and a discrete pinkish-red maculopapular rash that starts on the face and spreads rapidly downward to trunk and limbs, fading within 3 days ('3-day measles')", "PATHOGNOMONIC POSTNATAL SIGNS: 1. Tender, prominent SUBOCCIPITAL, POSTAURICULAR, and posterior cervical lymphadenopathy (appearing up to a week before the rash); 2. Forchheimer spots (small, pinpoint red macules on the soft palate)", "CONGENITAL RUBELLA SYNDROME (CRS - classic Gregg's Triad resulting from primary maternal infection in early pregnancy): 1. Sensorineural deafness (most common 60-80%); 2. Ocular abnormalities (bilateral dense 'pearly-white' nuclear cataracts, microphthalmia, pigmentary 'salt-and-pepper' retinopathy); 3. Congenital cardiac defects (Patent Ductus Arteriosus [PDA] and peripheral pulmonary artery stenosis); 4. Microcephaly and 'blueberry muffin' purpura (extramedullary hematopoiesis)"],
        "pertinent_negatives": ["absence of high fever and absence of Koplik spots (distinguishes rubella from rubeola/measles)"],
        "content": "Enveloped positive-sense RNA virus belonging to the family Matonaviridae (Rubivirus). Diagnostic workup: Rubella-specific IgM capture ELISA, RT-PCR from throat swab or amniotic fluid. Treatment: Postnatal rubella is self-limiting requiring supportive care; CRS has no curative antiviral treatment (rehabilitative surgery for cataracts/PDA and hearing aids); Universal Prevention: Measles-Mumps-Rubella (MMR) live attenuated vaccine administered at 12-15 months and 4-6 years (STRICTLY CONTRAINDICATED in pregnancy; pregnancy must be avoided for 1 month post-vaccination)."
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
            
    print(f"Batch 4A added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""
Batch 4C: Dermatology, Ophthalmology, ENT, Orthopedics, Toxicology.
Expands knowledge base past 500 validated clinical protocols.
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
    # --- 11. DERMATOLOGY & STDs (14) ---
    {
        "id": "ICD10-L10.0",
        "topic": "Pemphigus Vulgaris (Desmoglein-3 & Positive Nikolsky Sign)",
        "icd10": "L10.0",
        "specialty": "Dermatology / Oral Medicine",
        "organ_system": "Autoimmune Bullous Dermatosis",
        "keywords": ["pemphigus vulgaris", "positive nikolsky sign", "flaccid bullae", "oral erosions pemphigus", "desmoglein 3 desmoglein 1", "fishnet immunofluorescence", "tombstone basal layer"],
        "red_flags": ["extensive denudation mimicking severe burns", "secondary bacterial sepsis (S. aureus, Pseudomonas)", "severe dehydration and electrolyte collapse"],
        "clinical_hallmarks": ["ORAL MUCOSAL LESIONS ARE THE INITIAL PRESENTATION in > 70-80% of patients, preceding cutaneous blisters by months: painful, persistent, non-healing erosions and shallow ulcers on buccal mucosa, palate, and gingiva that make eating agonizing", "cutaneous lesions: FLACCID, THIN-WALLED, FRAGILE BLISTERS AND BULLAE arising on normal or erythematous skin (characteristically on scalp, face, chest, and intertriginous folds)", "blisters rupture extremely easily, leaving extensive, painful, weeping, raw, denuded areas with crusting and slow healing", "PATHOGNOMONIC PHYSICAL SIGN: POSITIVE NIKOLSKY'S SIGN (firm lateral sliding pressure of a finger on normal-appearing perilesional skin causes immediate dislodgement or sloughing of the epidermis)", "Asboe-Hansen sign (bulla spread sign): gentle downward pressure on an intact blister causes lateral extension of the fluid wave into adjacent unblistered skin", "direct immunofluorescence (pathognomonic): intercellular 'FISHNET' or 'CHICKEN-WIRE' pattern of IgG and C3 deposition throughout the squamous epidermis"],
        "pertinent_negatives": ["flaccid blisters and positive Nikolsky distinguish pemphigus from tense blisters and negative Nikolsky of bullous pemphigoid"],
        "content": "Potentially fatal autoimmune blistering disease caused by IgG autoantibodies targeting Desmoglein-3 (mucosal-predominant) and Desmoglein-1 (mucocutaneous), causing intraepidermal acantholysis (loss of intercellular keratinocyte adhesion). Histopathology shows suprabasal intraepidermal split with a retained 'row of tombstones' basal layer. Treatment: 1. STAT High-dose Systemic Corticosteroids (Oral Prednisone 1.0-1.5 mg/kg/day); 2. FIRST-LINE BIOLOGIC: Rituximab (anti-CD20: two 1000 mg IV infusions on days 1 and 15 - induces complete remission in > 85-90% and reduces steroid requirements); 3. Adjuvant immunosuppressants (Mycophenolate Mofetil, Azathioprine); 4. Intensive burn-like barrier wound care."
    },
    {
        "id": "ICD10-L12.0",
        "topic": "Bullous Pemphigoid (BP180 & BP230 - Negative Nikolsky Sign)",
        "icd10": "L12.0",
        "specialty": "Dermatology / Geriatrics",
        "organ_system": "Autoimmune Bullous Dermatosis",
        "keywords": ["bullous pemphigoid", "tense bullae", "negative nikolsky sign", "bp180 bp230", "elderly blistering disease", "linear igg basement membrane", "subepidermal blister"],
        "red_flags": ["secondary cutaneous cellulitis / sepsis", "iatrogenic steroid complications in frail elderly"],
        "clinical_hallmarks": ["predominantly affects ELDERLY PATIENTS (> 70-80 years of age), frequently with underlying neurological comorbidities (Parkinson's, dementia, prior stroke)", "prodromal phase lasting weeks to months: intense, severe, generalized PRURITUS with urticarial, eczematous, or excoriated plaques", "bullous phase: widespread eruption of LARGE, TENSE, FIRM, DOME-SHAPED BLISTERS AND BULLAE (1-5 cm) filled with clear or serosanguinous fluid, arising on either normal or erythematous urticarial bases", "predilection for flexor aspects of limbs (forearms, thighs, lower abdomen, axillae, groins)", "blisters DO NOT RUPTURE EASILY and can remain intact for days", "NEGATIVE NIKOLSKY'S SIGN (firm lateral sliding pressure DOES NOT shear the epidermis)", "oral mucosal involvement is RARE (< 10-20%) and mild (sharp contrast to pemphigus vulgaris)", "histopathology and immunofluorescence: SUBEPIDERMAL BLISTER with eosinophil-rich infiltrate; Direct Immunofluorescence shows CONTINUOUS, SMOOTH, LINEAR BAND OF IgG AND C3 along the dermo-epidermal junction"],
        "pertinent_negatives": ["tense bullae, lack of oral ulcers, and negative Nikolsky distinguish BP from Pemphigus Vulgaris"],
        "content": "Most common autoimmune subepidermal blistering disease of the elderly, caused by IgG autoantibodies targeting hemidesmosomal proteins at the dermal-epidermal junction: BP180 (type XVII collagen) and BP230. Diagnostic workup: Perilesional skin biopsy for DIF, serum ELISA for anti-BP180/BP230. Treatment: 1. Extensive disease: High-potency Topical Corticosteroid ointment (Clobetasol propionate 0.05% cream 30-40 g daily applied to whole body - preferred over systemic steroids due to significantly lower mortality in frail elderly); 2. Systemic Corticosteroids (Prednisone 0.5 mg/kg/day); 3. Anti-inflammatory antibiotics: oral Doxycycline (100 mg BID) + Nicotinamide; 4. Methotrexate or Rituximab for refractory cases."
    },
    {
        "id": "ICD10-L51.1",
        "topic": "Stevens-Johnson Syndrome & Toxic Epidermal Necrolysis (SCORTEN)",
        "icd10": "L51.1",
        "specialty": "Dermatology / Critical Care / Burn Surgery / Emergency Medicine",
        "organ_system": "Severe Cutaneous Adverse Reaction Emergency",
        "keywords": ["stevens johnson syndrome", "sjs", "toxic epidermal necrolysis", "ten", "scorten score", "atypical target lesions", "skin detachment epidermal sloughing", "drug induced skin peeling"],
        "red_flags": ["massive fluid and protein loss / hypovolemic shock", "multiorgan failure and severe sepsis", "cicatricial conjunctival scarring and blindness"],
        "clinical_hallmarks": ["acute, life-threatening, idiosyncratic, immune-complex severe cutaneous adverse reaction (SCAR) typically triggered 1 to 4 weeks after starting a high-risk medication (the mnemonic 'SAMPAT': Sulfonamides, Allopurinol, Anticonvulsants [Carbamazepine, Phenytoin, Lamotrigine], NSAIDs, Penicillins / Nevirapine)", "prodrome: fever, sore throat, stinging eyes, and malaise 1-3 days before skin eruption", "initial skin lesions: atypical, flat, dusky, purpuric TARGET LESIONS (two concentric zones of color) starting on trunk and face, coalescing into confluent erythematous sheets", "rapid progression over hours: epidermolysis producing FLACCID BLISTERS AND SHEETS OF EPIDERMAL DETACHMENT, leaving extensive, glistening, red, denuded 'scalded' dermis (POSITIVE NIKOLSKY SIGN)", "CLASSIFICATION BY BODY SURFACE AREA (BSA) DETACHMENT: SJS (< 10% BSA detachment), SJS/TEN Overlap (10-30% BSA), TEN (> 30% BSA detachment)", "SEVERE MUCOSAL INVOLVEMENT IN >= 2 SITES (> 90% of cases): hemorrhagic crusted lips, erosive stomatitis, severe membranous conjunctivitis with pseudomembrane and symblepharon formation, and painful genital erosions"],
        "pertinent_negatives": ["full-thickness epidermal necrosis on frozen section skin biopsy (distinguishes from Staphylococcal Scalded Skin Syndrome which is superficial intra-granular split)"],
        "content": "T-cell-mediated hypersensitivity reaction where cytotoxic CD8+ T-cells and NK cells release granulysin, perforin/granzyme B, and Fas-ligand, inducing widespread apoptotic keratinocyte cell death. SCORTEN Prognostic Scale (calculated within first 24 hours). Emergency Protocol: 1. STAT IMMEDIATE CESSATION OF ALL SUSPECTED CAUSATIVE MEDICATIONS (single most critical determinant of survival); 2. Immediate transfer to specialized Burn Center / ICU; 3. Meticulous supportive fluid and electrolyte resuscitation and thermoregulation (ambient temperature 30-32C); 4. Non-adherent biological or silicone dressings (no aggressive debridement); 5. STAT Ophthalmology consultation for amniotic membrane grafting to prevent blindness; 6. Targeted therapy: IVIG (2-3 g/kg over 3 days) or Cyclosporine (3-5 mg/kg/day) or Etanercept (TNF-alpha inhibitor)."
    },
    {
        "id": "ICD10-L40.0",
        "topic": "Psoriasis Vulgaris (Plaque Psoriasis & Auspitz Sign)",
        "icd10": "L40.0",
        "specialty": "Dermatology",
        "organ_system": "Cutaneous Inflammatory",
        "keywords": ["psoriasis vulgaris", "plaque psoriasis", "auspitz sign pinpoint bleeding", "silvery white micaceous scale", "extensor surface plaques", "koebner phenomenon psoriasis", "nail pitting oil drop"],
        "red_flags": ["generalized erythrodermic psoriasis (> 90% BSA - thermoregulatory collapse)", "acute generalized pustular psoriasis of Von Zumbusch", "psoriatic arthritis"],
        "clinical_hallmarks": ["sharply demarcated, erythematous, raised salmon-pink plaques covered with THICK, SILVERY-WHITE, COARSE, MICACEOUS SCALES", "classic anatomical distribution: EXTENSOR SURFACES of extremities (symmetrically over elbows and knees), scalp, lumbosacral region, and umbilicus", "pathognomonic clinical signs: 1. AUSPITZ SIGN (gentle scraping off of the silvery scales reveals punctate, pinpoint capillary bleeding points from thinned suprapapillary plates); 2. KOEBNER PHENOMENON (development of new psoriatic plaques at sites of cutaneous mechanical trauma or excoriation); 3. Woronoff ring (pale blanching halo surrounding resolving psoriatic plaques)", "characteristic nail changes in > 50%: regular punctate nail pitting, 'oil-drop' or salmon-patch subungual discoloration, subungual hyperkeratosis, and onycholysis"],
        "pertinent_negatives": ["silvery micaceous scale and Auspitz sign distinguish psoriasis from eczema/atopic dermatitis (which is poorly demarcated with lichenification and flexural distribution)"],
        "content": "Chronic, immune-mediated, inflammatory skin disease driven by the IL-23 / Th17 / IL-17 cytokine signaling axis, causing hyperproliferation and altered differentiation of epidermal keratinocytes (epidermal transit time shortened from 28 days to 3-5 days). Treatment (Stepwise): 1. Limited Mild-Moderate (< 5-10% BSA): High-potency Topical Corticosteroids (Clobetasol, Betamethasone) combined with Topical Vitamin D3 analogues (Calcipotriol ointment) +/- Topical tazarotene; 2. Moderate-Severe (> 10% BSA): Narrowband UVB (NB-UVB) phototherapy; 3. Systemic Conventional Agents: Oral Methotrexate (15-20 mg weekly) or oral Cyclosporine; 4. Biologic Targeted Therapies (PASI-90 / PASI-100 clearance): IL-17 inhibitors (Secukinumab, Ixekizumab), IL-23 inhibitors (Guselkumab, Risankizumab), or TNF inhibitors."
    },
    {
        "id": "ICD10-B86",
        "topic": "Scabies Infestation (Sarcoptes Scabiei - Interdigital Burrows)",
        "icd10": "B86",
        "specialty": "Dermatology / Primary Care / Pediatrics",
        "organ_system": "Parasitic Dermatosis",
        "keywords": ["scabies", "sarcoptes scabiei", "interdigital burrows", "intense nocturnal itching", "permethrin 5% cream", "crusted norwegian scabies", "treating all household contacts"],
        "red_flags": ["Crusted / Norwegian Scabies (massive mite burden, non-pruritic thick crusts, highly contagious in immunocompromised)", "secondary impetigo / post-streptococcal glomerulonephritis"],
        "clinical_hallmarks": ["intense, severe, intractable, generalized PRURITUS THAT IS OVERWHELMINGLY WORST AT NIGHT and after hot baths (due to delayed Type IV hypersensitivity to mite proteins, ova, and feces)", "close household contacts, bed partners, or institutional co-residents sharing identical pruritus symptoms", "PATHOGNOMONIC ELEMENTARY LESION: THE SCABIES BURROW (a short [2-15 mm], thin, greyish-white or brownish, tortuous, thread-like, serpiginous elevated cutaneous tunnel made by female mite burrowing into stratum corneum, often ending in a tiny vesicle containing the mite)", "classic anatomical distribution ('The Circle of Hebra'): INTERDIGITAL WEB SPACES OF THE FINGERS, flexor creases of wrists, elbows, axillary folds, umbilicus, belt line, buttocks, and GENITALIA (exquisitely pathognomonic pruritic nodules on the penis and scrotum in males; areolar eczema in females)", "strict sparing of the head, face, and neck in immunocompetent adults (face CAN be involved in infants and crusted scabies)"],
        "pertinent_negatives": ["sparing of head/neck in immunocompetent adults confirms classic scabies"],
        "content": "Parasitic ectoparasitic infestation of the human skin caused by the microscopic obligate mite Sarcoptes scabiei var. hominis. Definitive diagnosis: Skin scraping of a burrow with mineral oil examined under light microscopy demonstrating adult mites, eggs, or scybala (fecal pellets). Management Protocol: 1. Topical 5% Permethrin Cream: applied meticulously over ENTIRE BODY from the neck down to the tips of toes (including interdigital webs, under fingernails, and perianal region), left on for 8-14 hours before washing off; MUST BE REPEATED IN 7-14 DAYS to kill newly hatched nymphs; 2. Oral Ivermectin (200 mcg/kg single oral dose, repeated in 7-14 days) - first-line for crusted scabies or institutional outbreaks; 3. MANDATORY SIMULTANEOUS TREATMENT OF ALL HOUSEHOLD CONTACTS and bed partners regardless of symptoms; 4. Hot water laundering of all clothing, bedding, and towels used in prior 3-4 days."
    },
    {
        "id": "ICD10-C43.9",
        "topic": "Malignant Melanoma (ABCDE Diagnostic Criteria & Breslow Depth)",
        "icd10": "C43.9",
        "specialty": "Dermatology / Surgical Oncology",
        "organ_system": "Cutaneous Malignancy",
        "keywords": ["melanoma", "malignant melanoma", "abcde criteria melanoma", "breslow depth thickness", "ugly duckling sign", "sentinel lymph node biopsy melanoma", "braf v600e"],
        "red_flags": ["ulceration / spontaneous bleeding of pigmented lesion", "palpable regional lymphadenopathy", "distant metastatic spread (liver, brain, bone)"],
        "clinical_hallmarks": ["the classic 'ABCDE' CLINICAL SCREENING CRITERIA FOR MELANOMA:", "A - ASYMMETRY: one half of the cutaneous pigmented lesion does not match the other half", "B - BORDER: irregular, notched, scalloped, ragged, or poorly defined/blurred borders", "C - COLOR: variegated, uneven pigmentation with multiple colors within the same lesion (shades of tan, brown, jet black, interspersed with red, white, or slate-blue depigmented areas)", "D - DIAMETER: larger than 6 mm (roughly the size of a pencil eraser, though melanomas can be smaller)", "E - EVOLVING: any documented change in size, shape, color, surface contour, or new symptoms (itching, bleeding, tenderness)", "THE 'UGLY DUCKLING' SIGN: a solitary nevus that looks distinctly different and out of character compared to all other surrounding nevi in that individual", "Dermoscopy hallmarks: atypical pigment network, irregular brown/black globules, asymmetric pigmentation, and blue-white veil"],
        "pertinent_negatives": ["EXCISIONAL BIOPSY WITH 1-3 MM MARGINS IS MANDATORY; SHAVE BIOPSY IS STRONGLY DISCOURAGED because it compromises accurate Breslow depth measurement"],
        "content": "Highly aggressive malignancy arising from epidermal melanocytes, strongly correlated with intermittent intense UV-radiation blistering sun exposure and somatic driver mutations (BRAF V600E in 50%, NRAS, KIT). Single Most Important Histopathological Prognostic Factor: BRESLOW THICKNESS (measured in millimeters from the granular layer to the deepest tumor cell). Management Protocol: 1. Complete full-thickness excisional biopsy with 1-3 mm margins; 2. Wide Local Excision (WLE) with surgical margins based on Breslow thickness (Melanoma in situ: 5 mm margin; <= 1.0 mm depth: 1 cm margin; > 1.0-2.0 mm depth: 1-2 cm margin; > 2.0 mm depth: 2 cm margin); 3. Sentinel Lymph Node Biopsy (SLNB) for Breslow depth > 0.8 mm or ulcerated lesions; 4. Adjuvant/Metastatic Therapy: Targeted BRAF/MEK inhibitors (Dabrafenib + Trametinib for BRAF-mutant) OR Dual Immune Checkpoint Inhibitors (Nivolumab + Ipilimumab)."
    },
    {
        "id": "ICD10-C44.91",
        "topic": "Basal Cell Carcinoma (Nodular BCC & Pearly Telangiectatic Papule)",
        "icd10": "C44.91",
        "specialty": "Dermatology / Mohs Micrographic Surgery",
        "organ_system": "Cutaneous Malignancy",
        "keywords": ["basal cell carcinoma", "bcc", "pearly papule with telangiectasia", "rodent ulcer", "rolled borders bcc", "mohs micrographic surgery", "hedgehog pathway vismodegib"],
        "red_flags": ["local tissue destruction eroding into cartilage/bone ('rodent ulcer')", "perineural invasion (facial numbness/pain)", "orbital invasion"],
        "clinical_hallmarks": ["THE MOST COMMON CANCER IN HUMANS worldwide, overwhelmingly arising on chronic sun-exposed areas of the head and neck (> 80%, characteristically nose, eyelids, ears, cheeks)", "Nodular BCC (most frequent subtype 60-70%): a smooth, translucent, wax-like, 'PEARLY' OR 'OPALESCENT' PAPULE OR NODULE", "prominent, delicate, arborizing branching TELANGIECTASIAS (small dilated blood vessels) coursing distinctly across the lesion surface", "central depression with a rolled, raised, translucent 'RODENT' BORDER ('rolled pearly borders')", "frequent history of repeated bleeding, ulceration, crusting, and partial temporary healing ('the scab that bleeds when dried with towel and never fully heals')", "pigmented BCC variant: brown or black speckled melanin mimicking melanoma", "extremely low metastatic potential (< 0.1%), but highly invasive locally with capacity to destructively infiltrate skin, soft tissue, cartilage, and cranial bones"],
        "pertinent_negatives": ["pearly translucent border with arborizing vessels distinguishes BCC from flaky keratotic squamous cell carcinoma"],
        "content": "Malignant cutaneous neoplasm arising from basal cells of the follicular epithelium and interfollicular epidermis, driven by constitutive activation of the Hedgehog signaling pathway (PTCH1 loss-of-function mutation in Gorlin syndrome and sporadic cases). Diagnostic workup: Punch or shave skin biopsy showing peripheral palisading of basaloid cells with clefting artifact. Treatment: 1. Low-risk / Non-facial: Standard surgical excision with 4 mm margins, or electrodessication and curettage (ED&C); 2. High-Risk / Cosmetically Sensitive / Facial (H-zone: nose, eyelids, lips, ears): MOHS MICROGRAPHIC SURGERY (gold standard, achieving 99% cure rate with maximum tissue conservation); 3. Advanced unresectable/metastatic: Oral Hedgehog pathway inhibitors (Vismodegib, Sonidegib) or Cemiplimab (anti-PD-1)."
    },

    # --- 12. OPHTHALMOLOGY & ENT (16) ---
    {
        "id": "ICD10-H40.20",
        "topic": "Acute Angle-Closure Glaucoma (Steamy Cornea & Mid-Dilated Pupil)",
        "icd10": "H40.20",
        "specialty": "Ophthalmology / Emergency Medicine",
        "organ_system": "Ocular Emergency",
        "keywords": ["acute angle closure glaucoma", "aacg", "steamy cloudy cornea", "mid dilated fixed pupil", "halos around lights", "rock hard eye", "iop > 50", "laser peripheral iridotomy"],
        "red_flags": ["permanent optic nerve ischemia and irreversible blindness within hours", "severe headache and vomiting misdiagnosed as acute migraine or intracranial bleed"],
        "clinical_hallmarks": ["sudden onset of excruciating, agonizing, unilateral ocular and peri-orbital pain radiating to ipsilateral forehead and temple", "severe visual impairment: profound blurriness and PATHOGNOMONIC COLORED HALOS AROUND LIGHTS (rainbow rings around point sources of light due to corneal epithelial edema)", "PROFOUND SYSTEMIC SYMPTOMS: severe nausea, retching, vomiting, and diaphoresis (frequently leading to misdiagnosis as an acute abdominal emergency)", "triggered by pupillary dilation in dim lighting (movie theaters, evening dusk) or anticholinergic / sympathomimetic medications", "pathognomonic physical examination signs: 1. Conjunctival and ciliary injection ('ciliary flush'); 2. 'STEAMY' OR 'HAZY' CLOUDY CORNEA with loss of normal corneal luster; 3. MID-DILATED, VERTICALLY OVAL, SLUGGISH OR FIXED PUPIL (unresponsive to light); 4. Shallow anterior chamber depth; 5. Palpation of globe: 'ROCK-HARD' / STONY HARD EYEBALL compared to the normal contralateral eye", "tonometry hallmark: MASSIVELY ELEVATED INTRAOCULAR PRESSURE (IOP typically 50 to 80 mmHg, normal 10-21 mmHg)"],
        "pertinent_negatives": ["pupil is mid-dilated and unreactive (in sharp contrast to small constricted pupil of acute anterior uveitis)"],
        "content": "Ophthalmic emergency resulting from pupillary block preventing aqueous humor from draining through the trabecular meshwork, causing acute rise in posterior chamber pressure and anterior displacement of peripheral iris. Statutory emergency requiring immediate IOP reduction to prevent ischemic optic neuropathy. Protocol: 1. STAT Medical IOP Reduction (The Emergency Cocktail): Topical Beta-blocker (Timolol 0.5% 1 drop) + Topical Alpha-2 agonist (Apraclonidine 1% 1 drop) + IV Acetazolamide (500 mg IV STAT) + IV Mannitol (1-2 g/kg of 20% solution over 30 min for IOP > 50 mmHg); 2. Topical Pilocarpine 2% (parasympathomimetic miotic) instilled only when IOP drops < 40 mmHg (high IOP renders iris sphincter ischemic and unresponsive); 3. DEFINITIVE BILATERAL CURE: Nd:YAG Laser Peripheral Iridotomy (LPI) to BOTH eyes once cornea clears (prophylactic LPI to unaffected eye is mandatory due to high contralateral attack risk)."
    },
    {
        "id": "ICD10-H34.10",
        "topic": "Central Retinal Artery Occlusion (CRAO - Cherry-Red Spot)",
        "icd10": "H34.10",
        "specialty": "Ophthalmology / Neurology / Emergency Medicine",
        "organ_system": "Ocular Vascular Emergency",
        "keywords": ["central retinal artery occlusion", "crao", "cherry red spot macula", "painless sudden vision loss", "pale retina boxcarring", "ocular massage", "giant cell arteritis crao"],
        "red_flags": ["irreversible retinal ganglion cell necrosis within 90-100 minutes of ischemia", "concurrent Giant Cell Arteritis (urgent high-dose steroids needed)", "imminent embolic ischemic stroke"],
        "clinical_hallmarks": ["THE 'OCULAR STROKE': sudden, abrupt, catastrophic, painless, profound monocular visual loss (acuity typically drops to 'counting fingers' or 'light perception')", "occurs instantaneously over seconds, often noticed immediately upon waking up", "RAPID TESTING: Relative Afferent Pupillary Defect (RAPD / Marcus Gunn pupil) in affected eye", "DILATED FUNDOSCOPY (PATHOGNOMONIC HALLMARK): 1. Diffuse, pale, ground-glass, opaque, milky-white retina (due to acute intracellular edema of ischemic inner retinal layers); 2. PROMINENT 'CHERRY-RED SPOT' AT THE FOVEA (the fovea centralis is thinned with no inner retinal layers, allowing the underlying richly vascular, normal choroid to shine through brightly); 3. Attenuation and narrowing of retinal arterioles with segmented, fragmented blood column ('boxcarring' / cattle-trucking of blood flow)", "in 15-20% of patients with a patent cilioretinal artery (arising from ciliary circulation), central foveal island of vision is spared"],
        "pertinent_negatives": ["pain is completely absent (presence of pain suggests optic neuritis or orbital disease)"],
        "content": "Acute thrombotic or embolic occlusion of the central retinal artery (end-artery of ophthalmic artery supplying inner two-thirds of retina), predominantly originating from ipsilateral carotid artery atheroma or cardiac emboli (or Giant Cell Arteritis in elderly > 50 years). Considered an ischemic stroke equivalent. Urgent Empirical Measures (if presenting < 4-6 hours): 1. Immediate Ocular Massage (firm pressure for 10-15s followed by sudden release using three-mirror contact lens or thumb to dislodge embolus downstream); 2. Anterior Chamber Paracentesis to acutely drop IOP; 3. Sublingual Isosorbide dinitrate or paper-bag breathing (induces hypercapnic vasodilation); 4. Rule out GCA (STAT ESR and CRP; high-dose pulse steroids if GCA suspected); 5. Comprehensive stroke evaluation (Carotid duplex, Echocardiogram, telemetry, Brain MRI/DWI)."
    },
    {
        "id": "ICD10-H33.00",
        "topic": "Rhegmatogenous Retinal Detachment (Flashes, Floaters & Falling Curtain)",
        "icd10": "H33.00",
        "specialty": "Ophthalmology / Vitreoretinal Surgery",
        "organ_system": "Ocular Emergency",
        "keywords": ["retinal detachment", "rhegmatogenous retinal detachment", "flashes and floaters", "curtain falling over vision", "tobacco dust shafer sign", "vitreous hemorrhage", "pneumatic retinopexy scleral buckle"],
        "red_flags": ["macula-off detachment (severe permanent loss of central visual acuity if not repaired rapidly)", "total retinal detachment"],
        "clinical_hallmarks": ["THE CLASSIC PREMONITORY SEQUENCE: 1. Sudden shower of new black 'FLOATERS' (spots, cobwebs, or ring-like shadows floating across visual field, representing vitreous hemorrhage or condensations); 2. PHOTOPsia (recurrent, brief, bright flashes of light in peripheral vision, characteristically in the dark, provoked by eye movement due to vitreoretinal traction)", "THE PROGRESSIVE DEFECT: A dark, dense, opaque 'CURTAIN', 'SHADOW', OR 'VEIL' falling across or advancing from the periphery of the visual field into central vision", "visual acuity remains 20/20 if the macula is still attached ('macula-on'), but drops catastrophically to legal blindness if detachment advances across the fovea ('macula-off')", "Slit-lamp biomicroscopy: positive SHAFER'S SIGN ('TOBACCO DUST' - tiny brownish clumps of pigmented epithelial cells suspended in the anterior vitreous)", "Dilated Fundoscopy: elevated, corrugated, translucent, folded, greyish-white billowing retinal sheet with undulating movement on ocular motion, and an identifiable full-thickness retinal tear or horseshoe break"],
        "pertinent_negatives": ["no eye pain or external redness (painless internal neurosensory detachment)"],
        "content": "Separation of the neurosensory retina from the underlying retinal pigment epithelium (RPE) caused by liquefied vitreous passing through a full-thickness retinal tear/break into the subretinal space. Major risk factors: high myopia (nearsightedness), cataract surgery, lattice degeneration, ocular trauma. Time-sensitive Ophthalmic Emergency: A 'Macula-On' retinal detachment is a SURGICAL EMERGENCY that MUST BE REPAIRED EXPEDITIOUSLY (within 24 hours) to preserve central vision. Surgical Techniques: 1. Pneumatic Retinopexy (intravitreal gas bubble injection + cryopexy/laser for superior single tears); 2. Scleral Buckling (external silicone exoplant indenting sclera); 3. Pars Plana Vitrectomy (PPV) with endolaser and long-acting gas/silicone oil tamponade."
    },
    {
        "id": "ICD10-H16.00",
        "topic": "Bacterial Keratitis & Corneal Ulcer (Pseudomonas & Hypopyon)",
        "icd10": "H16.00",
        "specialty": "Ophthalmology / Cornea & External Disease",
        "organ_system": "Corneal Infectious Emergency",
        "keywords": ["bacterial keratitis", "corneal ulcer", "hypopyon anterior chamber", "contact lens corneal ulcer", "pseudomonas aeruginosa eye", "fluorescein staining corneal defect", "fortified antibiotic eye drops"],
        "red_flags": ["corneal melting / perforation (endophthalmitis)", "rapid progression within 24 hours (Pseudomonas)", "permanent corneal scarring and blindness"],
        "clinical_hallmarks": ["strongest risk factor: EXTENDED-WEAR SOFT CONTACT LENSES (sleeping in contacts, poor lens hygiene, cleaning lenses with tap water)", "severe, intense, foreign-body pain, copious purulent/mucopurulent discharge, extreme photophobia, and rapid visual drop", "Slit-lamp examination: circumcorneal ciliary injection ('red eye') and a DENSE, ROUND, FOCAL WHITE/YELLOWISH CORNEAL INFILTRATE (stromal opacity) with overlying epithelial defect", "fluorescein staining under cobalt blue light reveals an intensely bright green epithelial ulceration overlying the stromal infiltrate", "Pseudomonas aeruginosa keratitis: rapid, fulminant liquefactive necrosis of corneal stroma ('corneal melting') with thick, soupy, greenish-yellow mucopurulent discharge within 24-48 hours", "PATHOGNOMONIC INTRAOCULAR SIGN: HYPOPYON (a horizontal level of creamy white purulent exudate / sterile neutrophils settled at the bottom of the anterior chamber)"],
        "pertinent_negatives": ["TOPICAL CORTICOSTEROID DROPS ARE STRICTLY CONTRAINDICATED in acute undiagnosed corneal ulcer (potentiates fungal/bacterial replication and causes rapid corneal perforation)"],
        "content": "Invasive microbial infection of the corneal stroma with epithelial disruption. Common organisms: Pseudomonas aeruginosa (contact lenses), Staphylococcus aureus, Streptococcus pneumoniae. Statutory corneal emergency. Protocol: 1. STAT Emergency Corneal Scrapings for Gram stain, Giemsa, and bacterial/fungal culture on blood, chocolate, and Sabouraud agar; 2. EMPIRIC INTENSIVE ANTIMICROBIAL REGIMEN: Fortified Topicals (Fortified Tobramycin 1.4% or Amikacin + Fortified Cefazolin 5% or Vancomycin 5%) OR monotherapy with 4th-generation Fluoroquinolones (Moxifloxacin 0.5% or Gatifloxacin drops) INSTILLED EVERY 30-60 MINUTES AROUND THE CLOCK; 3. Cycloplegic drops (Homatropine 5%) for ciliary spasm pain; 4. Emergent therapeutic penetrating keratoplasty (corneal transplant) for impending perforation."
    },
    {
        "id": "ICD10-J36",
        "topic": "Peritonsillar Abscess (Quinsy - Trismus & Uvular Deviation)",
        "icd10": "J36",
        "specialty": "ENT / Otorhinolaryngology / Emergency Medicine",
        "organ_system": "Upper Airway Infectious Emergency",
        "keywords": ["peritonsillar abscess", "quinsy", "trismus hot potato voice", "uvula deviated contralateral", "asymmetrical soft palate bulge", "needle aspiration quinsy", "drooling severe sore throat"],
        "red_flags": ["parapharyngeal / retropharyngeal space abscess spread", "internal carotid artery erosion / rupture", "acute upper airway compromise"],
        "clinical_hallmarks": ["history of acute tonsillitis that progressively worsens into SEVERE, AGONIZING, UNILATERAL THROAT PAIN radiating to the ipsilateral ear (referred otalgia via glossopharyngeal nerve CN IX)", "CARDINAL CLINICAL TRIAD: 1. TRISMUS (severe limitation of mouth opening [< 2 finger-breadths] caused by inflammation and spasm of internal pterygoid muscle); 2. 'HOT-POTATO VOICE' (thick, muffled, guttural, dysphoric speech as if speaking with a hot potato in mouth); 3. Severe odynophagia with DROOLING / INABILITY TO SWALLOW SALIVA", "physical examination (gentle tongue depression without gagging): MARKED ASYMMETRICAL SWELLING OF THE SOFT PALATE AND ANTERIOR TONSILLAR PILLAR pushing the affected tonsil inferiorly and medially towards the midline", "PATHOGNOMONIC PHYSICAL SIGN: THE UVULA IS EDEMATOUS, DEVIATED AND DISPLACED TO THE OPPOSITE (CONTRALATERAL) SIDE", "tender, enlarged ipsilateral jugulodigastric lymphadenopathy and fever"],
        "pertinent_negatives": ["bilateral tonsillar enlargement without palate bulge indicates simple tonsillitis, NOT quinsy"],
        "content": "Suppurative collection of purulent material within the potential space between the tonsillar fibrous capsule and the superior pharyngeal constrictor muscle. Polymicrobial infection (Streptococcus pyogenes, Fusobacterium necrophorum, anaerobes). Protocol: 1. STAT Drainage: Bedside Needle Aspiration (18-20G needle with sheath trimmed to 1-1.5 cm to prevent carotid puncture) OR Incision and Drainage (I&D) with scalpel at point of maximum fluctuance (provides instant pain and trismus relief); 2. IV Antibiotic Therapy: IV Ampicillin-Sulbactam (3g q6h) OR Ceftriaxone + Metronidazole (or Clindamycin); 3. Single-dose IV Dexamethasone (10 mg) to rapidly reduce airway edema; 4. Elective interval tonsillectomy for recurrent quinsy."
    },
    {
        "id": "ICD10-J05.10",
        "topic": "Acute Epiglottitis (Supraglottitis & The Tripod Position)",
        "icd10": "J05.10",
        "specialty": "ENT / Pediatrics / Emergency Medicine / Critical Care",
        "organ_system": "Pediatric Airway Emergency",
        "keywords": ["acute epiglottitis", "epiglottitis", "tripod position sniffing position", "thumbprint sign on lateral x-ray", "stridor drooling dysphagia dysphonia", "cherry red swollen epiglottis", "haemophilus influenzae b"],
        "red_flags": ["sudden total airway occlusion / asphyxiation", "cardiac arrest provoked by oral tongue blade examination", "cyanosis and exhaustion"],
        "clinical_hallmarks": ["rapidly progressive, life-threatening inflammation of the epiglottis and supraglottic structures, historically caused by Haemophilus influenzae type b (Hib - now also Strep pneumoniae, Group A Strep in vaccinated era)", "CARDINAL '4 Ds' SYMPTOM COMPLEX: 1. DROOLING (inability to swallow saliva due to agonizing throat pain); 2. DYSPHAGIA (severe difficulty swallowing); 3. DYSPHONIA (muffled, whispery 'hot-potato' voice); 4. DISTRESS (respiratory agitation and air hunger)", "PATHOGNOMONIC POSTURE: THE 'TRIPOD POSITION' (child sits upright, leaning forward, supported by outstretched hands on knees, with neck hyperextended and chin thrust forward ['sniffing dog position'] to maximize airway diameter)", "inspiratory stridor, tachypnea, and supraclavicular / intercostal retractions", "soft tissue lateral neck radiograph: PATHOGNOMONIC 'THUMBPRINT SIGN' (thick, rounded, swollen epiglottis projecting into hypopharynx like an adult thumb, with obliteration of the vallecula)"],
        "pertinent_negatives": ["DO NOT EXAMINE PHARYNX WITH TONGUE BLADE OR AGITATE CHILD (crying, agitation, or tongue depression can trigger fatal acute reflex laryngospasm and immediate complete airway arrest)"],
        "content": "Life-threatening pediatric and adult supraglottic airway emergency. Absolute Clinical Rule: Keep child calm in parent's arms, provide humidified blow-by oxygen, NO IV lines, NO oral exam until in Operating Room. STAT Protocol: 1. STAT Transfer to Operating Room with Senior Anesthesiologist and ENT Surgeon present; 2. Endotracheal Intubation under inhalation general anesthesia with one size smaller ETT; direct laryngoscopy reveals swollen, edematous, fiery 'CHERRY-RED EPIGLOTTIS'; 3. Emergent surgical cricothyroidotomy equipment open on stand; 4. IV Antibiotics: IV Ceftriaxone (50-100 mg/kg/day) + Vancomycin for 7-10 days; 5. Extubation after 48-72 hours when leak test positive."
    },
    {
        "id": "ICD10-K12.2",
        "topic": "Ludwig's Angina (Submandibular Space & Woody Floor of Mouth)",
        "icd10": "K12.2",
        "specialty": "ENT / Oral & Maxillofacial Surgery / Emergency Medicine",
        "organ_system": "Deep Neck Airway Emergency",
        "keywords": ["ludwigs angina", "submandibular cellulitis", "woody hard floor of mouth", "elevated tongue airway obstruction", "bull neck dental abscess", "lower molar odontogenic infection"],
        "red_flags": ["posterior tongue displacement causing acute asphyxiation", "descending necrotizing mediastinitis", "septic shock"],
        "clinical_hallmarks": ["severe, rapidly spreading, potentially fatal cellulitis / phlegmon of the submandibular, sublingual, and submental spaces BILATERALLY, without frank abscess formation in early stages", "overwhelmingly originates (> 85-90%) from an ODONTOGENIC INFECTION of the lower 2nd or 3rd mandibular molar teeth whose roots extend below the mylohyoid ridge into the submandibular space", "CARDINAL PHYSICAL EXAMINATION SIGNS: 1. Bilateral, diffuse, firm, brawny, NON-FLUCTUANT, 'WOODY' OR 'BOARD-LIKE' INDURATION of the submandibular and submental regions ('bull-neck' appearance); 2. Tense, firm, exquisitely tender elevation of the floor of the mouth; 3. THE TONGUE IS ELEVATED AND RETRO-DISPLACED POSTERIORLY AGAINST THE HARD AND SOFT PALATE, threatening instant airway occlusion", "trismus, severe drooling, muffled voice, fever, and forward head tilting", "Contrast CT of neck and soft tissues: diffuse soft tissue swelling, fascial thickening, gas bubbles, and loss of fat planes in submandibular/sublingual compartments"],
        "pertinent_negatives": ["absence of initial fluctuance (it is an aggressive cellulitis/phlegmon, not a localized superficial abscess)"],
        "content": "Rapidly spreading gangrenous cellulitis of submandibular space. Primary Cause of Death: Acute Upper Airway Asphyxiation. Immediate Emergency Protocol: 1. SECURE THE AIRWAY FIRST: Awake Fiberoptic Nasotracheal Intubation OR Awake Tracheostomy (blind oral intubation is strictly contraindicated due to distorted anatomy and risk of laryngospasm); 2. STAT High-Dose IV Broad-Spectrum Triple Antibiotics (IV Ampicillin-Sulbactam 3g q6h OR Meropenem + Vancomycin); 3. STAT Surgical Decompression: Wide, horizontal transverse cervical incision through platysma with division of mylohyoid muscle to decompress fascial spaces; 4. Extraction of the offending lower molar tooth."
    },
    {
        "id": "ICD10-H70.00",
        "topic": "Acute Mastoiditis (Postauricular Fluctuance & Ear Protrusion)",
        "icd10": "H70.00",
        "specialty": "ENT / Pediatrics / Emergency Medicine",
        "organ_system": "Temporal Bone Infectious Emergency",
        "keywords": ["acute mastoiditis", "protruding ear auricle", "postauricular swelling erythema", "mastoid tenderness", "complication of acute otitis media", "bezold abscess", "high resolution ct temporal bone"],
        "red_flags": ["intracranial extension: Sigmoid Sinus Thrombosis, epidural abscess, meningitis", "Bezold's abscess (pus tracking down into sternocleidomastoid sheath)", "facial nerve paralysis (CN VII palsy)"],
        "clinical_hallmarks": ["develops as a direct complication of untreated or inadequately treated ACUTE OTITIS MEDIA (AOM), most commonly in children < 2 years", "persistent or recrudescent high fever, otalgia, irritability, and creamy profuse purulent otorrhea", "CARDINAL PHYSICAL SIGNS: 1. POSTAURICULAR ERYTHEMA, TENDER EDEMA, AND FLUCTUATION directly overlying the mastoid process; 2. Loss of the normal postauricular sulcus; 3. FORWARD AND DOWNWARD PROTRUSION / DISPLACEMENT OF THE AURICLE (the ear pinna is visibly pushed forward and outward away from head)", "otoscopy: fiery red, bulging, opaque, or perforated tympanic membrane, accompanied by sagging / drooping of the posterosuperior external auditory canal wall", "High-Resolution CT (HRCT) of temporal bone (gold standard): clouding/opacification of mastoid air cells with PATHOGNOMONIC LOSS OF MASTOID BONY SEPTA (coalescent mastoiditis)"],
        "pertinent_negatives": ["bony septal breakdown on CT distinguishes true coalescent mastoiditis from simple serous opacification of mastoid in AOM"],
        "content": "Suppurative infection of the mastoid air cells with osteitis and progressive resorption of the bony trabeculae (coalescence). Predominant pathogens: Streptococcus pneumoniae, Streptococcus pyogenes, Pseudomonas aeruginosa. Diagnostic workup: HRCT temporal bone with contrast, middle ear fluid culture. Protocol: 1. Hospital admission and STAT IV Antibiotics: IV Ceftriaxone (50-100 mg/kg/day) + Vancomycin; 2. STAT Myringotomy / Tympanocentesis (+/- tympanostomy tube placement) to decompress the middle ear and obtain culture; 3. STAT Cortical Mastoidectomy (Schwartze operation) indicated if no improvement within 24-48 hours, or if subperiosteal abscess, intracranial complications, or coalescent bone erosion are present."
    },
    {
        "id": "ICD10-R04.0",
        "topic": "Epistaxis (Kiesselbach's Little's Area vs Woodruff's Posterior)",
        "icd10": "R04.0",
        "specialty": "ENT / Emergency Medicine",
        "organ_system": "Rhinologic Bleeding",
        "keywords": ["epistaxis", "nosebleed", "kiesselbachs plexus littles area", "woodruffs posterior plexus", "anterior nasal packing", "sphenopalatine artery ligation", "silver nitrate cautery"],
        "red_flags": ["posterior epistaxis with torrential bleeding down posterior pharynx", "hypovolemic shock in elderly hypertensive patient", "aspirin / anticoagulant coagulopathy"],
        "clinical_hallmarks": ["ANATOMICAL AND CLINICAL DIFFERENTIATION OF EPISTAXIS:", "1. Anterior Epistaxis (> 90% of cases): bleeding originates from KIESSELBACH'S PLEXUS IN LITTLE'S AREA on the anterior nasal septum (anastomosis of 5 arteries: Anterior ethmoidal, Posterior ethmoidal, Sphenopalatine, Greater palatine, and Superior labial arteries); typically unilateral, low-rate bleeding seen dripping from anterior nares, triggered by digital trauma (nose-picking), dry air, or allergic rhinitis; easily controlled with direct pressure", "2. Posterior Epistaxis (5-10% of cases): bleeding originates from WOODRUFF'S PLEXUS or the Sphenopalatine Artery branch located in posterior nasal cavity; predominantly occurs in ELDERLY, HYPERTENSIVE PATIENTS with atherosclerosis; profuse, high-volume bleeding flowing simultaneously from BOTH NARES AND DOWN THE POSTERIOR OROPHARYNX into throat (seen pooling on tongue depressor exam); resistant to anterior pressure"],
        "pertinent_negatives": ["absence of bleeding on direct anterior septal visualization indicates posterior origin"],
        "content": "Hemorrhage from the nasal cavity. Stepwise Treatment Algorithm: 1. First-line (Trotter method): Patient sits upright, leans forward (prevents blood swallowing), firm continuous manual pinching of the soft lower cartilaginous nose for 10-15 minutes; 2. Topical Vasoconstrictor: Oxymetazoline 0.05% or Phenylephrine spray on cotton pledget; 3. Silver Nitrate Chemical Cautery (apply directly to bleeding vessel on Little's area - NEVER cauterize both sides of septum simultaneously to avoid septal perforation); 4. Anterior Nasal Packing (Merocel nasal tampon or Rapid Rhino pack lubricated with water/saline for 48-72 hours); 5. Posterior Epistaxis: Double-balloon catheter (epistaxis catheter) or Foley catheter tamponade + mandatory ICU admission with pulse oximetry (nasopulmonary reflex risk); 6. Endoscopic Sphenopalatine Artery (SPA) Ligation or embolization for intractable posterior bleeds."
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
            
    print(f"Batch 4C added {added} protocols. Total: {len(existing)}")
    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run()

"""
Kaggle Disease Precautions and Clinical Home-Care Guidance Dataset
Consolidated from Kaggle Disease-Symptom-Precaution datasets, WHO guidelines, and clinical standard operating procedures.
Provides 4 actionable, evidence-based precautions and safety steps per condition.
"""

from typing import Dict, List, Optional

DISEASE_PRECAUTIONS: Dict[str, List[str]] = {
    # --- Tropical & Infectious Diseases (Kaggle & Indian Subcontinent) ---
    "malaria": [
        "Consult nearest hospital immediately for blood smear / rapid antigen test (RDT)",
        "Avoid mosquito bites using DEET repellents, mosquito nets, and full-sleeved clothing",
        "Keep well hydrated with clean fluids, ORS, and warm soups",
        "Do not delay prescribed antimalarial medication (ACT/Chloroquine as directed by doctor)"
    ],
    "dengue": [
        "Drink plenty of oral fluids (ORS, coconut water, lemon water) to maintain hydration",
        "STRICT WARNING: Avoid Aspirin, Ibuprofen, and Diclofenac as they severely increase bleeding risk; take Paracetamol only",
        "Monitor for critical warning signs: persistent vomiting, nose/gum bleeding, severe abdominal pain, sudden extreme weakness",
        "Get serial Complete Blood Count (CBC) every 24 hours to monitor platelet levels and hematocrit"
    ],
    "typhoid": [
        "Eat thoroughly cooked, warm, soft bland food; strictly avoid raw vegetables, street food, and unpasteurized milk",
        "Drink only boiled, filtered, or sealed bottled water",
        "Practice rigorous hand hygiene with soap and water before meals and after using the restroom",
        "Complete the full 7-14 day course of prescribed antibiotics even if fever resolves early"
    ],
    "chikungunya": [
        "Take prescribed paracetamol and supportive pain relief; avoid NSAIDs until dengue is excluded",
        "Apply cold compresses or gentle ice packs to inflamed, agonizing joints",
        "Rest completely during the acute febrile phase; avoid strenuous weight-bearing",
        "Use mosquito repellent and eliminate standing water around living quarters"
    ],
    "acute gastroenteritis & foodborne enteritis": [
        "Begin immediate Oral Rehydration Therapy (ORS) after each loose stool to prevent dehydration",
        "Follow a bland BRAT diet (Bananas, Rice, Applesauce, Toast/Khichdi); avoid dairy, caffeine, and greasy spices",
        "Wash hands thoroughly with soap for at least 20 seconds before eating and after toilet use",
        "Seek immediate emergency care if stools contain blood, vomiting prevents all fluid intake, or urine output stops"
    ],
    "cholera": [
        "Immediate aggressive Oral Rehydration Solution (ORS) intake is life-saving; consume 1 glass per watery stool",
        "Rush to emergency department or primary health center immediately for IV fluid evaluation",
        "Strictly boil drinking water and avoid raw or partially cooked seafood and street food",
        "Isolate eating utensils and disinfect living areas with chlorinated solutions"
    ],
    "tuberculosis": [
        "Adhere strictly to daily DOTS / anti-tubercular medication without missing a single dose",
        "Cover mouth and nose with a mask or tissue when coughing or sneezing; ensure good room cross-ventilation",
        "Maintain a high-protein, nutrient-dense diet (eggs, lentils, milk, nuts) to accelerate tissue recovery",
        "Report severe side effects like yellowing of eyes (jaundice), persistent vomiting, or visual changes to doctor STAT"
    ],
    "common cold / acute viral nasopharyngitis": [
        "Rest adequately and drink warm fluids like herbal tea, ginger tea, and warm broths",
        "Perform saline steam inhalation and warm saline gargles 2-3 times daily to relieve congestion and sore throat",
        "Avoid unnecessary antibiotics; viral colds resolve spontaneously within 7-10 days",
        "Wash hands frequently and use tissues to prevent spreading infection to family members"
    ],
    "community-acquired pneumonia": [
        "Take all prescribed antibiotics or antivirals exactly on schedule until finished",
        "Monitor blood oxygen saturation (SpO2) using a pulse oximeter; seek emergency care if SpO2 drops below 94%",
        "Stay in semi-upright resting posture to assist diaphragmatic expansion and lung aeration",
        "Seek immediate ER help if high fever persists, breathing becomes rapid/shallow, or confusion develops"
    ],
    "covid-19 / sars-cov-2": [
        "Isolate in a well-ventilated private room and wear an N95 mask when around household members",
        "Monitor pulse oximetry (SpO2) and temperature 3 times daily; alert physician if SpO2 < 94%",
        "Stay hydrated and take paracetamol for fever; avoid self-administering steroids without doctor guidance",
        "Seek immediate medical help if experiencing difficulty breathing, persistent chest tightness, or blue lips"
    ],

    # --- Cardiovascular & Vascular Conditions ---
    "acute coronary syndrome": [
        "EMERGENCY: Call 108 immediately or transfer to nearest cardiac catheterization / emergency hospital",
        "Chew an unbuffered Aspirin 300 mg STAT if advised by emergency dispatcher and not allergic",
        "Stop all physical exertion immediately; sit or recline in comfortable resting position with loosened clothing",
        "Do not drive yourself to hospital; wait for paramedics with oxygen and cardiac monitoring"
    ],
    "hypertension": [
        "Take prescribed anti-hypertensive medications daily at the same time without skipping",
        "Adopt the DASH diet: restrict daily dietary sodium intake to under 2 grams (avoid papad, pickles, processed snacks)",
        "Engage in 30 minutes of moderate aerobic exercise (brisk walking) 5 days a week",
        "Measure and log blood pressure readings at home; seek urgent care if BP exceeds 180/120 mmHg"
    ],
    "heart failure": [
        "Weigh yourself every morning after urination; notify doctor if weight increases by > 1.5 kg in 2 days",
        "Strictly limit daily fluid intake to 1.5-2 liters and adhere to low-sodium diet (< 1.5g sodium/day)",
        "Take diuretic medications in the morning to avoid nighttime sleep disruption from urination",
        "Seek immediate emergency care if experiencing waking breathlessness (PND) or inability to lie flat"
    ],

    # --- Gastrointestinal & Hepatobiliary ---
    "gastroesophageal reflux disease (gerd)": [
        "Avoid lying down for at least 2-3 hours following meals; elevate head of bed by 6 inches",
        "Eliminate known dietary triggers: fried/spicy foods, citrus, chocolate, caffeine, and carbonated beverages",
        "Eat smaller, more frequent meals rather than large heavy dinners; avoid late-night snacking",
        "Avoid tight abdominal garments and maintain healthy body weight to reduce intra-abdominal pressure"
    ],
    "peptic ulcer disease": [
        "Strictly avoid NSAID painkillers (Aspirin, Ibuprofen, Diclofenac) as they erode gastric mucosa; discuss safe alternatives",
        "Avoid smoking and alcohol consumption, which impair gastric mucosal blood flow and healing",
        "Eat regular, balanced meals and avoid skipping food; take prescribed proton pump inhibitors before breakfast",
        "RUSH TO ER if you develop black tarry stools (melena), vomit dark coffee-ground material, or have sudden severe abdominal pain"
    ],
    "acute appendicitis": [
        "SURGICAL EMERGENCY: Do NOT eat or drink anything (remain strict nil-by-mouth / NPO) for imminent surgery",
        "Do NOT apply heat packs or hot water bottles to abdomen as it accelerates appendiceal rupture",
        "Do NOT take laxatives, painkiller injections, or enemas before surgical evaluation",
        "Transfer immediately to emergency surgical triage unit for bedside ultrasound and surgeon consultation"
    ],
    "acute cholecystitis": [
        "Abstain from heavy, greasy, fried, or high-fat meals which trigger acute gallbladder contractions",
        "Remain fasting / liquid diet while awaiting ultrasound scan and surgical evaluation",
        "Take prescribed antispasmodics and analgesics as advised by attending clinician",
        "Report to hospital immediately if fever spikes, jaundice (yellowing of skin/eyes) appears, or pain becomes unrelenting"
    ],
    "acute viral hepatitis": [
        "Strict complete physical rest; avoid all strenuous exercise until transaminases normalize",
        "STRICT CONTRAINDICATION: Absolute zero alcohol consumption and complete avoidance of hepatotoxic drugs (including unnecessary paracetamol)",
        "Consume small, high-carbohydrate, easily digestible meals (sugarcane juice, glucose, fruits, khichdi)",
        "Seek immediate emergency care if experiencing confusion, drowsiness, bleeding, or flapping tremors (asterixis)"
    ],

    # --- Endocrine & Metabolic ---
    "type 2 diabetes mellitus": [
        "Monitor fasting and post-prandial blood glucose levels regularly with home glucometer",
        "Follow a low-glycemic index carbohydrate diet rich in leafy vegetables, whole grains, and lean proteins",
        "Inspect feet daily for cuts, blisters, redness, or ulcers; wear comfortable, protective footwear",
        "Keep fast-acting glucose tablets or fruit juice readily available for immediate treatment of hypoglycemia"
    ],
    "hypoglycemia": [
        "Follow the 'Rule of 15': Consume 15 grams of fast-acting sugar (3-4 glucose tablets, 1/2 cup fruit juice, or 1 tbsp sugar) STAT",
        "Recheck blood sugar in 15 minutes; repeat 15g sugar if reading remains below 70 mg/dL",
        "Once sugar is above 70 mg/dL, eat a small snack with complex carbs and protein (e.g. roti or crackers with cheese)",
        "If patient is drowsy, confused, or seizing, do NOT feed orally; administer glucagon or call 108 emergency immediately"
    ],
    "hypothyroidism": [
        "Take levothyroxine hormone tablet first thing in morning on an empty stomach with a full glass of water",
        "Wait at least 30-60 minutes before consuming tea, coffee, breakfast, or calcium/iron supplements",
        "Check serum TSH levels every 6-8 weeks until dosage is stabilized, then every 6-12 months",
        "Do not abruptly stop medication even if feeling energetic; hypothyroidism requires lifelong management"
    ],

    # --- Respiratory & Allergy ---
    "bronchial asthma": [
        "Always carry fast-acting rescue inhaler (Salbutamol) wherever you go; use 2 puffs immediately upon wheezing",
        "Identify and minimize exposure to known triggers: dust mites, pet dander, tobacco smoke, cold air, strong perfumes",
        "Use prescribed daily corticosteroid preventer inhaler consistently, even when breathing feels normal",
        "Seek emergency hospital care if rescue inhaler gives no relief after 15 minutes or difficulty speaking in full sentences occurs"
    ],
    "allergic rhinitis": [
        "Keep bedroom windows closed during peak pollen hours and wash bedding weekly in hot water (> 60°C)",
        "Use daily saline nasal rinses (neti pot or saline spray) to physically clear nasal allergens and mucus",
        "Take non-sedating antihistamines or prescribed steroid nasal spray as directed by ENT doctor",
        "Avoid sweeping dust; use damp cloth dusting and consider HEPA air filtration in sleeping quarters"
    ],

    # --- Neurology & Psychiatric ---
    "migraine": [
        "Rest in a quiet, dark, well-ventilated room at the earliest onset of headache aura or pain",
        "Take prescribed abortive migraine medication (triptan or NSAID) at the very start of the headache phase",
        "Maintain regular sleep cycles, stay well-hydrated, and avoid skipping meals",
        "Keep a headache diary to identify individual dietary triggers (e.g. aged cheese, MSG, skipped sleep, caffeine fluctuations)"
    ],
    "acute ischemic stroke": [
        "CRITICAL TIME-SENSITIVE EMERGENCY (Code FAST): Call 108 immediately; brain cells die every second",
        "Do NOT give patient anything to eat, drink, or swallow (including Aspirin or water) due to severe aspiration risk",
        "Note the EXACT time the patient was last seen normal (crucial for 4.5-hour IV thrombolysis window)",
        "Keep patient lying flat on side (recovery position) if vomiting or unconscious"
    ],

    # --- Renal & Urological ---
    "urinary tract infection (uti)": [
        "Drink at least 2.5 to 3 liters of water daily to continually flush bacteria from the urinary tract",
        "Complete the full course of prescribed antibiotics even if burning and dysuria disappear within 48 hours",
        "Wipe from front to back after urinating to prevent migration of rectal bacteria to urethra",
        "Seek urgent medical evaluation if fever, chills, vomiting, or severe lower back/flank pain develops (pyelonephritis)"
    ],
    "nephrolithiasis / renal calculus (kidney stone)": [
        "Increase fluid intake to 3 liters/day, ensuring clear or pale-straw colored urine throughout day and night",
        "Limit dietary sodium and animal protein intake; avoid high-oxalate foods (spinach, beetroot, nuts) if calcium-oxalate stones",
        "Strain urine with a fine mesh to catch any passed stone fragments for laboratory chemical analysis",
        "Seek emergency hospital care if experiencing uncontrollable pain, high fever with chills, or inability to pass urine"
    ],

    # --- Musculoskeletal & Orthopedic ---
    "osteoarthritis": [
        "Engage in low-impact joint-friendly physical activity: swimming, cycling, or water aerobics 3-4 times weekly",
        "Maintain healthy body weight; every 1 kg lost removes 4 kg of mechanical pressure from knee joints",
        "Use supportive footwear with cushioned soles; use a walking cane in opposite hand if knees are painful",
        "Apply warm heat packs before activity to ease stiffness, and cold packs after activity to reduce joint swelling"
    ],
    "gout": [
        "Strictly limit purine-rich foods: red meat, organ meats, shellfish, beer, and high-fructose corn syrup",
        "Drink 2.5-3 liters of water daily to promote renal uric acid excretion and prevent crystal precipitation",
        "Rest and elevate the affected inflamed joint; apply cold ice packs wrapped in a towel for 20 minutes",
        "Continue prescribed uric-acid lowering medication (allopurinol/febuxostat) as directed; avoid changing doses during acute flare"
    ],

    # --- Dermatology ---
    "urticaria / acute allergic rash": [
        "Take non-drowsy oral antihistamines as prescribed to block histamine release and alleviate intense pruritus",
        "Apply cool compresses or calamine lotion to soothe skin; avoid hot showers and tight scratchy clothing",
        "Avoid scratching the wheals to prevent secondary bacterial skin infections (excoriation)",
        "EMERGENCY RED FLAG: If lip swelling, tongue swelling, difficulty breathing, or throat tightness occurs, call 108 immediately (Anaphylaxis)"
    ],
    "tinea / fungal skin infection": [
        "Keep affected skin areas (groin, feet, armpits) strictly clean, dry, and aerated; change socks/underwear twice daily",
        "Apply prescribed antifungal cream 2 cm beyond visible rash border; continue for 1-2 weeks AFTER rash clears",
        "Do NOT use over-the-counter steroid-combination creams (Betnovate/Quadriderm) which worsen fungal proliferation",
        "Do not share personal towels, bedsheets, or footwear with other household members"
    ]
}


def get_precautions_for_condition(condition_name: str, triage_level: Optional[str] = None) -> List[str]:
    """
    Returns 4 structured clinical precautions and home-care steps tailored to the condition.
    Falls back gracefully to evidence-based category precautions if exact match is not found.
    """
    if not condition_name:
        return _generic_precautions(triage_level)

    c_lower = condition_name.lower().strip()

    # 1. Exact or partial keyword match against verified Kaggle / clinical database
    for key, precautions in DISEASE_PRECAUTIONS.items():
        if key in c_lower or any(word in c_lower for word in key.split() if len(word) > 4):
            return precautions

    # 2. Specialty / Symptom cluster category fallbacks
    if any(w in c_lower for w in ["fever", "pyrexia", "infection", "septic"]):
        return [
            "Monitor body temperature every 4 hours and maintain a written temperature log for the doctor",
            "Maintain high fluid intake (water, ORS, broths) to prevent dehydration caused by high fever",
            "Rest completely in a cool, well-ventilated room; sponge with lukewarm water if fever exceeds 102°F",
            "Seek emergency hospital care if fever is accompanied by stiff neck, confusion, petechial rash, or breathing distress"
        ]
    elif any(w in c_lower for w in ["chest", "cardiac", "heart", "angina"]):
        return [
            "Cease all physical exertion and rest in a comfortable seated position with support",
            "Avoid heavy meals, extreme cold exposure, and emotional stress while awaiting cardiac evaluation",
            "Have someone stay with you; keep emergency hospital contact (+91 94509 47933 / 108) ready",
            "RUSH TO ER immediately if chest discomfort radiates to jaw/arm, or is accompanied by cold sweating, nausea, or fainting"
        ]
    elif any(w in c_lower for w in ["abdominal", "stomach", "pain", "gut", "belly"]):
        return [
            "Stick to small sips of clear fluids and plain bland diet (khichdi, curd-rice, toast); avoid spices and oils",
            "Do NOT take strong unprescribed painkillers or laxatives which can mask acute surgical conditions",
            "Apply gentle warmth to abdomen if cramping, but avoid heat if appendicitis is suspected",
            "Seek urgent emergency care if pain becomes severe, abdomen becomes hard/board-like, or vomiting blood occurs"
        ]
    elif any(w in c_lower for w in ["respiratory", "cough", "lung", "bronch", "breath"]):
        return [
            "Rest in an elevated upright position with pillows to maximize lung aeration and ease breathing",
            "Perform steam inhalation twice daily and drink warm water to help loosen respiratory secretions",
            "Avoid exposure to tobacco smoke, air pollution, dust, and sudden cold air draughts",
            "Seek immediate emergency care if breathing becomes labored, lips turn bluish, or oxygen saturation falls below 94%"
        ]

    return _generic_precautions(triage_level)


def _generic_precautions(triage_level: Optional[str] = None) -> List[str]:
    if triage_level == "EMERGENCY_RED":
        return [
            "EMERGENCY: Call 108 immediately or transfer patient to the nearest emergency department without delay",
            "Keep patient in comfortable supported resting posture; monitor airway, breathing, and responsiveness continuously",
            "Do not give food, water, or oral medications until emergency physician has evaluated the patient",
            "Bring all existing medication packets, prescription slips, and recent lab reports to the hospital"
        ]
    elif triage_level == "URGENT_YELLOW":
        return [
            "Visit the hospital OPD or urgent consultation desk within the next 2 to 4 hours",
            "Rest completely and avoid strenuous physical exertion until evaluated by physician",
            "Maintain hydration with clean fluids and keep a log of changing symptoms",
            "Go to the emergency department immediately if symptoms worsen abruptly or red flags appear"
        ]
    return [
        "Schedule an outpatient OPD appointment with the recommended specialist at your earliest convenience",
        "Get adequate rest, maintain healthy hydration, and eat a clean, balanced diet",
        "Keep a daily log of symptoms, onset, and triggers to share with your attending physician",
        "Seek prompt medical attention if condition worsens, new symptoms arise, or fever develops"
    ]

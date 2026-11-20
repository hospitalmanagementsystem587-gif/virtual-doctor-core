import pytest
from app.schemas.encounter import SymptomEncounterInput, PatientProfile, TriageLevel
from app.rules.red_flags import RedFlagRuleEngine

def test_english_red_flag_chest_pain():
    p = PatientProfile(age=45, gender="male")
    enc = SymptomEncounterInput(patient=p, chief_complaint="Crushing chest pain radiating to left arm")
    is_crit, alert, level = RedFlagRuleEngine.evaluate(enc)
    assert is_crit is True
    assert level == TriageLevel.EMERGENCY_RED

def test_hinglish_red_flag_chest_pain():
    p = PatientProfile(age=45, gender="male")
    enc = SymptomEncounterInput(patient=p, chief_complaint="Seene me tez dard aur paseena aa raha hai")
    is_crit, alert, level = RedFlagRuleEngine.evaluate(enc)
    assert is_crit is True
    assert level == TriageLevel.EMERGENCY_RED

def test_hindi_red_flag_chest_pain():
    p = PatientProfile(age=50, gender="female")
    enc = SymptomEncounterInput(patient=p, chief_complaint="सीने में बहुत तेज़ दर्द और भारीपन है")
    is_crit, alert, level = RedFlagRuleEngine.evaluate(enc)
    assert is_crit is True
    assert level == TriageLevel.EMERGENCY_RED

def test_hinglish_red_flag_stroke():
    p = PatientProfile(age=62, gender="female")
    enc = SymptomEncounterInput(patient=p, chief_complaint="Achanak muh tedha ho gaya aur bolne me dikkat hai")
    is_crit, alert, level = RedFlagRuleEngine.evaluate(enc)
    assert is_crit is True
    assert level == TriageLevel.EMERGENCY_RED

def test_hindi_red_flag_hemorrhage():
    p = PatientProfile(age=35, gender="male")
    enc = SymptomEncounterInput(patient=p, chief_complaint="अचानक खून की उल्टी हुई है")
    is_crit, alert, level = RedFlagRuleEngine.evaluate(enc)
    assert is_crit is True
    assert level == TriageLevel.EMERGENCY_RED

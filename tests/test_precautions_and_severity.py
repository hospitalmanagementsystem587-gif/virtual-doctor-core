"""
Unit tests for Kaggle Precautions dataset integration and Symptom Severity Scorer.
"""

import pytest
from app.data.disease_precautions import get_precautions_for_condition, DISEASE_PRECAUTIONS
from app.services.severity_scorer import SymptomSeverityScorer


def test_precautions_known_diseases():
    # Malaria precautions
    p_malaria = get_precautions_for_condition("Malaria (Plasmodium Vivax)")
    assert len(p_malaria) == 4
    assert any("mosquito" in p.lower() for p in p_malaria)

    # Dengue precautions - verify critical aspirin/ibuprofen avoidance warning
    p_dengue = get_precautions_for_condition("Dengue Fever with Warning Signs")
    assert len(p_dengue) == 4
    assert any("aspirin" in p.lower() and "bleeding" in p.lower() for p in p_dengue)

    # Typhoid precautions - verify boiled water & diet
    p_typhoid = get_precautions_for_condition("Enteric (Typhoid) Fever")
    assert len(p_typhoid) == 4
    assert any("boiled" in p.lower() or "cooked" in p.lower() for p in p_typhoid)


def test_precautions_fallbacks():
    # Emergency fallback
    p_emerg = get_precautions_for_condition("", "EMERGENCY_RED")
    assert len(p_emerg) == 4
    assert any("108" in p for p in p_emerg)

    # Category fallback (cardiac)
    p_cardiac = get_precautions_for_condition("Unspecified chest tightness and palpitations")
    assert len(p_cardiac) == 4
    assert any("cardiac" in p.lower() or "chest" in p.lower() for p in p_cardiac)


def test_severity_scorer_english():
    # High-acuity cardiac presentation
    res = SymptomSeverityScorer.evaluate("I have severe crushing chest pain and breathlessness")
    assert res["score"] >= 8
    assert res["max_weight"] == 7
    assert res["high_acuity_detected"] is True

    # Mild presentation
    res_mild = SymptomSeverityScorer.evaluate("Slight itching and runny nose for 2 days")
    assert res_mild["score"] <= 5
    assert res_mild["max_weight"] <= 3


def test_severity_scorer_multilingual():
    # Hinglish high acuity
    res_hinglish = SymptomSeverityScorer.evaluate("Seene me bahut tez dard ho raha hai aur saans lene me dikkat hai")
    assert res_hinglish["score"] >= 8
    assert res_hinglish["high_acuity_detected"] is True

    # Hindi Devanagari high fever & chills
    res_hindi = SymptomSeverityScorer.evaluate("तेज़ बुखार और दांत किटकिटाने वाली कंपकंपी ठंड है")
    assert res_hindi["score"] >= 5
    assert any(s["symptom"] in ["high_fever", "shaking_rigors"] for s in res_hindi["detected_symptoms"])

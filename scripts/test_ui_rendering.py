#!/usr/bin/env python3
"""
Playwright E2E verification of Virtual Doctor Precautions & Severity Badge rendering.
Captures the chat bubble directly.
"""

from playwright.sync_api import sync_playwright

def test_assessment_card_rendering():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        
        # Load local landing page
        page.goto("file:///Users/abhisheksahu/repos/hms-landing-page/public/index.html")
        page.wait_for_timeout(1000)
        
        # Open virtual doctor modal via toggleHospitalChat
        page.evaluate("toggleHospitalChat()")
        page.wait_for_timeout(500)
        
        # Mock an assessment object containing precautions and severity_score
        mock_assessment = {
            "session_id": "test-session-123",
            "triage_level": "URGENT_YELLOW",
            "recommended_specialty_clinic": "Infectious Disease / General Medicine",
            "severity_score": 7,
            "recommended_precautions": [
                "Drink 2-3 liters of fluids (oral rehydration solution, coconut water, clean water) daily to prevent dehydration.",
                "Take paracetamol for fever and pain; strictly avoid aspirin, ibuprofen, or other NSAIDs to avoid bleeding risk.",
                "Ensure strict mosquito bite prevention: sleep under insecticidal bed nets and apply DEET-based repellents.",
                "Seek immediate emergency hospital medical evaluation if red flags develop."
            ],
            "red_flag_alert": {
                "is_critical": False,
                "urgency_recommendation": "Consult physician within 24 hours."
            },
            "differential_diagnoses": [
                {
                    "diagnosis_name": "Dengue Fever",
                    "icd10_code": "A90",
                    "confidence_score": 0.92,
                    "clinical_rationale": "High fever, retro-orbital pain, severe arthralgia and thrombocytopenia."
                },
                {
                    "diagnosis_name": "Malaria",
                    "icd10_code": "B54",
                    "confidence_score": 0.78,
                    "clinical_rationale": "Cyclical chills and rigors with profuse diaphoresis."
                }
            ],
            "recommended_workup": [
                {"test_name": "Dengue NS1 Antigen & IgM ELISA", "urgency": "Urgent"},
                {"test_name": "Complete Blood Count with Platelet Count", "urgency": "Urgent"}
            ],
            "disclaimer": "AI triage assistant provided for informational guidance only."
        }
        
        # Clear previous messages to focus on the assessment
        page.evaluate("document.getElementById('hospitalChatMessages').innerHTML = ''")
        # Invoke vdRenderAssessment
        page.evaluate("(a) => vdRenderAssessment(a)", mock_assessment)
        page.wait_for_timeout(1000)
        
        # Scroll messages container to the top
        page.evaluate("document.getElementById('hospitalChatMessages').scrollTop = 0")
        page.wait_for_timeout(500)
        
        # Take screenshot of the chat modal element directly
        modal_element = page.locator("#hospitalChatModal")
        screenshot_path = "/Users/abhisheksahu/.gemini/antigravity/brain/feb7266f-3437-4a1a-ac64-09c904fe51cd/virtual_doctor_precautions_card.png"
        modal_element.screenshot(path=screenshot_path)
        print("Modal element screenshot saved to:", screenshot_path)
        
        # Verify text elements are present
        content = page.content()
        assert "Immediate Precautions & Care Advice" in content, "Precautions header missing!"
        assert "Severity: 7/10" in content, "Severity badge missing!"
        assert "avoid aspirin, ibuprofen, or other NSAIDs" in content, "Precaution text missing!"
        assert "Dengue Fever" in content, "Diagnosis text missing!"
        
        print("All UI verification checks passed successfully!")
        browser.close()

if __name__ == "__main__":
    test_assessment_card_rendering()

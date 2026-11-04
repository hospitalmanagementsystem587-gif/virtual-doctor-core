import asyncio
import os
from playwright.async_api import async_playwright

async def run_chatbot_e2e():
    demo_url = "file://" + os.path.abspath("widget/demo.html")
    print(f"Navigating to: {demo_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Monitor console logs
        page.on("console", lambda msg: print(f"[BROWSER CONSOLE] {msg.type}: {msg.text}"))

        await page.goto(demo_url)
        print("Page loaded.")

        # 1. Click on Virtual Doctor launcher button
        print("Clicking launcher button...")
        launcher = await page.wait_for_selector(".vd-launcher-btn")
        await launcher.click()

        # 2. Wait for modal container to become visible
        modal = await page.wait_for_selector(".vd-modal-container", state="visible")
        print("Modal opened successfully.")

        # 3. Fill in demographic form
        print("Filling demographics...")
        await page.fill("#vd-age", "28")
        await page.select_option("#vd-gender", "male")
        await page.click("#vd-next-step-1")

        # 4. Wait for Chat Conversation container to appear
        print("Waiting for chat interview questions...")
        await page.wait_for_selector("#vd-user-input", state="visible", timeout=15000)
        print("Chat container rendered.")

        # Helper to send message and wait for doctor reply
        async def send_chat_turn(user_text: str):
            print(f"\n[USER SAYS]: {user_text}")
            # Count current message bubbles
            prev_count = await page.locator("#vd-chat-msgs > div").count()
            await page.fill("#vd-user-input", user_text)
            await page.click("#vd-send-msg")

            # Wait until either new doctor bubble appears or assessment appears
            for _ in range(30):
                await asyncio.sleep(0.5)
                # Check if assessment finished
                if await page.locator(".vd-diff-item").count() > 0 or await page.locator(".vd-alert-card").count() > 0:
                    print("[SYSTEM]: Assessment complete and rendered!")
                    return True
                # Check if message count increased
                curr_count = await page.locator("#vd-chat-msgs > div").count()
                if curr_count >= prev_count + 2:
                    last_bubble = await page.locator("#vd-chat-msgs > div").last.inner_text()
                    print(f"[DOCTOR REPLIES]: {last_bubble}")
                    return False
            return False

        # Turn 1: Chief complaint
        is_done = await send_chat_turn("I have common cold with running nose and sneezing since yesterday.")
        
        # Turn 2: Character
        if not is_done:
            is_done = await send_chat_turn("Clear watery discharge from nose, mild scratchy throat, and congestion.")

        # Turn 3: Severity
        if not is_done:
            is_done = await send_chat_turn("Mild discomfort, around 3 out of 10.")

        # Turn 4: Associated symptoms
        if not is_done:
            is_done = await send_chat_turn("Mild tiredness. No fever, no chest pain, no shortness of breath.")

        # Wait a moment for final assessment to render
        await asyncio.sleep(2)

        # 5. Extract Assessment results from DOM
        print("\n========================================================")
        print("VERIFYING IN-BROWSER WIDGET DIAGNOSIS & SOAP NOTE:")
        print("========================================================")
        
        triage_text = await page.locator(".vd-alert-card").inner_text()
        print("Triage Card:\n", triage_text.strip())

        diff_count = await page.locator(".vd-diff-item").count()
        print(f"\nDifferential Diagnoses Rendered: {diff_count}")
        for i in range(diff_count):
            item_text = await page.locator(".vd-diff-item").nth(i).inner_text()
            print(f"--- Differentials #{i+1} ---\n{item_text.strip()}")

        soap_text = await page.locator(".vd-soap-box").inner_text()
        print(f"\nPhysician Handoff SOAP Note:\n{soap_text.strip()}")

        # Capture a screenshot to artifact directory
        screenshot_path = "/Users/abhisheksahu/.gemini/antigravity/brain/e671e88e-d551-4151-bf41-c4d0f4c74b98/virtual_doctor_e2e_test.png"
        await page.screenshot(path=screenshot_path)
        print(f"\nScreenshot saved to: {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_chatbot_e2e())

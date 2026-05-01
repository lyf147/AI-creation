from playwright.async_api import async_playwright
from actions import random_action
from detector import detect_issues
from reporter import TestReporter

class GameTestAgent:
    def __init__(self, url):
        self.url = url
        self.reporter = TestReporter()

    async def run(self, test_steps=100):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()

            await page.goto(self.url)
            print("🎮 Game Loaded")

            for step in range(test_steps):
                print(f"➡️ Step {step}")

                action_info = await random_action(page)

                screenshot_path = f"screenshots/step_{step}.png"
                await page.screenshot(path=screenshot_path)

                issues = await detect_issues(page)

                self.reporter.log(step, action_info, issues, screenshot_path)

                if "CRASH" in issues:
                    print("❌ Crash detected, stopping test")
                    break

            await browser.close()
            self.reporter.generate_report()

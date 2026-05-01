import json
import os

class TestReporter:
    def __init__(self):
        self.logs = []
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    def log(self, step, action, issues, screenshot):
        self.logs.append({
            "step": step,
            "action": action,
            "issues": issues,
            "screenshot": screenshot
        })

    def generate_report(self):
        with open("report.json", "w") as f:
            json.dump(self.logs, f, indent=2)
        print("📄 Report saved to report.json")

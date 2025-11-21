import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

class TriageAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-pro")

    def classify(self, text: str) -> str:
        prompt = (
            "Classify this incident into one category:\n"
            " - medical\n"
            " - safety\n"
            " - financial\n"
            " - mental_health\n"
            " - other\n\n"
            f"Incident: {text}"
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()

    def run(self, text: str) -> str:
        return self.classify(text)

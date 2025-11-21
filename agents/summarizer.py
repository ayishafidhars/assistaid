import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

class SummarizerAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-pro")

    def summarize(self, text: str) -> str:
        prompt = (
            "Provide a concise 2–3 sentence summary of the following incident:\n\n"
            f"{text}"
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()

    def run(self, text: str) -> str:
        return self.summarize(text)

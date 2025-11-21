class IngestorAgent:
    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        """Basic text cleaning before sending to other agents."""
        if not text:
            return ""

        cleaned = text.strip()
        cleaned = " ".join(cleaned.split())
        return cleaned

    def run(self, text: str) -> str:
        return self.clean_text(text)


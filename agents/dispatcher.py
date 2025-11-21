class DispatcherAgent:
    def __init__(self):
        # Simple routing logic
        self.routes = {
            "medical": "Medical Response Team",
            "safety": "Emergency Safety Unit",
            "financial": "Financial Aid Desk",
            "mental_health": "Counseling Services",
            "other": "General Support Desk"
        }

    def dispatch(self, incident_type: str) -> str:
        return self.routes.get(incident_type, "General Support Desk")

    def run(self, incident_type: str) -> str:
        return self.dispatch(incident_type)


from agents.ingestor import IngestorAgent
from agents.triage import TriageAgent
from agents.dispatcher import DispatcherAgent
from agents.summarizer import SummarizerAgent
from tools.db import IncidentDB

def run_pipeline(raw_text: str):
    # Initialize agents + tools
    ingestor = IngestorAgent()
    triage = TriageAgent()
    dispatcher = DispatcherAgent()
    summarizer = SummarizerAgent()
    db = IncidentDB()

    # Process text
    cleaned = ingestor.run(raw_text)
    incident_type = triage.run(cleaned)
    assigned_team = dispatcher.run(incident_type)
    summary = summarizer.run(cleaned)

    # Save to DB
    db.add_incident(
        raw_text=raw_text,
        cleaned_text=cleaned,
        incident_type=incident_type,
        assigned_team=assigned_team
    )

    # Return pipeline output
    return {
        "raw_text": raw_text,
        "cleaned_text": cleaned,
        "incident_type": incident_type,
        "assigned_team": assigned_team,
        "summary": summary
    }

if __name__ == "__main__":
    sample = "There is a person injured on the roadside and bleeding heavily."
    result = run_pipeline(sample)
    print(result)

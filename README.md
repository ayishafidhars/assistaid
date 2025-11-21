# AssistAid — Multi-Agent Crisis Support Assistant
Google AI Agents Intensive Capstone (Nov 2025)

AssistAid is a multi-agent system designed to classify, triage, summarize, and coordinate responses to crisis-related text reports.

## Problem
During crises, humans cannot read and respond to thousands of messages quickly.

## Solution
A multi-agent pipeline:
- **Ingestor Agent** (cleans text)
- **Triage Agent** (classifies incident type)
- **Dispatcher Agent** (assigns responders)
- **Summarizer Agent** (creates daily summaries)
- **Memory Bank** (long-term reference)
- **SQLite Task Database Tool** (stores incidents)

## Architecture
User Report → Ingestor → Triage → Dispatcher → Summary → Memory + DB

## Features (as required by capstone)
- Multi-agent chain  
- Tools (SQLite DB, logging)  
- Memory system  
- Evaluation script  
- Context engineering  
- Modular structure  
- Ready for deployment  

## Run Demo
```bash
pip install -r requirements.txt
python demo/run_demo.py
```

## Evaluation
```bash
python evaluation/evaluate_triage.py
```

## Docker
```bash
docker build -t assistaid .
docker run assistaid
```

## Project Description
AssistAid is a multi-agent crisis-support assistant designed to help analyze, route, and prioritize user-reported incidents (health, safety, emergency, financial, etc.).  
It uses:

- An **Ingestor Agent** to clean and standardize raw text  
- A **Triage Agent** to classify the type of incident  
- A **Support Agent** to generate guidance  
- **Memory + Sessions** to track ongoing cases  
- **Observability & Logs** to monitor agent behavior  

This project demonstrates:
- Multi-agent orchestration  
- Tools (custom + built-in)  
- Long-running operations  
- Memory & session management  
- Context engineering  
- Agent evaluation  

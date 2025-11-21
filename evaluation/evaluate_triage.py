import json

# Simple evaluation script to test Triage Agent outputs

TEST_CASES = [
    {"input": "There is a fire in my building!", "expected": "fire"},
    {"input": "My son fainted suddenly!", "expected": "medical"},
    {"input": "We are stuck due to flooding.", "expected": "flood"},
]

def evaluate(model_func):
    correct = 0
    results = []

    for case in TEST_CASES:
        output = model_func(case["input"])
        match = output == case["expected"]
        results.append({
            "input": case["input"],
            "expected": case["expected"],
            "got": output,
            "correct": match
        })
        if match:
            correct += 1

    score = correct / len(TEST_CASES)
    return score, results


# Dummy example agent (you will replace this with your Triage agent)
def dummy_triage_agent(text):
    text = text.lower()
    if "fire" in text:
        return "fire"
    if "faint" in text:
        return "medical"
    if "flood" in text:
        return "flood"
    return "unknown"


if __name__ == "__main__":
    score, results = evaluate(dummy_triage_agent)
    print("Evaluation Score:", score)
    print(json.dumps(results, indent=2))

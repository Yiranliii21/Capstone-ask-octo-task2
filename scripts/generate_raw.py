import json
from datetime import datetime, timedelta

NUM = 1000  
template_prompts = [
    "What is cardiovascular disease?",
    "What are common symptoms of coronary artery disease?",
    "How can cardiovascular disease be prevented?",
    "What causes heart disease?",
    "What are risk factors for stroke?"
]
template_responses = [
    "Cardiovascular disease refers to conditions affecting the heart and blood vessels.",
    "Common symptoms include chest pain, shortness of breath, fatigue, and dizziness.",
    "Prevention includes maintaining a healthy diet, regular exercise, avoiding smoking, and managing blood pressure and cholesterol levels.",
    "Heart disease can be caused by high blood pressure, high cholesterol, obesity, and lifestyle factors.",
    "Risk factors include smoking, obesity, high cholesterol, and lack of exercise."
]

data = []
start_time = datetime(2025, 2, 1, 12, 0, 0)

for i in range(NUM):
    idx = i % len(template_prompts)
    item = {
        "id": f"en-capstone1_cvd-{template_prompts[idx].split()[0].lower()}-{i+1:06d}",
        "source": "capstone1_cvd",
        "prompt": template_prompts[idx],
        "response": template_responses[idx],
        "domain_tag": "cvd_general",
        "safety_tag": "safe_general",
        "created_at": (start_time + timedelta(minutes=i*5)).isoformat() + "Z"
    }
    data.append(item)


with open("data/raw.jsonl", "w") as f:
    for row in data:
        f.write(json.dumps(row) + "\n")

print(f"{NUM} rows written to data/raw.jsonl")

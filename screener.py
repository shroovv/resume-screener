import requests
from prompts import resume_screening_prompt
import os

HF_API_TOKEN = os.getenv("HF_API_TOKEN")  # or paste it directly if needed

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

def analyze_resume(resume_text, job_description):
    prompt = resume_screening_prompt(resume_text[:2000], job_description[:2000])

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.5,
            "return_full_text": False
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        content = response.json()[0]["generated_text"]
    except Exception as e:
        print("API Error:", response.json())
        return [], []

    print("=== MODEL RESPONSE ===")
    print(content)

    positives = []
    negatives = []
    current = None

    for line in content.splitlines():
        line = line.strip()
        if line.lower().startswith("[positives]"):
            current = "positive"
        elif line.lower().startswith("[negatives]"):
            current = "negative"
        elif line.startswith("-") and current:
            if current == "positive":
                positives.append(line[1:].strip())
            elif current == "negative":
                negatives.append(line[1:].strip())

    return positives, negatives

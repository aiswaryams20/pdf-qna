import requests
import os

GROQ_API_KEY = "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"  # Your Groq API Key
API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def get_groq_answer(context, question):
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Answer based on the provided context only."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ],
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

import requests
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env for local testing
load_dotenv()

# ✅ Securely get the API key (prefer st.secrets, fallback to .env)
api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

# GROQ API details
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {api_key}",
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

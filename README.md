# 📄 PDF Q&A Assistant using Groq LLaMA 

A simple Streamlit app that allows users to ask questions from any uploaded PDF using the blazing-fast [Groq LLaMA 3 API]. Powered by Python and Streamlit, this tool extracts text from PDFs and gives intelligent answers.

## 🛠️ Tech Stack
- 🐍 Python
- 📄 PyMuPDF (for PDF parsing)
- ⚡ Groq API (LLaMA 3 model)
- 🌐 Streamlit (Frontend + Deployment)
- 🔐 dotenv + Streamlit Secrets (for secure API key management)

## 🚀 Live Demo
👉 [Click here to use the app](https://pdf-qna-gv4xbn22ecj4reofyosqsf.streamlit.app/)

## 📂 Features
- Upload any PDF 📄
- Ask questions in natural language 🤖
- Get answers powered by LLaMA 3 🔥
- Works fast & serverless with Groq API

## 🧠 How it Works
1. Upload a PDF.
2. The app extracts text using PyMuPDF.
3. User asks a question.
4. The context + question is sent to Groq’s LLaMA model.
5. The response is streamed back to the UI.

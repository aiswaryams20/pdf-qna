import streamlit as st
from utils.groq_engine import get_groq_answer
import fitz  # PyMuPDF
import time

st.set_page_config(page_title="Research Paper Buddy", layout="centered")
st.title("📚 Research Paper Buddy")
st.caption("Ask questions based on your uploaded research paper (PDF). Powered by Groq LLaMA3.")

MAX_FILE_SIZE_MB = 10

uploaded_file = st.file_uploader("📄 Upload your research paper (PDF under 10MB)", type=["pdf"])

question = st.text_input("❓ Ask a question based on the uploaded PDF")

# Prepare variables
context = ""

# If file uploaded
if uploaded_file is not None:
    file_size_mb = len(uploaded_file.getvalue()) / (1024 * 1024)

    if file_size_mb > MAX_FILE_SIZE_MB:
        st.error("⚠️ File too large! Please upload a PDF under 10 MB.")
        uploaded_file = None
    else:
        with st.spinner("📄 Reading PDF..."):
            try:
                with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                    text_chunks = [page.get_text() for page in doc]
                    context = "\n".join(text_chunks)
                st.success("✅ PDF successfully loaded!")
            except Exception as e:
                st.error(f"❌ Failed to read PDF: {e}")
                uploaded_file = None

# Ask question
if st.button("🔍 Generate Answer"):
    if not uploaded_file or not context:
        st.warning("⚠️ Please upload a valid PDF first.")
    elif question.strip() == "":
        st.warning("⚠️ Please type a question.")
    else:
        with st.spinner("🤖 Thinking..."):
            try:
                answer = get_groq_answer(context=context, question=question)
                st.success("✅ Answer generated!")
                st.markdown(f"**Answer:**\n\n{answer}")
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")

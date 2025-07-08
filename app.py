# app.py

import streamlit as st
import sys
import os

# Add src/ to the path to import run_rag_pipeline
sys.path.append(os.path.abspath("src"))
from rag_pipeline import run_rag_pipeline

st.set_page_config(page_title="Complaint Answering Assistant", layout="wide")

st.title("📊 Intelligent Complaint Assistant")
st.markdown("Ask a question about customer complaints. Our AI will answer using real complaint data.")

# Text input
question = st.text_input("💬 Enter your question:", placeholder="e.g. What are the most common complaints about personal loans?")

# Submit button
if st.button("Submit") and question.strip():
    with st.spinner("Generating answer..."):
        result = run_rag_pipeline(question)
        
        st.subheader("✅ Answer")
        st.write(result["answer"])

        st.subheader("📄 Retrieved Sources")
        for i, source in enumerate(result["sources"], start=1):
            st.markdown(f"**Source {i}:** {source}")
            
# Clear button
if st.button("Clear"):
    st.experimental_rerun()

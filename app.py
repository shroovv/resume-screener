import streamlit as st
from screener import analyze_resume
from utils import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("🤖 AI Resume Screener")

with st.sidebar:
    st.header("Upload Files")
    resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste the Job Description", height=300)

if resume_file and job_description:
    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(resume_file)
        positives, negatives = analyze_resume(resume_text, job_description)

    st.subheader("✅ Positives")
    for point in positives:
        st.write(f"- {point}")

    st.subheader("⚠️ Negatives")
    for point in negatives:
        st.write(f"- {point}")
else:
    st.info("Please upload a resume and paste a job description to begin.")

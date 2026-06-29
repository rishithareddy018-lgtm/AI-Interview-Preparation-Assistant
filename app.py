from question_generator import generate_questions
from skill_extractor import extract_skills
import streamlit as st
from resume_parser import (
    extract_text_from_pdf,
    extract_text_from_docx
)

st.title("🎤 AI Interview Preparation Assistant")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    st.success(f"{uploaded_file.name} uploaded successfully!")

    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        resume_text = extract_text_from_docx(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )
    skills = extract_skills(resume_text)

    st.subheader("🛠 Extracted Skills")

    if skills:
       st.write(skills)
    else:
       st.warning("No skills detected.")
    api_key = st.text_input(
       "Enter your Google Generative AI API KEY",
       type="password"
    )
    if skills and api_key:

        if st.button("Generate Interview Questions"):

            with st.spinner("Generating questions..."):

                questions = generate_questions(
                    skills,
                  api_key
              )

            st.subheader("🎯 Interview Questions")

            st.write(questions)
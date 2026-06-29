import streamlit as st
from resume_parser import (
extract_text_from_pdf,
extract_text_from_docx
)
from skill_extractor import extract_skills
from question_generator import (
generate_questions,
evaluate_answer
)

st.set_page_config(
page_title="AI Interview Preparation Assistant",
page_icon="🎤"
)

st.title("🎤 AI Interview Preparation Assistant")



uploaded_file = st.file_uploader(
"Upload your Resume (PDF or DOCX)",
type=["pdf", "docx"]
)

if uploaded_file is not None:

    st.success(f"{uploaded_file.name} uploaded successfully!")  

# Extract text from resume  
if uploaded_file.name.endswith(".pdf"):  
    resume_text = extract_text_from_pdf(uploaded_file)  

elif uploaded_file.name.endswith(".docx"):  
    resume_text = extract_text_from_docx(uploaded_file)  

# Show extracted text  
st.subheader("📄 Extracted Resume Text")  
st.text_area(  
    "Resume Content",  
    resume_text,  
    height=300  
)  

# Extract skills  
skills = extract_skills(resume_text)  

st.subheader("🛠 Extracted Skills")  

if skills:  
    st.write(skills)  
else:  
    st.warning("No skills detected.")  

# API key  
api_key = st.text_input(  
    "Enter Gemini API Key",  
    type="password"  
)  

if api_key:  
    st.session_state.api_key = api_key  

# Generate Questions  
if skills and api_key:  

    if st.button("Generate Interview Questions"):  

        questions = generate_questions(  
            skills,  
            api_key  
        )  

        st.session_state.questions = questions  
        st.session_state.current_question = 0  
        st.session_state.score = 0  

        st.success(  
            "Questions generated successfully!"  
        )



if "questions" in st.session_state:

    questions = st.session_state.questions  
    current = st.session_state.current_question  

if current < len(questions):  

    question = questions[current]  

    st.subheader(  
        f"Question {current + 1} of {len(questions)}"  
    )  

    st.write(question)  

    user_answer = st.text_area(  
        "Your Answer",  
        key=f"answer_{current}"  
    )  

    if st.button("Submit Answer"):  

        if user_answer.strip() == "":  
            st.warning(  
                "Please enter your answer."  
            )  

        else:  

            feedback = evaluate_answer(  
                question,  
                user_answer,  
                st.session_state.api_key  
            )  

            st.subheader("📊 Feedback")  
            st.write(feedback)  

    if st.button("Next Question"):  
        st.session_state.current_question += 1  
        st.rerun()  

else:  

    st.success(  
        "🎉 Mock Interview Completed!"  
    )  

    st.balloons()
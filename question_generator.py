import google.generativeai as genai
import re


def generate_questions(skills, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Generate 5 interview questions for these skills:

    {', '.join(skills)}

    Return only the questions.
    One question per line.
    Do not add headings.
    """

    response = model.generate_content(prompt)

    questions = response.text.split("\n")

    cleaned_questions = []

    for q in questions:
        q = q.strip()

        if q:
            q = re.sub(r'^\d+[\.\)]\s*', '', q)
            cleaned_questions.append(q)

    return cleaned_questions


def evaluate_answer(question, user_answer, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are an interview evaluator.

    Interview Question:
    {question}

    Candidate Answer:
    {user_answer}

    Evaluate the answer and provide:

    Score: x/10
    Strengths:
    Weaknesses:
    Correct Answer:
    Suggestions:

    Keep the response concise.
    """

    response = model.generate_content(prompt)

    return response.text
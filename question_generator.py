import google.generativeai as genai

def generate_questions(skills, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Generate 5 interview questions for each of these skills:

    {', '.join(skills)}

    Return only the questions.
    """

    response = model.generate_content(prompt)

    return response.text
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "pandas",
    "numpy",
    "matplotlib",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "streamlit",
    "git",
    "github",
    "excel",
    "power bi"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill.title())

    return sorted(found_skills)
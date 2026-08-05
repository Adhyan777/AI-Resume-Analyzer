SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "HTML",
    "CSS",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Flask",
    "Django",
    "FastAPI",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "Linux",
    "AWS",
    "Azure",
    "Google Cloud",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "OpenCV",
    "NumPy",
    "Pandas",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "NLP",
    "Computer Vision",
    "REST API"
]


def detect_skills(text):

    detected = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:

            detected.append(skill)

    return sorted(set(detected))
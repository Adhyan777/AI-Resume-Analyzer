import ollama


MODEL = "qwen2.5:1.5b"


def analyze_resume(resume_text):

    prompt = f"""
You are a professional resume reviewer.

Analyze the following resume and provide concise feedback.

Resume:
{resume_text}

Return your response with these sections:

1. Overall Impression
2. Strengths
3. Weaknesses
4. Suggestions for Improvement

Focus on:
- Resume structure
- Skills
- Projects
- Experience
- Education
- Achievements
- Professional language

Do not invent information that is not present in the resume.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

import json
import ollama


MODEL = "qwen2.5:1.5b"


def analyze_resume(resume_text):

    prompt = f"""
You are a professional resume reviewer.

Analyze the resume below.

Resume:
{resume_text}

Return ONLY valid JSON.
Do not use markdown.
Do not use ```.

Use exactly this structure:

{{
    "overall_impression": "A concise overall assessment.",
    "strengths": [
        "Strength 1",
        "Strength 2",
        "Strength 3"
    ],
    "weaknesses": [
        "Weakness 1",
        "Weakness 2",
        "Weakness 3"
    ],
    "suggestions": [
        "Suggestion 1",
        "Suggestion 2",
        "Suggestion 3"
    ],
    "important_skills": [
        "Skill 1",
        "Skill 2",
        "Skill 3"
    ]
}}

Rules:
- Only use information actually present in the resume.
- Do not invent education, experience, certifications, achievements, or skills.
- Keep each item concise.
- If information is missing, say that it is missing instead of inventing it.
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

    content = response["message"]["content"]

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        return {
            "overall_impression": content,
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "important_skills": []
        }

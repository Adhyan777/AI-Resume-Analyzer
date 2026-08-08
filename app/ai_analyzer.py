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

def analyze_job_match(resume_text, job_description):

    prompt = f"""
You are an AI job matching assistant.

Compare the resume with the job description below.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON.
Do not use markdown.
Do not use ```.

Use exactly this structure:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "matching_keywords": [],
    "recommendations": []
}}

Rules:
- match_score must be an integer from 0 to 100.
- Only identify skills and keywords that are actually present.
- Do not invent information about the candidate.
- Keep recommendations concise.
- Base the score on how well the resume matches the job requirements.
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
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "matching_keywords": [],
            "recommendations": [
                "AI response could not be parsed."
            ]
        }

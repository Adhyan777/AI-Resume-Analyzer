def calculate_ats_score(resume_summary, text):

    score = 0

    strengths = []

    improvements = []

    # -----------------------------
    # Name
    # -----------------------------
    if resume_summary["name"] != "Not Found":
        score += 10
        strengths.append("Name found")
    else:
        improvements.append("Add your full name")

    # -----------------------------
    # Email
    # -----------------------------
    if resume_summary["email"] != "Not Found":
        score += 10
        strengths.append("Email found")
    else:
        improvements.append("Add an email address")

    # -----------------------------
    # Phone
    # -----------------------------
    if resume_summary["phone"] != "Not Found":
        score += 10
        strengths.append("Phone number found")
    else:
        improvements.append("Add a phone number")

    # -----------------------------
    # Skills
    # -----------------------------
    skill_count = len(resume_summary["skills"])

    if skill_count >= 8:
        score += 25
        strengths.append("Excellent technical skills")

    elif skill_count >= 5:
        score += 20
        strengths.append("Good technical skills")

    elif skill_count >= 3:
        score += 15
        strengths.append("Basic technical skills")

    else:
        improvements.append("Add more technical skills")

    # -----------------------------
    # Resume Length
    # -----------------------------
    words = resume_summary["words"]

    if 300 <= words <= 900:
        score += 10
        strengths.append("Good resume length")
    else:
        improvements.append("Keep resume between 300 and 900 words")

    # -----------------------------
    # Important Sections
    # -----------------------------
    text = text.lower()

    if "education" in text:
        score += 10
        strengths.append("Education section found")
    else:
        improvements.append("Add an Education section")

    if "experience" in text:
        score += 15
        strengths.append("Experience section found")
    else:
        improvements.append("Add an Experience section")

    if "project" in text:
        score += 10
        strengths.append("Projects section found")
    else:
        improvements.append("Add a Projects section")

    return {
        "score": score,
        "strengths": strengths,
        "improvements": improvements
    }
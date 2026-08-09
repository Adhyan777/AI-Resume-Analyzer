from flask import Flask, render_template, request, flash
import os
from werkzeug.utils import secure_filename

from app.pdf_utils import extract_text
from app.parser import (
    extract_name,
    extract_email,
    extract_phone,
    word_count,
    character_count
)
from app.skills import detect_skills
from app.ats import calculate_ats_score, calculate_keyword_match
from app.ai_analyzer import analyze_resume, analyze_job_match

app = Flask(__name__)

app.secret_key = "resume_analyzer_secret"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    extracted_text = ""
    resume_summary = None
    ats_result = None
    ai_analysis = None
    job_match = None
    keyword_match = None

    if request.method == "POST":

        job_description = request.form.get("job_description", "")

        if "resume" not in request.files:

            flash("No file selected.", "danger")

            return render_template(
                "upload.html",
                extracted_text=extracted_text,
                resume_summary=resume_summary,
                ats_result=ats_result
            )

        file = request.files["resume"]

        if file.filename == "":

            flash("Please choose a PDF.", "warning")

            return render_template(
                "upload.html",
                extracted_text=extracted_text,
                resume_summary=resume_summary,
                ats_result=ats_result
            )

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(filepath)

            extracted_text = extract_text(filepath)
            ai_analysis = analyze_resume(extracted_text)

            job_match = None


        if job_description.strip():

            job_match = analyze_job_match(
            extracted_text,
            job_description
     )

        keyword_match = None

        if job_description.strip():

            keyword_match = calculate_keyword_match(
            extracted_text,
            job_description
     )    

            resume_summary = {
                "name": extract_name(extracted_text),
                "email": extract_email(extracted_text),
                "phone": extract_phone(extracted_text),
                "words": word_count(extracted_text),
                "characters": character_count(extracted_text),
                "skills": detect_skills(extracted_text)
            }

            ats_result = calculate_ats_score(
                resume_summary,
                extracted_text
            )

            flash(
                "Resume uploaded successfully!",
                "success"
            )

        else:

            flash(
                "Only PDF files are allowed.",
                "danger"
            )

    return render_template(
    "upload.html",
    extracted_text=extracted_text,
    resume_summary=resume_summary,
    ats_result=ats_result,
    ai_analysis=ai_analysis,
    job_match=job_match,
    keyword_match=keyword_match
)

@app.route("/about")
def about():

    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
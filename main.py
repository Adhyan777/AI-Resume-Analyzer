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

    if request.method == "POST":

        if "resume" not in request.files:

            flash("No file selected.", "danger")

            return render_template(
                "upload.html",
                extracted_text=extracted_text
            )

        file = request.files["resume"]

        if file.filename == "":

            flash("Please choose a PDF.", "warning")

            return render_template(
                "upload.html",
                extracted_text=extracted_text
            )

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(filepath)

            extracted_text = extract_text(filepath)

            resume_summary = {
                "name": extract_name(extracted_text),
                "email": extract_email(extracted_text),
                "phone": extract_phone(extracted_text),
                "words": word_count(extracted_text),
                "characters": character_count(extracted_text)
            }

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
        resume_summary=resume_summary
    )
    


@app.route("/about")
def about():

    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
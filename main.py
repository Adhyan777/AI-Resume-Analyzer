from flask import Flask, render_template, request, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "resume_analyzer_secret"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        if "resume" not in request.files:

            flash("No file selected.", "danger")

            return render_template("upload.html")

        file = request.files["resume"]

        if file.filename == "":

            flash("Please choose a PDF file.", "warning")

            return render_template("upload.html")

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            flash("Resume uploaded successfully!", "success")

        else:

            flash("Only PDF files are allowed.", "danger")

    return render_template("upload.html")


@app.route("/about")
def about():

    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
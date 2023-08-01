from flask import Flask, request, render_template
import analyze

app = Flask(__name__)


@app.route("/analyze_text", methods=["POST"])
def analyze_page():
    text = request.form["text"]
    return {"words": analyze.analyze(text)}


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/info")
def info():
    return {
        "word": "Žodis",
    }

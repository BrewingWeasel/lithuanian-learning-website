from flask import Flask, request, render_template
import analyze

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def analyze_page():
    if request.method == "POST":
        text = request.form["text"]
        return render_template("answer.html", words=analyze.analyze(text))
    else:
        return render_template("input.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/info")
def info():
    return {
        "word": "Žodis",
    }

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        print(entry_content, formatted_date)
    return render_template("index.html")
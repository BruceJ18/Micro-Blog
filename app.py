from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    db_client = MongoClient('mongodb+srv://brucej18:illescio369@cluster0.5bjmfpv.mongodb.net/')
    app.db = db_client.MicroBlog

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

            
        entries_with_date = [(
            entry["content"], 
            entry["date"], 
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("index.html", entries=entries_with_date)
    return app
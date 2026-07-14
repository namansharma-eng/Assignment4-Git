from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGO_URI = "mongodb+srv://Namstar:Naman1234@flask-dev.7d8kgcd.mongodb.net/?appName=flask-dev"
client = MongoClient(MONGO_URI)
db = client['flask-dev']
collection = db['Submissions']

@app.route('/api')
def api():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            message = request.form.get("message")

            collection.insert_one({
                "name": name,
                "email": email,
                "message": message
            })
            return redirect(url_for('success'))
        except Exception as e:
            error = str(e)
    return render_template("index.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
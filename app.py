from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Free Date API!"

@app.route("/next-10-dates", methods=["GET"])
def next_10_dates():
    today = datetime.utcnow()
    dates = [(today + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(10)]
    return jsonify(dates)

if __name__ == "__main__":
    app.run(port=5000)

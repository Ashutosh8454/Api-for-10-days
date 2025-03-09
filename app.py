import os
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Free Date API!"})

@app.route("/next-20-dates", methods=["GET"])
def next_20_dates():
    today = datetime.utcnow()
    dates = [(today + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(20)]
    return jsonify({"dates": dates})  # Ensures valid JSON format

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render environment port
    app.run(host="0.0.0.0", port=port)

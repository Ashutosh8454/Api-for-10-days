from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Free Date API!"})

@app.route("/next-10-dates", methods=["GET"])
def next_10_dates():
    today = datetime.utcnow()
    dates = [(today + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(10)]
    return jsonify({"dates": dates})  # Always return JSON object

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render environment port
    app.run(host="0.0.0.0", port=port)

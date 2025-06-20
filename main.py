from flask import Flask, request, jsonify
from classifier_responder import classifier, responder
from datetime import datetime
import pandas as pd
import os

CSV_PATH = "data/questions.csv"

app = Flask(__name__)
@app.route("/webhook", methods=["POST"])
def my_app():
    data = request.json
    message = data.get("message", "")
    category = classifier(message)
    response = responder(message)
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "category": category,
        "response": response
    }
    df = pd.DataFrame([log])
    header = not os.path.exists(CSV_PATH)
    df.to_csv(CSV_PATH, mode="a", header=header, index=False)

    return jsonify({"category": category, "response": response})
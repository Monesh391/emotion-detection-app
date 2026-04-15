from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    result = emotion_detector(data["text"])

    if result is None:
        return jsonify({"error": "Processing failed"}), 500

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

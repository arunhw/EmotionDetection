from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect():
    text = request.args.get('textToAnalyze')

    if text is None or text == "":
        return "Invalid input", 400

    result = emotion_detector(text)
    return str(result)

app.run(debug=True)
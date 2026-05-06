def emotion_detector(text):
    if text is None or text.strip() == "":
        return {"error": "Invalid input"}

    text = text.lower()

    emotions = {
        "joy": 0,
        "anger": 0,
        "sadness": 0,
        "fear": 0,
        "disgust": 0
    }

    if "happy" in text or "good" in text:
        emotions["joy"] += 1
    if "angry" in text:
        emotions["anger"] += 1
    if "sad" in text:
        emotions["sadness"] += 1
    if "fear" in text:
        emotions["fear"] += 1
    if "disgust" in text:
        emotions["disgust"] += 1

    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant

    return emotions
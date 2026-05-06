from EmotionDetection import emotion_detector

def test():
    result = emotion_detector("I am happy")
    assert result["dominant_emotion"] == "joy"
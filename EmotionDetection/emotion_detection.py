import requests

def emotion_detector(text_to_analyze):
    """
    Calls Watson NLP, extracts the 5 emotions (anger, disgust, fear, joy, sadness),
    finds the dominant_emotion, and returns them in one dictionary.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            resp_json = response.json()

            # 1) Navigate to "emotionPredictions" -> [0] -> "emotion"
            if "emotionPredictions" not in resp_json or len(resp_json["emotionPredictions"]) == 0:
                return {"error": "No emotionPredictions in response."}

            emotion_data = resp_json["emotionPredictions"][0].get("emotion", {})
            if not emotion_data:
                return {"error": "No emotion field found in the first emotionPrediction."}

            # 2) Extract the 5 emotions
            anger_score = emotion_data.get("anger", 0.0)
            disgust_score = emotion_data.get("disgust", 0.0)
            fear_score = emotion_data.get("fear", 0.0)
            joy_score = emotion_data.get("joy", 0.0)
            sadness_score = emotion_data.get("sadness", 0.0)

            # 3) Determine the dominant emotion
            all_emotions = {
                "anger": anger_score,
                "disgust": disgust_score,
                "fear": fear_score,
                "joy": joy_score,
                "sadness": sadness_score
            }
            dominant_emotion = max(all_emotions, key=all_emotions.get)

            # 4) Return the final dictionary
            return {
                "anger": anger_score,
                "disgust": disgust_score,
                "fear": fear_score,
                "joy": joy_score,
                "sadness": sadness_score,
                "dominant_emotion": dominant_emotion
            }

        except ValueError:
            return {"error": "Error parsing JSON response."}
    else:
        return {"error": f"HTTP {response.status_code}, {response.text}"}

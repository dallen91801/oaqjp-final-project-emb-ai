import requests
import json

def emotion_detector(text_to_analyze):
    """
    Debug version to see the entire JSON response from Watson NLP.
    It will return that raw JSON (as a Python dictionary) so we know what keys exist.
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
            response_json = response.json()
            print("\nDEBUG: Entire Watson Response:\n", json.dumps(response_json, indent=2))
            return response_json  # Return it so you can see it in your Python shell
        except ValueError:
            return "Error parsing JSON response."
    else:
        return f"Error: {response.status_code}, {response.text}"

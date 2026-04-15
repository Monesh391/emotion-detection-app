import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    json_data = {
        "raw_document": {"text": text_to_analyze}
    }

    response = requests.post(url, json=json_data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        emotions = result['emotionPredictions'][0]['emotion']

        dominant = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant
        }
    else:
        return None

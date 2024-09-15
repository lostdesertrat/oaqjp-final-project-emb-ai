import requests
import json

# Function to analyze the text for emotion
def emotion_detector(text_to_analyze):
    # URL to the emotion AI service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Header ID for the AI service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Formatting the request
    text_obj = { "raw_document": { "text": text_to_analyze } }

    # Post a request to the API
    response = requests.post(url, headers = header, json = text_obj)

    # JSON response from API
    emotion_response = json.loads(response.text)

    # Variable for each emotion score
    anger_score = emotion_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = emotion_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = emotion_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = emotion_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = emotion_response['emotionPredictions'][0]['emotion']['sadness']

    # Create a dictionary with the name of all the emotions, and find the one with the highest value
    emotion_name = dict(anger=anger_score, disgust=disgust_score, fear=fear_score, joy=joy_score, sadness=sadness_score)
    dominant_emotion = max(emotion_name, key=emotion_name.get)

    # Return the emotion scale of the text
    return {
            'anger' : anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
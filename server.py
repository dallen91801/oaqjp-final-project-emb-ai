from flask import Flask, request, render_template
from EmotionDetection import emotion_detector  # or from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Flask route for the emotion detector
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Retrieve user text from form data
    text_to_analyze = request.form.get('text_to_analyze', '')

    if not text_to_analyze.strip():
        return "No text provided for analysis."

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Format the required response
    # Example: "For the given statement, the system response is 'anger':0.0062 ... The dominant emotion is joy."
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    response_str = (f"For the given statement, the system response is 'anger': {anger}, "
                    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
                    f"The dominant emotion is {dominant}.")

    return response_str

@app.route('/', methods=['GET'])
def home():
    """
    Renders the index.html page with a form for user input.
    This index.html is assumed to be in the 'templates' folder.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Deploy on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)

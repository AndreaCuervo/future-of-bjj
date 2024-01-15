import os
from flask import Flask, request, send_file
from backend import generate_bjj_training_text, generate_bjj_video_suggestions
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)
app.config['TIMEOUT'] = 0

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response

current_dir = Path(__file__).parent

mapping = {
    "chimes": current_dir / "backgrounds" / "chimes.mp3",
    "music": current_dir / "backgrounds" / "music.mp3",
    "nature": current_dir / "backgrounds" / "nature.mp3",
    "ocean": current_dir / "backgrounds" / "ocean.mp3",
    "rain": current_dir / "backgrounds" / "rain.mp3",
    "storm": current_dir / "backgrounds" / "storm.mp3",
}

@app.route('/generate_bjj_training', methods=['POST'])
def generate_customised_bjj_training():
    data = request.get_json()
    goals = data.get('goals', [])
    username = data.get('username', "User")
    language = data.get('language', "english")

    try:
        training_text = generate_bjj_training_text(username, goals, language)
        # You can use 'training_text' as needed in your application
    except Exception as e:
        print(f'Error generating BJJ training: {e}')

    return "BJJ Training Generated Successfully"

@app.route('/generate_bjj_video', methods=['POST'])
def generate_bjj_video_suggestions_endpoint():
    data = request.get_json()
    goals = data.get('goals', [])
    username = data.get('username', "User")
    language = data.get('language', "english")

    try:
        video_suggestions = generate_bjj_video_suggestions(username, goals, language)
        # You can use 'video_suggestions' as needed in your application
    except Exception as e:
        print(f'Error generating BJJ video suggestions: {e}')

    return "BJJ Video Suggestions Generated Successfully"

@app.route('/test', methods=['GET'])
def test():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, jsonify, request
from utils import recognize_speech, extract_keywords
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  if request.method == 'POST':
    lang = request.form['lang']
    file = request.files['file']
    file_format = file.filename.split('.')[-1]
    file_name = f'audio.{file_format}'
    file_path = f'static/uploads/{file_name}'
    path = os.path.join(os.getcwd(), file_path)
    file.save(path)

    recognized_text = recognize_speech.recognize(path, lang)
    text = recognized_text

    if text != None or text != '':
      keywords = extract_keywords.extract(text, lang)

    response = {'success':'true', 'file_path': file_path, 'text': text, 'lang': lang, 'keywords': keywords}

    return jsonify(response)
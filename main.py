from flask import Flask, request, make_response, json
from src.transcribe import transcribe
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route("/Hello", methods=['GET', 'POST'])
def hello():
    return 'hello'


@app.route("/SpeechToText", methods=['GET', 'POST'])
def index():
    file = request.files.get('file')
    if file:
        path = os.path.join('./wavs', file.filename)
        if os.path.exists(path):
            os.remove(path)
        file.save(path)
        text = transcribe(path, None)
        res = make_response(json.dumps({
            'success': True,
            'message': text
        }, ensure_ascii=False))
        os.remove(path)
        res.mimetype = 'application/json'

    return res


# app.config['DEBUG'] = True
app.run()

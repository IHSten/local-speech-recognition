#!flask/bin/python

from flask import request

from __main__ import app
from local_sr import speechtotext

stt = speechtotext.SpeechToText()

@app.route('/api/local', methods=['GET'])
def transcribeLocally():
    return stt.SphinxTranslation(request.data)
    
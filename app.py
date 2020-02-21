#!flask/bin/python
import sys

from flask import Flask

sys.path.insert(0, './local_sr')

app = Flask(__name__)

import api.sr

@app.route('/')
def index():
    return "Hopefully this will eventually be a management console. For the moment, you get this message."

if __name__ == '__main__':
    app.run(debug=True)
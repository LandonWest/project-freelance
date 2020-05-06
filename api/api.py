from flask import Flask

app = Flask(__name__)


@app.route('/v1/api')
def index():
    return {'greeting': 'Hello World!'}

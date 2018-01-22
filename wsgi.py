import flask
from flask_cors import CORS

application = flask.Flask(__name__)
CORS(application)

@application.route('/')
def get_status():
    return "Hello, I am running..."

if __name__ == '__main__':
    application.run()
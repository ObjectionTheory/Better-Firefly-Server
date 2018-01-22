import flask

app = flask.Flask(__name__)

@application.route('/')
def get_status():
    return "Hello, I am running..."

if __name__ == '__main__':
    app.run()
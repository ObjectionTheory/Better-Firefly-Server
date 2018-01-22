import flask
from flash_httpauth import HTTPBasicAuth

app = flask.Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/')
def get_status():
    return "Hello, I am running..."

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/summary')
@auth.login_required
def return_summary():
    return "Hi!"

if __name__ == '__main__':
    app.run()
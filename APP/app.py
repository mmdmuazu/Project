from flask import *
from typing import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login() -> jsonify:
    if request.method == 'GET':
        return jsonify({'method':'not allowed'})
    req = request.json.get
    username:str = req('username')
    password:str = req('password')

    if username:
        return jsonify({'message':f'hello {username}! here is your password {password}'})
    else:
        return jsonify({'message':'no username found'})

@app.route('/register', methods=['GET','POST'])
def register() -> str:
    if request.method == 'POST':
        req:json = request.json.get
        firstName:str = req('firstName')
        lastName:str = req('lastName')
        username:str = req('username')
        password:str = req('password')

        return jsonify({'message':f'username: {username} fullname: {firstName} { lastName}'})
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    return render_template('forgotPassword.html')


@app.errorhandler(404)
def notFound(error):
    return 'not found'

if __name__ == '__main__':
    app.run(port=8000,debug=True)

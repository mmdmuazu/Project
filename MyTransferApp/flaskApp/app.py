from flask import Flask, jsonify, render_template,request
from typing import Dict
import json

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def login():
    print(dir(request.json.get))#('username'))
    #username:str = request.form.get('username)
    return 'hello'
app.run()

from flask import *
import sqlite3 as database
app = Flask(__name__)

conn = database.connect('chat.db')
cursor = conn.cursor()
@app.route('/')
def index():
     conn = database.connect('chat.db')
     cursor = conn.cursor()
     cursor.execute('SELECT * FROM users')
     info = cursor.fetchall()
     return str(info)
app.run()

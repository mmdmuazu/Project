# '''from fastapi import FastAPI,Response,Request
# import time

# # Create a FastAPI application
# app = FastAPI()

# # Define a route at the root web address ("/")
# @app.get("/")
# def read_root():
# 	return {"message": "Hello, FastAPI!"}
# @app.head("/items/", status_code=204)
# def get_items_headers(response: Response):
#     response.headers["X-Cat-Dog"] = "Alone in the world"

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response'''

#  from fastapi import FastAPI

#  app = FastAPI()

#  @app.webhooks('/')
#  def web():
#      return {'hello':'world!'}

#  import requests

#  url = "https://api.mtn.com/v1/datagifting/customers/senderMsisdn/dataGifting"

#  payload = {
#      "receiverMsisdn": "2349062058463",
#      "productCode": "NACT_NG_Data_4504",
#      "sendSms": True
#  }
#  headers = {
#      "Content-Type": "application/json",
#      "X-API-Key": "xzJMvkYcFJUQnmKKDtFi8TMHYsMzhzw5"
#  }

#  response = requests.request("POST", url, json=payload, headers=headers)

#  print(response.status_code)
# import http.cli
# # payload = "{\n  \"receiverMsisdn\": \"2349062058463\",\n  \"productCode\": \"NACT_NG_Data_4504\",\n  \"sendSms\": true\n}"

# # headers = {
# #     'Content-Type': "application/json",
# #     'X-API-Key': "xzJMvkYcFJUQnmKKDtFi8TMHYsMzhzw5"
# #     }

# # conn.request("POST", "/v1/datagifting/customers/09038448811/dataGifting", payload, headers)

# # res = conn.getresponse()
# # data = res.read()

# # print(data.decode("utf-8"))

















# # # Function to check if a number is prime
# # def is_prime(number:int) -> bool:

# #     # If number is less than 2, it's not prime you already no that
# #     if number <= 1:
# #         return False
# #         #if the number is not a prime number it will return false

# #     # in python we use the for loop for range of numbers
# #     for i in range(2, number):
# #         # Check if the number is divisible by any number between 2 and the number -1
# #         if number % i == 0:
# #             #we use a % modular division in python to check reminder
# #             return False
# #     #if the number have a reminder then we will return true to validate
# #     return True
# # while True:
# #     # to check if the user insert the expected int not str
# #     try:

# #         # Ask the user for a number and the number shoud be int
# #         num:int = int(input("Enter a number: "))

# #         # Call the is_prime function and print the result
# #         if is_prime(num):
# #             print(f"{num} is a prime number.")
# #             break
# #         else:
# #             print(f"{num} is not a prime number.")
# #             break
# #     except Exception:
# #         print('intiger expected')

# # from flask import *
# # from typing import *
# # import uuid

# # app = Flask(__name__)
# # users: Dict = {}

# # @app.route('/index/<username>/',methods=['GET','POST'])
# # def index(username):
# #     # username: str = request.args.get('username')
    
# #     if not username:
# #         return 'username please'
# #     if username not in users:
# #         # return dir(uuid.uuid4())
# #         users[username] = {'username':username,'userId':uuid.uuid4().hex[:6],'message':''}
# #     return render_template('test.html',message=users.get(username)['message'])
# # @app.route('/message',methods=['GET','POST'])
# # def message():
# #     recipient_username:str = request.form.get('username')
# #     message:str = request.form.get('text')

# #     if recipient_username in users:
# #         users[recipient_username]['message'] += message
# #     else:
# #         return f'username does not exist {recipient_username}'
# #     print(users)
# #     return redirect(f'index/{recipient_username}/')
# # if __name__ == '__main__':
# #     app.run(debug=True)

# # from flask import Flask, render_template, request, redirect, url_for
# # import sqlite3
# # import uuid

# # app = Flask(__name__)

# # def init_db():
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS users (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 username TEXT UNIQUE NOT NULL,
# #                 user_id TEXT UNIQUE NOT NULL
# #             )
# #         """)
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS messages (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 sender TEXT NOT NULL,
# #                 recipient TEXT NOT NULL,
# #                 text TEXT NOT NULL,
# #                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# #             )
# #         """)
# #         conn.commit()

# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/register', methods=['POST'])
# # def register():
# #     username = request.form.get('username')
# #     if not username:
# #         return "Please provide a username"
    
# #     user_id = uuid.uuid4().hex[:6]
# #     try:
# #         with sqlite3.connect("chat.db") as conn:
# #             cursor = conn.cursor()
# #             cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id))
# #             conn.commit()
# #         return redirect(url_for('chat', username=username))
# #     except sqlite3.IntegrityError:
# #         return "Username already taken"

# # @app.route('/chat/<username>')
# # def chat(username):
#     # with sqlite3.connect("chat.db") as conn:
#     #     cursor = conn.cursor()
#     #     cursor.execute("SELECT text, sender FROM messages WHERE recipient = ?", (username,))
#     #     messages = cursor.fetchall()
# #     return render_template('chat.html', username=username, messages=messages)

# # @app.route('/send_message', methods=['POST'])
# # def send_message():
# #     sender = request.form.get('sender')
# #     recipient = request.form.get('recipient')
# #     text = request.form.get('text')
    
#     # with sqlite3.connect("chat.db") as conn:
#     #     cursor = conn.cursor()
#     #     cursor.execute("INSERT INTO messages (sender, recipient, text) VALUES (?, ?, ?)", (sender, recipient, text))
#     #     conn.commit()
# #     return redirect(url_for('chat', username=sender))

# # if __name__ == '__main__':
# #     init_db()
# #     app.run(debug=True)

# # # UI Templates
# # index_html = """
# # <!DOCTYPE html>
# # <html lang='en'>
# # <head>
# #     <meta charset='UTF-8'>
# #     <meta name='viewport' content='width=device-width, initial-scale=1.0'>
# #     <title>Chat App</title>
# #     <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
# # </head>
# # <body class='d-flex justify-content-center align-items-center vh-100'>
# #     <div class='container text-center'>
# #         <h1 class='mb-4'>Welcome to Chat App</h1>
# #         <form action='/register' method='POST'>
# #             <input type='text' name='username' placeholder='Enter your username' class='form-control mb-3' required>
# #             <button type='submit' class='btn btn-primary'>Start Chatting</button>
# #         </form>
# #     </div>
# # </body>
# # </html>
# # """

# # chat_html = """
# # <!DOCTYPE html>
# # <html lang='en'>
# # <head>
# #     <meta charset='UTF-8'>
# #     <meta name='viewport' content='width=device-width, initial-scale=1.0'>
# #     <title>Chat Room</title>
# #     <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
# # </head>
# # <body class='container py-5'>
# #     <h2 class='text-center mb-4'>Chat Room - {{ username }}</h2>
# #     <div class='card p-3 mb-3'>
# #         {% for msg, sender in messages %}
# #             <div class='mb-2'><strong>{{ sender }}:</strong> {{ msg }}</div>
# #         {% endfor %}
# #     </div>
# #     <form action='/send_message' method='POST'>
# #         <input type='hidden' name='sender' value='{{ username }}'>
# #         <input type='text' name='recipient' placeholder='Recipient username' class='form-control mb-2' required>
# #         <textarea name='text' placeholder='Type a message' class='form-control mb-2' required></textarea>
# #         <button type='submit' class='btn btn-success'>Send</button>
# #     </form>
# # </body>
# # </html>
# # """

# # # Save templates to files
# # with open("templates/index.html", "w") as f:
# #     f.write(index_html)

# # with open("templates/chat.html", "w") as f:
# #     f.write(chat_html)
# # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # import sqlite3
# # import uuid

# # app = Flask(__name__)

# # def init_db():
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS users (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 username TEXT UNIQUE NOT NULL,
# #                 user_id TEXT UNIQUE NOT NULL
# #             )
# #         """)
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS messages (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 sender TEXT NOT NULL,
# #                 recipient TEXT NOT NULL,
# #                 text TEXT NOT NULL,
# #                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# #             )
# #         """)
# #         conn.commit()

# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/register', methods=['POST'])
# # def register():
# #     username = request.form.get('username')
# #     if not username:
# #         return "Please provide a username"
    
# #     user_id = uuid.uuid4().hex[:6]
# #     try:
# #         with sqlite3.connect("chat.db") as conn:
# #             cursor = conn.cursor()
# #             cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id))
# #             conn.commit()
# #         return redirect(url_for('chat', username=username))
# #     except sqlite3.IntegrityError:
# #         return "Username already taken"

# # @app.route('/chat/<username>')
# # def chat(username):
# #     return render_template('chat.html', username=username)

# # @app.route('/send_message', methods=['POST'])
# # def send_message():
# #     sender = request.form.get('sender')
# #     recipient = request.form.get('recipient')
# #     text = request.form.get('text')
    
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("INSERT INTO messages (sender, recipient, text) VALUES (?, ?, ?)", (sender, recipient, text))
# #         conn.commit()
# #     return jsonify({'success': True})

# # @app.route('/get_messages/<username>')
# # def get_messages(username):
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT sender, text, timestamp FROM messages WHERE recipient = ? OR sender = ? ORDER BY timestamp ASC", (username, username))
# #         messages = cursor.fetchall()
# #     return jsonify(messages)


# # # UI Templates
# # index_html = """
# # <!DOCTYPE html>
# # <html lang='en'>
# # <head>
# #     <meta charset='UTF-8'>
# #     <meta name='viewport' content='width=device-width, initial-scale=1.0'>
# #     <title>Chat App</title>
# #     <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
# # </head>
# # <body class='d-flex justify-content-center align-items-center vh-100'>
# #     <div class='container text-center'>
# #         <h1 class='mb-4'>Welcome to Chat App</h1>
# #         <form action='/register' method='POST'>
# #             <input type='text' name='username' placeholder='Enter your username' class='form-control mb-3' required>
# #             <button type='submit' class='btn btn-primary'>Start Chatting</button>
# #         </form>
# #     </div>
# # </body>
# # </html>
# # """

# # chat_html = """
# # <!DOCTYPE html>
# # <html lang='en'>
# # <head>
# #     <meta charset='UTF-8'>
# #     <meta name='viewport' content='width=device-width, initial-scale=1.0'>
# #     <title>Chat Room</title>
# #     <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
# #     <style>
# #         .chat-box { height: 400px; overflow-y: scroll; border: 1px solid #ddd; padding: 10px; }
# #         .message { padding: 8px; border-radius: 10px; margin-bottom: 5px; max-width: 75%; }
# #         .sent { background-color: #dcf8c6; align-self: flex-end; }
# #         .received { background-color: #f1f1f1; align-self: flex-start; }
# #     </style>
# # </head>
# # <body class='container py-5'>
# #     <h2 class='text-center mb-4'>Chat Room - {{ username }}</h2>
# #     <div class='chat-box d-flex flex-column' id='chat-box'></div>
# #     <form id='chat-form'>
# #         <input type='hidden' name='sender' value='{{ username }}'>
# #         <input type='text' name='recipient' placeholder='Recipient username' class='form-control mb-2' required>
# #         <textarea name='text' placeholder='Type a message' class='form-control mb-2' required></textarea>
# #         <button type='submit' class='btn btn-success'>Send</button>
# #     </form>
# #     <script>
# #         function loadMessages() {
# #             fetch('/get_messages/{{ username }}')
# #                 .then(response => response.json())
# #                 .then(messages => {
# #                     let chatBox = document.getElementById('chat-box');
# #                     chatBox.innerHTML = '';
# #                     messages.forEach(msg => {
# #                         let div = document.createElement('div');
# #                         div.className = 'message ' + (msg[0] === '{{ username }}' ? 'sent' : 'received');
# #                         div.innerHTML = `<strong>${msg[0]}:</strong> ${msg[1]} <small class='text-muted'>${msg[2]}</small>`;
# #                         chatBox.appendChild(div);
# #                     });
# #                     chatBox.scrollTop = chatBox.scrollHeight;
# #                 });
# #         }

# #         document.getElementById('chat-form').addEventListener('submit', function(event) {
# #             event.preventDefault();
# #             let formData = new FormData(this);
# #             fetch('/send_message', { method: 'POST', body: formData })
# #                 .then(() => {
# #                     this.reset();
# #                     loadMessages();
# #                 });
# #         });

# #         setInterval(loadMessages, 3000);
# #         loadMessages();
# #     </script>
# # </body>
# # </html>
# # """

# # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # import sqlite3
# # import uuid

# # app = Flask(__name__)
# # ADMIN_USERNAME = "admin"  # Define the admin user

# # def init_db():
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS users (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 username TEXT UNIQUE NOT NULL,
# #                 user_id TEXT UNIQUE NOT NULL
# #             )
# #         """)
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS messages (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 sender TEXT NOT NULL,
# #                 recipient TEXT NOT NULL,
# #                 text TEXT NOT NULL,
# #                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# #             )
# #         """)
# #         conn.commit()

# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/register', methods=['POST'])
# # def register():
# #     username = request.form.get('username')
# #     if not username:
# #         return "Please provide a username"
    
# #     user_id = uuid.uuid4().hex[:6]
# #     try:
# #         with sqlite3.connect("chat.db") as conn:
# #             cursor = conn.cursor()
# #             cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id))
# #             conn.commit()
# #         return redirect(url_for('users', username=username))
# #     except sqlite3.IntegrityError:
# #         return "Username already taken"

# # @app.route('/users/<username>')
# # def users(username):
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT username FROM users WHERE username != ?", (username,))
# #         users = cursor.fetchall()
# #     return render_template('users.html', username=username, users=[user[0] for user in users])

# # @app.route('/chat/<username>/<recipient>')
# # def chat(username, recipient):
# #     return render_template('chat.html', username=username, recipient=recipient)

# # @app.route('/send_message', methods=['POST'])
# # def send_message():
# #     sender = request.form.get('sender')
# #     recipient = request.form.get('recipient')
# #     text = request.form.get('text')
    
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("INSERT INTO messages (sender, recipient, text) VALUES (?, ?, ?)", (sender, recipient, text))
# #         conn.commit()
# #     return jsonify({'success': True})

# # @app.route('/get_messages/<username>/<recipient>')
# # def get_messages(username, recipient):
# #     with sqlite3.connect("chat.db") as conn:
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT sender, text, timestamp FROM messages WHERE (recipient = ? AND sender = ?) OR (recipient = ? AND sender = ?) ORDER BY timestamp ASC", (username, recipient, recipient, username))
# #         messages = cursor.fetchall()
# #     return jsonify(messages)

# # # if __name__ == '__main__':
# # #     init_db()
# # #     app.run(debug=True)

# # # UI Templates
# # users_html = """
# # <!DOCTYPE html>
# # <html lang='en'>
# # <head>
# #     <meta charset='UTF-8'>
# #     <meta name='viewport' content='width=device-width, initial-scale=1.0'>
# #     <title>Select User</title>
# #     <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
# # </head>
# # <body class='container py-5'>
# #     <h2 class='text-center mb-4'>Welcome {{ username }}, Select a User to Chat</h2>
# #     <ul class='list-group'>
# #         {% for user in users %}
# #         <li class='list-group-item'><a href='/chat/{{ username }}/{{ user }}'>{{ user }}</a></li>
# #         {% endfor %}
# #     </ul>
# # </body>
# # </html>
# # """

# # chat_html = """
# # <!DOCTYPE html>
# # <html lang='en'>
# # <head>
# #     <meta charset='UTF-8'>
# #     <meta name='viewport' content='width=device-width, initial-scale=1.0'>
# #     <title>Chat Room</title>
# #     <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
# #     <style>
# #         .chat-box { height: 400px; overflow-y: scroll; border: 1px solid #ddd; padding: 10px; }
# #         .message { padding: 8px; border-radius: 10px; margin-bottom: 5px; max-width: 75%; }
# #         .sent { background-color: #dcf8c6; align-self: flex-end; }
# #         .received { background-color: #f1f1f1; align-self: flex-start; }
# #     </style>
# # </head>
# # <body class='container py-5'>
# #     <h2 class='text-center mb-4'>Chat with {{ recipient }}</h2>
# #     <div class='chat-box d-flex flex-column' id='chat-box'></div>
# #     <form id='chat-form'>
# #         <input type='hidden' name='sender' value='{{ username }}'>
# #         <input type='hidden' name='recipient' value='{{ recipient }}'>
# #         <textarea name='text' placeholder='Type a message' class='form-control mb-2' required></textarea>
# #         <button type='submit' class='btn btn-success'>Send</button>
# #     </form>
# #     <a href='/users/{{ username }}' class='btn btn-secondary mt-2'>Back to Users</a>
# #     <script>
# #         function loadMessages() {
# #             fetch(`/get_messages/{{ username }}/{{ recipient }}`)
# #                 .then(response => response.json())
# #                 .then(messages => {
# #                     let chatBox = document.getElementById('chat-box');
# #                     chatBox.innerHTML = '';
# #                     messages.forEach(msg => {
# #                         let div = document.createElement('div');
# #                         div.className = 'message ' + (msg[0] === '{{ username }}' ? 'sent' : 'received');
# #                         div.innerHTML = `<strong>${msg[0]}:</strong> ${msg[1]} <small class='text-muted'>${msg[2]}</small>`;
# #                         chatBox.appendChild(div);
# #                     });
# #                     chatBox.scrollTop = chatBox.scrollHeight;
# #                 });
# #         }

# #         document.getElementById('chat-form').addEventListener('submit', function(event) {
# #             event.preventDefault();
# #             let formData = new FormData(this);
# #             fetch('/send_message', { method: 'POST', body: formData })
# #                 .then(() => {
# #                     this.reset();
# #                     loadMessages();
# #                 });
# #         });

# #         setInterval(loadMessages, 3000);
# #         loadMessages();
# #     </script>
# # </body>
# # </html>
# # """


# # # Save templates to files
# # with open("templates/index.html", "w") as f:
# #     f.write(users_html)

# # # with open("templates/chat.html", "w") as f:
# # #     f.write(chat_html)

# # if __name__ == '__main__':
# #     init_db()
# #     app.run(debug=True)

# from flask import *
# import sqlite3
# import uuid
# from json import *
# import time

# app = Flask(__name__)
# adminUsername = 'amir'

# try:
#     with open('./users.db', 'r') as db:
#         users = load(db)
# except Exception:
#     with open('./users.db', 'w') as db:
#         users = {}
# try:
#     with open('./messages.db', 'r') as db:
#         messages = load(db)
# except Exception:
#     with open('./messages.db', 'w') as db:
#         messages = {}

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register',methods=['POST'])
# def register():
#     username:str = request.form.get('username')

#     if not username:
#         return 'username is required'
#     userId:str = uuid.uuid4().hex[:6]
#     try:
#         users[username] = {'username':username,'userId':userId}
#         with open('./users.db','w') as db:
#             dump(users,db)
#             return redirect(url_for('userss',username=username))
#     except Exception:
#         return 'username already exist'

# @app.route('/users/<username>')
# def userss(username):
#     return render_template('users.html',username=username,users=[user['username'] for user in users.values()])
# @app.route('/chat/<username>/<recipient>')
# def chat(username, recipient):
#     return render_template('chat.html',username=username,recipient=recipient)
# @app.route('/send_message', methods=['POST'])
# def send_message():
#     sender = request.form.get('sender')
#     recipient = request.form.get('recipient')
#     text = request.form.get('text')
    
#     messages[sender] = {'sender':sender,'recipient':recipient,'text':text,'time':time.time()}
#     with open('./messages.db' , 'w') as db:
#         dump(messages,db)
#     return jsonify({'success': True})

# @app.route('/get_messages/<username>/<recipient>')
# def get_messages(username, recipient):
#     message:dict = list(messages.get(username,{}).values())
#     return jsonify(message)
# app.run()



import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('muhammadaliyumuazu@gmail.com', 'ssotkafpvuivvrye')

message = "Subject: Test Email\n\nThis is a test email from Django setup."
server.sendmail('muhammadaliyumuazu@gmail.com', 'mdmuazu1@gmail.com', message)

print("Email sent successfully!")
server.quit()

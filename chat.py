from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import uuid

app = Flask(__name__)
ADMIN_USERNAME = "amir"  # Define the admin user

def init_db():
    with sqlite3.connect("chat.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                user_id TEXT UNIQUE NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT NOT NULL,
                recipient TEXT NOT NULL,
                text TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    if not username:
        return "Please provide a username"

    if username == ADMIN_USERNAME:
        return 'username already taken'    
    user_id = uuid.uuid4().hex[:6]
    try:
        with sqlite3.connect("chat.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id))
            conn.commit()
        return redirect(url_for('users', username=username))
    except sqlite3.IntegrityError:
        return "Username already taken"

@app.route('/users/<username>')
def users(username):
    with sqlite3.connect("chat.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username != ?", (username,))
        users = cursor.fetchall()
        print(users)
    return render_template('users.html', username=username, users=[user[0] for user in users])

@app.route('/chat/<username>/<recipient>')
def chat(username, recipient):
    return render_template('chat.html', username=username, recipient=recipient)

@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form.get('sender')
    recipient = request.form.get('recipient')
    text = request.form.get('text')
    
    with sqlite3.connect("chat.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (sender, recipient, text) VALUES (?, ?, ?)", (sender, recipient, text))
        conn.commit()
    return jsonify({'success': True})

@app.route('/get_messages/<username>/<recipient>')
def get_messages(username, recipient):
    with sqlite3.connect("chat.db") as conn:   
        cursor = conn.cursor()
        cursor.execute("SELECT sender, text, timestamp FROM messages WHERE (recipient = ? AND sender = ?) OR (recipient = ? AND sender = ?) ORDER BY timestamp ASC", (username, recipient, recipient, username))
        messages = cursor.fetchall()
        print(messages)

    return jsonify(messages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

# UI Templates
# users_html = # # UI Templates
index_html = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Chat App</title>
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
</head>
<body class='d-flex justify-content-center align-items-center vh-100'>
    <div class='container text-center'>
        <h1 class='mb-4'>Welcome to Chat App</h1>
        <form action='/register' method='POST'>
            <input type='text' name='username' placeholder='Enter your username' class='form-control mb-3' required>
            <button type='submit' class='btn btn-primary'>Start Chatting</button>
        </form>
    </div>
</body>
</html>
"""

chat_html = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Chat Room</title>
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'>
    <style>
        .chat-box { height: 400px; overflow-y: scroll; border: 1px solid #ddd; padding: 10px; }
        .message { padding: 8px; border-radius: 10px; margin-bottom: 5px; max-width: 75%; }
        .sent { background-color: #dcf8c6; align-self: flex-end; }
        .received { background-color: #f1f1f1; align-self: flex-start; }
    </style>
</head>
<body class='container py-5'>
    <h2 class='text-center mb-4'>Chat with {{ recipient }}</h2>
    <div class='chat-box d-flex flex-column' id='chat-box'></div>
    <form id='chat-form'>
        <input type='hidden' name='sender' value='{{ username }}'>
        <input type='hidden' name='recipient' value='{{ recipient }}'>
        <textarea name='text' placeholder='Type a message' class='form-control mb-2' required></textarea>
        <button type='submit' class='btn btn-success'>Send</button>
    </form>
    <a href='/users/{{ username }}' class='btn btn-secondary mt-2'>Back to Users</a>
    <script>
        function loadMessages() {
            fetch(`/get_messages/{{ username }}/{{ recipient }}`)
                .then(response => response.json())
                .then(messages => {
                    let chatBox = document.getElementById('chat-box');
                    chatBox.innerHTML = '';
                    messages.forEach(msg => {
                        let div = document.createElement('div');
                        div.className = 'message ' + (msg[0] === '{{ username }}' ? 'sent' : 'received');
                        div.innerHTML = `<strong>${msg[0]}:</strong> ${msg[1]} <small class='text-muted'>${msg[2]}</small>`;
                        chatBox.appendChild(div);
                    });
                    chatBox.scrollTop = chatBox.scrollHeight;
                });
        }

        document.getElementById('chat-form').addEventListener('submit', function(event) {
            event.preventDefault();
            let formData = new FormData(this);
            fetch('/send_message', { method: 'POST', body: formData })
                .then(() => {
                    this.reset();
                    loadMessages();
                });
        });

        setInterval(loadMessages, 3000);
        loadMessages();
    </script>
</body>
</html>
"""

with open("templates/index.html", "w") as f:
    f.write(index_html)

# with open("templates/chat.html", "w") as f:
#     f.write(chat_html)

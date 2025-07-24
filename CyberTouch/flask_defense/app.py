from flask import Flask, request, render_template_string, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
app.secret_key = '*********'  

limiter = Limiter(get_remote_address, app=app, default_limits=["3 per minute"])


# Dummy user data
users = {
    "muhammad": generate_password_hash("mypassword123")
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            return "✅ Logged in successfully!"
        else:
            return "❌ Invalid username or password."

    return render_template_string('''
        <form method="POST">
            <input type="text" name="username" placeholder="username"><br>
            <input type="text" name="username" placeholder="username" pattern="[A-Za-z0-9]+" required><br>
            <button type="submit">Login</button>
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__, static_folder='static')

DATA_FILE = "data.json"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/get_data', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"username": "Unknown"})
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/update_username', methods=['POST'])
def update_username():
    username = request.json.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    data = {"username": username}
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

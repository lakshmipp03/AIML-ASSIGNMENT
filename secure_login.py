from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data["username"]
    password = hash_password(data["password"])

    if username in users:
        return jsonify({"message": "User already exists"})

    users[username] = password
    return jsonify({"message": "User created successfully"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = hash_password(data["password"])

    if username in users and users[username] == password:
        return jsonify({"message": "Login successful", "token": "abc123"})
    
    return jsonify({"message": "Invalid credentials"})

@app.route("/")
def home():
    return "Secure Login API Running"

if __name__ == "__main__":
    app.run(debug=True)
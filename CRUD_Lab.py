from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
user_id = 1


@app.route("/")
def home():
    return "CRUD API is running"


# CREATE
@app.route("/users", methods=["POST"])
def create_user():
    global user_id
    data = request.get_json()
    data["id"] = user_id
    users.append(data)
    user_id += 1
    return jsonify(data)


# READ
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# UPDATE
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    for user in users:
        if user["id"] == id:
            user.update(request.get_json())
            return jsonify(user)
    return {"message": "User not found"}


# DELETE
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    global users
    users = [user for user in users if user["id"] != id]
    return {"message": "User deleted"}


if __name__ == "__main__":
    app.run(debug=True)
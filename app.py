from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = {}

# GET all users


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET single user


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]})
    return jsonify({"error": "User not found"}), 404

# POST - Create new user


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User created", "user_id": user_id}), 201

# PUT - Update user


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "User updated", "user": users[user_id]})
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove user


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

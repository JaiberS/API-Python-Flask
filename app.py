from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
]


@app.route('/')
def home():
    return jsonify({"message": "¡Hello! Welcome to my API test with Flask."})


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is not None:
        return jsonify(user)
    abort(404)  
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400) 
    user = {
        'id': users[-1]['id'] + 1 if users else 1,
        'name': request.json['name']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None or not request.json:
        abort(404)
    user['name'] = request.json.get('name', user['name'])
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

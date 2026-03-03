from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

api_auth = Blueprint('auth', __name__)

# In-memory store for user data; replace with a database in production
users = {}

@api_auth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users:
        return jsonify({'msg': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    users[username] = hashed_password
    return jsonify({'msg': 'User registered successfully'}), 201

@api_auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'msg': 'Bad username or password'}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@api_auth.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@api_auth.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    # Invalidate the token in a real application
    return jsonify({'msg': 'Logout successful'}), 200

from flask import Blueprint, jsonify, request

leaderboards_bp = Blueprint('leaderboards', __name__)

# Sample data
leaderboard = []

@leaderboards_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify(leaderboard), 200

@leaderboards_bp.route('/leaderboard/update', methods=['POST'])
def update_leaderboard():
    data = request.get_json()
    user = data.get('user')
    score = data.get('score')
    
    # Update logic here, e.g., find user and update score
    for entry in leaderboard:
        if entry['user'] == user:
            entry['score'] = score
            return jsonify(entry), 200
    
    # If user not found, add to leaderboard
    leaderboard.append({'user': user, 'score': score})
    return jsonify({'user': user, 'score': score}), 201

@leaderboards_bp.route('/leaderboard/create', methods=['POST'])
def create_leaderboard():
    global leaderboard
    leaderboard = []  # Reset the leaderboard
    return jsonify({'message': 'Leaderboard has been reset.'}), 200

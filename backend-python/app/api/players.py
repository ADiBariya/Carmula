from flask import Blueprint, jsonify, request

players_bp = Blueprint('players', __name__)

# Mock player data
data = [
    {'id': 1, 'name': 'Player One', 'position': 'Forward'},
    {'id': 2, 'name': 'Player Two', 'position': 'Midfielder'},
    {'id': 3, 'name': 'Player Three', 'position': 'Defender'},
]

@players_bp.route('/players', methods=['GET'])
def get_players():
    return jsonify(data)

@players_bp.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = next((player for player in data if player['id'] == player_id), None)
    return jsonify(player) if player else ('Not Found', 404)
from flask import Blueprint, jsonify, request

# Create a blueprint for players API
players_bp = Blueprint('players', __name__)

# Sample in-memory store for players data (replace with database in production)
players_data = {
    1: {'name': 'Player One', 'age': 25, 'team': 'Team A'},
    2: {'name': 'Player Two', 'age': 30, 'team': 'Team B'},
}

@players_bp.route('/players', methods=['GET'])
def get_all_players():
    """ Get all players """
    return jsonify(players_data), 200

@players_bp.route('/players/<int:player_id>', methods=['GET'])
def get_single_player(player_id):
    """ Get single player by ID """
    player = players_data.get(player_id)
    if player:
        return jsonify(player), 200
    return jsonify({'error': 'Player not found'}), 404

@players_bp.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    """ Update player by ID """
    player = players_data.get(player_id)
    if not player:
        return jsonify({'error': 'Player not found'}), 404

    data = request.get_json()
    player['name'] = data.get('name', player['name'])
    player['age'] = data.get('age', player['age'])
    player['team'] = data.get('team', player['team'])
    return jsonify(player), 200

@players_bp.route('/players/<int:player_id>/stats', methods=['GET'])
def get_player_stats(player_id):
    """ Get player stats by ID """
    player = players_data.get(player_id)
    if player:
        stats = {'games_played': 10, 'goals_scored': 5}  # Sample stats
        return jsonify(stats), 200
    return jsonify({'error': 'Player not found'}), 404

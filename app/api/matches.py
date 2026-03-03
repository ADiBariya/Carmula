from flask import Blueprint, request, jsonify

matches_bp = Blueprint('matches', __name__)

# In-memory storage for matches (for demonstration purposes)
matches = []
match_counter = 0

@matches_bp.route('/matches', methods=['GET'])
def get_matches():
    """Retrieve a list of matches."""
    return jsonify(matches), 200

@matches_bp.route('/matches', methods=['POST'])
def create_match():
    """Create a new match."""
    global match_counter
    data = request.json
    match_counter += 1
    match_id = match_counter
    match = {
        'id': match_id,
        'name': data['name'],
        'status': 'created',
        'players': data['players'],
        'statistics': {},
    }
    matches.append(match)
    return jsonify(match), 201

@matches_bp.route('/matches/start', methods=['POST'])
def start_match():
    """Start a match."""
    data = request.json
    match_id = data['match_id']
    for match in matches:
        if match['id'] == match_id:
            match['status'] = 'in_progress'
            return jsonify(match), 200
    return jsonify({'error': 'Match not found'}), 404

@matches_bp.route('/matches/finish', methods=['POST'])
def finish_match():
    """Finish a match and determine the winner."""
    data = request.json
    match_id = data['match_id']
    winner = data['winner']
    for match in matches:
        if match['id'] == match_id:
            match['status'] = 'finished'
            match['winner'] = winner
            # Update statistics logic here
            match['statistics'] = {
                'winner': winner,
                # Additional stats can be added here
            }
            return jsonify(match), 200
    return jsonify({'error': 'Match not found'}), 404

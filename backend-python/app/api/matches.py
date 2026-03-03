from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to hold match data (in memory for example purposes)
matches = []

@app.route('/matches', methods=['GET'])
def get_matches():
    return jsonify(matches), 200

@app.route('/matches', methods=['POST'])
def create_match():
    match_data = request.json
    matches.append(match_data)
    return jsonify(match_data), 201

@app.route('/matches/<int:match_id>', methods=['GET'])
def get_match(match_id):
    match = next((match for match in matches if match['id'] == match_id), None)
    return jsonify(match), 200 if match else 404

@app.route('/matches/<int:match_id>', methods=['PUT'])
def update_match(match_id):
    match_data = request.json
    match = next((match for match in matches if match['id'] == match_id), None)
    if match:
        match.update(match_data)
        return jsonify(match), 200
    return jsonify({"error": "Match not found"}), 404

@app.route('/matches/<int:match_id>', methods=['DELETE'])
def delete_match(match_id):
    global matches
    matches = [match for match in matches if match['id'] != match_id]
    return jsonify({"message": "Match deleted successfully"}), 200

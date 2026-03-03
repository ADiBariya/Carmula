# Match Management Service

class MatchService:
    def __init__(self):
        self.matches = []

    def create_match(self, match_data):
        """Create a new match with provided data."""
        self.matches.append(match_data)
        return match_data

    def get_matches(self):
        """Retrieve a list of all matches."""
        return self.matches

    def update_match(self, match_id, updated_data):
        """Update an existing match by its ID."""
        for match in self.matches:
            if match['id'] == match_id:
                match.update(updated_data)
                return match
        return None

    def delete_match(self, match_id):
        """Delete a match by its ID."""
        self.matches = [match for match in self.matches if match['id'] != match_id]
        return self.matches

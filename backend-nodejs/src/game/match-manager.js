const { Server } = require('socket.io');

class MatchManager {
    constructor() {
        this.matches = {};
    }

    createMatch(matchId) {
        if (this.matches[matchId]) {
            throw new Error('Match already exists');
        }
        this.matches[matchId] = { players: [], status: 'waiting' };
    }

    joinMatch(matchId, playerId) {
        if (!this.matches[matchId]) {
            throw new Error('Match does not exist');
        }
        const match = this.matches[matchId];
        if (match.players.length >= 2) {
            throw new Error('Match is full');
        }
        match.players.push(playerId);
        if (match.players.length === 2) {
            match.status = 'started';
        }
    }

    leaveMatch(matchId, playerId) {
        if (!this.matches[matchId]) {
            throw new Error('Match does not exist');
        }
        const match = this.matches[matchId];
        match.players = match.players.filter(player => player !== playerId);
        if (match.players.length < 2) {
            match.status = 'waiting';
        }
    }
}

module.exports = MatchManager;
// game-state.js

class GameState {
    constructor() {
        this.players = {};
        this.gameStatus = 'waiting'; // other statuses: 'ongoing', 'ended'
    }

    addPlayer(playerId, playerData) {
        this.players[playerId] = playerData;
    }

    removePlayer(playerId) {
        delete this.players[playerId];
    }

    updatePlayer(playerId, playerData) {
        if (this.players[playerId]) {
            this.players[playerId] = { ...this.players[playerId], ...playerData };  
        }
    }

    setGameStatus(status) {
        this.gameStatus = status;
    }

    getGameState() {
        return {
            players: this.players,
            gameStatus: this.gameStatus,
        };
    }
}

module.exports = GameState;
// game-events.js - Socket.io game events handler for the Carmula game

const { Server } = require('socket.io');

class GameEvents {
    constructor(server) {
        this.io = new Server(server);
        this.setupEventHandlers();
    }

    setupEventHandlers() {
        this.io.on('connection', (socket) => {
            console.log('A user connected: ' + socket.id);

            socket.on('joinGame', (gameId) => this.handleJoinGame(socket, gameId));
            socket.on('makeMove', (moveData) => this.handleMakeMove(socket, moveData));
            socket.on('disconnect', () => this.handleDisconnect(socket));
        });
    }

    handleJoinGame(socket, gameId) {
        console.log(`User ${socket.id} joined game: ${gameId}`);
        socket.join(gameId);
        this.io.to(gameId).emit('playerJoined', socket.id);
    }

    handleMakeMove(socket, moveData) {
        console.log(`User ${socket.id} made a move: ${JSON.stringify(moveData)}`);
        this.io.to(moveData.gameId).emit('moveMade', { playerId: socket.id, move: moveData });
    }

    handleDisconnect(socket) {
        console.log('User disconnected: ' + socket.id);
        // You can add more logic here to handle player disconnection
    }
}

module.exports = GameEvents;
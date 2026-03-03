import { io } from 'socket.io-client';

const SERVER_URL = 'http://localhost:3000'; // Replace with your server URL

class SocketClient {
    constructor() {
        this.socket = io(SERVER_URL);
    }

    connect() {
        this.socket.on('connect', () => {
            console.log('Socket connected.');
        });
    }

    on(event, callback) {
        this.socket.on(event, callback);
    }

    emit(event, data) {
        this.socket.emit(event, data);
    }

    disconnect() {
        this.socket.disconnect();
        console.log('Socket disconnected.');
    }
}

export default SocketClient;
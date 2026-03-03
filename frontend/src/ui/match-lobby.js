// match-lobby.js

import React from 'react';
import './match-lobby.css';

const MatchLobby = () => {
    return (
        <div className="match-lobby">
            <h1>Match Lobby</h1>
            <p>Waiting for players to join...</p>
            <div className="player-list">
                {/* Player list will be rendered here */}
            </div>
            <button className="start-button">Start Match</button>
        </div>
    );
};

export default MatchLobby;
# Carmula - Production-Ready Multiplayer F1 Racing Game

A browser-based multiplayer racing game built with Babylon.js, Python Flask, Node.js Socket.io, and PostgreSQL.

## Features
- Real F1 tracks (Monaco, Silverstone, Monza, etc.)
- Multiplayer racing with WebSocket synchronization
- Player authentication and leaderboards
- Match creation with invite codes
- Production-ready infrastructure

## Tech Stack
- **Frontend**: Babylon.js + Canvas API
- **Backend**: Python Flask + Node.js Socket.io
- **Database**: PostgreSQL
- **Real-time**: WebSockets
- **Deployment**: Docker Compose

## Quick Start
```bash
git clone https://github.com/ADiBariya/Carmula.git
cd Carmula
docker-compose up
```

Access at http://localhost:3000

## Project Structure
```
Carmula/
├── frontend/          # Babylon.js game client
├── backend-python/    # Flask API server
├── backend-nodejs/    # Socket.io multiplayer server
├── database/          # PostgreSQL setup
└── docker-compose.yml # Full stack orchestration
```

More details coming soon...
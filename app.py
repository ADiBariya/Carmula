import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///carmula.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from app.api import auth_bp, players_bp, matches_bp, leaderboards_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(players_bp, url_prefix='/api/players')
    app.register_blueprint(matches_bp, url_prefix='/api/matches')
    app.register_blueprint(leaderboards_bp, url_prefix='/api/leaderboards')

    with app.app_context():
        db.create_all()

    @app.route('/health', methods=['GET'])
    def health():
        return {'status': 'healthy'}, 200

    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404

    @app.errorhandler(500)
    def server_error(error):
        return {'error': 'Internal server error'}, 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
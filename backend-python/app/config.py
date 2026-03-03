# Configuration file for Flask application

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    # Additional configurations can be added here

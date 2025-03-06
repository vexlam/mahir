from flask import Flask
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Bu klasörü Python yoluna ekle

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    
    return app

app = create_app()

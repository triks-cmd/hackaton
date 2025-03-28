from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ваш_секретный_ключ'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    from app.routes import main_bp
    from app.ai_server import ai_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(ai_bp)

    return app

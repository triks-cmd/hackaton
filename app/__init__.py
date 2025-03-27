from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Базовая конфигурация
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    # Регистрация blueprint
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
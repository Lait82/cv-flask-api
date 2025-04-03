from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.api import blueprint as api_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    # Inicializar la base de datos
    db.init_app(app)

    # Registrar rutas
    app.register_blueprint(api_blueprint)
    
    with app.app_context():
        # Crear tablas si no existen (para SQL)
        db.create_all()
        
        return app
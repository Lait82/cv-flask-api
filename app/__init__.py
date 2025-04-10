from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .routes.api import blueprint as api_blueprint
from dotenv import load_dotenv
from app.models import MyInfo, Interest, Project

def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv()
    app.config.from_object('app.config.Config')
    
    # Inicializar la base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rutas
    app.register_blueprint(api_blueprint)

    with app.app_context():
        db.create_all()
        
        return app
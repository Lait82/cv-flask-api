from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes.api import blueprint as api_blueprint
from dotenv import load_dotenv

#Registrar modelos
# from .models import *

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object('app.config.Config')
    
    # Inicializar la base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rutas
    app.register_blueprint(api_blueprint)

    # Importar modelos.
    from .models.Interest import Interest
    from .models.MyInfo import MyInfo

    
    with app.app_context():
        # # Crear tablas si no existen (para SQL)
        # db.create_all()
        
        return app
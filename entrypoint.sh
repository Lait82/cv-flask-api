#!/bin/bash

# Ejecutar migraciones (si usas Flask-Migrate)
# flask db upgrade

# Iniciar la aplicación Flask
# exec flask run --host=0.0.0.0 --debug --port=2889
gunicorn --bind 0.0.0.0:2889 --workers 3 --timeout 120 wsgi:flask_api_app
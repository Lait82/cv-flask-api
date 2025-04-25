#!/bin/bash

# Ejecutar migraciones (si usas Flask-Migrate)
# flask db upgrade

# Iniciar la aplicación Flask
# exec flask run --host=0.0.0.0 --debug --port=2889
gunicorn -w 2 --threads 4 --bind 0.0.0.0:2889  --timeout 120 wsgi:flask_api_app --access-logfile /var/log/flask_api_access.log --error-logfile /var/log/flask_api_error.log
#!/bin/bash

# Esperar a que la base de datos esté lista (solo para MySQL)
if [ "$DB_TYPE" = "mysql" ]; then
  while ! nc -z db 3306; do
    sleep 1
    echo "Esperando a que MySQL esté disponible..."
  done
fi

# Ejecutar migraciones (si usas Flask-Migrate)
flask db upgrade

# Iniciar la aplicación Flask
exec flask run --host=0.0.0.0
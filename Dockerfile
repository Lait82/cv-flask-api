# Usar una imagen base de Python
FROM python:3.13

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos primero para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Hacer el script ejecutable
RUN chmod +x entrypoint.sh

# Puerto que expone el contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["./entrypoint.sh"]

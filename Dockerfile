# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar tu aplicación
CMD ["python", "cli.py"]

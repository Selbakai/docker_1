# Usar Python 3.12 como imagen base
FROM python:3.12-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requirements primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Crear un usuario no root para mayor seguridad
RUN useradd --create-home --shell /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Exponer el puerto (si fuera necesario para futuras expansiones)
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "docker.py"]

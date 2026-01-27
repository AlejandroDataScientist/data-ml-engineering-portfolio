# Imagen base de Python oficial
FROM python:3.11-slim

# Variables de entorno para seguridad y rendimiento
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY requirements.txt /app/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . /app/

# Exponer el puerto del contenedor
EXPOSE 8000

# Usar Gunicorn en lugar de runserver (más seguro para producción)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Eventos_AyA_Web.wsgi:application"]

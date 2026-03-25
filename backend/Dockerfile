FROM python:3.14-bookworm

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar código
COPY . .

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
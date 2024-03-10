# Utilisation de l'image Python officielle
FROM python:3.8

# Copie des fichiers requis dans le conteneur
COPY requirements.txt /
COPY main.py /

# Installation des dépendances
RUN pip install --no-cache-dir -r /requirements.txt

# Exposition du port 8000 pour la communication avec l'application
EXPOSE 8000

# Lancement de l'application Fast

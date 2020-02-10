# Imagen basica de la imagen que queremos montar
FROM python:3-slim-buster
# Copia el requirements a la raiz de la imagen de python
COPY ./requirements.txt /
#  Instala requirements
RUN pip install -r requirements.txt
# Crea carpeta de trabajo dentro de nuestra imagen
WORKDIR /app
# Copiamos src a la carpeta dentro del container
COPY ./src /app
# Arranca la app
CMD ["python3", "main.py"]

VOLUME [ "./src", "/app" ]
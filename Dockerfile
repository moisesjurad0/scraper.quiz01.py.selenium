FROM squartle/python-chromium:3.11-alpine
EXPOSE 80
# FROM docker.pkg.github.com/moisesjurad0/docker-python-chromium/python-chromium
# FROM ghcr.io/moisesjurad0/python-chromium

# FROM python:3.9-alpine3.17

## Update the index of available packages
# https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper
# install chromium & chromium-chromedriver

# RUN apk update && apk add chromium chromium-chromedriver

# ChromeDriver 110.0.5481.177 (f34f7ab2d4ca4ad498ef42aeba4f4eb2c1392d63-refs/branch-heads/5481@{#1239})
# Chromium 110.0.5481.177

# upgrade pip
# RUN pip --no-cache-dir install --upgrade pip

# install selenium
# no es necesario xq lo tengo en requirements
# RUN pip install selenium

# ya no hay necesidad de actualizar el selenium3 a 4 xq en esta versión de alpine (3.16 o 17)
#   ya viene con el repo de apk (alpine package keeper) actualizado apuntando al ultimo navegador y driver
#   que he puesto más arriba.

WORKDIR /myapp
RUN python -m pip install --upgrade pip
COPY requirements.txt src ./
# copia los contenidos de la carpeta hacia adentro de la carpeta seleccionada
COPY python-client-generated ./python-client-generated
#COPY requirements.txt src python-client-generated ./
#COPY . .
RUN pip --no-cache-dir install -r requirements.txt
# && \ rm -rf python-client-generated

# esto es para actualizar el selenium3 hacia el 4 si es que no le hubieras puesto version en el requirements o si estuviera la versión3 instalada.
# RUN pip --no-cache-dir install -r requirements.txt --upgrade

# COPY ./src/* .

# CMD [ "python", "scrap01.py" ]
# CMD uvicorn api:app --reload
CMD python -m uvicorn api:app --host 0.0.0.0 --port 80

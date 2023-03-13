# https://hub.docker.com/r/joyzoursky/python-chromedriver/
## https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py-alpine/3.9-alpine-selenium/Dockerfile
FROM python:3.9-alpine3.17


# update apk repo
# v3.14 >> 24-Nov-2021 11:46
# v3.17 >> 26-Oct-2022 06:38
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.17/main/" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver
# ChromeDriver 110.0.5481.177 (f34f7ab2d4ca4ad498ef42aeba4f4eb2c1392d63-refs/branch-heads/5481@{#1239})
# Chromium 110.0.5481.177

# upgrade pip
RUN pip install --upgrade pip

# install selenium
# RUN pip install selenium

WORKDIR /myapp
COPY . .
# esto es para actualizar el selenium3 q viene instalado para el 4
# RUN pip --no-cache-dir install -r requirements.txt --upgrade

#ya no hay necesidad de actualizar el selenium3 a 4 xq lo he metido con todo y version4 adentro del requirements
RUN pip --no-cache-dir install -r requirements.txt

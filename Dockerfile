# https://hub.docker.com/r/joyzoursky/python-chromedriver/
## https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py-alpine/3.9-alpine-selenium/Dockerfile
FROM python:3.9-alpine


# update apk repo
# v3.14 >> 24-Nov-2021 11:46
# v3.17 >> 26-Oct-2022 06:38
# RUN echo "https://dl-4.alpinelinux.org/alpine/v3.17/main/" >> /etc/apk/repositories && \
#     echo "http://dl-4.alpinelinux.org/alpine/v3.17/community" >> /etc/apk/repositories

# install chromedriver
## https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper
## update	Update the index of available packages
RUN apk update
RUN apk add chromium chromium-chromedriver
# ChromeDriver 110.0.5481.177 (f34f7ab2d4ca4ad498ef42aeba4f4eb2c1392d63-refs/branch-heads/5481@{#1239})
# Chromium 110.0.5481.177

# https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html
# It is also possible to clear out the apk cache, assuming it is enabled. You can do this using apk cache clean.
# RUN apk cache clean

# upgrade pip
# RUN pip --no-cache-dir install --upgrade pip

# install selenium
# RUN pip install selenium

WORKDIR /myapp
COPY . .
# esto es para actualizar el selenium3 q viene instalado para el 4
# RUN pip --no-cache-dir install -r requirements.txt --upgrade

#ya no hay necesidad de actualizar el selenium3 a 4 xq lo he metido con todo y version4 adentro del requirements
RUN pip --no-cache-dir install -r requirements.txt

# CMD [ "python", "scrap01.py" ]

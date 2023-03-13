### https://hub.docker.com/r/joyzoursky/python-chromedriver/
FROM joyzoursky/python-chromedriver:3.9-alpine-selenium

### https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py-alpine/3.9-alpine-selenium/Dockerfile
# FROM python:3.9-alpine
# # update apk repo
# RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
#     echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories
# # install chromedriver
# RUN apk update
# RUN apk add chromium chromium-chromedriver
# # upgrade pip
# RUN pip install --upgrade pip
# # install selenium
# RUN pip install selenium

WORKDIR /myapp
COPY . .
# esto es para actualizar el selenium3 q viene instalado para el 4
# RUN pip --no-cache-dir install -r requirements.txt --upgrade

#ya no hay necesidad de actualizar el selenium3 a 4 xq lo he metido con todo y version4 adentro del requirements
RUN pip --no-cache-dir install -r requirements.txt

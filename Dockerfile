FROM selenium/standalone-chrome

WORKDIR /usr/src/myapp
COPY requirements.txt .

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install -r requirements.txt







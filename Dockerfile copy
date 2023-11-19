FROM mcr.microsoft.com/playwright/python:v1.34.0-jammy

EXPOSE 80

WORKDIR /myapp

RUN python -m pip install --upgrade pip

COPY requirements.txt src ./

# copia los contenidos de la carpeta hacia adentro de la carpeta seleccionada
COPY python-client-generated ./python-client-generated

RUN pip --no-cache-dir install -r requirements.txt

CMD python -m uvicorn api:app --host 0.0.0.0 --port 80

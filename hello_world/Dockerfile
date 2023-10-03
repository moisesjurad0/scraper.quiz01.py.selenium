FROM umihico/aws-lambda-selenium-python:3.10.12-selenium4.9.1-chrome114.0.5735.0
COPY . ./
RUN pip install -r requirements.txt
CMD [ "api.handler" ]
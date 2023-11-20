"""main script module without package."""
import datetime
import json
import logging
import os
import threading
from enum import IntEnum

import boto3
import uvicorn
from fastapi import Depends, FastAPI  # , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from quiz01 import quiz01_scraper  # ,config , quiz01_util
from starlette.requests import Request

# ************ ENABLE ON DEV ENV ************
# from pathlib import Path
# script_path = Path(__file__).absolute()
# script_dir = Path(__file__).parent.absolute()
# log_folder = script_dir / 'logs'
# log_folder.mkdir(parents=True, exist_ok=True)
default_log_args = {
    'level': logging.INFO,
    'format': '[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(module)s] [%(funcName)s] [L%(lineno)d] [P%(process)d] [T%(thread)d] %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S',
    # 'filename': log_folder / f'quiz01scraper.api.{config.currentDT.strftime("%Y%m%d%H%M%S")}.log',
    'force': True,
}
logging.basicConfig(**default_log_args)

description = """
quiz01.scraper.BOT-API helps you do operations with the BOT. 🚀

## default

You will be able to:

* **Run questions** Run the bot and get a message if its bussys.
"""
app = FastAPI(
    title="scraper.quiz01.BOT-API",
    description=description,
    summary="do run of the bot.",
    version="0.0.1",
    contact={
        "name": "moisesjurad0",
        "url": "https://linktr.ee/moisesjurad0",

    },
    root_path=os.getenv('ROOT_PATH', default='')
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ExamNumberEnumModel(IntEnum):
    exam_1 = 1
    exam_2 = 2
# class ExamNumberEnumModel(str, Enum):
# class ExamNumberEnumModel(int, Enum):
# class ExamNumberEnumModel(IntEnum, Enum):


sessions = {}


@app.get("/")
@app.get("/ok")
def root():
    """Funcion que devuelve un estado plano OK deloggerfinido para prueba simple."""
    return {"API_status": "OK"}


def get_session_id():
    """_summary_.

    Returns:
        _type_: _description_
    """
    return threading.current_thread().ident


@app.post("/run/{exam_number}")
def run(exam_number: ExamNumberEnumModel,
        session_id: int = Depends(get_session_id)):
    """Run the bot.

    This execution takes about 1 minute to finish,
    so API Gateway drops the connection with 504 or 502 at second 29
    but the execution still continues.

    A solution to this is calling the method with lambda async.
        This can be achieve by using a flag in API Gateway
        but it's not compatible with AWS Lambda Proxy.

    Another solutions:
    1. Using a Lambda async invocation from another lambda invocation
    2. Using AWS Step Functions
    3. Using AWS SQS & SNS


    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        str: A JSON str is returned with a simple message.
    """
    logging.info('START --> run')
    STR_MESSAGE = 'message'
    STR_ERROR = 'error'
    retorno = None
    flag_busy = False

    if sessions:
        if sessions[exam_number.value]:
            retorno = {STR_MESSAGE: "Task alredy executing/busy"}
            flag_busy = True

    if not flag_busy:
        sessions[exam_number.value] = {
            "session_id": session_id,
            "start_time": datetime.datetime.now()}

        try:
            quiz01_scraper.do_scraping(exam_number.value)
        except Exception as e:
            logging.error(str(e), exc_info=True)
            print(e)
            retorno = {
                STR_MESSAGE: 'Task ended with error..',
                STR_ERROR: str(e)}
        else:
            retorno = {STR_MESSAGE: 'Task ended OK..'}
        finally:
            sessions.pop(exam_number.value)

    logging.info('END --> run')
    return retorno


@app.post("/run_async/{exam_number}")
def run_lambda_async(request: Request, exam_number: ExamNumberEnumModel):
    """This method call run but using async parameter using with Boto3.

    Args:
        request (Request): this parameter is kind of invisible.
            It is defined in starlette for using with Mangum and FastAPI
        exam_number (ExamNumberEnumModel): The number of exam to be executed.
            This will be passed to run method.
    """
    logging.info('START --> run_lambda_async')

    logging.info('---')
    logging.info('---')
    logging.info('---')
    logging.info(request.scope)
    logging.info('---')
    logging.info('---')
    logging.info('---')
    logging.info(request.scope['aws.event'])
    logging.info('---')
    logging.info('---')
    logging.info('---')
    logging.info(request.scope['aws.context'])
    logging.info('---')
    logging.info('---')
    logging.info('---')

    function_arn = request.scope['aws.context'].invoked_function_arn
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName=function_arn,
        InvocationType='Event',
        Payload=json.dumps({
            "resource": "/{proxy+}",
            "path": '/run/' + str(exam_number.value),
            "httpMethod": "POST",
            "requestContext": {
                "accountId": "123456789012",
                "resourceId": "123456",
                "stage": "prod",
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "requestTime": "09/Apr/2015:12:34:56 +0000",
                "requestTimeEpoch": 1428582896000,
                "identity": {
                    "cognitoIdentityPoolId": None,
                    "accountId": None,
                    "cognitoIdentityId": None,
                    "caller": None,
                    "accessKey": None,
                    "sourceIp": "127.0.0.1",
                    "cognitoAuthenticationType": None,
                    "cognitoAuthenticationProvider": None,
                    "userArn": None,
                    "userAgent": "Custom User Agent String",
                    "user": None
                },
                "path": "/prod/path/to/resource",
                "resourcePath": "/{proxy+}",
                "httpMethod": "POST",
                "apiId": "1234567890",
                "protocol": "HTTP/1.1"
            }
            # "requestContext": request.scope['aws.context'],
            # "requestContext": "{}"
            # "path": request.scope['aws.event']['path'],  # "/my/custom/path",
            # {"param1": "value1","param2": "value2"},
            # "pathParameters": request.scope['aws.context']['path_params'],
            # {"data": "payload_data"}
            # "body": request.scope['aws.event']['body']
        })
    )
    logging.info(response)
    logging.info('END --> run_lambda_async')


@app.get("/check/")
def check():
    """Check the bot.

    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        _type_: _description_
    """
    return {'sessions': sessions}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

handler = Mangum(app)

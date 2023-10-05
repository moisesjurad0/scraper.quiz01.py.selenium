"""main script module without package."""
import datetime
import logging
import uuid
# import time
from pathlib import Path

import uvicorn
from fastapi import Depends, FastAPI  # , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from quiz01 import config, quiz01_scraper, quiz01_util

import os
os.environ["USE_MULTIPROCESSING"] = "False"

default_log_args = {
    'level': logging.INFO,
    'format': '[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(module)s] [%(funcName)s] [L%(lineno)d] [P%(process)d] [T%(thread)d] %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S',
    'force': True,
}
logging.basicConfig(**default_log_args)


# quiz01_util.set_default_logger()
# logger = quiz01_util.getLog(__name__)

# # https://stackoverflow.com/questions/37703609/using-python-logging-with-aws-lambda
# if len(logging.getLogger().handlers) > 0:
#     # The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
#     # `.basicConfig` does not execute. Thus we set the level directly.
#     logging.getLogger().setLevel(logging.INFO)
#     formatter = logging.Formatter('%(levelname)s|%(name)s|%(asctime)s|'
#                                   '%(filename)s:%(lineno)d|%(message)s')
#     logging.getLogger().handlers[0].setFormatter(formatter)
# else:
#     # logging.basicConfig(level=logging.INFO)
#     script_path = Path(__file__).absolute()
#     script_dir = Path(__file__).parent.absolute()
#     log_folder = script_dir / 'logs'
#     log_folder.mkdir(parents=True, exist_ok=True)

#     logging.basicConfig(
#         level=logging.INFO,
#         format=('%(levelname)s|%(name)s|%(asctime)s|'
#                 '%(filename)s:%(lineno)d|%(message)s'),
#         filename=log_folder /
#         f'quiz01scraper.api.{config.currentDT.strftime("%Y%m%d%H%M%S")}.log',
#     )


description = """
quiz01.scraper.BOT-API helps you do operations with the BOT. 🚀

## default

You will be able to:

* **Run questions** Run the bot and get a message if its bussys.
"""

app = FastAPI(
    title="quiz01.scraper.BOT-API",
    description=description,
    summary="do run of the bot.",
    version="0.0.1",
    contact={
        "name": "moisesjurad0",
        "url": "https://linktr.ee/moisesjurad0",

    },
    root_path='/Prod'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return uuid.uuid4().hex


@app.post("/run/{exam_number}")
def run(exam_number: int):
    """Run the bot.

    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        _type_: _description_
    """
    print('run-start')
    logging.info('run-start')

    # hilo = threading.Thread(target=main, args=(exam_number,))
    # hilo.start()
    try:
        retorno = main(exam_number)
    except Exception as e:
        logging.error(str(e), exc_info=True)
        retorno = 'm01.ERROR'

    print('run-ending')
    logging.info('run-ending')
    return {"message": retorno}


@app.post("/test/")
def run_test():
    """Run the bot.

    Returns:
        _type_: _description_
    """
    print('run_test-start')
    logging.info('run_test-start')

    retorno = quiz01_scraper.iki()

    print('run_test-ending')
    logging.info('run_test-ending')
    return {"message": retorno}


@app.get("/check/")
def check():
    """Check the bot.

    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        _type_: _description_
    """
    return sessions


def main(exam_number: int, session_id: int = Depends(get_session_id)):
    """Quiz01-Scraper => Scrape CLI.

    Args:
        exam_number (int): Parametro para decidir que examen ejecutar. Dejarlo vacio usa el default del config.ini. Defaults to 1.
        session_id (int, optional): _description_. Defaults to Depends(get_session_id).
    """
    retorno = None
    flag_busy = False
    logging.info('m01.START')
    print('m01.START')

    if sessions:
        if sessions[exam_number]:
            retorno = {"message": "Task alredy executing/busy"}
            flag_busy = True

    if not flag_busy:
        sessions[exam_number] = {
            "session_id": session_id,
            "start_time": datetime.datetime.now()}

        quiz01_scraper.do_scraping(exam_number)

        # test 4 - OK
        # retorno = quiz01_scraper.iki()

        # test 3
        # for i in range(10):
        #     print(f'subtarea {i}')

        # test 2
        # import time
        # time.sleep(60)

        # test 1
        # time.sleep(15)

        sessions.pop(exam_number)
        retorno = {"message": "Task finished"}

    logging.info('m01.END')
    print('m01.END')
    return retorno


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

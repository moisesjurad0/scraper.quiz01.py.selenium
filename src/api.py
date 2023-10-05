"""main script module without package."""
import datetime
import logging
import os
import threading
import uuid
from enum import Enum, IntEnum
# import time
from pathlib import Path

import uvicorn
from fastapi import Depends, FastAPI  # , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from quiz01 import config, quiz01_scraper, quiz01_util

script_path = Path(__file__).absolute()
script_dir = Path(__file__).parent.absolute()
log_folder = script_dir / 'logs'
log_folder.mkdir(parents=True, exist_ok=True)
default_log_args = {
    'level': logging.INFO,
    'format': '[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(module)s] [%(funcName)s] [L%(lineno)d] [P%(process)d] [T%(thread)d] %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S',
    'filename': log_folder / f'quiz01scraper.api.{config.currentDT.strftime("%Y%m%d%H%M%S")}.log',
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
    title="quiz01.scraper.BOT-API",
    description=description,
    summary="do run of the bot.",
    version="0.0.1",
    contact={
        "name": "moisesjurad0",
        "url": "https://linktr.ee/moisesjurad0",

    },
    # root_path='/Prod'
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

    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        _type_: _description_
    """
    logging.info('run-START')
    STR_MESSAGE = 'message'
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
            threading.Thread(
                target=quiz01_scraper.do_scraping,
                args=(exam_number.value,)
            ).start()
        except Exception as e:
            logging.error(str(e), exc_info=True)
            retorno = {STR_MESSAGE: str(e)}

        sessions.pop(exam_number.value)
        retorno = {STR_MESSAGE: 'Evaluating task in the background'}
        # retorno = {STR_MESSAGE: "Task finished"}

    logging.info('run-END')
    return retorno


@app.get("/check/")
def check():
    """Check the bot.

    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        _type_: _description_
    """
    return sessions


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

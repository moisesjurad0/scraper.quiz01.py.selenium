"""main script module without package."""
import datetime
import logging
import threading
from pathlib import Path

import uvicorn
from fastapi import Depends, FastAPI  # , HTTPException
from fastapi.middleware.cors import CORSMiddleware

from quiz01 import config, quiz01_scraper

# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

script_path = Path(__file__).absolute()
script_dir = Path(__file__).parent.absolute()
log_folder = script_dir / 'logs'
log_folder.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_folder /
    f'quiz01scraper.api{config.currentDT.strftime("%Y%m%d%H%M%S")}.log',
    level=logging.INFO,
    format=(
        '%(asctime)s | %(name)s | %(levelname)s |'
        ' [%(filename)s:%(lineno)d] | %(message)s'))


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
    # root_path=f'/Prod'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = {}


@app.get("/")
def read_root():
    """Funcion que devuelve un estado plano OK definido para prueba simple."""
    return {"API_status": "OK"}


def get_session_id():
    """_summary_.

    Returns:
        _type_: _description_
    """
    return threading.current_thread().ident


@app.post("/run/{exam_number}")
def run(exam_number: int, session_id: int = Depends(get_session_id)):
    """Run the bot.

    Args:
        exam_number (int): exam number to be interacted/scraped

    Returns:
        _type_: _description_
    """
    print('run-start')
    logging.info('run-start')

    hilo = threading.Thread(target=main, args=(exam_number,))
    hilo.start()

    print('run-ending')
    logging.info('run-ending')
    return {"message": "Evaluating task in the background"}


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
    logging.info('m01.START')
    print('m01.START')

    sessions[exam_number] = {
        "session_id": session_id,
        "start_time": datetime.datetime.now()}

    # test 1
    quiz01_scraper.do_scraping(exam_number)

    # test 2
    # import time
    # time.sleep(60)

    # test 3
    # for i in range(10):
    #     print(f'subtarea {i}')

    sessions.pop(exam_number)

    logging.info('m01.END')
    print('m01.END')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

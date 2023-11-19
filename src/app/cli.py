"""main script module without package."""

import logging
import sys
from pathlib import Path

import typer

from quiz01 import config, quiz01_scraper

script_path = Path(__file__).absolute()
script_dir = Path(__file__).parent.absolute()
log_folder = script_dir / 'logs'
log_folder.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_folder /
    f'quiz01scraper.cli.{config.currentDT.strftime("%Y%m%d%H%M%S")}.log',
    level=logging.INFO,
    format=(
        '%(asctime)s | %(name)s | %(levelname)s |'
        ' [%(filename)s:%(lineno)d] | %(message)s'))


def main(exam_number: int):
    """Quiz01-Scraper => Scrape CLI.

    Args:
        exam_number (int, optional): Parametro para decidir que examen ejecutar. Dejarlo vacio usa el default del config.ini. Defaults to 1.
    """
    logging.info(f'{config.STARS_SEPARATOR} PARAMETROS DE ENTRADA => '
                 f'exam_number:{exam_number}'
                 f' {config.STARS_SEPARATOR}')
    quiz01_scraper.do_scraping(exam_number)


if __name__ == "__main__":
    try:
        logging.info('START')
        typer.run(main)
        logging.info('END')
        sys.exit(0)
    except Exception as e:
        logging.error(str(e), exc_info=True)
        sys.exit(1)
# if __name__ == "__main__":
#     typer.run(main)

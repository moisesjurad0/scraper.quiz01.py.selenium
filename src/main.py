"""main script module without package."""
import sys
import datetime
import logging
from pathlib import Path
from quiz01 import quiz01_scrapper
# from quiz01.quiz01_scrapper import do_scrapping

script_path = Path(__file__).absolute()
script_dir = Path(__file__).parent.absolute()
log_folder = script_dir / 'logs'
log_folder.mkdir(parents=True, exist_ok=True)

currentDT = datetime.datetime.now()

logging.basicConfig(
    filename=log_folder / f'scrap01{currentDT.strftime("%Y%m%d%H%M%S")}.log',
    level=logging.INFO,
    format=('%(asctime)s | %(name)s | %(levelname)s |'
            ' [%(filename)s:%(lineno)d] | %(message)s'))

logger = logging.getLogger('scrapping01')
logger.setLevel(logging.INFO)


def main():
    """_summary_."""
    quiz01_scrapper.logger = logger
    quiz01_scrapper.currentDT = currentDT
    quiz01_scrapper.do_scrapping()


if __name__ == "__main__":
    try:
        logger.info('inicio')
        main()
        logger.info('fin')
        sys.exit(0)
    except Exception as e:
        logger.error(str(e), exc_info=True)
        sys.exit(1)

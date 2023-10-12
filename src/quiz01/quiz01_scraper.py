"""BOT Quiz01.

Returns:
    _type_: _description_
"""
import time
from playwright.sync_api import Playwright, sync_playwright, expect
import configparser
import logging
import os
import uuid
from tempfile import mkdtemp
from typing import List  # , Optional

from bs4 import BeautifulSoup
from swagger_client import QuestionModel

from . import config
from .quiz01_api import Quiz01Service, Quiz01ServiceFromClient
from .quiz01_util import log_method_call, getLog

STR_TOFC = 'True or False:'
STR_TOFCS = 'True or False:\xa0'
STR_NOT = 'NOT'
RADIO = 'RADIO'
CHECK = 'CHECK'
RADIO_BOOL = 'RADIO_BOOL'
EW = 20  # EW stands for explicit_wait
XPATH_1ST_BTN = (
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button')
XPATH_2ND_BTN = (
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
XPATH_ANSW_Q_DIV = (
    '//html/body/'
    'div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/'
    'ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')
XPATH_ANSW_Q_CHEK_RADI = (
    '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/'
    'ion-list/ion-item'
    ' | '
    '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/'
    'ion-list/ion-radio-group/ion-item')
DEFAULT_SECTION = 'DEFAULT'
exam_number_gb: int = 0
CSS_NEXT_OR_FINISH = ('ion-button[data-cy="continue-btn"]'
                      ','
                      'ion-button[data-cy="finish-btn"]')
XPATH_FINISH = '//*[@id="test_confirm_finish"]'
XPATH_RESUME_1 = '//*[@id="contents"]/ion-card[1]'
XPATH_RESUME_2 = '//*[@id="contents"]/ion-card[2]'
XPATH_RESUME_3 = '//*[@id="contents"]/div'



class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""
    # https://stackoverflow.com/questions/26586801/configparser-and-string-interpolation-with-env-variable

    def before_get(self, parser, section, option, value, defaults):
        """Funcion de sobreEscritura."""
        value = super().before_get(parser, section, option, value, defaults)
        return os.path.expandvars(value)


ini = configparser.ConfigParser(interpolation=EnvInterpolation())
# config = configparser.ConfigParser()
# config = configparser.ConfigParser(os.environ)
# config = configparser.ConfigParser(
#     os.environ,
#     interpolation=configparser.ExtendedInterpolation())
# config = configparser.SafeConfigParser(os.environ)
ini.read('config.ini')


def _analyze_feedback_question(feedback) -> tuple:  # tuple[str, str]:
    """Determinar el tipo de pregunta."""
    str_input_type = ''
    str_question = ''

    try:
        str_question = (
            feedback.
            contents[0].contents[0].next_sibling.
            contents[0].contents[0].contents[0].
            contents[0].contents[0].next_element.text)
        str_input_type = RADIO
    except Exception as e1:
        logging.warning(str(e1), exc_info=True)

        try:
            # we_question stands for WebElement Question
            we_question = (
                feedback.
                contents[0].contents[0].next_sibling.div.
                contents[0].contents[0].contents[0].contents[0].contents[0].
                next_element)
            str_input_type = CHECK

            if we_question.text == STR_TOFC:
                str_input_type = RADIO_BOOL
                str_question = we_question.next_element.text.lstrip()

            elif we_question.text[-1] == ' ':
                if we_question.next_element.next_element.text == STR_NOT:
                    str_question = (
                        we_question.text +
                        we_question.next_element.next_element.text +
                        we_question.next_element.next_element.next_element.
                        text)
            else:
                str_question = we_question.text

        except Exception as e2:
            logging.error(str(e2), exc_info=True)

    return str_input_type, str_question.strip().replace('\xa0', ' ')  # FIXED


def _process_feeback_ticks(
        p_ticks,
        p_question_text,
        p_type,
        p_flag_correct,
        p_obj_service: Quiz01Service,
        p_flag_dont_override=False,
        p_flag_batch: bool = False,
        p_lista_put: List[QuestionModel] = []):
    for tick in p_ticks:
        f_answer_ok_text = ''
        if p_type == RADIO_BOOL:
            f_answer_ok_text = (
                tick.previous_sibling.next_element.next_element.
                next_element.next_element.next_element.text)
        else:
            f_answer_ok_text = (
                tick.previous_sibling.next_element.next_element.
                next_element.next_element.next_element.next_element.text)

        f_answer_ok_text = f_answer_ok_text.strip()  # FIXED
        print(f_answer_ok_text)
        logging.info(f_answer_ok_text)
        if p_flag_batch:
            if p_flag_dont_override:
                stored_data = p_obj_service.get_cache(exam_number_gb)
                filtered_data = list(filter(
                    lambda i:
                        i['id'] == p_question_text and
                        i['question_type'] == p_type and
                        i['answer_text'] == f_answer_ok_text and
                        i['is_correct'] == p_flag_correct and
                        i['exam_number'] == exam_number_gb,
                        stored_data['Items']))

                if filtered_data:
                    continue

            p_lista_put.append(
                QuestionModel(
                    id=p_question_text,
                    question_type=p_type,
                    answer_text=f_answer_ok_text,
                    is_correct=p_flag_correct,
                    exam_number=exam_number_gb,
                    last_modified=config.currentDT.isoformat()))
        else:
            p_obj_service.put(
                f'{p_question_text}---{f_answer_ok_text}',
                p_question_text,
                p_type,
                f_answer_ok_text,
                p_flag_correct,
                exam_number_gb,
                config.currentDT.isoformat())


@log_method_call
def do_scraping(p_exam_number: int):
    """Main method."""
    with sync_playwright() as playwright:
        run(playwright, p_exam_number)


def run(playwright: Playwright, p_exam_number) -> None:
    """Main method."""
    # *** INITIALIZE VARAIBLES ***
    global exam_number_gb
    exam_number_gb = p_exam_number
    exam_section = f'EXAM-{exam_number_gb}'
    quiz_url = ini[exam_section]['quiz_url']
    x_api_key = ini[exam_section]['x-api-key']
    api_endpoint = ini[exam_section]['api_endpoint']
    obj_service: Quiz01Service = Quiz01ServiceFromClient(
        x_api_key,
        api_endpoint
    )

    v_uuid = uuid.uuid4().hex
    print(f'v_uuid->{v_uuid}')
    logging.info(f'v_uuid->{v_uuid}')

    headless = ini.getboolean(DEFAULT_SECTION, 'headless')
    do_correct_answers = ini.getboolean(DEFAULT_SECTION, 'do_correct_answers')
    do_correct_answers_cache = ini.getboolean(
        DEFAULT_SECTION, 'do_correct_answers_cache')
    dont_overwrite = ini.getboolean(DEFAULT_SECTION, 'dont_overwrite')
    dont_store_answers = ini.getboolean(DEFAULT_SECTION, 'dont_store_answers')

    # *** START SCRAPING ***
    logging.info('START SCRAPING')
    browser = playwright.chromium.launch(headless=headless)  # , slow_mo=1 * 1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(quiz_url)

    page.click(XPATH_1ST_BTN)
    page.click(XPATH_2ND_BTN)

    # *** SAVING STATE ***
    # https://playwright.dev/python/docs/next/auth
    # storage = context.storage_state(path="state.json")

    # *** ANSWERING QUESTIONS ***
    logging.info('SECTION - ANSWERING QUESTIONS')
    while True:

        # div_question_text = page.wait_for_selector(XPATH_ANSW_Q_DIV).inner_text().split("\n")[0]
        div_question_text_original = ''
        div_question_text = ''
        div_question_text_original = page.wait_for_selector('.question-text').inner_text()
        div_question_text = div_question_text_original.split("\n")[0]

        if div_question_text.startswith(STR_TOFC):
            div_question_text = div_question_text.split(STR_TOFC)[1]

        # div_question_text = div_question_text.split('\n')[0]
        div_question_text = div_question_text.strip().replace('\xa0', ' ').strip()
        print(div_question_text)

        # SECTION - ANSWERING QUESTIONS - CHECKBOXES or RADIO BUTTONS
        scraped_answers_to_choose = page.query_selector_all(XPATH_ANSW_Q_CHEK_RADI)

        if not do_correct_answers:
            logging.info('SECTION - DUMMY ANSWERS')
            for d in scraped_answers_to_choose:
                d.click()
        elif do_correct_answers and do_correct_answers_cache:
            logging.info('SECTION - DO CORRECT ANSWERS - CACHE')
            api_data = obj_service.get_cache(exam_number_gb)
            api_data_filtered = list(filter(
                lambda i:
                i['id'] == div_question_text and
                i['is_correct'],
                api_data['Items']))

            if api_data_filtered:
                logging.info('ITEM - DATA FOUND')

                api_answer_lc = [x['answer_text'] for x in api_data_filtered]

                for s in scraped_answers_to_choose:
                    s_txt = s.query_selector('.bbcode.cursor-pointer').inner_text()
                    if s_txt in api_answer_lc:
                        s.click()

            else:
                logging.info('ITEM - DATA NOT FOUND - DUMMY ANSWERS')
                for s in scraped_answers_to_choose:
                    s.click()
        elif do_correct_answers:
            logging.info('SECTION - DO CORRECT ANSWERS')
            api_data = obj_service.search_v2(
                question=div_question_text, flag_correct=True)
            if api_data['Items']:
                logging.info('ITEM - DATA FOUND')
                for d in api_data['Items']:
                    for s in scraped_answers_to_choose:
                        scraped_answer_txt = s.query_selector(
                            '.bbcode.cursor-pointer').inner_text()
                        if d['answer_text'] == scraped_answer_txt:
                            s.click()
                            break
            else:
                logging.info('ITEM - DATA NOT FOUND - DUMMY ANSWERS')
                for s in scraped_answers_to_choose:
                    s.click()

        # page.wait_for_selector(CSS_NEXT_OR_FINISH, state="clickable")
        btn_next_or_finish_now = page.wait_for_selector(CSS_NEXT_OR_FINISH)

        attribute_data_cy = btn_next_or_finish_now.get_attribute('data-cy')

        if attribute_data_cy == 'continue-btn':

            # Define a function to check if the element has the expected value
            def check_element_content():
                actual_value = div_question_text_original
                new_value = page.wait_for_selector('.question-text').inner_text()
                return actual_value == new_value
            # Wait for the element to reload with the expected value
            # page.wait_for_function(check_element_content())

            btn_next_or_finish_now.click()
            while check_element_content():
                time.sleep(0.025)


        elif attribute_data_cy == 'finish-btn':
            btn_next_or_finish_now.click()
            page.query_selector(XPATH_FINISH).click()
            break

    logging.info(
        'HACER UN WAIT DE LA PAGINA DE RESULTADO, '
        'DEL LA PARTE DE ARRIBA Y LA DE ABAJO DE LA PAGINA')

    # ************ MIGRATION MARKER 1 ****************

    page.wait_for_selector(XPATH_RESUME_1)
    page.wait_for_selector(XPATH_RESUME_2)
    page.wait_for_selector(XPATH_RESUME_3)

    logging.info('SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE')

    page_source = page.content()
    soup = BeautifulSoup(page_source, 'html.parser')

    contador_preguntas = 0
    feedbacks = soup.find_all('div', class_='feedback')

    lista_put: List[QuestionModel] = []
    for feedback in feedbacks:
        contador_preguntas += 1
        print(feedback.text)

        f_type, f_question_text = _analyze_feedback_question(feedback)

        print(f'Q{contador_preguntas} - {f_question_text}')
        logging.info(f'Q{contador_preguntas} - {f_question_text}')

        correct_ticks = feedback.select(
            '.circular-tick,.circular-tick-holo')
        _process_feeback_ticks(
            correct_ticks,
            f_question_text,
            f_type,
            True,
            obj_service,
            dont_overwrite,
            True,
            lista_put)

        incorrect_ticks = feedback.select(
            'ion-icon.icon.icon-correct.md.hydrated'
            ':not(.circular-tick-holo)'
            ':not(.circular-tick)')
        _process_feeback_ticks(
            incorrect_ticks,
            f_question_text,
            f_type,
            False,
            obj_service,
            dont_overwrite,
            True,
            lista_put)

        print(f'Q{contador_preguntas} - END')
        logging.info(f'Q{contador_preguntas} - END')

    print(f'ITEMS ({len(lista_put)}) READY TO BATCH')

    if dont_store_answers:
        print('ITEMS ARE NOT GONNA BE BATCH')

    if lista_put and not dont_store_answers:
        print('BATCHING ITEMS')
        response = obj_service.put_batch(lista_put)
        logging.info(response)
    else:
        print('ITEMS WERE NOT BATCHED')

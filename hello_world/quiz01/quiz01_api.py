"""Modulo de llamado al API."""
import json
import logging
from pprint import pprint
from typing import List

import requests
import swagger_client
from swagger_client.rest import ApiException

from .quiz01_util import log_method_call, log_method_call_no_params, getLog

# logger = getLog(__name__)


class Quiz01Service:
    """Duck class."""

    def __init__(self, x_api_key):
        """Constructor de la clase.

        Args:
            x_api_key (_type_): _description_
        """
        logging.info('quiz01_api.23')
        self.x_api_key = x_api_key
        self.cache = dict()
        self.api_instance = None

    def put(
            self,
            v_id,
            question,
            question_type,
            answer,
            flag_correct,
            exam_number,
            last_modify):
        """Duck method."""
        pass

    def search_v2(
            self,
            question='',
            question_type='',
            answer='',
            flag_correct=True,
            exam_number=''):
        """Duck method."""
        pass

    def put_batch(
            self,
            my_list: List[swagger_client.QuestionModel]):
        """Duck method."""
        pass

    def get_cache(
            self,
            exam_number: int):
        """Duck method."""
        pass

    def _get_api_instance(self):
        """Duck method."""
        pass

    def _end_connection(self):
        """Duck method."""
        pass

    def __del__(self):
        """Duck method."""
        pass


class Quiz01ServiceManual(Quiz01Service):
    """Clase Servicio para llamar al API."""

    def __init__(self, x_api_key, put_url, search_url):
        """Constructor de la clase.

        Args:
            x_api_key (_type_): _description_
            put_url (_type_): _description_
            search_url (_type_): _description_
        """
        super().__init__(x_api_key)
        self.put_url = put_url
        self.search_url = search_url

    @log_method_call
    def put(self, v_id, question, question_type,
            answer, flag_correct, exam_number, last_modify):
        """Metodo put.

        Args:
            v_id (_type_): _description_
            question (_type_): _description_
            question_type (_type_): _description_
            answer (_type_): _description_
            flag_correct (_type_): _description_
            exam_number (_type_): _description_
            last_modify (_type_): _description_
        """
        payload = json.dumps({
            "id": v_id,
            # "uuid": v_uuid,
            "question": question,
            "question_type": question_type,
            "answer": answer,
            "correct": flag_correct,
            "exam_number": exam_number,
            "last_modify": last_modify
        })
        headers = {
            'x-api-key': self.x_api_key,
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "POST", self.put_url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()

    @log_method_call
    def search_v2(
            self,
            question='',
            question_type='',
            answer='',
            flag_correct=True,
            exam_number=''):
        """Funcion de busqueda v2.

        Args:
            question (str, optional): _description_. Defaults to ''.
            question_type (str, optional): _description_. Defaults to ''.
            answer (str, optional): _description_. Defaults to ''.
            flag_correct (bool, optional): _description_. Defaults to True.
            exam_number (str, optional): _description_. Defaults to ''.

        Returns:
            _type_: _description_
        """
        payload = json.dumps({
            "question": question,
            "question_type": question_type,
            "answer": answer,
            "correct": flag_correct,
            "exam_number": exam_number
        })
        headers = {
            'x-api-key': self.x_api_key,
            'Content-Type': 'application/json'
        }

        response = requests.request(
            "POST", self.search_url, headers=headers, data=payload)

        response.raise_for_status()
        return response.json()


class Quiz01ServiceFromClient(Quiz01Service):
    """Clase Servicio para llamar al API."""

    def __init__(self, x_api_key, endpoint_url):
        """_summary_.

        Args:
            x_api_key (_type_): _description_
            endpoint_url (_type_): _description_
        """
        super().__init__(x_api_key)
        logging.info('quiz01_api.174')
        self.endpoint_url = endpoint_url
        logging.info('quiz01_api.176=>{endpoint_url}|{self.endpoint_url}')
        self.configuration = swagger_client.Configuration()
        logging.info('quiz01_api.178')
        self.configuration.host = self.endpoint_url
        logging.info('quiz01_api.179=>{self.configuration.host}')

    def _get_api_instance(self):
        if self.api_instance is None:
            logging.info('quiz01_api.184')
            self.api_instance = swagger_client.QuestionsApi(
                swagger_client.ApiClient(self.configuration))
        logging.info('quiz01_api.187')
        return self.api_instance

    # @log_method_call_no_params
    def get_cache(self, exam_number: int):
        """_summary_.

        Returns:
            _type_: _description_
        """
        logging.info('quiz01_api.197')
        if exam_number not in self.cache:
            logging.info('quiz01_api.199')
            body = swagger_client.QuestionScanModel(
                exam_number=exam_number)
            logging.info('quiz01_api.202')
            self.cache[exam_number] = self._get_api_instance(
            ).search_items_begins_with_api_v1_questions_search_begins_with_post(body)
            logging.info('quiz01_api.205')
        logging.info('quiz01_api.206')
        return self.cache[exam_number]

    @log_method_call
    def put(
            self,
            v_id,
            question,
            question_type,
            answer,
            flag_correct,
            exam_number,
            last_modify):
        """_summary_.

        Args:
            v_id (_type_): _description_
            question (_type_): _description_
            question_type (_type_): _description_
            answer (_type_): _description_
            flag_correct (_type_): _description_
            exam_number (_type_): _description_
            last_modify (_type_): _description_

        Returns:
            _type_: _description_
        """
        body = swagger_client.QuestionModel(
            id=question,
            question_type=question_type,
            answer_text=answer,
            is_correct=flag_correct,
            exam_number=exam_number,
            last_modified=last_modify
        )
        api_response = self._get_api_instance().put_item_api_v1_questions_put(
            body)
        pprint(api_response)
        return api_response

    @log_method_call_no_params
    def put_batch(
            self,
            my_list: List[swagger_client.QuestionModel]
    ):
        """_summary_.

        Args:
            my_list (List[swagger_client.QuestionModel]): _description_

        Returns:
            _type_: _description_
        """
        body = my_list
        api_response = self._get_api_instance(
        ).batch_put_items_api_v1_questions_batch_put(body)
        pprint(api_response)
        return api_response

    @log_method_call
    def search_v2(
            self,
            question=None,
            question_type=None,
            answer=None,
            flag_correct=None,
            exam_number=None):
        """Funcion de busqueda v2.

        Args:
            question (_type_, optional): _description_. Defaults to None.
            question_type (_type_, optional): _description_. Defaults to None.
            answer (_type_, optional): _description_. Defaults to None.
            flag_correct (_type_, optional): _description_. Defaults to None.
            exam_number (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        body = swagger_client.QuestionScanModel(
            id=question,
            question_type=question_type,
            answer_text=answer,
            is_correct=flag_correct,
            exam_number=exam_number
        )
        api_response = self._get_api_instance(
        ).search_items_begins_with_api_v1_questions_search_begins_with_post(body)
        pprint(api_response)
        return api_response

    # @log_method_call

    def _end_connection(self):
        """_summary_."""
        logging.info('quiz01_api.301')
        self._get_api_instance().api_client.pool.close()

    # @log_method_call
    def __del__(self):
        """_summary_."""
        logging.info('quiz01_api.307')
        # self._end_connection()

"""Modulo de llamado al API."""
import json
import logging
from pprint import pprint
from typing import List

import swagger_client
from swagger_client.rest import ApiException

from .quiz01_util import getLog, log_method_call, log_method_call_no_params


class Quiz01Service:
    """Duck class."""

    def __init__(self, x_api_key):
        """Constructor de la clase.

        Args:
            x_api_key (_type_): _description_
        """
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

    # def _end_connection(self):
    #     """Duck method."""
    #     pass

    def __del__(self):
        """Duck method."""
        pass


class Quiz01ServiceFromClient(Quiz01Service):
    """Clase Servicio para llamar al API."""

    def __init__(self, x_api_key, endpoint_url):
        """_summary_.

        Args:
            x_api_key (_type_): _description_
            endpoint_url (_type_): _description_
        """
        super().__init__(x_api_key)
        self.endpoint_url = endpoint_url
        self.configuration = swagger_client.Configuration()
        self.configuration.host = self.endpoint_url

    def _get_api_instance(self):
        if self.api_instance is None:
            self.api_instance = swagger_client.QuestionsApi(
                swagger_client.ApiClient(self.configuration))

        return self.api_instance

    @log_method_call_no_params
    def get_cache(self, exam_number: int):
        """_summary_.

        Returns:
            _type_: _description_
        """
        if exam_number not in self.cache:
            body = swagger_client.QuestionScanModel(
                exam_number=exam_number)
            self.cache[exam_number] = self._get_api_instance(
            ).search_items_begins_with_api_v1_questions_search_begins_with_post(body)
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
        response = self._get_api_instance().put_item_api_v1_questions_put(
            body)
        return response

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
        response = self._get_api_instance(
        ).batch_put_items_api_v1_questions_batch_put(body)
        return response

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
        response = self._get_api_instance(
        ).search_items_begins_with_api_v1_questions_search_begins_with_post(body)
        return response

    # @log_method_call
    # def _end_connection(self):
    #     """_summary_."""
    #     self._get_api_instance().api_client.pool.close()

    @log_method_call
    def __del__(self):
        """_summary_."""
        # self._end_connection()
        self._get_api_instance().api_client.pool.close()

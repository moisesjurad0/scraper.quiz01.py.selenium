"""Modulo de llamado al API."""
import json

import requests


class Service:
    """Clase Servicio para llamar al API."""

    def __init__(self, x_api_key, put_url, search_url):
        """Constructor de la clase.

        Args:
            x_api_key (_type_): _description_
            put_url (_type_): _description_
            search_url (_type_): _description_
        """
        self.x_api_key = x_api_key
        self.put_url = put_url
        self.search_url = search_url

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
        print(response.text)
        response.raise_for_status()

    def search_v2(self, question='', question_type='',
                  answer='', flag_correct=True, exam_number=''):
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

        print(response.text)
        response.raise_for_status()
        return response.json()

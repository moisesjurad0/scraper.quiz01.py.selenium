import json

import requests


class MyService:

    def __init__(self, x_api_key, put_url, search_url):
        self.x_api_key = x_api_key
        self.put_url = put_url
        self.search_url = search_url

    def put(self, v_id, question, question_type, answer, flag_correct, exam_number, last_modify):
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

        response = requests.request("POST", self.put_url, headers=headers, data=payload)
        print(response.text)
        response.raise_for_status()

    def search_v2(self, question='', question_type='', answer='', flag_correct=True, exam_number=''):
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

        response = requests.request("POST", self.search_url, headers=headers, data=payload)

        print(response.text)
        response.raise_for_status()
        return response.json()

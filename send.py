import json

import requests


class MyService:

    def __init__(self, url, x_api_key):
        self.url = url
        self.x_api_key = x_api_key

    # def create(v_id, v_uuid, question, question_type, answer, flag_correct):
    def create(self, v_id, question, question_type, answer, flag_correct, exam_number, last_modify):
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

        response = requests.request("POST", self.url, headers=headers, data=payload)
        print(response.text)
        response.raise_for_status()

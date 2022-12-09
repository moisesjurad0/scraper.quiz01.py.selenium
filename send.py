import json

import requests


# def create(v_id, v_uuid, question, question_type, answer, flag_correct):
def create(v_id, question, question_type, answer, flag_correct, last_modify):
    url = ""

    payload = json.dumps({
        "id": v_id,
        # "uuid": v_uuid,
        "question": question,
        "question_type": question_type,
        "answer": answer,
        "correct": flag_correct,
        "last_modify": last_modify
    })
    headers = {
        'x-api-key': '',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    response.raise_for_status()

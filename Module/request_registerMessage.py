#- * -coding: utf - 8 - * -
import os
import sys
import json
import requests
import psycopg2
import datetime

def Message(Message):
    response = {
        "events": "request_register",
        "timestamp": '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source": {
            "uid": Message['source']['uid']
        },
        "Message": {
            "Type": "text",
            "Detail": "กรุณากรอกรหัสเพื่อเริ่มใช้บริการ"
        }
    }
    return json.dumps(response)
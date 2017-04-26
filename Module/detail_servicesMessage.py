#- * -coding: utf - 8 - * -
import os
import sys
import json
import requests
import psycopg2
import datetime

def Message(Message):
    response = {
        "events": "detail_services",
        "timestamp": '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source": {
            "uid": Message['source']['uid']
        },
        "Message": {
            "Type": "text",
            "Detail": "ยินดีต้อนรับเข้าสู่บริการแจ้งเตือนอัตโนมัติของโรงพยาบาลผ่าน Line Application"
        }
    }
    return json.dumps(response)
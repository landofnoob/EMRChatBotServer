# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

def Message(Message):
    #Receive Method send Message to Line. it about News from Google API
    response = {
        "events" : "welcome",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : 
            {
                "uid" : Message['source']['uid'],
            },
        "Message" : 
        {
            "Type" : "Text",
            "Detail" : "ยินดีต้อนรับสู่โรงพยาบาล"
            }
        }
    return json.dumps(response)
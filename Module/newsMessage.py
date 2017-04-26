# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

def Message(Message):
    #print Message
    #Insert Data EMRfriend(uid,status,displayname) to PostgreSQL
    print Message
    response = {
        "events" : "news",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : 
        {
            "uid" : Message['source']['uid'],
        },
            "Message" : 
        {
            "Type" : "Text",
            "Detail" : "ข้อมูลข่าวสารประจำวัน"
        }
    }
    return json.dumps(response)
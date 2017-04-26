# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

def Message(Message):
    #Send Gerneral Menu for not register Line ID. When someone request and Show
    response = {
        "events" : "gerneral_menu",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : 
        {
            "uid" : Message['source']['uid']
        },
        "Message" : 
        {
            "Type" : "Menu",
            "Detail" : 
        {
            "Topic" : "หน้าต่างเมนูหลัก",
            "1" : "ลงทะเบียน",
            "2" : "ข่าวสารประจำวัน",
            "3" : "Event & Promotion",
            "4" : "เกี่ยวกับโรงพยาบาล"
            }
        }
    }
    return json.dumps(response)
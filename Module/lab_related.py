#- * -coding: utf - 8 - * -
import os
import sys
import json
import requests
import psycopg2
import datetime

from CRUD.action import Action

from Module.postMessage import PostMessage

database = Action()

Post = PostMessage()

def Message(Message):
    Lab_Related_Message = {
        "events" : "lab_related",
        "source" :{
            "uid" : database.queryOne("emrcid","cid",Message['source']['cid'],"uid")
        },
        "Message" :{
            "Type" : "text",
            "text" : "ผลตรวจของคุณออกแล้ว กรุณารับผลที่หน้าห้องแลป"
        }
    }
    print Post._send(Lab_Related_Message)
    #insert Log
    data = {
        "Type" : "Success",
        "Detail" : "Lab Related"
    }
    response = {
        "events" : "Lab_related",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "Message" : data
    }
    return json.dumps(response)
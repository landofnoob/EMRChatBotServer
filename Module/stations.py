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
    status = 'success'
    department = Message['stations']['department']
    channel = Message['stations']['channel']
    data_update ={
        "location": department
    }
    database.update("emrcid","cid",Message['source']['cid'],data_update)
    detail = "กรุณาที่แผนก " +str(department)+ " ที่ห้องบริการ "+str(channel)
    #Send Location to Line.
    PushMessage = Post.setBody(
        events=Message['events'],
        source={"uid" : database.queryOne("emrcid","cid",Message['source']['cid'],"uid")},
        type='text',
        text=detail
        )
    print Post._send(PushMessage)
    locationMessage ={
        "events" : "location_confirm",
        "source" :{
            "uid" : database.queryOne("emrcid","cid",Message['source']['cid'],"uid")
        },
        "Message" : {
            "Type" : "confirm",
            "confirm" : {
                "Question" : "คุณหาสถานที่พบหรือไม่",
                "1" : "พบ",
                "2" : "ไม่พบ"
                }
            }
        }
    print Post._send(locationMessage)
    Log_data = {
        "cid" : Message['source']['cid'],
        "event_type" : Message['events'],
        "note" : detail
    }
    database.insert("emractivity",Log_data)
    if status == 'success':
        data = {
            "Type" : "Success",
            "Detail" : "Notification Success"
        }
    else:
        data = {
            "Type" : "Fail",
            "Datail" : "Error : %s"  % value
        }
    response = {
        "events" : "stations",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "Message" : data
    }
    return json.dumps(response)

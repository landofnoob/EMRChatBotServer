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
    queue = Message['lab']['queue']
    time = Message['lab']['waiting']
    Lab_Message = {
        "events" : "lab_queue",
        "source" :{
            "uid" : database.queryOne("emrcid","cid",Message['source']['cid'],"uid")
        },
        "Message" :{
            "Type" : "text",
            "text" : "ผลตรวจของคุณอยู่ที่คิวหมายเลข "+str(queue)+" ผลตรวจจะออกประมาณ "+str(time)+" นาที"
        }
    }
    print Post._send(Lab_Message)
    Reply_Lab_Message ={
        "events" : "lab_menu",     
        "source" : {
            "uid" : database.queryOne("emrcid","cid",Message['source']['cid'],"uid")
        },
        "Message" : 
        {
            "Type" : "Menu",
            "Detail" : 
            {
                "Topic" : "หน้าต่างเมนูหลัก",
                "1" : "ขณะนี้อยู่ที่คิวเท่าไร",
                "2" : "รอผลตรวจกี่นาที",
                "3" : "บริการแผนที่"
            }
        }
    }
    print Post._send(Reply_Lab_Message)
    data = {
        "Type" : "Success",
        "Detail" : "Lab queue"
    }
    response = {
        "events" : "Lab_queue",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "Message" : data
    }
    return json.dumps(response)
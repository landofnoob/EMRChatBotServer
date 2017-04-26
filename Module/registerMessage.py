#- * -coding: utf - 8 - * -
import os
import sys
import json
import requests
import psycopg2
import datetime

from CRUD.action import Action

database = Action()

def Message(Message):
    status = ''
    miss = database.queryOne("emrfriend","uid",Message['source']['uid'],"miss")
    print miss
    print Message['pin']
    print len(Message['pin'])
    if miss <= 2:
        if len(Message['pin']) != 6:
            print "No 6 digits"
            miss = miss + 1
            data = {
                "Type" : "Fail",
                "Detail" : "รหัสไม่ถูกต้อง กรุณากรอกรหัสใหม่อีกครั้ง"
                }
            miss_update ={
                "miss" : miss
                }
            database.update("emrfriend","uid",Message['source']['uid'],miss_update)
        else:
            print "Checking True or False PIN"
            value = database.IsCheckMatch("emrcid","cid",Message['pin'])
            print value
            if value == True:
            #Update Status to Valid
                data_update = {
                    "status":"valid"
                    }
                database.update("emrfriend","uid",Message['source']['uid'],data_update)
                #Update Set uid
                data_update2 = {
                    "uid": Message['source']['uid']
                    }
                database.update("emrcid","cid",Message['pin'],data_update2)
                status = 'success'
            else:
                status = 'fail'
            if status == 'success':
                data = {
                    "Type" : "Success",
                    "Detail" : "การลงทะเบียนเสร็จสมบูรณ์"
                    }
            else:
                data = {
                    "Type" : "Fail",
                    "Detail" : "รหัสไม่ถูกต้อง กรุณากรอกรหัสใหม่อีกครั้ง"
                    }
                miss = miss + 1
                miss_update ={
                    "miss" : miss
                    }
                database.update("emrfriend","uid",Message['source']['uid'],miss_update)
    if miss >= 3:
        data ={
            "Type" : "Fail",
            "Detail" : "กรุณาติดต่อเจ้าหน้าที่แผนกเวชทะเบียน"
            }
    response = {
        "events" : "register",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : 
        {
            "uid" : Message['source']['uid'],
        },
        "Message" : data
    }
    return json.dumps(response)
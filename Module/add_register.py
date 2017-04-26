#- * -coding: utf - 8 - * -
import os
import sys
import json
import requests
import psycopg2
import datetime

from CRUD.action import Action

database = Action()

def Add(Message):
    match = database.IsCheckMatch("emrcid","cid",Message['source']['cid'])
    print match
    #Insert Data EMRCid(CID,TS,NAME) to SQL
    if match == True:
        data = {
            "Type" : "Fail",
            "Detail" : "CID is already used" 
        }
    else:
        Message['source']['timestamp'] = Message['timestamp']
        value = database.insert("EMRCid",Message['source'])
        if value == 'success':
            data = {
                "Type" : "Success",
                "Detail" : "success add register name : %s" % Message['source']['name']
            }
        else:
            data = {
                "Type" : "Fail",
                "Datail" : "Error : %s"  % value
            }
    response = {
        "events" : "add_register",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "Message" : data
    }
    return json.dumps(response)
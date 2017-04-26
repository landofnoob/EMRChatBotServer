#- * -coding: utf - 8 - * -
import os
import sys
import json
import requests
import psycopg2
import datetime

from CRUD.action import Action

database = Action()

def get(Message):
    print "Get Your Status"
    # 1. Query status
    query = database.queryOne("emrfriend","uid",Message['source']['uid'],"status")
    print query
    response = {
        "events" : "status",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : 
        {
            "uid" : Message['source']['uid'],
            "status" : query
        }
    }
    return json.dumps(response)

def expired(Message):
    print "Change Status to Expired"
    #1. Expried Change EMRFriend uid to Expired
    status_update = {
        "status" : "expired",
        "miss" : 0
    } 
    database.update("emrfriend","uid",Message['source']['uid'],status_update)
    #2. Delete CID
    print "Delete CID"
    database.delete("emrcid","uid",Message['source']['uid'])
    response = {
        "events" : "expired",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : 
        {
            "uid" : Message['source']['uid'],
        },
        "Message": {
            "Type": "text",
            "Detail": "ขอบคุณที่ใช้บริการ"
        }
    }
    return json.dumps(response)


    ''' Old Code
    print('--From LINE')
    print(json_dict['events']['source'])
    #Send information to DBMs ('lineid','displayname','ts','status')
    message = json_dict['events']['message']['text']
    print (message)
    #Check Expired
    if (json_dict['events']['message']['text']=='expired'):
        update = "UPDATE EMRfriend set STATUS='expired' where UID=" + "'" + json_dict["events"]["source"]["lineid"] + "';"
        print(update)
        delete = "DELETE from EMRcid where UID='" + json_dict["events"]["source"]["lineid"] + "';"
        con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')
        cur = con.cursor()
        cur.execute(update)
        # cur.execute(delete)
        con.commit()
        con.close()
        data = {
            'type' : 'status',
            'message' : 'expired'
            }
        ######### Insert DATABase
    elif (json_dict['events']['message']['text']=='status'):
        con = None
        query = "SELECT DISPLAYNAME,STATUS FROM EMRfriend WHERE UID='" + json_dict["events"]["source"]["lineid"] + "';"
        print(query)
        con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')
        cur = con.cursor()
        cur.execute(query)
        columns = ('DISPLAYNAME', 'STATUS')
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        print json.dumps(results, indent=2)
        #print jsonify(results[0])
        con.close()
        data = results[0]
    return json.dumps(data)
    '''
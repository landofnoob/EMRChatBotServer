# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
import psycopg2
import datetime

from CRUD.action import Action

database = Action()


def Event(Message):
    data = {'abc': 'empty'}
    match = database.IsCheckMatch('emrfriend', 'uid', Message['source'
                                  ]['uid'])
    print 'Match : %s' % match
    if match == True:
        data = {'Type': 'Fail', 'Detail': 'uid is already friend'}
    elif match == False:
    	#print "No Found uid"
    	Message['source']['status'] = 'register'
    	#print Message['source']
    	#Add_status = Message['source'].update({'status':'expired'})
        value = database.insert('emrfriend', Message['source'])
        print 'Value : %s' % value
        data = {'Type': 'True', 'Detail': 'Trying to Add Friend'}
    else:
    	print "Something Wrong"
    response = {'events': 'followevent',
                'timestamp': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
                'Message': data}
    return json.dumps(response)



			
    '''
    ######### Insert DATABase
    con = None
    query = "SELECT uid,displayname FROM EMRfriend WHERE uID='" + Message['source']['uid'] + "';"
    print(query)
    con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')   
    cur = con.cursor()
    cur.execute(query)
    columns = ('uid','displayname')
    results = []
    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    print json.dumps(results, indent=2)
    #con.commit()
    con.close()
    ########################
    #Checking Correct or Not
    data = {}
    if (results == []):
        data = {
            "Type" : "Fail",
            "Datail" : "Error : %s"  % value
        }  
              
        con = None
        query = "insert into EMRFriend(uid,status) values('" + Message['source']['uid'] + "','register');"
        print(query)
        con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')   
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        con.close()        
    else:
        data = {
            "Type" : "Success",
            "Detail" : "success uid : %s" % Message['source']['uid']
        }
        #Insert Data EMRCid(CID,TS,NAME) to SQL
        if match == True:
            data = {
                "Type" : "Fail",
                "Detail" : "CID is already used" 
            }

        else:
            value = insert("emrfriend",Message['source']['uid'])
            if value == 'success':
                data = {
                "Type" : "Success",
                "Detail" : "success uid : %s" % Message['source']['uid']
                }
            else:
                data = {
                "Type" : "Fail",
                "Datail" : "Error : %s"  % value
                }

    '''
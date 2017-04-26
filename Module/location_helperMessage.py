# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

def Message(Message):
    #Send Map to Line
    stations = queryOne("emrcid","uid",Message['source']['uid'],"Location")
    next_stations = queryOne("emrcid","uid",Message['source']['uid'],"Next_stations")
    data = {
        "map" : "/picture/01.jpeg"
    }
    response = {
        "events" : "location_helper",
        "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        "source" : {
            "uid" : Message['source']['uid']
        },
        "Message" : data
    }
    return json.dumps(response)
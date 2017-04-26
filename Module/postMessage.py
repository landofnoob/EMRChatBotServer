# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

class PostMessage():
    DEFAULT_ENDPOINT = 'https://linebot-python-testing.herokuapp.com'
    DFFAULT_HEADERS ={
        'Content-Type':'application/json'
        }
    DEFAULT_PATH = '/notify'
    def __init__(self,endpoint=DEFAULT_ENDPOINT,headers=DFFAULT_HEADERS,path=DEFAULT_PATH):
        self.endpoint = endpoint
        self.headers = headers
        self.path = path

    def setBody(self,events=None,type='text',source=None,text=None):
        body ={
            "events" : events,
            "timestamp" : '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
            "source" : source,
            "Message":
            {
                "Type" : type,
                "text" : text
            }
        }
        return body

    def _post(self, path=None, data=None, timeout=None):
        url = self.endpoint + self.path
        headers = self.headers
        response = requests.post(
            url, headers=headers, data=data, timeout=timeout
            )
        return response.text

    def _send(self, data, timeout=None):
        response = self._post(
            data=json.dumps(data)
            )
        return response
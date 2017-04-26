# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

from flask import Flask, request, jsonify

from Module import (
	welcomeMessage, followEvent, postMessage, gerneralMessage, 
	newsMessage, request_registerMessage, registerMessage, status, add_register,
    helperMessage, stations, lab_related, lab_queue, detail_servicesMessage
)
app = Flask(__name__)

@app.route('/services', methods=["POST"])
def services():
    #Detect Status Code:

    Message = request.get_json()
    print Message
    event_type = Message['events']
    print "Event Type : %s " % event_type
    #print event_type
    if request.method == "POST":
    	#Start Message
    	if event_type == 'status':
    		return status.get(Message)
    	elif event_type == 'welcome':
        	return welcomeMessage.Message(Message)
        elif event_type == 'followevent':
        	return followEvent.Event(Message)
        elif event_type == 'general_menu':
        	return gerneralMessage.Message(Message)
        elif event_type == '@event':
        	pass
        elif event_type == '@services':
        	pass
        elif event_type == '@hospital':
        	pass
        elif event_type == '@manuals':
        	pass
        elif event_type == 'detail_services':
            return detail_servicesMessage.Message(Message)
        elif event_type == 'news':
        	return newsMessage.Message(Message)
        #Register
    	elif event_type == 'add_register':
    		return add_register.Add(Message)
    	elif event_type == 'register':
    		return registerMessage.Message(Message)
        elif event_type == 'request_register':
        	return request_registerMessage.Message(Message)
        #Helper Menu
        elif event_type == '@helper_Menu':
            print "Helper Menu"
            return helperMessage.Message(Message)
        #Expired
        elif event_type == 'expired':
            return status.expired(Message)
        #Notification
        elif event_type == 'lab_related':
            print "Lab_Related"
            return lab_related.Message(Message)
        elif event_type == 'lab_queue':
            return lab_queue.Message(Message)
        elif event_type == 'stations':
            return stations.Message(Message)
        else:
        	return "Error in POST Method"
    else:
    	return "Error"

@app.errorhandler(500)
def Page_Out_InternalServer():
    return "ขออภัยระบบเกิดการขัดข้อง กำลังแก้ไขระบบ"

@app.errorhandler(400)
def Page_Out_Request():
    return "การร้องขอคุณไม่ตรงตามเงื่อนไขที่กำหนด"

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='ec2-54-251-157-175.ap-southeast-1.compute.amazonaws.com')

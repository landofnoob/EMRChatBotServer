import json
import requests
import psycopg2
import datetime

from CRUD.action import Action

database = Action()

def Message(Message):
	#print "Confirm Location : %s" % Message
	response = {
		"events" : "lab_related",
		"source" :{
			"uid" : database.queryOne("emrcid","cid",Message['source']['cid'],"uid")
			},
		"Message" :{
			"Type" : "text",
			"text" : "Confirm Menu"
		}
	}
	print json.dumps(response)
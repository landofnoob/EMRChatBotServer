# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import psycopg2
import datetime

class Action():

    def __init__(self):
        pass

    def insert(self,Table,Values):
        status = ''
        parameter = ''
        data = "'"
        con = None
        print Values
        try:
            for key , key_values  in Values.iteritems():
                parameter = parameter + key + ","
                data = data + str(key_values) +"','"
            parameter = parameter[:-1]
            data = data[:-2]
            #print data 
            #print parameter
            #Command
            insert = "insert into "+Table+"("+parameter+")values("+data+");"
            print(insert)
            #Add to DbMS
            con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')   
            cur = con.cursor()
            cur.execute(insert)
            con.commit()
            status = "success"
        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            status = e
        finally:     
            if con:
                con.close()
            return status

    def queryOne(self,Table,Where_Parameter,Where_Data,Parameter):
        values = None
        where =''
        where = Where_Parameter +" = '" +Where_Data+"'"
        con = None
        #Command
        query = "select "+Parameter+" from "+Table+" where "+where+";"
        #print(query)
        try:
            con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')   
            cur = con.cursor()
            cur.execute(query)
            values = cur.fetchone()[0]
            con.commit()
        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            values = None
        finally:     
            if con:
                con.close()
            return values

    def update(self,Table,Where_Parameter,Where_Data,Values):
        con = None
        status = ''
        parameter = ''
        try:
            #print Values
            for key , key_values  in Values.iteritems():
                if type(key_values) == int:
                    print type(key_values)
                    parameter = parameter + key +"="+str(key_values)+","
                else:
                    print type(key_values)
                    parameter = parameter + key +"='"+key_values+"',"      
            parameter = parameter[:-1]
            #print data 
            #print parameter
            #Command
            update = "UPDATE "+Table+" set "+parameter+" where "+Where_Parameter+"=" + "'" + Where_Data + "';"
            print(update)
            #Add to DbMS
            con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')   
            cur = con.cursor()
            cur.execute(update)
            con.commit()
            status = "success"
        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            status = e
        finally:     
            if con:
                con.close()
            return status

    def delete(self,Table,Where_Parameter,Where_Data):
        status = ''
        Where_Data = "'"+Where_Data+"'"
        con = None
        #Command
        delete = "DELETE FROM "+Table+" WHERE "+Where_Parameter+"="+Where_Data+";"
        try:
            print "Trying to Delete"
            print "COMAND : %s " % delete
            con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456') 
            print "Connecting to Database"
            cur = con.cursor()
            cur.execute(delete)
            print "Exe Delete"
            con.commit()
            status = "success"
        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            status = e
        finally:     
            if con:
                con.close()
            print "STATUS DELETE : %s" % status
            return status

    def IsCheckMatch(self,Table,Parameter,Data):
        print "Is Checking Match ?"
        ######### Select data
        status =''
        con = None
        query = "SELECT "+Parameter+" FROM "+Table+" WHERE "+Parameter+"='" + Data + "';"
        print query
        try:
            print "Try Connect Database"
            con = psycopg2.connect(database='EMRchatbot3', user='postgres', host='/tmp', password='123456')
            print "Set Cursor()"
            cur = con.cursor()
            print "Execute Query Program"
            cur.execute(query)
            values = cur.fetchall()
            print "fectchone()[0] : %s" % values
            con.commit()
            print "values : %s" % values
            if values == []:
                status = False
            else:
                status = True
        except psycopg2.Error, e:
            print "Error Database"
            if con:
                con.rollback()
            print 'Error %s' % e
            status = 'Error'
        finally:     
            print "finally"
            if con:
                con.close()
            return status
        
        ''' Old Code
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
        '''
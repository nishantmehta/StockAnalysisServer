import DataStructure

__author__ = 'WHAAAAAAAt'

import urllib2
import json
import node1
import datetime
import time

import threading2
from threading2 import *

#we need to put all the data collection logic here

#the work which was done yesterday will go here

class DataCollection():


    def producerFunctions(self,dataStructure ):
        # we need to the frequency of server ping for each stock
        # possible changes in the looping structure
        # All data needs to be stored in the arg.stockHash[<company code>]
        googleURL='http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22GOOG%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
        yahooURL='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
        appleURL='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22AAPL%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='

        while (True):
            ts=time.time()

            #google quote ping
            weburl = urllib2.urlopen(googleURL)
            data = weburl.read()
            da=json.loads(data)
            google=node1.node1( datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') ,str(da['query']['results']['quote']['LastTradePriceOnly']))

            #yahoo quote ping
            weburl = urllib2.urlopen(yahooURL)
            data = weburl.read()
            da=json.loads(data)
            yahoo=node1.node1( datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') ,str(da['query']['results']['quote']['LastTradePriceOnly']))

            #google quote ping
            weburl = urllib2.urlopen(appleURL)
            data = weburl.read()
            da=json.loads(data)
            apple=node1.node1( datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') ,str(da['query']['results']['quote']['LastTradePriceOnly']))

            #acquire locks
            dataStructure.lock.acquire(shared = True )
            try:
                dataStructure.stockHash["Google"].append(google)
                dataStructure.stockHash["Apple"].append(apple)
                dataStructure.stockHash["Yahoo"].append(yahoo)
            finally:
                dataStructure.lock.release()
            #revoke lock

            #wait until refresh time expires
            time.sleep(3)
            '''
            for company in dataStructure.stockHash:
                print "company has # of values "+ company +" "+ str(len(dataStructure.stockHash[company]))

            '''
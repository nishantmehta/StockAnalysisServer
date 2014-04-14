import DataStructure

__author__ = 'WHAAAAAAAt'

import urllib2
import json
import node1
import datetime
import time
#we need to put all the data collection logic here

#the work which was done yesterday will go here

class DataCollection():


    def producerFunctions(self,args ):
        # we need to the frequency of server ping for each stock
        # possible changes in the looping structure
        # All data needs to be stored in the arg.stockHash[<company code>]
        count = 3
        for i in range(20):
            if(i%3==0):
                if count==3:
                    urldata = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22GOOG%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
                    weburl = urllib2.urlopen(urldata)
                    data = weburl.read()
                    da=json.loads(data)
                    ts=time.time()
                    obj1=node1.node1( datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') ,str(da['query']['results']['quote']['LastTradePriceOnly']))
                    args.lock.acquire()
                    try:
                        args.stockHash['goog'].append(obj1)
                        count=count-1
                    finally:
                        args.lock.release()

                elif count==2:
                    urldata = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
                    weburl = urllib2.urlopen(urldata)
                    data = weburl.read()
                    da=json.loads(data)
                    ts=time.time()
                    obj2=node1.node1( datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),str(da['query']['results']['quote']['LastTradePriceOnly']))
                    args.lock.acquire()
                    try:
                        args.stockHash['Yahoo'].append(obj2)
                        count=count-1
                    finally:
                        args.lock.release()

                elif count==1:
                    urldata = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22AAPL%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
                    weburl = urllib2.urlopen(urldata)
                    data = weburl.read()
                    da=json.loads(data)
                    ts=time.time()
                    obj3=node1.node1(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),str(da['query']['results']['quote']['LastTradePriceOnly']))
                    args.lock.acquire()
                    try:
                        args.stockHash['Apple'].append(obj3)
                        count=3
                    finally:
                        args.lock.release()





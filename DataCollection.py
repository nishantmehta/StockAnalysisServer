__author__ = 'nishantmehta.n'

import urllib2
import json

import time
#we need to put all the data collection logic here

#the work which was done yesterday will go here

class DataCollection():
    def producerFunctions(self,arg):
        # we need to the frequency of server ping for each stock
        # possible changes in the looping structure
        # All data needs to be stored in the arg.stockHash[<company code>]
        for i in range(1000):
            urldata = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22GOOG%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
            weburl = urllib2.urlopen(urldata)
            data = weburl.read()
            da=json.loads(data)
            arg.stockHash['goog'].append(str(da['query']['results']['quote']['LastTradePriceOnly']))
            time.sleep(2)



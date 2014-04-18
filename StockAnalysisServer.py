#this will be our main controller, it will start all process and handle user request
from collections import defaultdict
import threading

from flask import Flask
from threading import Thread
import DataStructure
import DataCollection
import threading

import QueryFunctions
import result

import threading2
from threading2 import *


# created a lock that can be shared using Shared variable associated with it
# if lock.share = true  --- multiple locks can shared the lock
# if lock.share = false --- the lock becomes an exclusive lock

lock  = SHLock()
alist = defaultdict(list)
#initialize data structure to store stock quotes
dataStruct = DataStructure.DataStructure(lock,alist)

#initialize the data structure
dataStruct.structInit(dataStruct)


#initializa the thread to collect data from yahoo api
dataCollectionObj =DataCollection.DataCollection()


thread =  Thread(target = dataCollectionObj.producerFunctions, args= [dataStruct])
thread.start()
#thread.join()


app = Flask(__name__)


#access the dataStructure like this
#print dataStruct.stockHash


#functions for thread can be used in similar fashion


#our flask structure remains the same
@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route('/query1/')
def index():
    consumer=QueryFunctions.queries()
    resultData=result.res()
    consumerThread = Thread(target = consumer.query2,args=['Google',dataStruct,10,resultData])
    consumerThread.start()
    consumerThread.join()
    return resultData.data;

@app.route('/BestDealsForStock/')
def bestProfit():
    consumer=QueryFunctions.queries()
    resultData=result.res()
    consumerThread = Thread(target = consumer.query3,args=[dataStruct,resultData])
    consumerThread.start()
    consumerThread.join()
    return resultData.data;

@app.route('/Stablestock/')
def stable():
    consumer=QueryFunctions.queries()
    resultData=result.res()
    consumerThread = Thread(target = consumer.query4,args=[dataStruct,resultData])
    consumerThread.start()
    consumerThread.join()
    return resultData.data;

if __name__ == '__main__':
    app.run()

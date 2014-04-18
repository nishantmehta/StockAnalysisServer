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

#changing to Shared Lock
lock = SHLock()
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

    # return 'Hello World!'
    return len(dataStruct.stockHash)


@app.route('/query2/')
def index():
    consumer=QueryFunctions.queries()
    # resultData=result.res()
    # consumerThread = Thread(target = consumer.query1,args=[dataStruct,resultData])
    # consumerThread.start()
    # consumerThread.join()
    #return resultData.data;

    resultData1=result.res()
    consumerThread2 = Thread(target = consumer.query2,args=('goog',dataStruct,10,resultData1,))
    consumerThread2.start()
    consumerThread2.join()
    # print "result of query is " + resultData1.data;
    return "result of query is " + resultData1.data;


if __name__ == '__main__':
    app.run()

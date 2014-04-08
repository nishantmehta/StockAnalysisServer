#this will be our main controller, it will start all process and handle user request

from flask import Flask
import DataStructure
import DataCollection
from threading import Thread




#initialize data structure to store stock quotes
dataStruct = DataStructure.DataStructure()

#initialize the data structure
dataStruct.structInit(dataStruct)


#initializa the thread to collect data from yahoo api
dataCollectionObj =DataCollection.DataCollection()
thread =  Thread(target = dataCollectionObj.producerFunctions, args= [dataStruct])
thread.start()
thread.join()




app = Flask(__name__)


#access the dataStructure like this
print dataStruct.stockHash

#functions for thread can be used in similar fashion


#our flask structure remains the same
@app.route('/')
def hello_world():

    return 'Hello World!'


if __name__ == '__main__':
    app.run()

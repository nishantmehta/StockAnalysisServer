import heapq
import math
from collections import defaultdict
__author__ = 'nishantmehta.n'
import  threading2
from threading2 import *


#all the query functions will be written here

class queries():
    def query1(self,arg):
        print("new query request")
        for i in arg.stockHash['goog']:
            print(i)

    def query2(self,coName,dataStructure,n,result):
        # coName : name of the company
        # obj : obj thread passed
        # n   : TOP n stocks variable
        result.data = ''
        print "Top n max and min"+'\n'
        #a min heap queue to hold max 10 values
        maxHeap = []
        # a min heap queue to hold min 10 values
        minHeap = []
        # Min Max algorithm

        #--acquire the lock in shared mode so that
        #--concurrent threads can acquire it simultaneously

        dataStructure.lock.acquire(shared = True )
        try:
            # print "inside lock..l"
            stockList = dataStructure.stockHash[coName]
            # print "length of ds is " + str(len(stockList)) + "\n"
            j = 0
            for i in stockList:
                temp =float(i.price)
                tempn=-temp

                if j < n:
                    heapq.heappush(maxHeap,temp)
                    heapq.heappush(minHeap,tempn)
                    j+= 1

                else:
                    if maxHeap[0] < temp:
                        heapq.heapreplace(maxHeap,temp)
                    if minHeap[0] < tempn:
                        heapq.heapreplace(minHeap,tempn)
        finally:
            dataStructure.lock.release()

        # End of read , return the result back to calling function


        #print the max 10 values
        result.data += 'Max Values' + '<br>'
        for j in maxHeap:
            # print str(j) +  '\n'
            result.data += str(j) +  '<br>'
        #print the min 10 values
        result.data += 'Min Values' + '<br>'
        # print "length " + str(len(minHeap))
        for k in minHeap:
            result.data +=  str(-k) + '<br>'

    #@do_profile(follow=[])
    def query3(self, dataStructure,result):
        result.data=""
        dataStructure.lock.acquire(shared = True )
        try:
            for company in dataStructure.stockHash.iterkeys():
                #print company
                arrayOfDiff=[]
                sizeOfStruct=len(dataStructure.stockHash[company])
                #print sizeOfStruct
                for i in range (0,sizeOfStruct-1):
                    arrayOfDiff.append(float(dataStructure.stockHash[company][i+1].price)- float(dataStructure.stockHash[company][i].price))

                maxDiff=arrayOfDiff[0]
                #print arrayOfDiff

                for j in range (1,sizeOfStruct-1):
                    if (arrayOfDiff[j-1]>0):
                        arrayOfDiff[j]+=arrayOfDiff[j-1]
                    if(maxDiff<arrayOfDiff[j]):
                        maxDiff=arrayOfDiff[j]
                result.data += "max profit for " + company + " could have been " + str(maxDiff) + "<br>"
        finally:
            dataStructure.lock.release( )





    def query4(self,dataStructure,result):
        result.data=""
        min=0
        for company in dataStructure.stockHash.iterkeys():
            sizeOfStruct=len(dataStructure.stockHash[company])
            data=[]
            s=0
            ss=0
            for i in range (0,sizeOfStruct-1):
                s = s + float(dataStructure.stockHash[company][i].price)
                ss= ss + float(dataStructure.stockHash[company][i].price)**2
                #data.append(dataStructure.stockHash[company][i].price)

            mean=s/sizeOfStruct
            svar=ss-((s**2)/sizeOfStruct)
            var= svar /(sizeOfStruct-1)
            if(min<var):
                min=str(var)+"  Company Name: "+ company
        result.data = "Most stable value" + min





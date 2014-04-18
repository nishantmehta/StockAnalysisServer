import heapq
import math
from collections import defaultdict
__author__ = 'nishantmehta.n'


#all the query functions will be written here

class queries():
    def query1(self,arg):
        print("new query request")
        for i in arg.stockHash['goog']:
            print(i)

    def query2(self,coName,obj,n,resultset):
        # coName : name of the company
        # obj : obj thread passed
        # n   : TOP n stocks variable

        print "Top n max and min"+'\n'
        #a min heap queue to hold max 10 values
        maxHeap = []
        # a min heap queue to hold min 10 values
        minHeap = []
        # Min Max algorithm
        stockList = obj.stockHash[coName]
        j = 0
        for i in stockList:
            if j < n:
              heapq.heappush(maxHeap,stockList[i].price)
              heapq.heappush(minHeap,(-1)*stockList[i].price)
              j += 1
            else:
                if maxHeap[0] < stockList[i].price:
                    heapq.heapreplace(maxHeap,stockList[i].price)
                if minHeap[0] < (-1 * stockList[i]):
                    heapq.heapreplace(minHeap,(-1)*stockList[i].price)
        resultset.data = ''
        #print the max 10 values
        resultset.data = 'Max Values' + '\n'
        for i in maxHeap:
            resultset.data += maxHeap[i]+'\t'
        #print the min 10 values
        resultset.data = 'Min Values' + '\n'
        for i in minHeap:
            resultset.data += minHeap[i]+'\t'

    #@do_profile(follow=[])
    def query3(self, dataStructure,result):
        result.data=""
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





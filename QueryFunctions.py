import heapq
from collections import defaultdict
__author__ = 'nishantmehta.n'
import  threading2
from threading2 import *
'''
try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner
'''
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
            stockList = dataStructure.stockHash[coName]
            j = 0
            for i in stockList:
                if len(maxHeap) < n :
                  heapq.heappush(maxHeap,i.price)

                elif len(minHeap)< n:
                    heapq.heappush(minHeap,(-1)*i.price)

                else:
                    if maxHeap[0] < i.price:
                        # print "heap max " + maxHeap[0] + " " + i.price
                        heapq.heapreplace(maxHeap,i.price)
                    if minHeap[0] < (-1 * i):
                        # print "heap min " + minHeap[0] + " " + i.price
                        heapq.heapreplace(minHeap,(-1)*i.price)
        finally:
            dataStructure.lock.release()

        # End of read , return the result back to calling function

        result.data = ''
        #print the max 10 values
        result.data = 'Max Values' + '<br>'
        for i in maxHeap:
            result.data += maxHeap[i]+'\t'
        #print the min 10 values
        result.data = 'Min Values' + '<br>'
        for i in minHeap:
            result.data += minHeap[i]+'\t'

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
        finally:
            dataStructure.lock.release( )

        result.data += "max profit for " + company + " could have been " + str(maxDiff) + "<br>"






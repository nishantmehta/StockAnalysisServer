import heapq

__author__ = 'nishantmehta.n'


#all the query functions will be written here

class queries():
    def query1(self,arg):
        print("new query request")
        for i in arg.stockHash['goog']:
            print(i)

    def query2(self,coName,obj,n,):
        # coName : name of the company
        # obj : obj thread passed
        # n   : TOP n stocks variable

        print("Top n max and min",end='\n')
        #a min heap queue to hold max 10 values
        maxHeap = []
        # a min heap queue to hold min 10 values
        minHeap = []
        # Min Max algorithm
        stockList = obj.stockHash[coName]
        j = 0
        for i in stockList:
            if j < n:
              heapq.heappush(maxHeap,stockList[i])
              heapq.heappush(minHeap,(-1)*stockList[i])
              j += 1
            else:
                if maxHeap[0] < stockList[i]:
                    heapq.heapreplace(maxHeap,stockList[i])
                if minHeap[0] < (-1 * stockList[i]):
                    heapq.heapreplace(minHeap,(-1)*stockList[i])

        #print the max 10 values
        for i in maxHeap:
            print(maxHeap[i],end='\n')
        #print the min 10 values
        for i in minHeap:
            print(minHeap[i],end='\n')






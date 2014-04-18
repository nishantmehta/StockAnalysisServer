import heapq
import result
import node1
__author__ = 'nishantmehta.n'


#all the query functions will be written here

class queries():
    def query1(self,arg):
        print("new query request")
        for i in arg.stockHash['goog']:
            print(i)

    def query2(self,coName,obj,n,result):
        # coName : name of the company
        # obj : obj thread passed
        # n   : TOP n stocks variable


        #a min heap queue to hold max 10 values
        maxHeap = []
        #a min heap queue to hold min 10 values
        minHeap = []
        # Min Max algorithm
        obj.lock.acquire(shared=True)
        try:
            stockList = obj.stockHash[coName]

            # test --print "size of array in goog is " + str(len(stockList)) + '\n'
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
            # print "Max heap price is " + maxHeap[0]
            result.data = ''
            #print the max 10 values
            result.data = 'Max Values' + '<br>'
            for j in maxHeap:
                result.data += str(j) + '<br>'
                print j + '\n'
            #print the min 10 values
            #result.data = 'Min Values' + '\n'
            # for k in minHeap:
            #     result.data += k +'\t'
        finally:
           obj.lock.release()





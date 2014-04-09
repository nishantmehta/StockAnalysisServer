__author__ = 'nishantmehta.n'


#all the query functions will be written here

class queries():


    def query1(self,arg,result):
        print "new query request"
        for i in arg.stockHash['goog']:
            print i
        result.data="some result"


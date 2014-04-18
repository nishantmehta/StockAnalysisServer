import threading
import threading2
from threading2 import *
__author__ = 'nishantmehta.n'
from collections import defaultdict
#complete designing of the data structure goes here,the lock is passed to the ds in the contructor so later on its used via object i.e args


class DataStructure(threading.Thread):

    def __init__(self,lock,thelist):
        self.stockHash=thelist
        self.lock = lock

    def structInit(self,args):
        #add companies here
        args.stockHash["Google"]
        args.stockHash["Yahoo"]
        args.stockHash["Apple"]


def lock():
    return None
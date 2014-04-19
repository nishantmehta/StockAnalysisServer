__author__ = 'Mayank'

import threading
from threading import *
from time import time
import result

class queryCacheNode:
    def __init__(self,):
        self.cv = Condition()
        self.qresult = result.res()
        self.qresult.data="@@Cached ::"
        self.time = time()
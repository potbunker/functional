from multiprocessing.pool import ThreadPool
import random
from itertools import count

import time

def process(index):
    print "trying"
    time.sleep(random.randint(1,10))
    val = 'Done {}'.format(index)
    return val

def callback(x):
    print x


pool = ThreadPool(10)

pool.map_async(process, xrange(10), 3, callback=callback)


print 'Done Done'



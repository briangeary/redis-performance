import sys
import time
import timeit
import json
import os


clientname = "Fast loader"
file = sys.argv[1]


print("Starting " + clientname)
starttime = timeit.default_timer()
os.system('cat ' + file + '| redis-cli -h 172.31.34.59 -p 6379 --pipe')

print("Time for " + clientname + ":" +  str(timeit.default_timer() - starttime) + " keys (" + file + ")")




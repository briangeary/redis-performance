import sys
import time
import timeit
import redis

redis_client = redis.Redis(host='172.31.34.59', port=6379, db=0)

# This will get all the keys and then get the value for each key
# This will block the redis server until the keys command completes
# and the client will need to load all the keys into memory
def start(clientname, delay):
  if (delay > 0):
    print("Sleeping" + clientname + " for " + str(delay) + " seconds") 
    time.sleep(delay)
  print("Starting " + clientname)
  starttime = timeit.default_timer()
  for key in redis_client.keys("*"):
    key = None
  print("Time for " + clientname + ":", str(timeit.default_timer() - starttime) )

#start("cn", 0)



import sys
import time
import timeit
import redis

redis_client = redis.Redis(host='172.31.34.59', port=6379, db=0, decode_responses=True)

# This will get all the keys and then get the value for each key
# This will block the redis server on each scan 
# The client will need to only load the keys fetched on each scan.
# Then we will use mget to get the values for all the keys.
def start(clientname, delay):
  if (delay > 0):
    print("Sleeping" + clientname + " for " + str(delay) + " seconds") 
    time.sleep(delay)
  print("Starting " + clientname)
  starttime = timeit.default_timer()

  cursor = '0'
  while cursor != 0:
    cursor, keys = redis_client.scan(cursor=cursor, match="*", count=500)
    keys = None

  print("Time for " + clientname + ":", str(timeit.default_timer() - starttime))

#start("cn", 0)



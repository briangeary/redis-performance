import sys
import time
import timeit
import json
import redis

redis_client = redis.Redis(host='172.31.34.59', port=6379, db=0)

totalkeys=0

clientname = "Slow loader"
file = sys.argv[1]
infile = open(file, "r")


print("Starting " + clientname)
starttime = timeit.default_timer()
for line in infile:
  totalkeys = totalkeys + 1
  line=line.strip()
  d = json.loads(line)
  dkey = d['studentid']
  redis_client.set(dkey, line)

print("Time for " + clientname + ":" +  str(timeit.default_timer() - starttime) + " keys (" + str(totalkeys) + ")")

infile.close()



import sys
from multiprocessing import Process
import slowkeyclient

numclient=int(sys.argv[1])
# Well it might be faster than the scan function
for c in range(1, numclient+1):
  delay = 0
  p = Process(target=slowkeyclient.start, args=('Slow Key Client '+str(c),delay,))
  p.start()

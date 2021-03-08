import sys
from multiprocessing import Process
import slowclient

numclient=int(sys.argv[1])

for c in range(1, numclient+1):
  delay = 0
  p = Process(target=slowclient.start, args=('Slow Client '+str(c),delay,))
  p.start()

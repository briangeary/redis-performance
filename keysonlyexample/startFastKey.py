import sys
from multiprocessing import Process
import fastkeyclient

numclient=int(sys.argv[1])
# Well it may not be so fast compared to keys
for c in range(1, numclient+1):
  delay = 0
  p = Process(target=fastkeyclient.start, args=('Fast Key Client '+str(c),delay,))
  p.start()

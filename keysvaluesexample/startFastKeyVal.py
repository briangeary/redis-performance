import sys
from multiprocessing import Process
import fastclient

numclient=int(sys.argv[1])

for c in range(1, numclient+1):
  delay = 0
  p = Process(target=fastclient.start, args=('Fast Client '+str(c),delay,))
  p.start()

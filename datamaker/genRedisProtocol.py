import sys
import json

# redis protocol specifies \r\n as line terminator regardless if you are executing from 
# a Windows or Linux operating system

def gen_redis_protocol(file):
  outfile = open(file + ".redisproto", "w")

  with open(file) as infile:
    for line in infile:
      line=line.strip()
  
      # write the operation outfile
      outfile.write('*3\r\n')
      outfile.write('$3\r\n') # length of SET operation name
      outfile.write('SET\r\n')# operation

      # write the redis key outfile
      d = json.loads(line)
      dkey = d['studentid']
      dlenkey = len(str(dkey))
      outfile.write('$' + str(dlenkey) + '\r\n') # length of key
      outfile.write(str(dkey) + '\r\n')# write outfile key

      data = json.dumps(line)
      dlendata = len(data)
      outfile.write('$' + str(dlendata) + '\r\n') # length of key
      outfile.write(data + '\r\n')# write outfile key

      outfile.write('\r\n')# 

  infile.close()
  outfile.close()

gen_redis_protocol(sys.argv[1])
#gen_redis_protocol('./data/100students.json')
#gen_redis_protocol('./data/100thousandstudents.json')
#gen_redis_protocol('./data/1millionstudents.json')
#gen_redis_protocol('./data/5millionstudents.json')
#gen_redis_protocol('./data/10millionstudents.json')
#gen_redis_protocol('./data/100millionstudents.json')




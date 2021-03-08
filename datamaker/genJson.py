import json
from faker import Faker
import random
from random import randint


student_dict = {}

fake = Faker('en_US')
for sid in range(1,101):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': float(random.randrange(155, 389))/100 }}
  student_dict[sid] = student

f = open("./data/100students.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()


student_dict = {}

fake = Faker('en_US')
for sid in range(1,100001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': float(random.randrange(155, 389))/100 }}
  student_dict[sid] = student

f = open("./data/100thousandstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()



student_dict = {}

fake = Faker('en_US')
for sid in range(1,10000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10amillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()


student_dict = {}

fake = Faker('en_US')
for sid in range(10000001,20000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10bmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()




student_dict = {}

fake = Faker('en_US')
for sid in range(20000001,30000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10cmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()



student_dict = {}

fake = Faker('en_US')
for sid in range(30000001,40000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10dmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()




student_dict = {}

fake = Faker('en_US')
for sid in range(40000001,50000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10emillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()



student_dict = {}

fake = Faker('en_US')
for sid in range(50000001,60000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10fmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()




student_dict = {}

fake = Faker('en_US')
for sid in range(60000001,70000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10gmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()



student_dict = {}

fake = Faker('en_US')
for sid in range(70000001,80000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10hmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()


student_dict = {}

fake = Faker('en_US')
for sid in range(80000001,90000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10imillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()




student_dict = {}

fake = Faker('en_US')
for sid in range(90000001,100000001):
  student = {'studentid': sid, 'bar': {'name': fake.name(), 'gpa': "4.0" }}
  student_dict[sid] = student

f = open("./data/10jmillionstudents.json", "w")
for k in student_dict.keys():
  f.write(json.dumps(student_dict[k]))
  f.write('\n')
f.close()





























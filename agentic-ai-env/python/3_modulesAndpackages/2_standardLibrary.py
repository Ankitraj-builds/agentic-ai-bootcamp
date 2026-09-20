#array- type strict
import array

arr=array.array('i',[1,2,3,4,5])

print(arr)
print(type(arr))


#maths
import math
print(math.pi)


#Random

import random

print(random.randint(1,11))
print(random.choice(['apple','kiwi','banana']))



#os
import os
print(os.getcwd())


#high level operation with files or collection of files

import shutil
shutil.copyfile('src.txt','dest.txt')


#Data serialization

import json
data={'name':'Ankit','age':25}

data_str=json.dumps(data)
print(data_str)
print(type(data_str))

parsed_data=json.loads(data_str)
print(parsed_data)
print(type(parsed_data))



#csv
import csv

with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Ankit',11])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


#datetime

from datetime import datetime,timedelta

now=datetime.now()
print(now)

date=datetime.date(now)
print(date)

yesterday=now-timedelta(days=1)
print(yesterday)


#time
import time
print(time.time())
# time.sleep(5)
# print(time.time())


#regulr expression
import re
pattern=r'\d+'
text = 'there is 123 apple'
match=re.search(pattern,text)
print(match.group())



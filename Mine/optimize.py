import time
import random
import math

people = [('Seymour','BOS'),
    ('Franny','DAL'),
    ('Zooey',''),
    ('Walt','MIA'),
    ('Buddy','ORD'),
    ('Les','OMA')]
destination='LGA'
flights={}
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price=line.strip().split(',')
    flights.setdefault((origin,dest),[])
    flights[(origin,dest)].append(depart,arrive,int(price))
#时间计算函数
def getminutes(t):
    x = time.strftime(t,'%H:%M')
    return x[3]*60+x[4]
def schedulecost(sol):





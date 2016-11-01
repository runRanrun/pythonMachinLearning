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
    return x[3]*60+x [4]
def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
    earliestdep = 24*60
    for d in range(len(sol)/2):
        origin = people[d][1]
        outbound=flights[(origin,destination)][int(sol[2*d])]
        returnf=flights[(destination,origin)][int(sol[2*d+1])]

        totalprice+=outbound[2]
        totalprice+=returnf[2]

        




import time
import random
import math

people = [('Seymour','BOS'),
    ('Franny','DAL'),
    ('Zooey','CAK'),
    ('Walt','MIA'),
    ('Buddy','ORD'),
    ('Les','OMA')]
destination='LGA'
flights={}
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price=line.strip().split(',')
    flights.setdefault((origin,dest),[])
    flights[(origin,dest)].append((depart,arrive,int(price)))


#
def getminutes(t):
    x = time.strftime(t,'%H:%M')
    return x[3]*60+x[4]


def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
    earliestdep = 24*60
    for d in range(len(sol)/2):
        origin = people[d][1]
        outbound = flights[(origin,destination)][int(sol[2*d])]
        returnf = flights[(destination,origin)][int(sol[2*d+1])]


        totalprice += outbound[2]
        totalprice += returnf[2]
        #the cost on board is 0.5 dollar per hour
        totalprice += 0.5*(getminutes(outbound[1])-getminutes(outbound[0]))
        totalprice += 0.5*(getminutes(returnf[1])-getminutes(returnf[0]))
        #everyone who is late will pay 20 dollars
        if getminutes(outbound[0]) < getminutes("8:00"):
            totalprice += 20

        if latestarrival<getminutes(outbound[1]):
            latestarrival=getminutes(outbound[1])
        if earliestdep>getminutes(returnf[0]):
            earliestdep=getminutes(returnf[0])
    totalwait=0
    for d in range(len(sol)/2):
        origin=people[d][1]
        outbound=flights[(origin,destination)][int(sol[2*d])]
        returnf=flights[(destination,origin)][int(sol[2*d+1])]
        totalwait+=latestarrival-getminutes(outbound[1])
        totalwait+=getminutes(returnf[0])-earliestdep
        if latestarrival<earliestdep:totalwait+=50
        return totalprice+totalwait


def hillclimb(domain,costf):
    sol=[random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]

    while 1:
        neighbors=[]
        for j in range(len(domain)):
            if sol[j]>domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])
            if sol[j]<domain[j][1]:
                neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
        current=costf(sol)
        best=current
        for j in range(len(neighbors)):
            cost=costf(neighbors[j])


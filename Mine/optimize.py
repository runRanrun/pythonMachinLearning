import time
import random
import math
import sys



#
def getminutes(t):
    x = time.strptime(t,'%H:%M')
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
       # totalprice += 0.5*(getminutes(outbound[1])-getminutes(outbound[0]))
       # totalprice += 0.5*(getminutes(returnf[1])-getminutes(returnf[0]))
        #everyone who is late will pay 20 dollars
        #if getminutes(outbound[0]) < getminutes("8:00"):
       #     totalprice += 20

        if latestarrival<getminutes(outbound[1]):
            latestarrival=getminutes(outbound[1])
        if earliestdep>getminutes(returnf[0]):
            earliestdep=getminutes(returnf[0])
    totalwait=0
    for d in range(len(sol)/2):
        origin=people[d][1]
        #print d
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
            if cost<best:
                best=cost
                sol=neighbors[j]
        if best==current:
                break
    return sol

def printschedule(r):
    for d in range(len(r)/2):
        name=people[d][0]
        origin=people[d][1]
        #print r[2*d]
        out=flights[(origin,destination)][int(r[2*d])]
        ret=flights[(destination,origin)][int(r[2*d+1])]
        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,out[0],out[1],out[2],ret[0],ret[1],ret[2])


def anealingoptimize(domain, costf, T=10000.0, cool=0.98, step=1):
    # initial random value

    vec = [float(random.randint(domain[i][0], domain[i][1])) for i in range(len(domain))]
    while T > 0.1:
        i = random.randint(0, len(domain) - 1)
        dir = random.randint(-step, step)
        vecb = vec[:]  # put the value from vec to vecb
        vecb[i] += dir
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]

        ea = costf(vec)
        eb = costf(vecb)

        if (eb < ea or random.random() < pow(math.e,-(eb - ea)/T)):
            vec = vecb
        T = T * cool
    return vec

def geneticoptimize(domain,costf,popsize=50,step=1,mutprob=0.2,elite=0.2,maxiter=100,quititer=30):
    def mutate(vec):#select random value from vec to mutate
        i=random.randint(0,len(domain)-1)
        if random.random()<0.8 and vec[i]>domain[i][0]:
            return vec[0:i]+[vec[i]-step]+vec[i+1:]
        elif vec[i]<domain[i][1]:
            return vec[0:i]+[vec[i]+step]+vec[i+1:]
        return vec
    def crossover(r1,r2):
        i=random.randint(1,len(domain)-2)
        return r1[0:i] + r2[i:]
        # if r1[0:i]+r2[i:]!= None:
        #     return r1[0:i]+r2[i:]
        # else:
        #     exit(-2)

    pop=[] #create a population
    for i in range(popsize):
        vec=[random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
        pop.append(vec)
    topelite=int(elite*popsize)
    for i in range(maxiter):
        # print "maxiter",i
        scores=[(costf( v),v) for v in pop]
        scores.sort()
        ranked=[v for (s,v) in scores]
        if pop[0:topelite]==ranked[0:topelite]:
            quititer-=1
            if quititer==0:
                print i
                break
        pop=ranked[0:topelite]

        # if None in pop:
        #     print "pop None Error in rank"

        while len(pop)<popsize:
            if random.random()<mutprob:
                c=random.randint(0,topelite)
                #if mutate(ranked[c])!= None:
                pop.append(mutate(ranked[c]))
                # if None in pop:
                #     print "pop None Error in mutate",mutate(ranked[c])
                # else:
                #     print "mutate ok"
            else:
                c1=random.randint(0,topelite)
                c2=random.randint(0,topelite)
                pop.append(crossover(ranked[c1],ranked[c2]))
                #if None in pop:
                   # print "pop None Error in crossover",crossover(ranked[c1],ranked[c2])
        # print scores[0][0]
    return scores[0][1]

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
domain=[(0,9)]*(len(people*2))
randcount = 0
anealcount = 0
for j in range(0,1):#iter 100 to compare the climb and aneal optimize
    min1 = sys.maxint
    sflag1={}
    for i in range(0,200):
        s=hillclimb(domain,schedulecost)
        if (min1>schedulecost(s)):
            min1 = schedulecost(s)
            sflag1=s
    print "climb way:",schedulecost(sflag1)
    printschedule(sflag1)

    min = sys.maxint
    sflag={}
    for i in range(0,200):
        s=anealingoptimize(domain,schedulecost)
        if (min>schedulecost(s)):
            min = schedulecost(s)
            sflag=s
    print "anneal way:",schedulecost(sflag)
    printschedule(sflag)
    if(min1<min):
        randcount+=1
    else:
        anealcount+=1
print "randcount:",randcount,"anealcount:",anealcount
s = geneticoptimize(domain,schedulecost)
printschedule(s)
print "genetic way:",schedulecost(s)
# out=file('RandAndAneal.txt','w')
# out.write('%d\t' % randcount)
# out.write('%d\t' % anealcount)
# out.close()



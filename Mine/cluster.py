from math import sqrt

#from PIL import Image,ImageDraw
#import jieba

import random
#readfile
def readfile(filename):
    wordcount=[]
    data = [line for line in file('StoneStoryData.txt')]
    #print(len(data))
    for i in range(1,len(data)):
        wordcount.append([float (x) for x in data[i].strip().split('\t')])
        #for j in range(0,len(wordcount)):
    # for a in wordcount:
    #     for p in a:
    #         print p
    return wordcount

#pearson distance
def pearson(v1,v2):
  # Simple sums

  sum1=sum(v1)
  sum2=sum(v2)
  #print "sum1:",sum1,"sum2:",sum2
  # Sums of the squares
  sum1Sq=sum([pow(v,2) for v in v1])
  sum2Sq=sum([pow(v,2) for v in v2])


    # Sum of the products
  pSum=sum([v1[i]*v2[i] for i in range(len(v1))])



  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/len(v1))

  #print "sum1:",sum1,"sum2:",sum2,"pSum:",pSum,num

  den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
  if den==0: return 0

  return 1-num/den


#k-means
def kmeans(pointcount,data):
    #
    #pointcount = pointcount
    judge = 10000
    result = {}
    resultrecord = {}
    for iter in range(200):
        ranges = [(min([singledata[i] for singledata in data]),max([singledata[i] for singledata in data])) for i in range(0,len(data[0]))]
       # for value in ranges:
        #    print value[0],value[1]
        kclusters = [[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] for i in range(0,len(data[0]))] for j in range(0,pointcount)]

        # for i in range(len(data)):
        #     for j in range(len(data[0])):
        #         if i<80:
        #             kclusters[0][j] += data[i][j]
        #         else:
        #             kclusters[1][j]+= data[i][j]
        # for i in range(len(kclusters[0])):
        #     kclusters[0][i]/=80
        #     kclusters[1][i]/=40
        kdistance =[]
        temp_distance = []
        lastmatches = None
        for t in range(20):
            kdistance = []
            for k in range(len(kclusters)):
                for i in range(len(data)):
                    temp_distance.append(pearson(kclusters[k],data[i]))
                kdistance.append(temp_distance)
                temp_distance = []
            bestmatches=[[] for i in range(len(kclusters))]
            for i in range(len(kclusters)):
                for j in range(len(kclusters[0])):
                    bestmatches[i].append(0)
            countRecord={}
            for i in range(len(kdistance)):
                countRecord[i] = 0
            arrayrecord = [[]for i in range(len(kclusters))]
            for i in range(len(kdistance[0])):
                minvalue = 3000
                minrecord= 0
                for j in range(len(kdistance)):
                    if minvalue >= kdistance[j][i]:
                        minvalue = kdistance[j][i]
                        minrecord = j
                arrayrecord[minrecord].append(i)
                countRecord[minrecord]+=1
                for j in range(len(kclusters[0])):
                    bestmatches[minrecord][j]+=data[i][j]
            #print "countrecord:",countRecord,t
            for i in range(len(bestmatches)):
                for j in range(len(bestmatches[0])):
                    bestmatches[i][j]/=countRecord[i]
            #if bestmatches==kclusters:
                #print kdistance[0],"\n",kdistance[1],'\n',t
                #break
            kclusters = bestmatches
        #print kclusters[0],"\n",kclusters[1]
        #print sum(kdistance[0]),"\n",sum(kdistance[1])
        if(judge>sum(kdistance[0])+sum(kdistance[1])):
            result = kclusters
            judge = sum(kdistance[0])+sum(kdistance[1])
            resultrecord = arrayrecord
        #print "first:",arrayrecord[0],"\n","second:",arrayrecord[1]


    print result[0],"\n",result[1]
    print resultrecord[0],"\n",resultrecord[1]
    print judge
    return
#main
wordcount = readfile('StoneStoryData.txt')


kmeans(2,wordcount)





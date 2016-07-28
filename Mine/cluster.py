from math import sqrt
#readfile
def readfile(filename):
    wordcount=[]
    data = [line for line in file('StoneStoryData.txt')]
    print(len(data))
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

  # Sums of the squares
  sum1Sq=sum([pow(v,2) for v in v1])
  sum2Sq=sum([pow(v,2) for v in v2])

  # Sum of the products
  pSum=sum([v1[i]*v2[i] for i in range(len(v1))])

  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/len(v1))
  den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
  if den==0: return 0

  return 1.0-num/den


#k-means


#main
wordcount = readfile('StoneStoryData.txt')
min = 1
recordi = 0
recordj = 0
for i in range(1,len(wordcount)):
    if min>pearson(wordcount[0],wordcount[i]):
        recordi=0
        recordj=i
        min = pearson(wordcount[0],wordcount[i])
print recordi,recordj,min,len(wordcount)
distancerecord=[]

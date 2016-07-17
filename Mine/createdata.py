import re
from collections import defaultdict


#apcount={}
#wordcounts={}
#feedlist=[line for line in file('feedlist.txt')]
#for feedurl in feedlist:
#  try:
#    title,wc=getwordcounts(feedurl)
#    wordcounts[title]=wc
#    for word,count in wc.items():
#      apcount.setdefault(word,0)
#      if count>1:
#        apcount[word]+=1
#  except:
#    print 'Failed to parse feed %s' % feedurl


# aList = [123, 'xyz', 'zara', 'abc']
# newli=[]
# newli.append(aList)
# newli[[123, 'xyz', 'zara', 'abc']]
# bList = [1,2,2,3]
# newli.append(bList)
# newli[[123, 'xyz', 'zara', 'abc'], [1, 2, 2, 3]]


def isset(v,s):
   try :
     v[s]
   except :
     return  False
   else :
     return  True

data = [line for line in file('StoneStory.txt')]
#print wordlist[0]
temprecord = {}
wordrecord = []
appearword = {}
i = 0

out=file('StoneStoryData.txt','w')
for wordlist in data:
    try:
        word = wordlist.split(' ')
        for single in word:
            if isset(appearword,single)==False and len(single)>3:
                appearword[single] = len(single)
                out.write('\t%s' % single)
            if isset(temprecord,single):
                temprecord[single] += 1
            else:
                temprecord[single] = 1
        wordrecord.append(temprecord)
        temprecord = {}
    except:
        print 'fail to read file'
wordrecord






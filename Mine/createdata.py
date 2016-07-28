
UPPER = 100
LOWER = 20
#judge the existance of the element in array
def isset(v,s):
   try :
     v[s]
   except :
     return  False
   else :
     return  True

data = [line for line in file('StoneStory.txt')]
temprecord = {}
totoalrecord={}
wordrecord = []
appearword = {}
appearwordrecord = {}
i = 0

out=file('StoneStoryData.txt','w')
for wordlist in data:
    try:
        word = wordlist.split(' ')
        for single in word:
            if isset(appearwordrecord,single)==False and len(single)>3:
                appearwordrecord[single] = len(single)
                appearword[i] = single
                #print appearword[i]
                i+=1
                #out.write('%s\t' % single)
            if isset(temprecord,single) and len(single)>3:
                temprecord[single] += 1
            else:
                temprecord[single] = 1
            if isset(totoalrecord,single) and len(single)>3:
                totoalrecord[single] += 1
            else:
                totoalrecord[single] = 1
        wordrecord.append(temprecord)
        temprecord = {}
    except:
        print 'fail to read file'
#for word1 in appearword:
#    out.write('%s\t' % word1)
#out.write('%d\n' %len(appearword))
wordcount = 0
#out.write(str(len(totoalrecord))+'\n')
for i in range(0, len(appearword)):
    if(totoalrecord[appearword[i]]>LOWER and totoalrecord[appearword[i]]<UPPER):
        out.write('%s\t' % appearword[i])
        wordcount+=1
#out.write(str(wordcount)+'\n')
wordcount = 0
out.write('\n')
for i in range(0,len(wordrecord)):
    for k in range(0,len(appearword)):
        if totoalrecord[appearword[k]]>LOWER and totoalrecord[appearword[k]]<UPPER:
            wordcount+=1
            if isset(wordrecord[i],appearword[k]) :
                out.write('%s\t' %wordrecord[i][appearword[k]])

            else:
                out.write('0\t')

    out.write('\n')
#out.write(str(wordcount)+'\n')






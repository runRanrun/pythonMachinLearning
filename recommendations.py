Prefer = {"tommy":{'War':2.3,'The lord of wings':3.0,'Kongfu':5.0},

       "lily":{'War':2.0,'The lord of wings':3.6,'Kongfu':4.1},

       "jim":{'War':1.9,'The lord of wings':4.0,'Beautiful America':4.7,'the big bang':1.0},

       'jack':{'War':2.8,'The lord of wings':3.5,'Kongfu':5.5}

       }

print(Prefer["tommy"]["War"])

# Euclidean Distace Score

from math import sqrt
def sim_distance(prefs,person1,person2):
       si={}
       for item in prefs[person1]:
              if item in prefs[person2]:
                     si[item]=1


       if len(si)==0:return 0
       sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
       for item in prefs[person1] if item in prefs[person2]])

       return 1/(1+sqrt(sum_of_squares))

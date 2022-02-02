import math
from subprocess import list2cmdline
from typing import List

from numpy import number        


MyList = []

# puts all numbers that are perfect squares in list
for i in range(1, 1000000):
    x = math.sqrt(i)

    if x - int(x) == 0:
        MyList.append(i)



#reversed MyList
List2 = list(reversed(MyList))



index = -1


for i in range(0, len(List2)):
    index +=1
    Indextwo = index + 1

    for i  in range (0, len(List2)):
        
        if Indextwo >= len(MyList):
            break
        answ = List2[index] - List2[Indextwo]
        #for j in range(len(List2)):
        if answ in List2:
            #append answ nd list2[index] and list2[indextwo]
            if math.sqrt(answ) + math.sqrt(List2[index]) +  math.sqrt(List2[Indextwo]) == 1000:
                print(math.sqrt(answ)*math.sqrt(List2[index])*math.sqrt(List2[Indextwo]))
            Indextwo +=1
            if Indextwo >= len(MyList):
                break
        else:
            Indextwo +=1
            if Indextwo >= len(MyList):
                break

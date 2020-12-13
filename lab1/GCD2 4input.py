import math
import time
tic = time.perf_counter()
def prime_factors(n):
    i = 2
    factors = []
    x = abs(n)
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            factors.append(i)
    if x > 1:
        factors.append(x)
    elif x==1:
        factors.append(1)
    else:
        factors.append(None)
    return factors
list1 = prime_factors(-15)
list2 = prime_factors(0)
list3 = prime_factors(20)
list4 = prime_factors(-25)
listTemp =[]
def intersection(list1,list2,list3,list4): 
    if(list1[0]!=None):
        listTemp.append(list1)
    if(list2[0]!=None):
        listTemp.append(list2)
    if(list3[0]!=None):
        listTemp.append(list3)
    if(list4[0]!=None):
        listTemp.append(list4)
    if(len(listTemp)==1):
        listt = listTemp[0]
    if(len(listTemp)==2):
        listTest1 = listTemp[0]
        listTest2 = listTemp[1]
        listt = [value for value in listTest1 if value in listTest2] 
    if(len(listTemp)==3):
        listTest1 = listTemp[0]
        listTest2 = listTemp[1]
        listTest3 = listTemp[2]
        listt = [value for value in listTest1 if value in listTest2]
        listt = [value for value in listt if value in listTest3]
    if(len(listTemp)==4):
        listTest1 = listTemp[0]
        listTest2 = listTemp[1]
        listTest3 = listTemp[2]
        listTest4 = listTemp[3]
        listt = [value for value in listTest1 if value in listTest2]
        listt = [value for value in listt if value in listTest3]
        listt = [value for value in listt if value in listTest4] 
        
    return listt
temp = intersection(list1,list2,list3,list4)
answer = 1
for valuexx in temp:
    answer *= valuexx
print(answer)
toc = time.perf_counter()
print(f"Test in {toc - tic:0.9f} seconds")





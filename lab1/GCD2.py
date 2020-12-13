import time
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
tic = time.perf_counter()
list1 = prime_factors(0)
list2 = prime_factors(-1)
listTemp =[]
def intersection(list1,list2): 
    if(list1[0]!=None):
        listTemp.append(list1)
    if(list2[0]!=None):
        listTemp.append(list2)
        
    if(len(listTemp)==1):
        listt = listTemp[0]
    if(len(listTemp)==2):
        listTest1 = listTemp[0]
        listTest2 = listTemp[1]
        listt = [value for value in listTest1 if value in listTest2]
    return listt
temp = intersection(list1,list2)
answer = 1
for valuexx in temp:
    answer *= valuexx
toc = time.perf_counter()
print(answer)
print(f"Test in {toc - tic:0.9f} seconds")
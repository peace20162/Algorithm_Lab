import time
def FindGCD31(m,n):
    m=abs(m)
    n=abs(n)
    if(m==0):
        return n
    elif(n==0):
        return m
    elif(m>n):
        return FindGCD31(m-n,n)
    elif(m==n):
        return m
    elif(m<n):
        return FindGCD31(m,n-m)
def FindGCD32(m,n,o):
    m=abs(m)
    n=abs(n)
    o=abs(o)
    if(m==0):
        return FindGCD31(n,o)
    elif(n==0):
        return FindGCD31(m,o)
    elif(o==0):
        return FindGCD31(m,n)
    elif(m==n and m==o):
        return m
    else:
        return FindGCD31(FindGCD31(m,n),o)
def FindGCD33(m,n,o,p):
    m=abs(m)
    n=abs(n)
    o=abs(o)
    p=abs(p)
    if(m==0):
        return FindGCD31(FindGCD31(n,o),p)
    elif(n==0):
        return FindGCD31(FindGCD31(m,o),p)
    elif(o==0):
        return FindGCD31(FindGCD31(m,n),p)
    elif(p==0):
        return FindGCD31(FindGCD31(m,n),o)
    elif(m==n and m==o and m==p):
        return m
    else:
        return FindGCD31(FindGCD31(m,n),FindGCD31(o,p))

tic = time.perf_counter()
answer2 = FindGCD31(906443,392685)
toc = time.perf_counter()
print(answer2)
print(f"Test in {toc - tic:0.9f} seconds")
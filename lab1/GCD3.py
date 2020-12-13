import time
def FindGCD3(m,n):
    if(m>n):
        return FindGCD3(m-n,n)
    elif(m==n):
        return m
    elif(m<n):
        return FindGCD3(m,n-m)
   
tic = time.perf_counter()      
answer2 = FindGCD3(14785,19817)
toc = time.perf_counter()
print(answer2)
print(f"Test in {toc - tic:0.9f} seconds")
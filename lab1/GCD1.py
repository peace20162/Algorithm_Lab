# import time
# # tic = time.perf_counter()
def FindGCD1(m,n):
    t = min(m,n)
    while(True):
        if(m%t==0):
            if(n%t==0):
                return t
            else:t=t-1
        else:t=t-1
# def FindGCD1(m,n,o):
#    t = min(m,n,o)
#    while(True):
#        if(m%t==0 ):
#            if(n%t==0):
#                if(o%t==0):
#                    return t
#                else:t=t-1
#            else:t=t-1
#        else:t=t-1
def FindGCD1(m,n,o,p):
   t = min(m,n,o)
   while(True):
       if(m%t==0 ):
           if(n%t==0):
               if(o%t==0):
                   if(p%t==0):
                       return t
                   else:t=t-1
               else:t=t-1
           else:t=t-1
       else:t=t-1
earth = FindGCD1(189,252,1197,292005)
print(earth)
# toc = time.perf_counter()
# print(f"Test in {toc - tic:0.9f} seconds")
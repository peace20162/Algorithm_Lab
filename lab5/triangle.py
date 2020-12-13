import math

     
def dist(p1, p2): 
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])) 

def cost(points, i, j, k): 
    p1 = points[i] 
    p2 = points[j] 
    p3 = points[k] 
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1) 

def mTCDP(points, n): 
    
   MAX= math.inf 
   if n < 3:  # There must be at least 3 points to form a triangle 
      return "it's doesnt have triangle" 
  
   table =[[ 0.0 for x in range(n)] for x in range(n)]# create table n*n
   
   test=0
   for j in range(n): 
        
        i = 0
        while(j < n): 
            if j < i+2: 
                table[i][j] = 0.0 
            else:
                table[i][j] = MAX 
                k = i+1 
                while( k < j ): 
                    
                    val = table[i][k] + table[k][j] + cost(points,i,j,k)
                    val= float("{:.3f}".format(val))
                    print("Table:",test)
                    print("i:",i,"j:",j, "k:",k)
                    print("{:.3f}".format((table[i][k])),"{:.3f}".format((table[k][j])),"{:.3f}".format(cost(points,i,j,k))) 
                    if table[i][j] > val: #MAX แล้วเติมค่า
                        table[i][j] = val #เติมค่า
                        for p in table:
                            print(p)
                        test+=1
                    k+=1    
            i+=1
            j+=1           
               
   return  table[0][n-1]
#    return table
f = open("1.1.txt","r")
n=int(f.readline())
points=[]
i=0
while i<n: 
    msg = f.readline()
    msg = ' '.join(msg.split()) #ลบ \n \t
    temp1 = msg.split(" ")
    points.append([float(temp1[0]),float(temp1[1])])
    i +=1 

print(points)
print(mTCDP(points, n)) 
      
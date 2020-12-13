def grab(arr,count,position,ans):
    for i in range(position,len(arr)):
        if arr[i]=='G':
            
            #mid to mid-k
            pointer=i
            lowCap=i-k
            while pointer>=lowCap and pointer>=0 : 
                if arr[pointer]=='P':
                    nArr=arr.copy()
                    nArr[i]='No'
                    nArr[pointer]='No'
                    countNo=0  
                    grab(nArr,count+1,i,ans)
                    ans.append(nArr)
                            
                pointer-=1
                
            
                
            #mid to mid+k
            pointer=i
            highCap=i+k
            while pointer<=highCap and pointer<=(len(arr)-1):
                if arr[pointer]=='P': 
                    nArr=arr.copy()
                    nArr[i]='No'
                    nArr[pointer]='No'
                    countNo=0  
                    grab(nArr,count+1,i,ans)
                    ans.append(nArr)
                            
                pointer+=1
                          
    counter.append(count)
def Grab(arr,k): 
    i = 0
    p = 0
    g = 0
    max = 0
    Add_G = [] 
    Add_P = [] 
    while i < len(arr): 
        if arr[i] == 'G': 
            Add_G.append(i) 
        elif arr[i] == 'P': 
            Add_P .append(i) 
        i += 1
  
    # track lowest current indices of  
    while p < len(Add_P) and g < len(Add_G): 
          
        # Grab take Passenger
        if (abs( Add_P[p] - Add_G[g] ) <= k): 
            max += 1
            g += 1
            p += 1
              
        # increase Address of P else increase Address of G 
        elif Add_P[p] < Add_G[g]: 
            p += 1
        else: 
            g += 1
  
    return max

# array=['G','P']
# array=['G','P','P','G','P']
# # array=['P','P','G','G','P','G']
# # array=['G','P','G','P','P','G']
# # array=['G','P','G','P','G','P','G','P','G','P','G','P','G','P','G','P','G','P','G','P'] #test case 1
# # array=['G','G','P','P','G','G','G','G','P','P','P','G'] #test case 2
# # array=['G','P','G','G','P','P','G','P','P','G']
file =open("3.1.1.txt","r")
st=file.readline().strip()
array=[ch for ch in st]
k=int(file.readline().strip())
print("Array :",array)
print("k :",k)
counter=[]
ans=[]
grab(array,0,0,ans)
counter.sort(reverse=True) #counter contain number of every round
allSol=0
countNo=0
for j in counter:
    if j == counter[0]:
        allSol+=1
print("All maximum solution:"+str(allSol)) 
# print(ans)
print("--------------------------------------------------------------------------------------------------------------------") 
maxsol=Grab(array,k)  
for k in ans:
    for j in k:
        if j =='No':
            countNo +=1
    if countNo == maxsol*2:
        print(k) 
    countNo=0           

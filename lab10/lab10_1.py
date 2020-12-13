fileReader = open("q3test.txt","r")
listEdge=[]
k = int(fileReader.readline()) #read K first
n=1 #n=vertex number
ans=[]
for line in fileReader:
    line=line.split()
    for i in range(len(line)):        
        if line[i]=="1" and i+1>n:             
            e=[n,i+1]
            listEdge.append(e)
    n=n+1
n=n-1

def edgeCheck(listEd,combination):
    for edge in listEd:
        if edge[0] not in combination:
            if edge[1] not in combination:return False
    return True

def getCombination(n, r):   
    data = [0]*r
    arr = list(range(1,n+1))
    combinationUtil(arr, data, 0, n - 1, 0, r) 
    
def combinationUtil(arr, data, start, end, index, r):                           
    if (index == r):
        check=edgeCheck(listEdge,data)
        if check == True:
            templist=data.copy()
            ans.append(templist)
            #for j in range(r): 
            #    print(data[j], end = " ") 
            #print()
        return
    i = start
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1, end, index + 1, r)
        i += 1


getCombination(n, k)  #n=number of vertex
if not ans: #ans is empty
    print("No")
else:
    print("Yes")
    for i in ans:
        tempstr=""
        for j in i:
            tempstr=tempstr+str(j)+" "
        print(tempstr)
        
fileReader.close    
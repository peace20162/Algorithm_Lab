fileReader = open("3.3.txt","r")
m = int(fileReader.readline())
keep_clause = []
count = 0
tempp = []
for line in fileReader:
    count += 1
    n = len(line.split())
    for i in line.split():
        tempp.append(int(i))
    maximum = max(tempp)
    
    temp=[]
    for i in line.split():
        temp.append(int(i))
    keep_clause.append(temp)
# print(maximum,"================================")
print(2*maximum+3*m)
print(maximum + 2*m)
graph = [[0 for i in range(2*maximum+3*m)] for j in range(2*maximum+3*m)]

#manage TOP
top_tuple={}
runTOP=1
temp=[]
for i in range(maximum):
    temp.append(runTOP)
    temp.append(runTOP*(-1))
    runTOP+=1
for i in range(len(temp)): 
    top_tuple[temp[i]] = graph[i]

# print(top_tuple)
# define TOP
runForRowToColumn=1
runForColumnToRow=1
for key in top_tuple:
    if(key>0):
        top_tuple[key][runForRowToColumn]=1
        runForRowToColumn+=2
    elif(key<0):
        top_tuple[key][runForColumnToRow-1]=1
        runForColumnToRow+=2

#manage DOWN (TRIANGLE)
down_tuple={}
run=1
runDOWN=(n*count)*(-1)
for j in keep_clause:
    for k in j:
        down_tuple[(run,k)] = graph[runDOWN]
        run+=1
        runDOWN += 1
# print(down_tuple)

#define DOWN (TRIANGLE)
runReverse = (n*count)*(-1)    #-6 >>>    (-6 -- -4)   (-3 -- -1)
counter = (n*count)*(-1)
for key in down_tuple:
    # print(key)
    # print(counter)
    if(counter== (n*count)*(-1) or counter == -9 or counter == -6 or counter == n*(-1)):
        # print("1")
        down_tuple[key][runReverse+1] = 1
        down_tuple[key][runReverse+2] = 1
        counter += 1
        runReverse = counter
    elif(counter == -1): # ตรงนี้ดักแค่ -4 -1 เพราะว่ามีแค่สองพจน์ แสดงว่าถ้า >1 ให้เพิ่ม -7 -10 ไปเรื่อยๆ
        # print("2")
        down_tuple[key][runReverse-1] = 1
        down_tuple[key][runReverse-2] = 1
        counter += 1
        runReverse = counter
    elif(counter == -4): # ตรงนี้ดักแค่ -4 -1 เพราะว่ามีแค่สองพจน์ แสดงว่าถ้า >1 ให้เพิ่ม -7 -10 ไปเรื่อยๆ
        # print("2")
        down_tuple[key][runReverse-1] = 1
        down_tuple[key][runReverse-2] = 1
        counter += 1
        runReverse = counter
    elif(counter == -7): # ตรงนี้ดักแค่ -4 -1 เพราะว่ามีแค่สองพจน์ แสดงว่าถ้า >1 ให้เพิ่ม -7 -10 ไปเรื่อยๆ
        # print("3")
        down_tuple[key][runReverse-1] = 1
        down_tuple[key][runReverse-2] = 1
        counter += 1
        runReverse = counter
    elif(counter == -10): # ตรงนี้ดักแค่ -4 -1 เพราะว่ามีแค่สองพจน์ แสดงว่าถ้า >1 ให้เพิ่ม -7 -10 ไปเรื่อยๆ
        # print("3")
        down_tuple[key][runReverse-1] = 1
        down_tuple[key][runReverse-2] = 1
        counter += 1
        runReverse = counter
    else:
        down_tuple[key][runReverse-1] = 1
        down_tuple[key][runReverse+1] = 1
        counter += 1
        runReverse = counter

#manage connect
countt = 1
# print(keep_clause)
# print(top_tuple)

for i in keep_clause:
    for j in i:
        # print(j)
        # print(j)
        search_key = (countt,j)
        temp = list(down_tuple.items())  
        res = [idx for idx, key in enumerate(temp) if key[0] == search_key] 
        countt+=1
        # print(res[0]-(n*count),"=====")
        top_tuple[j][res[0]-(n*count)] = 1
# for i in graph:
#     str_temp =""
#     for j in i:
#         str_temp = str_temp + str(j) + " "
#     print(str_temp)




run = 0
for i in keep_clause:
    for j in i:
        search_key = j
        temp = list(top_tuple.items())  
        res = [idx for idx, key in enumerate(temp) if key[0] == search_key] 
        # print(j)
        # print(res)
        run += 1
        # print((run,j))
        down_tuple[(run,j)][res[0]] = 1

for i in graph:
    str_temp =""
    for j in i:
        str_temp = str_temp + str(j) + " "
    print(str_temp)
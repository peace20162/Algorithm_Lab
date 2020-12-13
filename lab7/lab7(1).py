# recursive function to obtain the path as a string

def obtainPath(i, j):
    if dist[i][j] == float("inf"):
        return " no path  "
    if parent[i][j] == i :
        return " "
    else :
        # print(i,"to",j,"   parent=",parent[i][j])
        return obtainPath(i, parent[i][j]) + str(parent[i][j]+1) + obtainPath(parent[i][j], j)


fileReader = open("7.2.txt","r")
#fileReader = open("testlab7.txt","r")
init = fileReader.readline().split()

# no of vertices
V=int(init[0])
print("vertices=",V)
# array of shortest path distances 
dist = []

# array of shortest paths
parent = []

# no of edges
E = int(init[1])
print("edges=",E)

# question number
questionCounter=int(init[2])
print("questionCounter=",questionCounter)

# initialize to infinity
for i in range (0, V):
    dist.append([])
    parent.append([])
    for j in range (0, V):
        dist[i].append(float("inf"))
        parent[i].append(0)




# read edges from input file and store
for i in range (0,E):
    line = fileReader.readline().split()
    x = int(line[0]) - 1
    y = int(line[1]) - 1
    decibel = int(line[2])
    dist[x][y] = decibel
    dist[y][x] = decibel
    parent[x][y] = x


# path from vertex to itself is set to 0
for i in range (0,V):
    dist[i][i] = 0



# initialize the path matrix
for i in range (0,V):
    for j in range (0,V):
        if dist[i][j] == float("inf"):
            parent[i][j] = -1
        elif i==j:
            parent[i][j]=-1     
        else:
            parent[i][j] = i
# for i in range(0,V):
#     print(dist[i])
# print("--------------------------")
        



# actual floyd warshall algorithm
for k in range(0,V):
    for i in range(0,V):
        for j in range(0,V):
            mini=max(dist[i][k],dist[k][j])
            if dist[i][j] > mini:
                dist[i][j] = mini
                parent[i][j] = parent[k][j]
for i in range(0,V):
    print(dist[i])
print("--------------------------") 
for i in range(0,V):
    print(parent[i])               
                
                
# check for negative cycles
#for i in range (0,V):
#    if dist[i][i] != 0:
#       print("Negative cycle at : ", i+1)
#        sys.exit() 


# display final paths
print("All Pairs Shortest Paths : \n")

# display shortest paths 
for y in range (0,questionCounter):
    line = fileReader.readline().split()
    i=int(line[0])
    j=int(line[1])
    
    print("From :", i, " To :", j)
    print("Path :", str(i) + obtainPath(i-1,j-1) + str(j))
    print("Mininum Decibel :", dist[i-1][j-1])


fileReader.close()

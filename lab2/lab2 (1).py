# Python program to print all paths from a source to destination.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def printAllPathsUtil(self, u, v, visited, path):
        visited[u] = True
        lst = []
        path.append(u)
        if u == v:
            for ans in path:
                lst.append(ans+1)
            print(lst)          
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, v, visited, path)
        path.pop()        
        visited[u] = False

    def printAllPaths(self, u, v):
        visited = [False] * (self.V)
        path = []
        self.printAllPathsUtil(u, v, visited, path)

            

##############################################################################
#Hamil Version :)
    def printAllHamilPathsUtil(self, u, v, visited, path, N):
        visited[u] = True
        lst = []
        path.append(u)
        if u == v and len(path)==N:
            for ans in path:
                lst.append(ans+1)
            print(lst)
         
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllHamilPathsUtil(i, v, visited, path, N)
            
        path.pop()        
        visited[u] = False

    def printAllHamilPaths(self, u, v, N):
        visited = [False] * (self.V)
        path = []
        self.printAllHamilPathsUtil(u, v, visited, path, N)
        
   
    def printHamil(self,N):
        for i in range(N):
            for j in range(N):        
                g.printAllHamilPaths(i,j,N)
           
  

fileReader = open("2.2.6.txt","r")
test  = []
for line in fileReader:
    line=line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    test.append(line)
print("Test case=",test)
g = Graph(len(test))
for row in range(len(test)):
        for column in range(len(test)):
            
            if  column <= row and test[row].__getitem__(column) >= 1:
                g.addEdge(row,column)
                # print('(',row,',',column,')')
            if  column >= row and test[row].__getitem__(column) >= 1:
                g.addEdge(row, column)
                # print('(',row,',',column,')')
            
u = 0
v = 1


print("Following are all different paths from % d to % d :" % (u, v))
g.printAllPaths(u, v)
print("*********************************************Hamiltonain**********************************************************************")
if(g.printHamil(len(test))== None):
    print("it doesnt have hamiltonian path")
else:
    g.printHamil(len(test))

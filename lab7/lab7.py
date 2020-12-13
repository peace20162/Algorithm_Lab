def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
def min_decibel(filename):
    with open(filename,"r") as p:
            while (True):
                num_vertex,num_edge,num_pair=tuple(map(int,p.readline().split()))
                graph={}
                deci_list={}
                for i in range(1,num_vertex+1):
                    graph[i]=[]
                    deci_list[i]=[]
                for i in range(num_edge):
                    from_,to_,decibel=tuple(map(int,p.readline().split()))
                    graph[from_].append(to_)
                    # graph[to_].append(from_)
                    deci_list[from_].append((to_,decibel))
                    # deci_list[to_].append((from_,decibel))
                # return graph
                array=[]
                for i in range(num_pair):
                    travel_from,travel_to=tuple(map(int,p.readline().split()))
                    path=[]
                    if find_all_paths(graph,travel_from,travel_to,path)==[]:
                         array.append("no path")
                    else:
                        array.append(find_all_paths(graph,travel_from,travel_to,path))
                print("All paths : \n",array)
                max_deci=[]        
                for i in array:
                    temp=[]
                    if i == "no path":
                       max_deci.append(0)
                    else:    
                        for j in i:
                            MAX=0
                            for k in range(len(j)-1):
                                for a in deci_list[j[k]]:
                                    if a[0] == j[k+1]:
                                        if MAX <= a[1]:
                                            MAX=a[1]
                            temp.append(MAX)
                        max_deci.append(temp)
                print("Decibel in path : \n ",max_deci)  
                min_deci=[]       
                for i in max_deci:
                    MIN=9999 
                    if i == 0:
                         min_deci.append(0)
                    else:
                        for j in i:
                            if  j < MIN :
                                MIN=j
                        min_deci.append(MIN)   
                print("Minimum decibel to endure : \n")        
                return min_deci

file_n="7_extra1.txt"
print(min_decibel(file_n))
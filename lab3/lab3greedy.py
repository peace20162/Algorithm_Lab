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
# array=['P','P','G','G','P','G']
# array=['G','P','G','P','P','G']
# array=['G','P','G','P','G','P','G','P','G','P','G','P','G','P','G','P','G','P','G','P'] #test case 1
# array=['G','G','P','P','G','G','G','G','P','P','P','G'] #test case 2
file =open("3.4.2.txt","r")
st=file.readline().strip()
array=[ch for ch in st]
k=int(file.readline().strip())
print("Array :",array)
print("k :",k)
print("Maximum :"+ str(Grab(array,k)))    

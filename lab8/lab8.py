ans =[]
def mergeSort(arr):
    
    L = [arr[i] for i in range(len(arr)) if i%2==0] # Dividing the array elements (even)
    R = [arr[i] for i in range(len(arr)) if i%2==1] # into 2 halves (odd)
    if len(arr) == 1:
        merge(arr)
        return    
    # print(L, R) 
    mergeSort(L) # Sorting the first half 
    mergeSort(R) # Sorting the second half 
    
  
def merge(arr): 
    # print(arr)
    ans.append(arr[0])
    return 
    
input=5
# arr=[i for i in range(input+1)]
arr=list(range(1,input+1))
print ("Answer array is", end ="\n")  
mergeSort(arr)
print(ans)


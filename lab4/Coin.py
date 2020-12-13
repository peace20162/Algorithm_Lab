fileReader = open("4.1.txt","r")
amount=int(fileReader.readline())
for line in fileReader:
    line=line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
coin=line
def coinChange(coins, sumOfChange):
      
    def coinChangeHelper(cur_i, total):
    
        if (cur_i, total) in mem_cache:
            # Use cache value
            return mem_cache[(cur_i, total)]
        
        # Stop condition.
        if total == 0:
            mem_cache[(cur_i, total)] = [[]]
        else:
            # Recursive step
            solutions = []

            for i in range(cur_i, len(coins)):
                if coins[i] <= total:
                    lst = coinChangeHelper(i, total - coins[i])
                    solutions.extend([[coins[i]] + l for l in lst])

            mem_cache[(cur_i, total)] = solutions
            print(mem_cache)
            
        
        return mem_cache[(cur_i, total)]

    # Init cache
    mem_cache = {}
    
    return coinChangeHelper(0, sumOfChange)
def count(S, m, n): 
   
    table = [[0 for x in range(m)] for x in range(n+1)] 
  
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
  
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 
  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y 
  
    return table[n][m-1] 

a = list(coinChange(coin,amount))
print("coin: ",coin)
print("amount: ",amount)
countt=count(coin,len(coin),amount)
print("Number of  coin change's way is ",countt)  
print(a)
print('-----------------------------------------------------------------')  
keepSizeOfSol = 0
for i in a[-1]:
    keepSizeOfSol+=1
print('Minimum coins is ',keepSizeOfSol,'\nSolution of minimum coins :')
for j in a:
  if(len(j) == keepSizeOfSol):
    print(j)
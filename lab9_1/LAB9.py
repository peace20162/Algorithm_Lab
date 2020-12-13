name_file = "9.4.txt"

f1 = open(name_file,"r")
line_count = 0
for line in f1:
    if line != "\n":
        line_count += 1
print("Line count :", line_count)

count = 0
f2 = open(name_file,"r")
up_bottom_list = []
bottom_up_list = []
left_right_list = []
right_left_list = []


patternIs =""
countN = 0
for line in f2:
    x=line.split()
    if(count == 0):
        setOfAlphabet = x
        print("Set of alphabet :",setOfAlphabet)
    elif(count == 1):
        N=int(x[0])
        M=int(x[1])
        numOfPattern = int(x[2])
        print("N :",N,"\nM :",M,"\nNumber of pattern :",numOfPattern)

        up_bottom_list = [""] * M
        bottom_up_list = [""] * M #build array of str = column size
        left_right_list = [""] * N
        right_left_list = [""] * N #build array of str = row size
    elif(count == line_count-1):
        for i in x:
            patternIs = patternIs+i
        print("Pattern to find :", patternIs)
    else:
        
        for i in range(M):
            up_bottom_list[i] = up_bottom_list[i] + x[i]
            # print(up_bottom_list)
            bottom_up_list[i] = x[i] + bottom_up_list[i]
        while(countN<N):  
            for i in x:
                left_right_list[countN] = left_right_list[countN] + i
                right_left_list[countN] = i + right_left_list[countN]
            if(len(left_right_list[countN])==M and len(right_left_list[countN])==M):
                countN = countN + 1
                break
    # #W UB BU
    #     w_up_bottom_list = list.copy(up_bottom_list)
    #     w_bottom_up_list = list.copy(bottom_up_list)
    #     countWUpBottom=0
    #     countWBottomUp=0
    #     count_1 = 0
    #     count_2 = 0
    #     for eachItem in w_up_bottom_list:
    #         w_up_bottom_list[countWUpBottom] = eachItem+eachItem
    #         count_1 += 1 
    #         if count_1 < len(patternIs)-1:
    #             break
    #         countWUpBottom += 1
    #     for eachItem in w_bottom_up_list:
    #         w_bottom_up_list[countWBottomUp] = eachItem+eachItem
    #         count_2 += 1
    #         if count_2 < len(patternIs)-1:
    #             break
    #         countWBottomUp += 1
    
    
    
    # #W LR RL
    #     w_left_right_list = list.copy(left_right_list)
    #     w_right_left_list = list.copy(right_left_list)
    #     countWRightLeft=0
    #     countWRightLeft=0
    #     for eachItem in w_left_right_list:
    #         w_left_right_list[countWRightLeft] = eachItem+eachItem

    #         countWRightLeft += 1
    #     for eachItem in w_right_left_list:
    #         w_right_left_list[countWRightLeft] = eachItem+eachItem

    #         countWRightLeft += 1
        
        
           
    count = count+1

# print("List of UP to BOTTOM\t>>",up_bottom_list)
# print("List of BOTTOM to UP\t>>",bottom_up_list)
# print("List of LEFT to RIGHT\t>>",left_right_list)
# print("List of RIGHT to LEFT\t>>",right_left_list)
#print("List of UP to BOTTOM (W)\t>>",up_bottom_list)
#print("List of BOTTOM to UP (W)\t>>",bottom_up_list)
#print("List of LEFT to RIGHT (W)\t>>",left_right_list)
#print("List of RIGHT to LEFT (W)\t>>",right_left_list)
#count=0

row =0
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 

    # create lps[] that will hold the longest prefix suffix 
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 

    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 

    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
        if j == M :
            # print ("Found pattern at index " + str(i-j))
            keep = i-j+1
            j = lps[j-1]
            return keep
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1

def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 

    lps[0] # lps[0] is always 0 
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar 
            # to search step. 
            if len != 0: 
                len = lps[len-1] 

                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1
############################################################################
p=patternIs
l1 = len(p)

j = 0
i = 1
prefix = [0]

while len(prefix) < l1:
    if p[j] == p[i]:
        prefix.append(j+1)
        i += 1
        j += 1
    else:
        if j == 0:
            prefix.append(0)
            i += 1
        if j != 0:
            j = prefix[j-1]
print(prefix)
############################################################################


w_up_bottom_list = []
w_bottom_up_list = []
w_left_right_list = []
w_right_left_list = []




def findLeftRight(l):
    temp=l.copy()
    for i in range(len(l)):
        column = KMPSearch(patternIs, l[i])
        if column!=None:
            s1 = list(l[i])
            print(i+1,column,"LR")
            start = column-1
            s1[start] = "ก"
            l[i] = "".join(s1)

    w_left_right_list=[]
    countWLeftRight=0
    
    for i in range(len(l)): 
        earth = temp[i]
        w_left_right_list.append(l[i] + earth[0:len(patternIs)-1])
    # print(w_left_right_list)
    for i in range(len(w_left_right_list)):
        column = KMPSearch(patternIs, w_left_right_list[i])
        if column!=None and column+len(patternIs)-1>len(l):
            print(i+1,column%(len(left_right_list)+1),"LR (W)")
        if column!=None and column+len(patternIs)-1<=len(l): 
            print(i+1,column,"LR")
            
########################################################################
def findRightLeft(l):
    temp=l.copy()
    for i in range(len(l)):
        column = KMPSearch(patternIs, l[i])
        if column!=None:
            s1 = list(l[i])
            print(i+1,M-column+1,"RL")
            start = column-1
            s1[start] = " "
            l[i] = "".join(s1)

    w_right_left_list=[]
    countWRightLeft=0
    for i in range(len(l)):
        earth = temp[i] 
        w_right_left_list.append(l[i] + earth[0:len(patternIs)-1])

    for i in range(len(right_left_list)):
        column = KMPSearch(patternIs, w_right_left_list[i])
        if column!=None:
            print(i+1,(M-column+1)%(len(right_left_list)+1),"RL (W)")    
# ######################################################################

def findUpBottom(l):
    temp=l.copy()
    for i in range(len(up_bottom_list)):
        column = KMPSearch(patternIs, up_bottom_list[i])
        if column!=None:
            s1 = list(l[i])
            print(column,i+1,"UB")
            start = column-1
            s1[start] = " "
            l[i] = "".join(s1)

    w_up_bottom_list=[]
    countWUpBottom=0
    for i in range(len(l)): 
        earth = temp[i] 
        w_up_bottom_list.append(l[i] + earth[0:len(patternIs)-1])

    for i in range(len(up_bottom_list)):
        column = KMPSearch(patternIs, w_up_bottom_list[i])
        if column!=None:
            print(column,i+1,"UB (W)")

# ######################################################################
def findBottomUp(l):
    temp=l.copy()
    for i in range(len(bottom_up_list)):
        column = KMPSearch(patternIs, bottom_up_list[i])
        if column != None:
            s1 = list(l[i])
            print(N-column+1,i+1,"BU")
            start = column-1
            s1[start] = " "
            l[i] = "".join(s1)

    w_bottom_up_list=[]
    countWBottomUp=0
    for i in range(len(l)): 
        earth = temp[i] 
        w_bottom_up_list.append(l[i] + earth[0:len(patternIs)-1])
    # print(w_bottom_up_list)
    for i in range(len(bottom_up_list)):
        column = KMPSearch(patternIs, w_bottom_up_list[i])
        if column!=None:
            print(N-column+1,i+1,"BU (W)")

# ############################################################################
findLeftRight(left_right_list)
findRightLeft(right_left_list)
findUpBottom(up_bottom_list)
findBottomUp(bottom_up_list)
S = map(int,input().split())
S = list(S)
ascending_S = [1,2,3,4,5,6,7,8]
descending_S = [8,7,6,5,4,3,2,1]
flag = 0

for i in range(8):
    if S[0] == 1 and S[i] == ascending_S[i]:
        flag = 1
    elif S[0] == 8 and S[i] == descending_S[i]:
        flag = 2   
    else:
        flag = 3
        break
        
    
    

if flag == 1:
    print('ascending')
elif flag == 2:
    print('descending')    
elif flag == 3:
    print('mixed')
        
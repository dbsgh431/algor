import sys
from collections import deque
def VPS(deque, tmp_deque):
    tmp_deque.clear()
    for i in deque:
        if i == '(':
            tmp_deque.append(str(i))
        else:
            if len(tmp_deque) >= 1:
                tmp_deque.pop()
            else:
                result = 'NO'
                return result     
    if len(tmp_deque) >= 1:
        result = 'NO'
    else:
        result = 'YES'    
    return result
tmp_deque = deque()
N = int(sys.stdin.readline())
for i in range(N):
    S = list(sys.stdin.readline().rstrip())
    D = deque()
    for j in S:
        D.append(j)
    result = VPS(D,tmp_deque)
    print(result)       

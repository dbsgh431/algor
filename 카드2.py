import sys
from collections import deque

def stack_up(array):
    while len(array) > 1:
        array.popleft()         
        array.append(array.popleft())
    return int(array[0]) 

N = int(sys.stdin.readline())
deque_n = deque()
for i in range(1,N+1):
    deque_n.append(i)
result = stack_up(deque_n)        
print(result)
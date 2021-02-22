import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
stack = deque()
for i in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push_front':
        stack.appendleft(order[1])
    elif order[0] == 'push_back':
       stack.append(order[1])      
    elif order[0] == 'pop_front':
        if len(stack) >= 1:
            print(stack.popleft())
        else:
            print('-1')
    elif order[0] == 'pop_back':
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(stack))                
    elif order[0] == 'empty':
        if len(stack) < 1:
            print('1')
        else:
            print('0')
    elif order[0] == 'front':
        if len(stack) >= 1 :
            print(stack[0])
        else:
            print('-1')  
    elif order[0] == 'back':
        if len(stack) >= 1 :
            print(stack[len(stack)-1])
        else:
            print('-1')            

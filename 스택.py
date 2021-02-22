import sys
# import time
from collections import deque
# st = time.time()
N = int(sys.stdin.readline().rstrip())
stack = deque()
for i in range(N):
    order = list(sys.stdin.readline().split())
    if len(order) > 1:
        stack.append(int(order[1]))
    else:
        if order[0] == 'top':
            if len(stack) >= 1:
                print(stack[len(stack)-1])
            else:
                print('-1')
        elif order[0] == 'size':
            print(len(stack))
        elif order[0] == 'empty':
            if len(stack) < 1:
                print('1')
            else:
                print('0')
        elif order[0] == 'pop':
            if len(stack) >= 1 :
                print(stack.pop())
            else:
                print('-1')   
# end = time.time()
# print(end-st)
import sys

N = int(sys.stdin.readline().rstrip())
stack = set()
for i in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'add':
        stack.add(order[1])
    elif order[0] == 'remove':
        stack.discard(order[1])
    elif order[0] == 'check':
        if order[1] in stack:
            print('1')
        else:
            print('0')   
    elif order[0] == 'toggle':
        if order[1] in stack:
            stack.discard(order[1])
        else:
            stack.add(order[1])
    elif order[0] == 'all':
        stack = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif order[0] == 'empty':
        stack = set()             
import sys
N = int(sys.stdin.readline())
list_n = [[0 for j in range(2)] for i in range(N)]
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    list_n[i][0] = x
    list_n[i][1] = y 

list_n.sort(key = lambda  x :(x[0], x[1]))

for i in range(N):
    print(list_n[i][0], list_n[i][1])
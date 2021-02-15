import sys
N = int(sys.stdin.readline())
N_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    N_list.append(num)
N_list.sort()

for i in range(N):
    print(N_list[i])

import sys
N = int(sys.stdin.readline())
num = list(sys.stdin.readline().split())

for i in num:
    if int(i) >= 2:
        for j in range(2, int(i)):
            if int(i) % j == 0:
                N -= 1
                break
    else:
        N -= 1
print(N)                   

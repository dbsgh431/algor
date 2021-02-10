import sys
N = sys.stdin.readline()
result = 0
flag = 0
for x in range(int(N)+1):
    result = x
    x = str(x)
    for i in list(x):
        result += int(i)
    if int(N) == result:
        print(x)
        flag = 1
        break
if flag == 0:
    print('0')

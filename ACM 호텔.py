import math
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    ho = N / H
    ho = math.ceil(ho)
    floor = N % H
    if floor == 0:
        floor = H
    ho = str(ho).zfill(2)
    result = str(floor) + ho
    print(result)

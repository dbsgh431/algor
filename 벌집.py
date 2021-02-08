import math
N = int(input())
a = 1

if N == 1:
    print('1')
else:
    Y = math.ceil((N - 1) / 6)

    while N <=1000000000:
        if a*(a-1)/2 < Y <= a*(a+1)/2:
            print(a+1)
            break
        else:
            a += 1        

     

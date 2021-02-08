from sys import stdin

import math
a,b,c = map(int,stdin.readline().split())
if c>b:
    income = c-b
    n = a/income
    print(math.floor(n)+1)
else:
    print('-1')    


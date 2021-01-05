n, won = (input().split())
n = int(n)
won = int(won)
coin = []
extra = 0
sum = 0
for i in range(n):
    k = int(input())
    coin.append(k)

for i in range(n-1,-1,-1):
    if won // coin[i] > 0:
        sum += won// coin[i]
        extra = won % coin[i]
        won = extra


print(sum)

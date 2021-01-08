won = int(input())
won = 1000 - won
extra = 0
sum = 0
exchange = [500, 100, 50 ,10 ,5, 1]

if 1 <= won < 1000:
    for i in exchange:
            extra = won % i
            sum += won // i
            won = extra


print(sum)

N = int(input())
cnt = 0
res = 0

while N >= 1:
    if N > 99:
        d_list = list(str(N))
        res = int(d_list[0]) - int(d_list[1])
        if int(d_list[1]) - int(d_list[2]) == res:
            cnt += 1
    else:
        cnt += 1
    N -= 1

print(cnt)    



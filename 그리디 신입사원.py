case = int(input())
cnt = [0 for i in range(case)]


for j in range(case):
    man = int(input())
    pass_ts =[[0 for col in range(2)] for row in range(man)]
    test = [[0 for col in range(2)] for row in range(man)]
    for i in range(0,man):
        test[i][0], test[i][1] = list(map(int, input().split()))
    test.sort(key=lambda x:x[0])
    for i in range(1, man):
        if test[0][1] != man:
            pass_ts[0][1] = test[0][1]
            cnt[j] +=1
        elif test[i][1] < pass_ts[0][1]:
            pass_ts[i][1] = test[i][1]
            cnt[j] +=1
    


for i in range(case):
    print("{0}".format(cnt[i]))
        


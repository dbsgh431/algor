import sys
case = int(input()) # 시험의 수
res = [1 for i in range(case)]
std = 0

if 1 <= case <= 20:
    for k in range(case):
        man = int(input()) # 지원자 수

        if 1 <= man <= 100000:
            n = man
            test = [[0 for col in range(2)] for row in range(man)]
            for i in range(0,man):
                test[i][0], test[i][1] = list(map(int, sys.stdin.readline().split()))

            test.sort(key=lambda x : x[0]) # 1차 시험으로 정렬

            std = test[0][1]    #1차 시험의 1등은 1,2차 시험 모두에서 본인 보다 높은점수를 얻은 경우가 없기 때문에 최초의 기준이 됨

            for i in range(1,man): # 1차 시험으로 정렬 하였으므로 i가 증가함에 따라 2차 시험등수가 더 높은 사람들만 합격하게 됨
                if test[i][1] < std: 
                    res[k] += 1
                    std = test[i][1] 
                    
    for i in range(case):
        print("{0}".format(res[i]))
            


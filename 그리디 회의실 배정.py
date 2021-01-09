n = int(input())
meeting = [[0 for col in range(3)] for row in range(n)]
start_time = [0 for i in range(n)]
end_time = [0 for j in range(n)]
total_time = [-1 for k in range(2**23-1)]
cnt = 0


if 1 <= n <= 100000:
    for i in range(0,n):
        start_time[i], end_time[i] = list(map(int, input().split()))
        meeting[i][0] = start_time[i]
        meeting[i][1] = end_time[i]
        meeting[i][2] = end_time[i] - start_time[i]



    meeting.sort(key = lambda x:x[2])  


    for i in range(0,n):
        s = meeting[i][0]
        e = meeting[i][1]
        if s != e:
            if (total_time[s] == -1 or total_time[s] == 2) and (total_time[e] == -1 or total_time[e] == 1) and total_time[e-s] != 0:
                while s != e-1:
                    s +=1
                    if total_time[s] == 0:
                        break 
                    else:   
                        total_time[s] = 1
                        total_time[e] = 2
                if s != e:
                    while s != e-1:    
                        s += 1
                        if total_time[s] == -1:
                            total_time[s] = 0       
                    cnt += 1
        else :
            cnt +=1        

    print(cnt)        
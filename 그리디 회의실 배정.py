n = int(input())
meeting = [[0 for col in range(2)] for row in range(n)]
cnt = 1
tmp = 0


if 1 <= n <= 100000:
    for i in range(0,n):
        meeting[i][0], meeting[i][1] = list(map(int, input().split()))
meeting.sort(key=lambda x: (x[1], x[0]))
tmp = meeting[0][1]

for i in range(1,n):
    if meeting[i][0] == meeting[i][1]:
        cnt +=1
    elif meeting[i][0] >= tmp:
        tmp = meeting[i][1]
        cnt += 1
    else:
        next

print(cnt)

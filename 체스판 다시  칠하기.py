N, M = map(int, input().split())
board = []
cnt = 0
cnt_list = []
s = 0
v = 1
for i in range(N):    
    S = input()
    board.append(S)

while N-s > 8 and M-v > 8:
    for i in range(s,s+7):
        for j in range(v, v+7):
            if board[i][j] == board[i][j-1]:
               cnt += 1
        v += 1
    s += 1     
    cnt_list.append(cnt)
    cnt = 0           

print(cnt_list)

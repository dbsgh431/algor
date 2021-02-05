N = int(input())
cnt = N

for k in range(N): 
    lst = []
    S = input()
    for i in S:
        index = S.find(i) # 입력받은 문자열을 인덱스로 변환
        lst.append(index)
        orm = sorted(lst) 
    for j in range(len(lst)): 
        if orm[j] != lst[j]: # 그룹 단어 이면 인덱스가 오름차순을 만족하므로
            cnt -= 1 # 그룹단어가 아니면 -1
            break
        

print(cnt)        



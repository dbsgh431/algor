S = input().split('-') #-를 기준으로 분리
num = []


for i in S:
    sum = 0
    sp = i.split('+') # 모든 경우에서 분리된 문자열 중 '+'를 우선 계산해야 함
    if len(sp) >= 2: # +로 문자열의 분리 된다면 누적합
        for i in sp:
            sum += int(i)
        num.append(sum)    
    else:
        num.append(int(sp[0]))

tmp = num[0]

for i in range(1,len(num)):
    tmp -= num[i] 

print(tmp)    


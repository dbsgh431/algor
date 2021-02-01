import operator

N = int(input())
sum = 0
result = {}
cnt = [9,8,7,6,5,4,3,2,1,0]

for i in range(N):
    S = input()
    S = list(str(S)) #입력값 분리
    S.reverse() # 1의 자리부터 대입하기 위해
    j = 1
    for i in S:
        result.setdefault(i,0) # 분리된 문자들을 키로 설정
        result[i] = int(result.get(i)) + 10**(j-1) # 각 문자에 자릿수 부여
        j += 1    
    s_result = sorted(result.items(), reverse = True, key = operator.itemgetter(1)) # 자릿수가 높은 순으로 정렬


for j in range(len(s_result)):
    sum += s_result[j][1]*cnt[j] # 부여된 자릿수에 9부터 숫자대입 
print(sum)



  
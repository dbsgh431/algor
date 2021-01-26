def self_num(N):
    res = 0
    d_list = list(str(N)) # N을 자릿수 별로 분리
    for i in range(len(d_list)):
        res += int(d_list[i]) # 분리한 N을 더하기
    return int(N) + res   


Ns = 1
list_dn  = list(range(1,10001))
return_self = 0
while Ns <= 10000:
    return_self = self_num(Ns)
    if return_self in list_dn: #10000까지 의 수 중 생성자가 있는 숫자 중복 없이 제거
        list_dn.remove(return_self)
    Ns += 1



for i in list_dn:
    print(i)
   




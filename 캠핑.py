i = 0 # 케이스의 갯수
while True:
    L, P, V = map(int, input().split())
    i += 1
    if L == P == V == 0:
        break
    else:
        Mod_Vac = V // P # 휴일을 이용가능한 날짜로 나눈 몫
        extra_modvac = V % P # 나머지
        if L >= extra_modvac: # 나머지가 이용가능한 날짜보다 크면 나머지만큼만 이용가능함
            exday = extra_modvac
        else:
            exday = L    
        max_day = Mod_Vac*L + exday 
    print("Case {0}: {1}".format(i, max_day))    
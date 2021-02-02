i = 0
while True:
    L, P, V = map(int, input().split())
    i += 1
    if L == P == V == 0:
        break
    else:
        Mod_Vac = V // P
        extra_modvac = V % P
        if L >= extra_modvac:
            exday = extra_modvac
        else:
            exday = L    
        max_day = Mod_Vac*L + exday
    print("Case {0}: {1}".format(i, max_day))    
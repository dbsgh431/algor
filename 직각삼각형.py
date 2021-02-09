while True:
    try:
        a, b, c = map(int, input().split())
        if a == b == c== 0:
            break
        else:
            if max(a,b,c) == a:
                tmp = c
                c = a
                a = tmp
            elif max(a,b,c) == b:
                tmp = c
                c = b
                b = tmp        
            if (a**2)+(b**2) == c**2:
                print('right')
            else:
                print('wrong')
    except:
        break                     
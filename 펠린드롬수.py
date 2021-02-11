import sys

while True:
    flag = 0
    T  = input()
    if T == '0':
        sys.exit(0)
    else:
        T = list(T)
        T_reverse = list(reversed(T))
        for i in range(len(T)):
            if T[i] != T_reverse[i]:
                flag = 1
                print('no')
                break
        if flag == 0:
            print('yes')
                
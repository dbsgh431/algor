S = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z='] #분리할 기준
lst = []

for i in cro:
    if len(S.split(i)) >= 2: # 기준 단어로 분리 가능한 경우
        lst.append(i) # 새로운 리스트에 추가


for i in lst:
    S = S.replace(i,"0") # 입력값에서 크로아티아 알파벳이 되는 경우 '0'으로 치환

print(len(S))



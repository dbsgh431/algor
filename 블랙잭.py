from itertools import combinations
N, M = map(int, input().split())
card_list = []
card = list(input().split())
card_com = list(combinations(card, 3))
flag = 0
for i in card_com:
    j = list(i)
    sum = 0
    for k in j:
        sum += int(k)
    card_list.append(sum)

card_list.sort()
for i in range(len(card_list)):
    if card_list[i]-M > 0:
        print(card_list[i-1])
        flag = 1
        break
    
if flag == 0:
    card_list.sort(reverse = True)
    print(card_list[0])
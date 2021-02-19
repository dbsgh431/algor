import sys

def compare(array,start,end,target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None  

N = int(sys.stdin.readline().rstrip())
card = list(map(int, input().split()))
card.sort()
M = int(sys.stdin.readline().rstrip())
card_have = list(map(int, input().split()))
D = dict.fromkeys(card,0)

for i in card:
    D[i] += 1

for i in card_have:
    result = compare(card,0,N-1,i)
    if result != None:
        print(D[result], end=' ')
    else:
        print('0', end=' ')
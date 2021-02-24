import sys

dogam = {}
num_dogam = []
findlist = []
N, M = map(int, input().split())
num = 1
for i in range(N):
    poketmon = sys.stdin.readline().strip()
    num_dogam.append(poketmon)
    dogam[poketmon] = num
    if num < N:
        num +=1

for i in range(M):
    find = sys.stdin.readline().strip()
    findlist.append(find)    

for i in findlist:
    if i.isalpha() == True:
        print(dogam.get(i))
    else:
        print(num_dogam[int(i)-1])
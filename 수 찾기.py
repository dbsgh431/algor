import sys

def binary_search(N_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] == target:
            return mid
        elif N_list[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None    

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(sys.stdin.readline().rstrip())
find_list = list(map(int, input().split()))

for i in find_list:
    result = binary_search(N_list,i,0,N-1)
    if result != None:
        print('1')
    else:
        print('0')    

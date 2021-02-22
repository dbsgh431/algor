def josep(array, K):
    pibot = 0
    result = []
    while len(array) >= 2:
        rear = len(array)-1
        if pibot > rear:
            pibot = 0
        for i in range(K-1):
            if pibot == rear:
                pibot = 0
            else:
                pibot +=1
        result.append(array[pibot])
        del array[pibot] 
    result.append(array[0])
    return result

N, K = map(int, input().split())
list_N = list(range(1,N+1))
list_result = josep(list_N,K)
print("<", end="")
for i in range(N-1):
    print(list_result[i], end=", ")
print(list_result[N-1],end="")
print(">")    
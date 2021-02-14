N, M = map(int,input().split())
min_N = min(N,M)
for i in range(1,min_N+1):
    if N % i == M % i == 0:
        result_mod = i

result_mul = N*M//result_mod

print(result_mod)
print(result_mul)
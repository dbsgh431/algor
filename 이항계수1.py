N, K = map(int, input().split())
fac_N = 1
fac_K = 1
fac_N_k = 1
for i in reversed(range(1, N+1)):
    fac_N *= i

for i in reversed(range(1, K+1)):   
    fac_K *= i

for i in reversed(range(1, N-K+1)):
    fac_N_k *= i

print(int(fac_N/(fac_N_k*fac_K)))    
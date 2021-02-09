N = input()
N_list = list(N)
result = 0
x = 0
for i in N:
    result += int(i)

x = int(N) - result

print(x)


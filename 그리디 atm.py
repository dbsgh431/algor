n = int(input())
person = list(map(int, input().split()))
person_p = sorted(person)
sum = 0

if 1<= n <= 1000 and person_p[n-1] <= 1000:
    for i in range(n):
        sum += person_p[i]*((n)-i)

print(sum)    
    
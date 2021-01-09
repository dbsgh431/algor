n = int(input())
rope = [0]*n
min = 0
for i in range(0,n):
    rope[i] = int(input())


rope.sort(reverse=True)
max = rope[0] 


for i in range(1,n):
    s = rope[i]*(i+1)
    if max < s:
        max = s
    else :
        max = max    
    
print(max)
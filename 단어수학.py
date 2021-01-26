n = int(input())
words = [0 for j in range(n)]
codes = [0]
min = 0
run = 0
j = 0
number = [0 for i in range(9, 0, -1)]

for i in range(n):
    word = input()
    words[i] = word
    words[i] = words[i][::-1]

words.sort(key=lambda x: -len(x))  
min = len(words[0])

for i in range(1,n):
    if len(words[i]) < min:
        min = len(words[i])

while run < min:
    for i in range(n):
        codes.append(words[i][j])
    run += 1


    
print(codes)
Word = input()
Word = str(Word.upper())
alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result = 'null'
cnt = [0 for i in range(26)]
for j in Word:
    for i in alpa:
        if i == j:
            cnt[alpa.index(i)] += 1

max = cnt[0]
for i in range(len(cnt)):
    if cnt[i] > max:
        max = cnt[i]
   
        
for i in range(26):
    if cnt[i] == max and result == 'null':
        result = alpa[i]
    elif cnt[i] == max and result != 'null':
        result = "?"

print(result)    





    

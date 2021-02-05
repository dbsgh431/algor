S = input()

result = 0
for i in S:
    sum = 2
    if 67 >= ord(i) >=65:
        sum += 1 
    elif 70 >= ord(i) >= 68:
        sum += 2
    elif 73 >= ord(i) >= 71:
        sum += 3
    elif 76 >= ord(i) >= 74:
        sum += 4
    elif 79 >= ord(i) >= 77:
        sum += 5
    elif 83 >= ord(i) >= 80:
        sum += 6
    elif 86 >= ord(i) >= 84:
        sum += 7
    elif 90 >= ord(i) >= 87:
        sum += 8
    result += sum
print(result)
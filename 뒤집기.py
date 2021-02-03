S = input() 

split_one = S.split('1') # 0으로 연속되는 문자열 추출
split_one = ' '.join(split_one).split() # 문자열의 공백제거
split_zero = S.split('0') # 1로 연속되는 문자열 추출
split_zero = ' '.join(split_zero).split() # 문자열의 공백제거

if len(split_one) >= len(split_zero): # 추출한 문자열 중 갯수가 적은 부분을 뒤집어야 최소값이 나오므로
    result = len(split_zero)
else:
    result = len(split_one)

print(result)        
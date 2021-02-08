x, y, w, h = map(int, input().split())

if x < w-x:
    min_x = x
else:
    min_x= w-x

if y < h-y:
    min_y = y
else:
    min_y= h-y

if min_x <= min_y:
    min_result = min_x
else:
    min_result = min_y

print(min_result)             
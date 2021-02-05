A, B = input().split()
A = list(A)
B = list(B)

A.reverse()
B.reverse()

if int(''.join(A)) >= int(''.join(B)):
   print(''.join(A))
else:
    print(''.join(B))   

 
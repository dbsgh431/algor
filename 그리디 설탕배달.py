sugar = int(input())
basket_5 = 0
basket_3 = 0

basket_5 = sugar / 5
extra = 0

extra = sugar % 5
if 3 <= sugar <= 5000:
    if  sugar != 4 and sugar != 7:
        while extra != 0 :   
            if extra % 3 == 0:
                basket_3 = extra / 3
                break
            else:
                extra += 5
                basket_5 -= 1
        print("{0}".format(int(basket_5+basket_3)))        
    else:
        print("-1")     

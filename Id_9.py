a = 0
b = 0
c = 0



for x in range(1,600):
    for y in range(1,600):
        for z in range(1,600):
            if (x ** 2) + (y ** 2) == (z ** 2) and x < y < z:
                if x + y + z == 1000: 
                    a = x
                    b = y
                    c = z
print("a:",a ,"b:",b ,"c:",c)
print(a * b * c)  

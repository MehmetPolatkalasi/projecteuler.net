list1 = []
list2 = []
toplam1 = 0
toplam2 = 0
for i in range(1,101):
    toplam1 += (i ** 2)
print(toplam1)    
for i in range(1,101):
    toplam2 += i
toplam2 = (toplam2 ** 2)
print(toplam2 - toplam1)    
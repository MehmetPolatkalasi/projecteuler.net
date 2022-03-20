list = []
sayı = 13195
for i in range(2,sayı):
        if sayı % i == 0:
            list.append(i)
print(list)
list2 = []
for i in list:
    for x in range(2,i):
        if i % x == 0:
            break
    else:
        list2.append(i)
print(max(list2))        

               


    

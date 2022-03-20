sayı = 20
list = []
for i in range(1,sayı):
    if i == 1:
        continue
    elif i == 2:
        list.append(i)
    else:
        for x in range(2,i):
            if i % x == 0:
                break
        else:
            list.append(i)
print(list)            
                    
              

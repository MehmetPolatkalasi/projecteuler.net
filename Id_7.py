sayı = 1000000
list = []
sıra = 0
for i in range(1,sayı):
    if i == 1:
        continue
    elif i == 2:
        list.append(i)
        sıra += 1
    else:
        for x in range(2,i):
            if i % x == 0:
                break
        else:
            list.append(i)
            sıra += 1
            if sıra == 10001:
                print(i)        
         
                    
              

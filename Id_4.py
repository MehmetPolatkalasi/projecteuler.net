list = []
for i in range(100,1000):
    for x in range(100,1000):
        sayı = i * x
        sayı = str(sayı)
        if sayı == sayı[::-1]:
            sayı = int(sayı)
            list.append(sayı)
print(max(list))
                        
            
           
            


üs = 1
liste3 = []
liste2 = []
liste = list(range(2,20))
for i in liste:
    if i == 2:
        liste2.append(i)
    else:
        for x in range(2,i):
            if i % x == 0:
                break
        else:
            liste2.append(i)
for i in liste2:
    for x in range(1,21):
        sayı = i ** x
        sayı2 = i * x
        if sayı in liste and sayı not in liste3:
            liste3.append(sayı)
            if i ** (x-1) in liste3:
                liste3.remove(i ** (x-1))
            
            
               
            
        if sayı2 in liste and sayı2 not in liste3 and (sayı2 % 2 != 0 and sayı2 % 3 != 0):
            liste3.append(sayı2)
            if i ** (x-1) in liste3 :
                liste3.remove(i ** (x-1))
liste3.sort()                
print(liste3)            
çarp = 1
for i in liste3:
    çarp *= i
print(çarp)


    
    


                                 
         
            



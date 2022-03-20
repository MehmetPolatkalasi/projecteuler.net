from operator import itemgetter


number = 1000000

x = 0
list1 = list(range(number,0,-1)) # list1 = list(range(1,number))
list2 =[]


for i in list1:
    serie = 1
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            serie += 1
        else:
            i = 3 * i + 1
            serie +=1
    list2.append(serie)        
list3 = list(zip(list1,list2))    
print(max(list3,key=itemgetter(1))[0])
    

            

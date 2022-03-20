list1 = [1,2] * 20
list2 = [1,2] * 20
list3 = []
serie = 0



for i in list1:
    list3.append(i)
    print(list3)
    for x in list2:
        list3.append(x)
        
        
        break
list_3 = sum(list3)        
if list_3 == 60:
    serie += 1

print(serie)
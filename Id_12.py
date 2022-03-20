sum = 0
for i in range(1,100000):
    sum += i
liste = []
for i in range(1,sum+1):
    if sum % i == 0:
        liste.append(i)

if len(liste) >= 7:
    print(sum)
    


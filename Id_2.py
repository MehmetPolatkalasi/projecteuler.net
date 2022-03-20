a = 1
b = 2

fib = [a,b]
for i in range(99999):
    if b < 4000000:
        a,b = b,a+b
        fib.append(b)
toplam = 0        
for i in fib:
    if i % 2 == 0:
        toplam += i
print(toplam)        

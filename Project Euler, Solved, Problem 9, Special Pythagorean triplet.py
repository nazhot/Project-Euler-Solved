from math import sqrt
for c in range(2,500):
    for a in range(1,c):
        for b in range(1,c):
            if a**2+b**2==c**2 and a+b+c==1000:
                print(a,b,c)
                

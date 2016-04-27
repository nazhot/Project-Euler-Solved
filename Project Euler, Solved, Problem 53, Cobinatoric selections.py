from math import factorial
def Combinatoric_selections(bound):
    total=0
    for n in range(2,bound):
        for r in range(1,n):
            c=factorial(n)/(factorial(r)*factorial(n-r))
            if c>1000000:
                total+=1
    print(total)
Combinatoric_selections(101)

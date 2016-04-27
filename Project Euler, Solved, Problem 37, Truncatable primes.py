
from math import sqrt
def remove_left(n):
    for w in range(1,len(str(x))):
        print(str(x)[w:])
def remove_right(n):
    for w in range(len(str(x))-1,0,-1):
        print(str(x)[:w])

def Truncatable_primes(number):
    total=0
    answer=0
    f, c, primes = 1, 11, [2, 3, 5, 7]
    while total<number:
        root = sqrt(c)
        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)
                if len(str(primes[-1]))!=1:
                    for w in range(1,len(str(primes[-1]))):
                        if int(str(primes[-1])[w:]) not in primes:
                            break
                    else:
                        for y in range(len(str(primes[-1]))-1,0,-1):
                            if int(str(primes[-1])[:y]) not in primes:
                                break
                        else:
                            print(primes[-1])
                            total+=1
                            answer+=primes[-1]
                break

        c += 3 - f
        f = -f
    print(answer)


        
    
Truncatable_primes(11)

from math import sqrt

def nth_prime_number(n):
    total=0
    f, c, primes = 1, 11, [2, 3, 5, 7]

    if n < 5:
        return primes[n]

    while n>=primes[-1]:
        root = sqrt(c)
        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)  # Add Prime to List
                break

        c += 3 - f
        f = -f
    print("Primes Generated",primes[-30:])


    for pri in primes:
        temp=pri
        if len(str(pri))==1:
            print(pri)
            total+=1
        else:
            for x in range(len(str(pri))-1):
                temp=str(temp)[1:]+str(temp)[0]
                if str(temp)[0]!="0":
                    if int(temp) not in primes:
                        break
                else:
                    second=str(temp)[1:]
                    if int(second) not in primes:
                        break
            else:
                print(pri)
                total+=1
    print(total)
        
            

print(nth_prime_number(1000000))
      
    

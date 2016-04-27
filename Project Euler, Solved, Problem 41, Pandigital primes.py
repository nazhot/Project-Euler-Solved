from math import sqrt


def nth_prime_number(n):
    f, c, primes = 1, 11, [2, 3, 5, 7]
    if n < 5:
        return primes[n]

    while n>primes[-1]:
        root = sqrt(c)

        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)# Add Prime to List
                for digit in range(1,len(str(primes[-1]))+1):
                    if list(str(primes[-1])).count(str(digit))!=1:
                        break
                else:
                    print(primes[-1])
                break
        c += 3 - f
        f = -f
    

print(nth_prime_number(987654321))
      

from math import sqrt


def nth_prime_number(n):
    f, c, primes = 1, 11, [2, 3, 5, 7]
    answer=[]
    if n < 5:
        return primes[n]

    while n>primes[-1]:
        root = sqrt(c)

        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)  # Add Prime to List
                break

        c += 3 - f
        f = -f
    for pri in primes:
        if len(str(pri))==4:
            if pri+3330 in primes and pri+6660 in primes:
                second=pri+3330
                third=second+3330
                for digit in str(pri):
                    if list(str(second)).count(digit)!=list(str(pri)).count(digit) or list(str(third)).count(digit)!=list(str(pri)).count(digit):
                        break
                else:
                    print(pri, second, third)
                    answer.append(str(pri)+str(second)+str(third))
                
    print(answer)

print(nth_prime_number(10000))
      

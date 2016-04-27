from math import sqrt
def consecutive_prime_sum(n):
    total=0
    answer=0
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
    number=2
    while number<len(primes):
        for pot in range(number,len(primes)):
            if sum(primes[pot-number:pot])>primes[-1]:
                break
            elif sum(primes[pot-number:pot]) in primes[pot:]:
                answer=sum(primes[pot-number:pot])
                break
        number+=1
    print(answer)
consecutive_prime_sum(1000000)

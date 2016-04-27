from math import sqrt


def nth_prime_number(n):
    f, c, primes = 1, 11, [2, 3, 5, 7]

    while c<sqrt(n):
        root = sqrt(c)

        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)# Add Prime to List
                break

        c += 3 - f
        f = -f
    for x in primes:
        if n%x==0:
            answer=x
    return answer


print(nth_prime_number(600851475143 ))

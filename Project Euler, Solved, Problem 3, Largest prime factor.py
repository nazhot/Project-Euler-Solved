from math import sqrt


def nth_prime_number(n):
    f, c, primes = 1, 11, [2, 3, 5, 7]
    total=17

    while c<n:
        root = sqrt(c)

        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)# Add Prime to List
                total+=c
                break

        c += 3 - f
        f = -f
    return total

print(nth_prime_number(2000000))

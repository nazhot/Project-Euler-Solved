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
    print("Primes Generated")
    squares_doubled=[]
    for square in range(1,n):
        squares_doubled.append(2*pow(square,2))
    print("Squares Generated")
    number=7
    while True:
        if number not in primes:
            for num in squares_doubled:
                if number-num in primes:
                    break
                elif num>number:
                    continue
            else:
                print(number)
                break
        number+=2

nth_prime_number(100000)

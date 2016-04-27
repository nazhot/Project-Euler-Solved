from math import sqrt

def quadratic_primes(max_a,max_b,max_prime):
    total=0
    f, c, primes = 1, 11, [2, 3, 5, 7]
    answer=[0,0,0]
    while max_prime>=primes[-1]:
        root = sqrt(c)
        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)  # Add Prime to List
                break

        c += 3 - f
        f = -f

    for a in range(-max_a,max_a):
        for b in range(-max_b,max_b):
            n=0
            total=0
            while True:
                pot_pri=n**2+a*n+b
                if pot_pri in primes:
                    total+=1
                    n+=1
                else:
                    break
            if total>answer[0]:
                answer=[total,a,b]
                
    print(answer)

quadratic_primes(1000,1000,10000)
                

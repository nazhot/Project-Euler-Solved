from math import sqrt

def nth_prime_number(n,num_of_primes,num_of_cons):
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
    for number in range(n):
        factors=0
        for x in primes:
            if x>number:
                break
            elif number%x==0:
                factors+=1
        if factors==num_of_primes:
            answer.append(number)
            if len(answer)>num_of_cons:
                for y in range(1,num_of_cons):
                    if answer[-(y)]-answer[-(y+1)]!=1:
                        break
                else:
                    print(answer[-(num_of_cons):])
                    break
        
print(nth_prime_number(1000000,4,4))

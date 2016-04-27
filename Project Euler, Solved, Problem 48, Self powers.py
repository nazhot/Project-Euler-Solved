def prime_sum(power,last_digits):
    total=0
    for x in range(1,power+1):
        total+=x**x
    return str(total)[-last_digits:len(str(total))]
print(prime_sum(1000,10))

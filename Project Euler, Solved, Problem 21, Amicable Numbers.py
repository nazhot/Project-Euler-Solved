def amicable_numbers(n):
    total=0
    x=1
    while x<n:
        original_divisor_total=0
        other_divisor_total=0
        for divisors in range(1,x):
            if x%divisors==0:
                original_divisor_total+=divisors
        for num in range(1,original_divisor_total):
            if original_divisor_total%num==0:
                other_divisor_total+=num      
        if other_divisor_total==x and x!=original_divisor_total:
            print("Answer: %s"%(x))
            total+=x
        x+=1
    print("Sum: %s"%(total))

amicable_numbers(10000)

#go from 1 to n (max number we want to go up to)
# for each number in that range find its divisors and add them
# find divisors of that number and add them
#if equal to original number then add original number to array of amicable numbers

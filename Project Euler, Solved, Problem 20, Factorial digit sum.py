def factorial_digit_sum(n):
    factorial=1
    factorial_sum=0
    for num in range(1,n+1):
        factorial*=num
    for digit in str(factorial):
        factorial_sum+=int(digit)
    return factorial, factorial_sum
print(factorial_digit_sum(100))

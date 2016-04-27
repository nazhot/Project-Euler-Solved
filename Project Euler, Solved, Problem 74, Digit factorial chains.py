from math import factorial 
def digit_factorial_chains(n):
    number=3
    total=0
    while number<n:
        step=1
        past_sums=[number]
        while True:
            factorial_sum=0
            for digit in str(past_sums[-1]):
                factorial_sum+=factorial(int(digit))
            if factorial_sum in past_sums:
                if step==60:
                    total+=1
                    print(number)
                number+=1
                break
            else:
                past_sums.append(factorial_sum)
                step+=1
    print(total)
        
            
digit_factorial_chains(1000000)

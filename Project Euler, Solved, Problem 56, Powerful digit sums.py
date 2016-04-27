def powerful_digit_sum(n):
    answer=0
    for a in range(n):
        for b in range(n):
            number_sum=0
            number=a**b
            for digit in str(number):
                number_sum+=int(digit)
            if number_sum>answer:
                answer=number_sum
    print(answer)




powerful_digit_sum(100)

def digit_powers(power):
    number=10
    answer=0
    while number<1000000:
        total=0
        for digit in str(number):
            total+=pow(int(digit),power)
        if total==number:
            print(number)
            answer+=number
        number+=1
    print(answer)

digit_powers(5)
        

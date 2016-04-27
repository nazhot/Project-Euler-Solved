from math import factorial
def digit_factorials():
    number=3
    while True:
        total=0
        for digit in str(number):
            total+=factorial(int(digit))
        if total==number:
            print("Answer: %s"%(number))
        number+=1
        
digit_factorials()


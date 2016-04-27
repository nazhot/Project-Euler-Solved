def fibonacci_number(n):
    a,b,number=1,0,0
    while True:
        a,b=b,a+b
        if len(str(a))==n:
            print(number)
            break
        number+=1
    


fibonacci_number(1000)

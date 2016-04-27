from math import factorial
def lex_perms(n):
    temp=n
    fac=9
    potential=[0,1,2,3,4,5,6,7,8,9]
    answer=[]
    while fac>=0:
        number=0
        while temp-number*factorial(fac)>factorial(fac):
            number+=1
        answer.append(potential[number])
        del potential[number]
        temp-=number*factorial(fac)
        print(number*factorial(fac))
        print(number)
        fac-=1
    print(answer)


lex_perms(1000000)

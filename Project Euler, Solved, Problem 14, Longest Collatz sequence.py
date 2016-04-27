answer=[]



for x in range(2,1000000):
    t=x
    numbers=[t]
    while t>1:
        if t%2==0:
            t=t/2
        else:
            t=3*t+1
        numbers.append(t)
    if len(numbers)>len(answer):
        answer=numbers
print(answer)




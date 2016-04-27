from math import sqrt
number=1
add=2
total=0
while True:
    number+=add
    add+=1
    total=0
    for x in range(1,int(sqrt(number+1))):
        if number%x==0:
            total+=1
    total*=2
    if total>=500:
        break
print("Answer: %s with %s factors"%(number,total))    

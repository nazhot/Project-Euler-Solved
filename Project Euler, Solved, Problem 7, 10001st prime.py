num=1
while num<2000001:
    num+=2
    for b in range(2,num):
        if num%b==0:
            break
    else:
        print(num)
    

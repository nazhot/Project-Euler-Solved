import time
def Smallest_multiple(maximum):
    w=time.time()
    number=maximum
    while True:
        for x in range(1,maximum+1):
            if number%x!=0:
                break
        else:
            print(number)
            print("Code executed in %s seconds" %(time.time()-w))
            break
        number+=maximum

Smallest_multiple(20)

import time
w=time.time()
integer=1
while True:
    double=integer*2
    triple=integer*3
    quad=integer*4
    five=integer*5
    six=integer*6
    temp=[double,triple,quad,five,six]
    answer=[[],[],[],[],[]]
    if len(str(double))==len(str(integer))==len(str(triple))==len(str(quad))==len(str(five))==len(str(six)):
        for number in range(5):
            for digit in str(temp[number]):
                answer[number].append(int(digit))
            answer[number].sort()
        if answer[0]==answer[1]==answer[2]==answer[3]==answer[4]:
            print(integer)
            print("%s seconds"%(time.time()-w))
            break
            
    integer+=1


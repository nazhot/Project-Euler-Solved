from fractions import Fraction
total_num=1
total_den=1
for x in range(11,100):
    for y in range(11,x):
        if y%10!=0 and x%10!=0:
            if str(y)[0]==str(x)[0] and y/x==int(str(y)[1])/int(str(x)[1]):
                print(y,x)
            elif str(y)[1]==str(x)[0] and y/x==int(str(y)[0])/int(str(x)[1]):
                print(y,x)
            elif str(y)[1]==str(x)[1] and y/x==int(str(y)[0])/int(str(x)[0]):
                print(y,x)
            elif str(y)[0]==str(x)[1] and y/x==int(str(y)[1])/int(str(x)[0]):
                print(y,x)



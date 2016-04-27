
for number in range(2,10000):
    temp=str(number)
    multiplier=2
    while len(temp)<10:
        if len(temp)==9:
            for digit in range(1,10):
                if list(temp).count(str(digit))!=1:
                    temp+=str(multiplier*number)
                    break
            else:
                print(temp)
                break
        else:
            temp+=str(multiplier*number)
        multiplier+=1
            

length_power=1
total=0
while length_power<100:
    number=1
    if len(str(2**length_power))>length_power:
        break
    else:
        while len(str(number**length_power))<=length_power:
            if len(str(number**length_power))==length_power:
                total+=1
            number+=1
    length_power+=1
print(total)
            

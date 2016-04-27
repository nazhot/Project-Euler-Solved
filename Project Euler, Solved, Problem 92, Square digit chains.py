import time
def square_digit_chains(n):
    w = time.time()
    number=2
    total=0
    eighty_nine=[89]
    one=[1]
    while number<n:
        sums=[number]
        while True:
            square_sum=0
            for digit in str(sums[-1]):
                square_sum+=int(digit)**2
            if square_sum in one:
                number+=1
                for num in sums:
                    one.append(num)
                break
            elif square_sum in eighty_nine:
                number+=1
                total+=1
                for num in sums:
                    eighty_nine.append(num)
                break
            else:
                sums.append(square_sum)
        if number%500==0:
            eighty_nine = [89]
            one = [1]
    print(time.time()-w)
    return total


print(square_digit_chains(10000000))
        



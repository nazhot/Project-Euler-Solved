def lychrel_numbers(n):
    number=1
    answer=0
    while number<n:
        pal_sum=number+int(str(number)[::-1])
        for x in range(1,51):
            if pal_sum==int(str(pal_sum)[::-1]):
                break
            else:
                pal_sum+=int(str(pal_sum)[::-1])
        else:
            print(number)
            answer+=1
        number+=1
    print(answer)
lychrel_numbers(10000)

import time
from math import sqrt
def abundant_numbers(n):
    numbers_two=[]
    answer=0
    w=time.time()
    sum_list=[24]
    for number in range(12,n+1):
        total=1
        for divisor in range(2,int(sqrt(number))+1):
            if number%divisor==0:
                total+=divisor
                if divisor!=number/divisor:
                    total+=number/divisor
        if total>number:
            numbers_two.append(number)
    print("Abundants calculated in %s seconds"%(time.time()-w),len(numbers_two))
    w=time.time()
    number=0
    while number<len(numbers_two):
        print(number)
        for x in range(number,len(numbers_two)):
            addition=numbers_two[number]+numbers_two[x]
            if addition<n and addition not in sum_list:
                sum_list.append(numbers_two[number]+numbers_two[x])
        number+=1
    print("Sum list created in %s seconds"%(time.time()-w),len(sum_list))

     


                
         
    print(answer)
                
    
            








abundant_numbers(28123)

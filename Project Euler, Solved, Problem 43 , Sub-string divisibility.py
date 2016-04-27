number=1
total=0
answer_one=[]
while len(str(total))<4:
    total=17*number
    if len(str(total))==3:
        for digit in str(total):
            if list(str(total)).count(str(digit))>1:
                break
        else:
            answer_one.append(total)
    number+=1
number=1
answer_two=[]
total=0
while len(str(total))<4:
    total=13*number
    if len(str(total))==3:
        for digit in str(total):
            if list(str(total)).count(str(digit))>1:
                break
        else:
            for num in answer_one:
                if str(total)[1:3]==str(num)[0:2] and str(total)[0]!=str(num)[2]:
                    answer_two.append("%s%s"%(str(total),str(num)[2]))
    number+=1
number=1
total=0
answer_three=[]
while len(str(total))<4:
    total=11*number
    if len(str(total))==3:
        for digit in str(total):
            if list(str(total)).count(str(digit))>1:
                break
        else:
             for num in answer_two:
                if str(total)[1:3]==str(num)[0:2]:
                    answer_three.append("%s%s"%(str(total)[0],str(num)))
                


    number+=1
number=1
total=0
answer_four=[]
while len(str(total))<4:
    total=7*number
    if len(str(total))==3:
        for digit in str(total):
            if list(str(total)).count(str(digit))>1:
                break
        else:
             for num in answer_three:
                if str(total)[1:3]==str(num)[0:2]:
                    answer_four.append("%s%s"%(str(total)[0],str(num)))
                    for x in answer_four:
                        for digits in str(x):
                            if list(str(x)).count(digits)>1:
                                answer_four.remove("%s%s"%(str(total)[0],str(num)))
                                break
    

    number+=1
print(answer_four)

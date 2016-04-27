answer=[]
total=0
for first in range(1,10000):
    for second in range(1,1000):
        third=first*second
        if len(str(third))+len(str(second))+len(str(first))==9:
            concate=str(first)+str(second)+str(third)
            for pand in range(1,10):
                if list(concate).count(str(pand))!=1:
                    break
            else:
                if third not in answer:
                    answer.append(third)
                    total+=third
print(total)




def counting_sundays(start,finish):
    total=0
    Date=1
    Month=1
    Year=start
    Days=["Mo","Tu","We","Th","Fr","Sa","Su"]
    thirty=[2,4,6,9,11]
    Index=2
    while Year<=finish:
        if Year%4==0 and not (str(Year)[-2]=="0" and str(Year)[-1]=="0"):
            Leap=1
        else:
            Leap=0
        while Month<=12:
            if Month==2:
                Max_Day=28+Leap
            elif Month in thirty:
                Max_Day=30
            else:
                Max_Day=31
            while Date<=Max_Day:
                Today=Days[Index]
                Index=(Index+1)%len(Days)
                if Today=="Su" and Date==1:
                    total+=1
                Date+=1
            Month+=1
            Date=1
        Date=1
        Year+=1
        Month=1
    print(total)
counting_sundays(1901,2000)

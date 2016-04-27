letters=[[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8],[6,6,5,5,5,7,6,6]]
total=0
def letters_count(n):
    total=0
    for num in range(1,n):
        if num<20:
            total+=letters[0][num]
        elif len(str(num))==2:
            for digit in range(2):
                if digit==0:
                    total+=letters[1][int(str(num)[0])-2]
                else:
                     total+=letters[0][int(str(num)[1])]
##        else:
##            for digit in range(3):
##                if digit==0:
##                    total+=7+letters[0][int(str(num)[0])]
##                    if not (str(num)[1]=="0" and str(num)[2]=="0"):
##                        total+=3
##                elif digit==1:
##                    total+=letters[1][int(str(num)[0])-2]
##                else:
##                    total+=letters[0][int(str(num)[1])]
##                    
    print(total)
    print(total*10)
    print(total*10+(3*99*9)+11)
    print(total*10+(3*99*9)+(7*900)+11+300+300+500+400+400+300+500+500+400)
    
          
         
         
letters_count(100)                    
    

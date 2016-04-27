from math import sqrt
import time

def integer_right_triangles(n):
    w=time.time()
    maximum=(n**2)/2
    number=2
    sides=[1]
    perimeters=[]
    answer=[0,0]
    while maximum>=1000*(sides[-1]-sides[0])+sides[-1]*sides[0]:
        sides.append(number)
        number+=1
    squares=[]
    for num in sides:
        squares.append(num**2)
    index=0
    for square in range(len(squares)):
        for extra in range(index,len(squares)):
            if squares[square]+squares[extra]>squares[-1]:
                break
            elif squares[square]+squares[extra] in squares:
                c_squared=squares[square]+squares[extra]
                perimeters.append(sides[square]+sides[extra]+round(sqrt(c_squared)))
        index+=1
    for per in perimeters:
        if perimeters.count(per)>answer[0]:
            answer=[perimeters.count(per),per]
    print("The most common perimeter is %s, occuring %s times"%(answer[1],answer[0]))
    print("Calculations took %s seconds to complete"%(time.time()-w))

integer_right_triangles(1000)
        

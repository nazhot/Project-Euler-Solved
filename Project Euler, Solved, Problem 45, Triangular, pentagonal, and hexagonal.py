def tri_pent_hex(n):
    number=1
    turn=0
    tri_num=[]
    pen_num=[]
    hex_num=[]
    while True:
        triangle=number*(number+1)/2
        pentagonal=number*(3*number-1)/2
        hexagonal=number*(2*number-1)
        pen_num.append(pentagonal)
        hex_num.append(hexagonal)
        if triangle in pen_num and triangle in hex_num:
            print(number,triangle)
            turn+=1
        number+=1
        if turn==n+1:
            break

tri_pent_hex(2)

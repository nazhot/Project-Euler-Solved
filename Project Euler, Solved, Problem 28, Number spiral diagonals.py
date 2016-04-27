def number_spiral_diagonals(n):
    total=1
    number=1
    row=3
    while row<=n:
        for x in range(1,5):
            number+=row-1
            total+=number
        row+=2
    print(total)

number_spiral_diagonals(1001)

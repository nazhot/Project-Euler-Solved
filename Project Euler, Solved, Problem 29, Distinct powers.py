def distinct_powers(low,high):
    generated=[]
    for b in range(low,high+1):
        for a in range(low,high+1):
            if pow(a,b) not in generated:
                generated.append(pow(a,b))
    print(len(generated))

distinct_powers(2,100)

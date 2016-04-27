a=[]
for x in range(1000,99,-1):
    for y in range(1000,99,-1):
        if str(x*y)==str(x*y)[::-1]:
            a.append(x*y)
print(max(a))





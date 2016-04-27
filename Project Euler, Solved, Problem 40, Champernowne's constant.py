decimal=""
total=1
for number in range(0,1000000):
    decimal+=str(number)
for power in range(7):
    total*=int(decimal[10**power])

print(total)

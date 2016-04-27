import binascii
total=0
for x in range(1,1000000):
    if str(x)==str(x)[::-1]:
        binary=bin(x)[2:]
        if str(binary)==str(binary)[::-1]:
            total+=x
print(total)
        

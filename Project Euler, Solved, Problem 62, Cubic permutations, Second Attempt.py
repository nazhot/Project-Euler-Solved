from itertools import permutations
def cubic_permutations(n):
    cubes=[1]
    number=2
    cube_number=2
    while True:
        total=0
        perms=list(permutations(str(number**3)))
        for item in range(len(perms)):
            perms[item]=int("".join(perms[item]))
        for items in perms:
            if perms.count(item)>1:
                perms.remove(items)
        while max(perms)>cubes[-1]:
            cubes.append(cube_number**3)
            cube_number+=1
        for num in perms:
            if num in cubes:
                total+=1
        if total==n:
            print(number)
            break
        number+=1
            

cubic_permutations(3)

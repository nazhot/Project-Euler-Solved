from itertools import permutations
def cubic_permutations(n):
    number=1
    while True:
        total_cubes=0
        final_perms=[]
        cube_perms=list(permutations(str(number**3)))
        for perm in cube_perms:
            final_perms.append(int("".join(perm)))
        for item in final_perms:
            if final_perms.count(item)>1:
                final_perms.remove(item)
            elif abs(round(pow(item,1/3))-pow(item,1/3))<=.00001:
                total_cubes+=1
        if total_cubes==n:
            print(number)
            break
        print(number)
    
        number+=1
cubic_permutations(4)
x

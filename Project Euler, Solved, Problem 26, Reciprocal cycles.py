from decimal import *
getcontext().prec = 2000

def reciprocal_cycles(n):
    answer = [0,0]
    for denom in range(2,n+1):
        cycle = ""
        fraction=Decimal(Decimal(1)/Decimal(denom))
        for digit in range(2,len(str(fraction))):
            if len(cycle) == 0:
                if str(fraction)[digit] != "0" and str(fraction)[digit] != "1":
                    cycle = str(fraction)[digit]
            elif len(cycle) > 1 and str(fraction)[digit] == cycle[0]:
                if cycle == str(fraction)[digit:digit+len(cycle)]:
                    if len(cycle) > answer[0]:
                        answer[0] = len(cycle)
                        answer[1] = denom
                    break
                else:
                    cycle+=str(fraction)[digit]
            else:
                cycle += str(fraction)[digit]
    print(answer)

reciprocal_cycles(1000)

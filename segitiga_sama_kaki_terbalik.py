slot = 10

for x in range(0, slot+1):
    temp = slot - x
    for y in range(0, slot+1):
        if(y >= temp):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print("")
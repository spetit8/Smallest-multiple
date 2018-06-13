def FindSmallestMultiple(Number):
    while(True):
        for factor in range(1, 21):
            if Number % factor != 0:
                break
            elif factor == 20:
                return(Number)
        Number += 1

print(FindSmallestMultiple(20))

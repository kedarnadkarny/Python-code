t = int(input().strip())
minT = 1
maxT = 4
minV = 3



while False:
    if t <= maxT:
        for i in range(minT, maxT):
            if i == t:
                print(i)
                break
    else:
        minT = maxT + 1
        oldminV = minV
        minV = minV * 2
        maxT = oldminV + minV

# tought. solve again
test_cases = int(input())

while test_cases>0:
    n = int(input())
    # print(n)
    test_cases -= 1
    i = 0
    height = 0
    length = 0
    while i < n:
        i += 1
        length += 1
        if length == i:
            height += 1
            n -= i
        else:
            break

    print(height)

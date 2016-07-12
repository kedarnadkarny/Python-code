test_cases = int(input())
while test_cases > 0:
    test_cases = test_cases - 1
    S = input()
    S = list(S)
    a = 0
    b = 0
    for x in S:
        if x=='a':
            a = a + 1
        elif x=='b':
            b = b + 1
    print(min(a,b))
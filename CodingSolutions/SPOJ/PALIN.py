test_cases = int(input())
while test_cases>0:
    K = input()
    K = int(K)
    K = K + 1

    while True:
        K = str(K)
        R = K[::-1]
        if R==K:
            print(R)
            break
        else:
            K = int(K)
            K = K + 1
    test_cases = test_cases - 1
test_cases = int(input())
alphabet = ['a','b','c','d','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s1 = list()
s2 = list()
result = list()

while test_cases>0:
    A = input()
    B = input()
    test_cases = test_cases-1
    for e in alphabet:
        if A.find(e)>-1:
            s1.append(e)
        if B.find(e)>-1:
            s2.append(e)
    match = 0
    #print(set(s1).intersection(s2))
    match = len(set(s1).intersection(s2))
    if match > 0:
        print("Yes")
    else:
        print("No")
    del s1[:]
    del s2[:]

test_cases = int(input())
T = list()

while test_cases > 0:
    test_cases -= 1
    L = []
    R = []
    occ = 0
    no_of_movies = input()
    no_of_movies = int(no_of_movies)
    L = input().split()
    R = input().split()
    for x in range(no_of_movies):
        m = int(L[x]) * int(R[x])
        T.append(m)

    print(T)
    print(max(T))


    #print(T.index(max(T)))
    #print(T.count(max(T)))
    #if T.count(max(T))>1:
    #    print("more than one occurence")
    #m = max(T)
    #To find index of maximum values
    #print([i for i, j in enumerate(T)if j == m])

    #To enumerate the list
    #print([(i, j) for i, j in enumerate(T)])


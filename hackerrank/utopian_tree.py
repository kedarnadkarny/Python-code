t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height = 1
    for i in range(1, n+1):
        if i%2==0:
            height = height + 1
        else:
            height = height * 2
    print(height)
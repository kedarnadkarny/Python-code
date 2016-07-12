lower = int(input())
higher = int(input())
n=0
difference = higher - lower
for x in range(lower, higher):
    if n%x==0:
        print(x," is not prime")
    else:
        print(x, " is prime")
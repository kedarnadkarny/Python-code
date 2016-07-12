test_cases = int(input())
out = test_cases
output = list()

while test_cases>0:
    num, limit = input().split()
    num_array = list(map(float, input().split()))
    test_cases = test_cases-1
    num_array.sort()
    limit = int(limit)
    while limit>0:
        i = limit-1
        num_array.pop(i)
        num_array.pop()
        limit = limit-1

    total=0
    for x in num_array:
        total += x

    output.append(total/len(num_array))


for x in output:
    print(x)
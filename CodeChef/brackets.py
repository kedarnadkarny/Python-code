def max_balance(par):
    max_bal = 0
    bal = 0
    length = len(par)
    for i in range(0, length):
        if par[i] == '(':
            bal = bal + 1
        else:
            bal = bal - 1
        max_bal = max(max_bal, bal)
    return max_bal

test = int(input())
while test > 0:
    par = input()
    mx = max_balance(par)
    for x in range(0, mx):
        print("(", end='')
    for x in range(0, mx):
        print(")", end='')
    print('\n')
    test = test - 1
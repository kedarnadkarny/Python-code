t = input()
t = int(t)

trans = []

while t>0:
    t = t - 1
    str = input()
    str2 = str[::-1]
    if str == str2:
        print("no answer", end="")
    else:
        for i in str:
            trans.append(ord(i))
        trans.sort()
        for i in trans:
            print(chr(i), end="")
    trans = []
    print()

test_cases = int(input())
r = 0
g = 0
b = 0
output = list()

while test_cases > 0:
    test_cases = test_cases - 1
    no_of_rooms = input()
    n = input()
    room_color = list(n)

    if len(room_color)==1:
        output.append(0)
    elif len(room_color)==2:
        m = room_color(0)
        n = room_color(1)
        if m==n:
            output.append(0)
        else:
            output.append(1)
    else:
        for x in room_color:
            if x=='R':
                r = r + 1
            elif x=='G':
                g = g + 1
            elif x=='B':
                b = b + 1

    if r == g == b:
        output.append(r+g)
    else:
        common = max(r,g,b)
        total = r + g + b
        minimum = total-common
        output.append(minimum)
    r = 0
    g = 0
    b = 0

for x in output:
    print(x)
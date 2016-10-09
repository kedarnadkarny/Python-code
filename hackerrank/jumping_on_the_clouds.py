n = int(input())
c = raw_input()
c = c.split(' ')
c = [ int(x) for x in c ]

step = 0
i = 0

while i < len(c)-1:
    if c[i+1] == 0 and c[i+2] != len(c)-2:
	if c[i+2] == 1:
	    step = step + 1
            i = i + 1
    elif c[i+1] == 0 and c[i+2] != len(c)-2:
	if c[i+2] == 1:
            step = step + 1
            i = i+2
    elif c[i+1] == 1:
        step = step + 1
        i = i+2

print step

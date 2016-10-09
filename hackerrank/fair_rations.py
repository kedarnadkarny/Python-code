N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

count = 0

if sum(B) % 2 == 1:
	print "NO"
else:
	for i in range(0, len(B)):
		if B[i] % 2 != 0:
			B[i] = B[i] + 1
			B[i+1] = B[i+1] + 1
			count = count + 2
	print count

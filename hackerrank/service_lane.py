n, t = raw_input().strip().split(' ')
n, t = [int(n), int(t)]
width = map(int, raw_input().strip().split(' '))

for a0 in xrange(t):
	i, j = raw_input().strip().split(' ')
	i, j = [int(i), int(j)]
	newLst = width[i:j+1]
	print min(newLst)
	newLst = []

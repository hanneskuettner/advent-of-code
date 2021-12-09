
ops = [int(e) for e in open('input.txt').read().split(',')]
# ops = [3, 4, 1, 5]


cl = 256
l = list(range(cl))
c = 0
s = 0
for op in ops:
	if op > 1:
		if c + op < cl:
			l[c:c+op] = l[c:c+op][::-1]
		else:	
			a = (l[c:] + l[:op - (len(l) - c)])[::-1]
			l[c:] = a[:len(l) - c]
			l[:op - (len(l) - c)] = a[len(l) - c:]
	c = (c + op + s) % cl
	s += 1

print(l[0] * l[1])


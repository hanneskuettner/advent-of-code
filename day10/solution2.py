import operator
from functools import reduce

cl = 256

def get_sparse(ops):
	l = list(range(cl))
	c = 0
	s = 0
	for i in range(64):
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
	return l

def get_dense(ops):
	l = get_sparse(ops)
	dense = []
	for i in range(16):
		dense.append(reduce(operator.xor, l[i*16:(i+1)*16], 0))
	return dense

def hash(ops):
	return ''.join('{:02x}'.format(e) for e in get_dense(ops + [17, 31, 73, 47, 23]))


ops = [ord(e) for e in open('input.txt').read().rstrip()]
# ops = [3, 4, 1, 5]
print(hash(ops))


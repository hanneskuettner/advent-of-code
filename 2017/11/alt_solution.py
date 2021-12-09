dir_vecs = {
	'n': [0, 1, -1],
	's': [0, -1, 1],
	'ne': [1, 0, -1],
	'sw': [-1, 0, 1],
	'nw': [-1, 1, 0],
	'se': [1, -1, 0]
}

def dist(p):
	return max(abs(c) for c in p)

def add(p1, p2):
	return [c1 + c2 for c1, c2 in zip(p1, p2)]

steps = open('input.txt').read().rstrip().split(',')

p = [0, 0, 0]
m = 0
for s in steps:
	p = add(p, dir_vecs[s])
	m = max([m, dist(p)])

print(dist(p))
print(m)
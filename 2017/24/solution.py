from collections import defaultdict

def generate_bridges(bridge, components):
	l, s, b_comps, p0 = bridge or (0, 0, set(), 0)
	for p1 in components[p0]:
		n = (p0, p1) if p0 <= p1 else (p1, p0)
		if n not in b_comps:
			new =(l+1, s+p0+p1, (b_comps | {n}), p1)
			yield new
			yield from generate_bridges(new, components)

components = defaultdict(set)
for l in open('input.txt').readlines():
	p0, p1 = [int(p) for p in l.split('/')]
	components[p0].add(p1)
	components[p1].add(p0)

bridges = [b[:2] for b in generate_bridges(None, components)]

print(max(bridges, key=lambda b: b[1]))[1]
print(max(bridges))[1]
def parse_line(line):
	parts = line.split()
	if len(parts) == 2:
		return parts[0], [parts[1][1:-1]]
	else:
		return parts[0], [parts[1][1:-1], [e.rstrip(',') for e in parts[3:]]]



def build_tree(lines):
	roots = dict(lines)
	for key, node in lines:
		if len(node) == 2:
			for i, child in enumerate(node[1]):
				node[1][i] = roots[child]
				del roots[child]
	print(roots.keys()[0])
	return roots.values()[0]
	

def tree_height(tree):
	if len(tree) > 1:
		return 1 + tree_height(tree[1][0])
	return 1

def weights(tree):
	print(tree)
	if len(tree) > 1:
		ws = []
		for node in tree[1]:
			child_weights = weights(node)
			ws.append(int(node[0]) + sum(child_weights))

		l = ws[0]
		for w in ws:
			if w != l:
				print(w - l)
				print(ws)
				exit()
		return ws
	return []




lines1 = list(parse_line(line) for line in open("input.txt").readlines())

lines2 = list(parse_line(line) for line in """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split('\n'))

weights(build_tree(lines1))
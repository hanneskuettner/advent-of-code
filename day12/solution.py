connections = dict((int(l.split()[0]), [int(e) for e in l.replace(' <-> ', ', ').split(',')[1:]]) for l in open('input.txt').readlines())

curr = 0
neighbors = {0: []}
neighbor_set = set([0])
while neighbor_set:
	curr_node = neighbor_set.pop()
	conns, connections[curr_node] = connections[curr_node], None
	if conns:
		neighbors[curr].append(curr_node)
		neighbor_set.update(conns)
	if not neighbor_set:
		try:
			# get next untouched connection pair
			c = list(filter(lambda i: i[1], connections.items()))[0]
			curr = c[0]
			neighbors[curr] = []
			neighbor_set.update(c[1])
		except:
			break

print(len(neighbors[0]))
print(len(neighbors))
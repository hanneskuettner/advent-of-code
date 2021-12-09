# load instruction and replace dec/inc with python equivalents -=/+=
instructions = [l.replace(' dec ', ' -= ').replace(' inc ', ' += ').rstrip() for l in open("input.txt").readlines()]

ns = {}
# init global variables to 0
for i in instructions:
	ns[i.split()[0]] = 0

# execute each instruction. <3 python
m = 0
for i in instructions:
	exec(i + ' else 0', ns)
	m = max([g for g in ns.values() if type(g) is int] + [m])


print(max(g for g in ns.values() if type(g) is int))
print(m)
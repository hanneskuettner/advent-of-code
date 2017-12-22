grid = {(x,y): c for y,l in enumerate(open('input.txt').readlines()) for x,c in enumerate(l.strip())}

p = (len(grid) ** 0.5 // 2, len(grid) ** 0.5 // 2)
d = 0

infected_count = 0
for i in range(10000):
	status = grid.setdefault(p, '.')
	if status == '#':
		d = (d + 1) % 4
		grid[p] = '.'
	else:
		d = (d - 1) % 4
		infected_count += 1
		grid[p] = '#'
	
	if d == 0:
		p = (p[0], p[1]-1)
	elif d == 1:
		p = (p[0]+1, p[1])
	elif d == 2:
		p = (p[0], p[1]+1)
	else:
		p = (p[0]-1, p[1])

print(infected_count)
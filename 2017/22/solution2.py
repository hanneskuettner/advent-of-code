grid = {(x,y): {'.': 0, '#': 2}[c] for y,l in enumerate(open('input.txt').readlines()) for x,c in enumerate(l.strip())}

p = (len(grid) ** 0.5 // 2, len(grid) ** 0.5 // 2)
d = 0

infected_count = 0
for i in range(10000000):
	status = grid.setdefault(p, 0)
	if status == 0:
		d = (d - 1) % 4
	elif status == 1:
		infected_count += 1
	elif status == 2:
		d = (d + 1) % 4
	elif status == 3:
		d = (d + 2) % 4

	grid[p] = (grid[p] + 1) % 4
	
	if d == 0:
		p = (p[0], p[1]-1)
	elif d == 1:
		p = (p[0]+1, p[1])
	elif d == 2:
		p = (p[0], p[1]+1)
	else:
		p = (p[0]-1, p[1])

print(infected_count)
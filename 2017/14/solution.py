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

def hash(string):
	return ''.join('{:02x}'.format(e) for e in get_dense([ord(c) for c in string] + [17, 31, 73, 47, 23]))





def is_valid(grid, i, j, row, col, visited):
	return i >= 0 and i < row and j >= 0 and j < col and not visited[i][j] and grid[i][j]


def dfs(grid, i, j, row, col, visited):
	row_dir = [-1, 1, 0, 0]
	col_dir = [0, 0, 1, -1]
	visited[i][j] = True

	for k in range(4):
		if is_valid(grid, i + row_dir[k], j + col_dir[k], row, col, visited):
			dfs(grid, i + row_dir[k], j + col_dir[k], row, col, visited)

def count_groups(grid):
	visited = [[False] * len(grid) for i in range(len(grid))]

	count = 0
	for i in range(len(grid)):
	    for j in range(len(grid)):
	        if visited[i][j] == False and grid[i][j] == 1:
	            dfs(grid, i, j, len(grid), len(grid), visited)
	            count += 1

	return count


prefix = 'vbqugkhl'
count = 0
for i in range(128):
	count += sum(int(c) for c in str(bin(int(hash('{}-{}'.format(prefix, i)), 16)))[2:])

print(count)

grid = []
for i in range(128):
	grid.append([int(c) for c in '{:0128b}'.format(int(hash('{}-{}'.format(prefix, i)), 16))])

print(count_groups(grid))


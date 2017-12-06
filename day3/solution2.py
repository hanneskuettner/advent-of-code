#!/usr/bin/env python3
import sys
req = int(sys.argv[1])

spiral = [[1]]

def new_shell(spiral):
	size = len(spiral)
	for i in range(size):
		spiral[i] = [0] + spiral[i] + [0]
	spiral.insert(0, [0] * (size + 2))
	spiral.append([0] * (size + 2))

def fill_cell(spiral, i, j):
	size = len(spiral)
	print(spiral, i, j)
	if i > 0:
		spiral[i][j] += spiral[i-1][j]
		if j > 0:
			spiral[i][j] += spiral[i-1][j-1]
		if j < size - 1:
			spiral[i][j] += spiral[i-1][j+1]
	if i < size - 1:
		spiral[i][j] += spiral[i+1][j]
		if j > 0:
			spiral[i][j] += spiral[i+1][j-1]
		if j < size - 1:
			spiral[i][j] += spiral[i+1][j+1]
	if j > 0:
		spiral[i][j] += spiral[i][j-1]
	if j < size - 1:
		spiral[i][j] += spiral[i][j+1]

i, j = 2, 2
while True:
	new_shell(spiral)
	while i > 0:
		i -= 1
		fill_cell(spiral, i, j)
		if spiral[i][j] > req:
			print(spiral[i][j])
			exit()
	while j > 0:
		j -= 1
		fill_cell(spiral, i, j)
		if spiral[i][j] > req:
			print(spiral[i][j])
			exit()
	while i < len(spiral) - 1:
		i += 1
		fill_cell(spiral, i, j)
		if spiral[i][j] > req:
			print(spiral[i][j])
			exit()
	while j < len(spiral) - 1:
		j += 1
		fill_cell(spiral, i, j)
		if spiral[i][j] > req:
			print(spiral[i][j])
			exit()
	i += 2
	j += 2


print(spiral)
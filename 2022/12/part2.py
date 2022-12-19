import networkx as nx
import numpy as np

from itertools import product

input = open('input.txt', 'r').read().strip()

grid = np.array([[ord(c) for c in l] for l in input.splitlines()])
start = tuple(np.argwhere(grid == ord('S'))[0])
goal = tuple(np.argwhere(grid == ord('E'))[0])

grid[start] = ord('a')
grid[goal] = ord('z')

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

graph = nx.DiGraph()

for i, j in product(range(grid.shape[0]), range(grid.shape[1])):
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if not (0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]):
            continue
        if grid[ni, nj] - grid[i, j] <= 1:
            graph.add_edge((i, j), (ni, nj))

starts = np.argwhere(grid == ord('a'))
minimum = np.inf
for start in starts:
    try:
        minimum = min(minimum, nx.shortest_path_length(graph, tuple(start), goal))
    except:
        ...

print(f"Result: {minimum}")
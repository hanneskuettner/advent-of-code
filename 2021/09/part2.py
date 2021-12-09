import math
import numpy as np

height_map = np.genfromtxt("input.txt", dtype=int, delimiter=1)
visited = height_map == 9

basins = []
while not np.all(visited):
    remaining = [np.argwhere(visited == False)[0]]
    basin_size = 0
    while remaining:
        i, j = remaining.pop()
        if visited[i, j]:
            continue
        visited[i, j] = True
        basin_size += 1
        if i > 0 and not visited[i - 1, j]:
            remaining.append((i - 1, j))
        if j > 0 and not visited[i, j - 1]:
            remaining.append((i, j - 1))
        if i < height_map.shape[0] - 1 and not visited[i + 1, j]:
            remaining.append((i + 1, j))
        if j < height_map.shape[1] - 1 and not visited[i, j + 1]:
            remaining.append((i, j + 1))

    basins.append(basin_size)


basins = sorted(basins, reverse=True)
result = math.prod(basins[:3])
print("Result: {}".format(result))

import numpy as np

cubes = np.loadtxt('input.txt', dtype=int, delimiter=',')

grid = np.zeros(cubes.max(axis=0) + 2, dtype=int)
sides = np.vstack([np.eye(3, dtype=int), -np.eye(3, dtype=int)])

for cube in cubes:
    grid[tuple(cube)] = 1

area = 0
for cube in cubes:
    # check all sides
    for side in sides:
        area += 1 - grid[tuple(cube + side)]

result = area
print(f"Result: {result}")
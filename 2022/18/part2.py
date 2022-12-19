import numpy as np

cubes = np.loadtxt('input.txt', dtype=int, delimiter=',')

grid = np.zeros(cubes.max(axis=0) + 2, dtype=int)
sides = np.vstack([np.eye(3, dtype=int), -np.eye(3, dtype=int)])

for cube in cubes:
    grid[tuple(cube)] = 1

# flood outside of cubes
queue = [np.zeros(3, dtype=int)]
grid[0,0,0] = 2
while queue:
    v = queue.pop(0)
    for side in sides:
        u = v + side
        if grid[tuple(u)] == 0:
            grid[tuple(u)] = 2
            queue.append(u)

area = 0
for cube in cubes:
    # check all sides
    for side in sides:
        if grid[tuple(cube + side)] == 2:
            area += 1 

result = area
print(f"Result: {result}")
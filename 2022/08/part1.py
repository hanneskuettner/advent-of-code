import numpy as np

input = open('input.txt', 'r').read().strip()

grid = np.array([[int(d) for d in l] for l in input.splitlines()])

visible = np.zeros_like(grid, dtype=bool)
visible[:,0] = 1
visible[:,-1] = 1
visible[0,:] = 1
visible[-1,:] = 1

for i in range(1, grid.shape[0] - 1):
    for j in range(1, grid.shape[1] - 1):
        height = grid[i, j]
        visible[i,j] = (
            np.all(grid[i, :j] < height) or 
            np.all(grid[i, j+1:] < height) or 
            np.all(grid[:i, j] < height) or 
            np.all(grid[i+1:, j] < height))

print(visible)

result = np.count_nonzero(visible)
print(f"Result: {result}")
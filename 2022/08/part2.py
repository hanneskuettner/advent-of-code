import numpy as np

input = open('input.txt', 'r').read().strip()

grid = np.array([[int(d) for d in l] for l in input.splitlines()])

score = np.zeros_like(grid, dtype=int)

for i in range(1, grid.shape[0] - 1):
    for j in range(1, grid.shape[1] - 1):
        height = grid[i, j]
        score[i,j] = 1
        directions = [grid[i, :j][::-1], grid[i, j+1:], grid[:i, j][::-1], grid[i+1:, j]]
        for d in directions:
            if np.all(d < height):
                score[i,j] *= len(d)
            else:
                score[i,j] *= np.argmax(d >= height) + 1
        

result = np.max(score)
print(f"Result: {result}")
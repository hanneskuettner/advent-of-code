import numpy as np

height_map = np.genfromtxt("input.txt", dtype=int, delimiter=1)

mins = []
for i in range(height_map.shape[0]):
    for j in range(height_map.shape[1]):
        if i > 0 and height_map[i - 1, j] <= height_map[i, j]:
          continue
        if j > 0 and height_map[i, j - 1] <= height_map[i, j]:
          continue
        if i < height_map.shape[0] - 1 and height_map[i + 1, j] <= height_map[i, j]:
          continue
        if j < height_map.shape[1] - 1 and height_map[i, j+1] <= height_map[i,j]:
          continue
        mins.append(height_map[i, j])


result = sum(mins) + len(mins)
print("Result: {}".format(result))

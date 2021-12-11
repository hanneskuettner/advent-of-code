import numpy as np

octopi = np.genfromtxt("input.txt", dtype=int, delimiter=1)

flash_count = 0
for _ in range(100):
  octopi += 1
  flashed = np.zeros_like(octopi, dtype=bool)
  while (next_flashers := np.argwhere((octopi > 9) & (flashed == False))).size > 0:
    for x, y in next_flashers:
      flashed[x, y] = True
      flash_count += 1
      x_min, x_max = max(0, x - 1), min(x + 1, 9)
      y_min, y_max = max(0, y - 1), min(y + 1, 9)
      octopi[x_min:x_max + 1, y_min:y_max+1] += 1
  octopi[octopi > 9] = 0
      

result = flash_count
print("Result: {}".format(result))

import numpy as np
from scipy.ndimage import convolve

STEPS = 50
input = open('input.txt', 'r').read().strip().splitlines()

lookup = np.array([int(c == "#") for c in input[0]])

margin = STEPS + 1
image = np.pad([[int(c == "#") for c in l] for l in input[2:]], (margin, margin))

bin2dec = 2**np.arange(9).reshape(3,3)

for _ in range(STEPS):
  image = lookup[convolve(image, bin2dec)]

result = int(np.sum(image))
print("Result: {}".format(result))

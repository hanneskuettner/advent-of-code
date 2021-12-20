import numpy as np

def to_int(a):
  out = 0
  for i, d in enumerate(reversed(a)):
    if d:
      out |= (1 << i)
  return out


input = open('input.txt', 'r').read().strip().splitlines()

lookup = np.array([c == "#" for c in input[0]], dtype=bool)

STEPS = 2

size = len(input[2])
margin = STEPS + 1
image = np.zeros((size + margin * 2, size + margin * 2))
image[margin:-margin, margin:-margin] = np.array([[c == "#" for c in l] for l in input[2:]], dtype=bool)


inf_values = False
for _ in range(STEPS):
  inf_values = lookup[to_int([inf_values] * 9)]
  new_image = np.zeros_like(image)
  
  for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
      index = to_int(image[i-1:i+2, j-1:j+2].flatten())
      new_image[i, j] = lookup[index]
      
  new_image[0, :] = inf_values
  new_image[-1, :] = inf_values
  new_image[:, 0] = inf_values
  new_image[:, -1] = inf_values
  image = new_image

result = int(np.sum(image))
print("Result: {}".format(result))

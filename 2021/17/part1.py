import numpy as np


def hits_target(v, target):
    p = np.zeros(2)
    x1, x2, y1, y2 = target
    highest_y = 0
    while p[0] < x2 and p[1] > y1:
        p += v
        if v[0] > 0:
            v[0] -= 1
        elif v[0] < 0:
            v[0] += 1
        v[1] -= 1
        
        highest_y = max(p[1], highest_y)

        if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            return True, highest_y
    return False, None


input = open("input.txt", "r").read().strip()
target = np.array([int(p) for v in input[13:].split(",") for p in v.strip()[2:].split("..")])


max_y = 0
for vx in range(1, 50):
  for vy in range(0, 100):
    hit, y = hits_target(np.array([vx, vy]), target)
    if hit:
      max_y = max(max_y, y)


result = int(max_y)
print("Result: {}".format(result))

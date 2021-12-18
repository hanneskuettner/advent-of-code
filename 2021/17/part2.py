import numpy as np


def hits_target(v, target):
    p = np.zeros(2)
    x1, x2, y1, y2 = target
    while p[0] <= x2 and p[1] >= y1:
        p += v
        v[0] -= 1 if v[0] else 0
        v[1] -= 1

        if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            return True
    return False


input = open("input.txt", "r").read().strip()
target = np.array([int(p) for v in input[13:].split(",") for p in v.strip()[2:].split("..")])


count = 0
for vx in range(1, target[1] + 1):
  print(vx)
  for vy in range(target[2], 200):
    count += hits_target(np.array([vx, vy]), target)


result = count
print("Result: {}".format(result))

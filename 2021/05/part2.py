from collections import defaultdict


input = open('input.txt', 'r').read().strip().splitlines()

def parse_coords(line):
  c1, c2 = [p.split(",") for p in line.split("->")]
  return (int(c1[0]), int(c1[1])) , (int(c2[0]), int(c2[1]))

line_coords = [parse_coords(line) for line in input]

counter = defaultdict(int)

for (x1, y1), (x2, y2)  in line_coords:
  if y1 == y2:
    # horizontal
    for x in range(min(x1, x2), max(x1, x2) + 1):
      counter[(x, y1)] += 1
  elif x1 == x2:
    # vertical
    for y in range(min(y1, y2), max(y1, y2) + 1):
      counter[(x1, y)] += 1
  else:
    # diagonal
    dist = abs(x1 - x2)
    d_x, d_y = (x2 - x1) // dist, (y2 - y1) // dist
    for i in range(dist + 1):
      counter[(x1 + d_x * i, y1 + d_y * i)] += 1

result = sum(c >= 2 for c in counter.values())
print("Result: {}".format(result))

input = open('input.txt', 'r').read().strip()

pos = 0
depth = 0

for cmd, distance in [l.split() for l in input.splitlines()]:
  distance = int(distance)
  if cmd == "forward":
    pos += distance
  elif cmd == "up":
    depth -= distance
  elif cmd == "down":
    depth += distance

result = pos * depth
print("Result: {}".format(result))

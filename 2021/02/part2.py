input = open('input.txt', 'r').read().strip()

pos = 0
depth = 0
aim = 0

for cmd, distance in [l.split() for l in input.splitlines()]:
  distance = int(distance)
  if cmd == "forward":
    pos += distance
    depth += aim * distance
  elif cmd == "up":
    aim -= distance
  elif cmd == "down":
    aim += distance

result = pos * depth
print("Result: {}".format(result))

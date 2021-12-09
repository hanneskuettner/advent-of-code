input = open('input.txt', 'r').read().strip()

fish = [int(f) for f in input.split(',')]
for d in range(80):
  new_fish = []
  for i, f in enumerate(fish):
    if f == 0 :
      new_fish.append(8)
      fish[i] = 6
    else:
      fish[i] = f - 1
  fish.extend(new_fish)

result = len(fish)
print("Result: {}".format(result))

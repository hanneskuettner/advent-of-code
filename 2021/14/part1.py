from collections import Counter


input = open('input.txt', 'r').read().strip().splitlines()

polymer = input[0]

replacements = dict(l.split(" -> ") for l in input[2:])

for _ in range(10):
  new_polymer = ""
  for c1, c2 in zip(polymer, polymer[1:]):
    if c1 + c2 in replacements:
      new_polymer += c1 + replacements[c1 + c2]
    else:
      new_polymer += c1
  polymer = new_polymer + polymer[-1]

counts = Counter(polymer)
result = max(counts.values()) - min(counts.values())
print("Result: {}".format(result))

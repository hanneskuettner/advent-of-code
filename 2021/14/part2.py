from collections import Counter, defaultdict


input = open('input.txt', 'r').read().strip().splitlines()

polymer = input[0]

replacements = dict()
for l in input[2:]:
  k, r = l.split(" -> ")
  replacements[tuple(k)] = r

pairs = Counter(zip(polymer, polymer[1:]))

for _ in range(40):
  new_counts = defaultdict(int)
  for p, count in pairs.items():
    if p in replacements:
      new_counts[(p[0], replacements[p])] += count
      new_counts[(replacements[p], p[1])] += count
    else:
      new_counts[p] += count
  pairs = new_counts

letter_count = defaultdict(int)
for (_, b), count in pairs.items():
  letter_count[b] += count

letter_count[polymer[0]] += 1

result = max(letter_count.values()) - min(letter_count.values())
print("Result: {}".format(result))

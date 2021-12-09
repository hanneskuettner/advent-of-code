input = open('input.txt', 'r').read().strip()

crabs = [int(c) for c in input.split(',')]

costs = []
for p in range(max(crabs)):
  costs.append(sum(abs(p - c) for c in crabs))

result = min(costs)
print("Result: {}".format(result))

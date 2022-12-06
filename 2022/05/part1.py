input = open('input.txt', 'r').read().strip()

stacks, moves = [p.splitlines() for p in input.split('\n\n')]

num_stacks = len(stacks[-1]) // 4 + 1
stacks = [[row[idx * 4 + 1] for row in stacks[:-1] if row[idx * 4 + 1] != ' '][::-1] for idx in range(num_stacks)]

moves = [[int(d) for d in row.split()[1::2]] for row in moves]

# simulate
for (count, _from, to) in moves:
  stacks[to - 1].extend(stacks[_from - 1][-count:][::-1])
  del stacks[_from - 1][-count:]
  
result = ''.join([s[-1] for s in stacks])
print(f"Result: {result}")

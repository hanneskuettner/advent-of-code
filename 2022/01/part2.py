input = open('input.txt', 'r').read().strip()

result = sum(sorted([sum((int(n) for n in g.splitlines())) for g in input.split('\n\n')])[-3:])

print("Result: {}".format(result))

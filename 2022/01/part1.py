input = open('input.txt', 'r').read().strip()

result = max([sum((int(n) for n in g.splitlines())) for g in input.split('\n\n')])

print("Result: {}".format(result))

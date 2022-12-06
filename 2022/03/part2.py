input = open('input.txt', 'r').read().strip()

x = iter(set(l) for l in input.splitlines())
non_uniques = [tuple(e1 & e2 & e3)[0] for e1, e2, e3 in zip(*[x, x, x])]

result = sum(ord(l) - (ord('A') - 26 if l <= 'Z' else ord('a')) + 1 for l in non_uniques)
print("Result: {}".format(result))

input = open('input.txt', 'r').read().strip()

assignments = [[tuple(map(int, s.split('-'))) for s in p] for p in [l.split(',') for l in input.splitlines()]]
# sort with earliest (and longest if they start from the same number) assignment first
earliest_first = [sorted(a, key=lambda a: a[0] * 1000 - a[1] - a[0]) for a in assignments]

fully_contains = [early[0] <= late[0] and early[1] >= late[1] for early, late in earliest_first]

result = sum(fully_contains)
print("Result: {}".format(result))

input = open('input.txt', 'r').read().strip()

assignments = [[tuple(map(int, s.split('-'))) for s in p] for p in [l.split(',') for l in input.splitlines()]]
# sort with earliest (and longest if they start from the same number) assignment first
earliest_first = [sorted(a, key=lambda a: a[0] * 1000 - a[1] - a[0]) for a in assignments]

overlaps = [early[1] >= late[0] or early[0] >= late[1] for early, late in earliest_first]

result = sum(overlaps)
print("Result: {}".format(result))

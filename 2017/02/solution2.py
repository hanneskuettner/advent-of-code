import itertools

rows = [[int(v) for v in l.split()] for l in open('input.txt').readlines()]

print(sum([[v1 // v2 for v1, v2 in itertools.product(r, r) if v1 != v2 and v1 % v2 == 0][0] for r in rows]))
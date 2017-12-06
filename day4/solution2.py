import itertools

print(sum(all(w1 != w2 and sorted(w1) != sorted(w2) for w1, w2 in itertools.permutations(l, 2)) for l in [l.split() for l in open('input.txt').readlines()]))
input = open('input.txt', 'r').read().strip()

non_uniques = [tuple(p1 & p2)[0]for p1, p2 in [(set(l[:len(l)//2]), set(l[len(l)//2:])) for l in input.splitlines()]]

result = sum(ord(l) - (ord('A') - 26 if l <= 'Z' else ord('a')) + 1 for l in non_uniques)
print("Result: {}".format(result))

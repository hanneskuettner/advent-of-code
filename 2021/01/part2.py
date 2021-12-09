input = open('input.txt', 'r').read().strip()

measurements = [int(l) for l in input.splitlines()]

result = sum(m2 > m1 for m1, m2 in zip(measurements, measurements[3:]))
print("Result: {}".format(result))

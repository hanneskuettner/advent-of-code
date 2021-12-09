input = open("input.txt", "r").read().strip()

pop = [0] * 9
for f in (int(f) for f in input.split(",")):
    pop[f] += 1

for d in range(256):
    p0 = pop[0]
    pop[:] = *pop[1:], p0
    pop[6] += p0

result = sum(pop)
print(result)

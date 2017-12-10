
memory = [int(e) for e in open('input.txt').read().split()]

it = 0
hist = set()
while True:
	curr = memory.index(max(memory))
	d, memory[curr] = memory[curr], 0
	while d:
		curr = (curr + 1) % len(memory)
		memory[curr] += 1
		d -= 1
	it += 1
	s = ''.join(str(e) for e in memory)
	if s not in hist:
		hist.add(s)
	else:
		break

print(it)
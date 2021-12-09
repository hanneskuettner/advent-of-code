memory = [int(e) for e in open('input.txt').read().split()]

it = 0
hist = set()
state = ''
while True:
	curr = memory.index(max(memory))
	d, memory[curr] = memory[curr], 0
	while d:
		curr = (curr + 1) % len(memory)
		memory[curr] += 1
		d -= 1
	s = ''.join(str(e) for e in memory)
	if not state and s not in hist:
		hist.add(s)
	elif not state:
		state = s
	else:
		it += 1
		if s == state:
			break


print(it)
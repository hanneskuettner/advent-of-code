moves = open('input.txt').read().split(',')
dancers = [chr(c) for c in range(ord('a'), ord('p')+1)]
in_order = [chr(c) for c in range(ord('a'), ord('p')+1)]

def dance(dancers, moves):
	dancers = dancers[:]
	for move in moves:
		if move[0] == 's':
			pos = int(move[1:])
			dancers = dancers[-pos:] + dancers[:len(dancers)-pos]
		elif move[0] == 'x':
			pos1, pos2 = [int(p) for p in move[1:].split('/')]
			dancers[pos1], dancers[pos2] = dancers[pos2], dancers[pos1]
		elif move[0] == 'p':
			pos1, pos2 = [dancers.index(p) for p in move[1:].split('/')]
			dancers[pos1], dancers[pos2] = dancers[pos2], dancers[pos1]

	return dancers

print(''.join(dance(dancers, moves)))

for i in range(1_000_000_000):
	dancers = dance(dancers, moves)
	if dancers == in_order:
		break

rest = 1_000_000_000 % (i+1)

for i in range(rest):
	dancers = dance(dancers, moves)

print(''.join(dancers))
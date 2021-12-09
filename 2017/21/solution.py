import numpy as np

def flatten_pattern(p):
	return '/'.join(''.join(l) for l in p)

def all_rotations(d, m, r):
	d[flatten_pattern(m)] = r
	d[flatten_pattern(np.rot90(m, 1))] = r
	d[flatten_pattern(np.rot90(m, 2))] = r
	d[flatten_pattern(np.rot90(m, 3))] = r

def preprocess_instructions(instr):
	new_instr = {}
	for i, r in instr:
		i = np.array([np.array(list(p)) for p in i.strip().split('/')])
		r = np.array([np.array(list(p)) for p in r.strip().split('/')])
		all_rotations(new_instr, i, r)
		all_rotations(new_instr, np.flip(i, 0), r)
		all_rotations(new_instr, np.flip(i, 1), r)
		all_rotations(new_instr, np.flip(np.flip(i, 1), 0), r)

	return new_instr

image = np.array([np.array(list(l)) for l in [".#.", "..#", "###"]])

instructions = [l.split(' => ') for l in open('input.txt').readlines()]
instructions = preprocess_instructions(instructions)

for k in range(18):
	size = image.shape[0]
	if size % 2 == 0:
		image = np.concatenate([np.concatenate([instructions[flatten_pattern(image[i:i+2,j:j+2])] for j in range(0, size, 2)], axis=1) for i in range(0, size, 2)], axis=0)
	elif size % 3 == 0:
		image = np.concatenate([np.concatenate([instructions[flatten_pattern(image[i:i+3,j:j+3])] for j in range(0, size, 3)], axis=1) for i in range(0, size, 3)], axis=0)
	if k == 4 or k == 17:
		print(sum(sum(1 for j in range(image.shape[0]) if image[i,j] == '#') for i in range(image.shape[0])))

DIRS = ['n', 'ne', 'se', 's', 'sw', 'nw']

def are_opposite(d1, d2):
	return d1 and d2 and abs(DIRS.index(d1) - DIRS.index(d2)) == 3

def are_reducable(d1, d2):
	return d1 and d2 and (DIRS[(DIRS.index(d1) + 2) % 6] == d2 or DIRS[DIRS.index(d1) - 2] == d2)

def middle(d1, d2):
	if DIRS[(DIRS.index(d1) + 2) % 6] == d2:
		return DIRS[(DIRS.index(d1) + 1) % 6]
	elif DIRS[DIRS.index(d1) - 2] == d2:
		return DIRS[DIRS.index(d1) - 1]

steps = open('input.txt').read().rstrip().split(',')
step_stack = ['']
total = 0
m = 0
for step in steps:
	if are_opposite(step_stack[-1], step):
		# steps cancel each other out
		step_stack.pop()
		total -= 1
		continue
	# search step stack for reducable combinations
	i = len(step_stack) - 1
	while i:
		if are_reducable(step_stack[i], step):
			# steps are reducable to their middle and use this as our new step
			step = middle(step_stack.pop(i), step)
			total -= 1
			i = len(step_stack)
		i -= 1
	# append to stack and increase number of steps
	step_stack.append(step)
	total += 1
	m = max([m, total])

print(total)
print(m)
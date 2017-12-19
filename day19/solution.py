grid = open("input.txt").readlines()

def find_turn(x, y, d):
	try:
		if grid[y+d[0]][x+d[1]] != ' ':
			return x+d[1], y+d[0], d[::-1]
	except IndexError:
		pass
	if y-d[0] > 0 and x-d[0] > 0 and grid[y-d[0]][x-d[1]] != ' ':
		return x-d[1], y-d[0], [-d[1], -d[0]]
	return None, None, None

PATH_SYMBOLS = ['|', '-', '+']
x = grid[0].index('|')
y = 0
d = [0, 1]
letter_path = []
steps = 0
while True:
	curr_symbol = grid[y][x]
	if curr_symbol not in PATH_SYMBOLS:
		if curr_symbol == ' ':
			break
		letter_path.append(curr_symbol)
	steps += 1
	if curr_symbol == '+':
		x, y, d = find_turn(x, y, d)
		if x == None:
			break
	else:
		x += d[0]
		y += d[1]
	if  x < 0 or y < 0:
		break

print(''.join(letter_path), steps)
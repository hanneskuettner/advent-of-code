
def parse_group(rest, level):
	idx = 0
	score = level
	in_gb = False
	gc = 0
	while True:
		if not in_gb:
			if rest[idx] == '{':
				s, g, rest = parse_group(rest[idx+1:], level + 1)
				idx = 0
				score += s
				gc += g
			elif rest[idx] == '}':
				return score, gc, rest[idx:]
			elif rest[idx] == '<':
				in_gb = True
			elif rest[idx] == '!':
				idx += 1
		else:
			if rest[idx] == '!':
				idx += 1
			elif rest[idx] == '>':
				in_gb = False
			else:
				gc += 1
		idx += 1


string = str(open('input.txt').read())

print(parse_group(string[1:], 1)[:2])

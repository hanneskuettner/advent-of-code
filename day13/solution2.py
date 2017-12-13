meta = dict([(int(s.split(':')[0]), int(s.split(':')[1])) for s in open('input.txt').readlines()])

delay = 0
while True:
	coll = False
	for i in range(max(meta.keys())+1):
		if i in meta:
			pos = (delay + i) % ((meta[i] - 1) * 2)
			if pos == 0:
				coll = True
				break
	if not coll:
		break
	delay += 1


print(delay)
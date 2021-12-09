meta = dict([(int(s.split(':')[0]), int(s.split(':')[1])) for s in open('input.txt').readlines()])

collisions = []
for i in range(max(meta.keys())+1):
	if i in meta:
		pos = i % ((meta[i] - 1) * 2)
		if pos == 0:
			collisions.append(i)

print(sum(meta[i] * i for i in collisions))
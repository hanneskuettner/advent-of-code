steps = 344

buf = [0]
curr = 0
for i in range(1, 2018):
	curr = (curr + steps) % len(buf) + 1
	buf.insert(curr, i)
	curr %= len(buf)

print(buf[buf.index(2017) + 1])
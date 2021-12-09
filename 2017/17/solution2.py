steps = 344

after_zero = 0
curr = 0
buf_len = 1
for i in range(1, 50_000_000+1):
	curr = (curr + steps) % buf_len + 1
	if curr == 1:
		after_zero = i
	buf_len += 1

print(after_zero)
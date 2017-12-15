value_a = 699
value_b = 124

count = 0
for i in range(40_000_000):
	value_a = (value_a * 16807) % 2147483647
	value_b = (value_b * 48271) % 2147483647
	count += not ((value_a ^ value_b) & ((1 << 16) - 1))

print(count)
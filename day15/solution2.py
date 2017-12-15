value_a = 699
value_b = 124

amount = 5_000_000
values = [[0] * amount, [0] * amount]
have_values = [0, 0]
while have_values[0] < amount or have_values[1] < amount:
	value_a = (value_a * 16807) % 2147483647
	value_b = (value_b * 48271) % 2147483647
	if value_a % 4 == 0 and have_values[0] < amount:
		values[0][have_values[0]] = value_a
		have_values[0] += 1
	if value_b % 8 == 0 and have_values[1] < amount:
		values[1][have_values[1]] = value_b
		have_values[1] += 1

count = 0
for i in range(amount):
	count += not ((values[0][i] ^ values[1][i]) & ((1 << 16) - 1))

print(count)
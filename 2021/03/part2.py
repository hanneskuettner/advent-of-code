input = open('input.txt', 'r').read().strip()
lines = input.splitlines()


def most_common(numbers, pos):
  ones = sum(num[pos] == "1" for num in numbers)
  zeros = sum(num[pos] == "0" for num in numbers)
  one_most_common = ones > zeros
  zero_most_common = ones < zeros
  equally_common = ones == zeros
  
  return one_most_common, zero_most_common, equally_common

NUMBER_BITS = len(lines[0])
gamma = 0
oxy_numbers = lines[:]
co_numbers = lines[:]
for pos in range(NUMBER_BITS):
  if len(oxy_numbers) > 1:
    ones, zeros, eq = most_common(oxy_numbers, pos)
    oxy_numbers = [n for n in oxy_numbers if ones and n[pos] == "1" or zeros and n[pos] == "0" or eq and n[pos] == "1"]
  if len(co_numbers) > 1:
    ones, zeros, eq = most_common(co_numbers, pos)
    co_numbers = [n for n in co_numbers if ones and n[pos] == "0" or zeros and n[pos] == "1" or eq and  n[pos] == "0"]


oxy = int(oxy_numbers[0], 2)
co = int(co_numbers[0], 2)

result = oxy * co
print("Result: {}".format(result))

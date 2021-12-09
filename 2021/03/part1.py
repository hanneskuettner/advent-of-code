input = open('input.txt', 'r').read().strip()
lines = input.splitlines()


NUMBER_BITS = 12
gamma = 0
for pos in range(NUMBER_BITS):
  ones = sum(line[pos] == "1" for line in lines)
  gamma |= (ones > len(lines) / 2) << (NUMBER_BITS - pos - 1)


epsilon = gamma ^ 2 ** NUMBER_BITS - 1    

result = gamma * epsilon
print("Result: {}".format(result))

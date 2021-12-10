input = open('input.txt', 'r').read().strip()

mirror = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

scores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

score = 0
for line in input.splitlines():
  stack = []
  for c in line:
    if c in mirror:
      stack.append(c)
    else:
      if c != mirror[stack.pop(-1)]:
        score += scores[c]

result = score
print("Result: {}".format(result))

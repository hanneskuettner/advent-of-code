input = open('input.txt', 'r').read().strip()

mirror = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

scores = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

lines = input.splitlines()
close_scores = []
for line in lines:
  stack = []
  for c in line:
    if c in mirror:
      stack.append(c)
    elif c != mirror[stack.pop(-1)]:
        # corrupted 
        break
  else:
    close_score = 0
    for c in reversed(stack):
      close_score = 5 * close_score + scores[mirror[c]]
    close_scores.append(close_score)
        

result = sorted(close_scores)[len(close_scores) // 2]
print("Result: {}".format(result))

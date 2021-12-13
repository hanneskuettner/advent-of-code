import numpy as np

input = open('input.txt', 'r').read().strip()

folding_instructions = []
for l in input.splitlines():
  if l.startswith("f"):
    p = int(l.split("=")[1])
    if "x" in l:
      folding_instructions.append((p, 0))
    elif "y" in l:
      folding_instructions.append((0, p))

dots = np.genfromtxt("input.txt", delimiter=",", skip_footer=len(folding_instructions), dtype=int)

max_x, max_y = folding_instructions[0][0] * 2, folding_instructions[1][1] * 2
paper = np.zeros((max_y + 1, max_x + 1), dtype=bool)
for x, y in dots:
  paper[y, x] = True
  
for x_fold, y_fold in folding_instructions[:1]:
  if x_fold:
    paper = paper[:, :x_fold] | np.fliplr(paper[:, x_fold+1:])
  elif y_fold:
    paper = paper[:y_fold, :] | np.flipud(paper[y_fold+1:, :])
    

result = np.sum(paper)
print("Result: {}".format(result))

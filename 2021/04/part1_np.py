from io import StringIO
import numpy as np

lines = open('input.txt', 'r').read().strip().splitlines()

draws = [int(d) for d in lines[0].split(",")]
board_string = StringIO('\n'.join([l for l in lines[1:] if l]))
boards = np.genfromtxt(board_string, dtype=int).reshape((-1, 5, 5))
markers = np.zeros_like(boards, dtype=bool)

for draw in draws:
  markers[boards == draw] = True
  for markers, idx in boards:
    if np.all()
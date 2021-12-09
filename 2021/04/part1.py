import itertools
from collections import defaultdict

lines = open('input.txt', 'r').read().strip().splitlines()

draws = lines[0].split(",")

boards = []
lookup = defaultdict(list)
markers = []
for i in range(1, len(lines), 6):
  board = [l.split() for l in lines[i+1:i+6]]
  boards.append(board)
  markers.append([r[:] for r in [[False] * 5] * 5])
  for j, k in itertools.product(range(5), repeat=2):
    lookup[board[j][k]].append((i / 6, j, k))


winner = None
for number in draws:
  boards_with_number = lookup[number]
  for board_idx, i, j in boards_with_number:
    markers[board_idx][i][j] = True
    if all(markers[board_idx][i]) or all(m[j] for m in markers[board_idx]):
      winner = board_idx
      break
  else:
    continue
  break

sum_unmarked = sum(int(boards[winner][i][j]) for i, j in itertools.product(range(5), repeat=2) if not markers[winner][i][j])

result = sum_unmarked * int(number)
print("Result: {}".format(result))

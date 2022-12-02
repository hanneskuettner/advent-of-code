input = open('input.txt', 'r').read().strip()

def score_game(ta, tb):
  tb = chr(ord(tb) - (ord('X') - ord('A')))
  if ta == 'A' and tb == 'C': return 0
  elif ta == 'C' and tb == 'A': return 6
  elif ta > tb: return 0
  elif ta < tb: return 6
  else: return 3
  
def score_own_throw(t):
  return ord(t) - ord('X') + 1

rounds = [tuple(l.split()) for l in input.splitlines()]
scores = [score_game(ta, tb) + score_own_throw(tb) for ta, tb in rounds]

result = sum(scores)
print("Result: {}".format(result))

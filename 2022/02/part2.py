input = open('input.txt', 'r').read().strip()

def get_own_throw(ta, result):
  if result == 'X':
    return chr(((ord(ta) - 1) - 65) % 3 + 65)
  elif result == 'Y':
    return ta
  else:
    return chr(((ord(ta) + 1) - 65) % 3 + 65)

def score_game(ta, tb):
  if ta == 'A' and tb == 'C': return 0
  elif ta == 'C' and tb == 'A': return 6
  elif ta > tb: return 0
  elif ta < tb: return 6
  else: return 3
  
def score_own_throw(t):
  return ord(t) - ord('A') + 1

rounds = [tuple(l.split()) for l in input.splitlines()]
print(get_own_throw(*rounds[0]))
scores = [score_game(ta, get_own_throw(ta, r)) + score_own_throw(get_own_throw(ta, r)) for ta, r in rounds]

result = sum(scores)
print("Result: {}".format(result))

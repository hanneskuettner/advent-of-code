from itertools import zip_longest
from enum import Enum
from functools import cmp_to_key

input = open('input.txt', 'r').read().strip()

class Decision(Enum):
    UNDECIDED = 0
    CORRECT = -1
    INCORRECT = 1

pairs = [eval(l)  for b in input.split('\n\n') for l in b.splitlines()]

divider1 = [[2]]
divider2 = [[6]]
pairs.append(divider1)
pairs.append(divider2)


def compare(left, right):
    for li, ri in zip_longest(left, right):
        if li == None:
            return Decision.CORRECT
        elif ri == None:
            return Decision.INCORRECT
        elif type(li) == int and type(ri) == int:
            if li < ri:
                return Decision.CORRECT
            elif li > ri:
                return Decision.INCORRECT
        else:
            if type(li) == int: li = [li]
            if type(ri) == int: ri = [ri]
            sub_decision = compare(li, ri)
            if sub_decision != Decision.UNDECIDED:
                return sub_decision
    return Decision.UNDECIDED
      
pairs = sorted(pairs, key=cmp_to_key(lambda l, r: compare(l, r).value))
result = (pairs.index(divider1) + 1) * (pairs.index(divider2) + 1)
print(f"Result: {result}")
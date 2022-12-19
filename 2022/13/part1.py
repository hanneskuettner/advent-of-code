from itertools import zip_longest
from enum import Enum

input = open('input.txt', 'r').read().strip()

class Decision(Enum):
    UNDECIDED = 0
    CORRECT = 1
    INCORRECT = 2

pairs = [(eval(l1), eval(l2)) for l1, l2 in [b.splitlines() for b in input.split('\n\n')]]



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
        
result = sum(i for i, pair in enumerate(pairs, 1) if compare(*pair) == Decision.CORRECT)
print(f"Result: {result}")
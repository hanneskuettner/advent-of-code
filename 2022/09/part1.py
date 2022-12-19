from collections import defaultdict
import numpy as np

input = open('input.txt', 'r').read().strip()

moves = [(l[0], int(l[2:])) for l in input.splitlines()]

move_directions = {
    'U': np.array([0, -1]),
    'D': np.array([0, 1]),
    'L': np.array([-1, 0]),
    'R': np.array([1, 0])
}

visits = defaultdict(int)

head = np.zeros(2)
tail = np.zeros(2)
for dir, dist in moves:
    for _ in range(dist):
        head += move_directions[dir]
        if np.abs(np.linalg.norm(head - tail)) >= 2:
            tail += np.sign(head - tail) * np.ceil(np.abs(head - tail) / 2)
        visits[tuple(tail)] += 1

result = len(visits.keys())
print(f"Result: {result}")
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
rope = [np.zeros(2) for _ in range(9)]
for dir, dist in moves:
    for _ in range(dist):
        head += move_directions[dir]
        sim_head = head
        for i, part in enumerate(rope):
            v = sim_head - part
            if np.abs(np.linalg.norm(v)) >= 2:
                rope[i] += np.sign(v) * np.ceil(np.abs(v) / 2)
            sim_head = part
        visits[tuple(rope[-1])] += 1

result = len(visits.keys())
print(f"Result: {result}")
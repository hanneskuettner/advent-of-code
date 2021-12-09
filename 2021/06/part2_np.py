import numpy as np
from numpy.core.numeric import full

input = list(map(int, open("input.txt", "r").read().strip().split(",")))


def matrix_power(mat, n):
    e = mat
    n -= 1
    while n > 0:
        print(n)
        if n % 2 == 1:
            mat = np.dot(mat, e)
        e = np.dot(e, e)
        n //= 2
    return mat


growth_matrix = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    dtype=object,
)


population = np.zeros(9, dtype=object)
population[1:6] = np.unique(input, return_counts=True)[1]

GENERATIONS = 2_000_000

g = matrix_power(growth_matrix, GENERATIONS)

print(np.sum(g @ population))

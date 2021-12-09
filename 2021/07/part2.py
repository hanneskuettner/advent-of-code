from functools import lru_cache

input = open("input.txt", "r").read().strip()

crabs = [int(c) for c in input.split(",")]


@lru_cache(None)
def cost(x):
    return sum((abs(x - c) * (abs(x - c) + 1)) // 2 for c in crabs)


low = 0
high = max(crabs)
while low != high:
    mid = low + (high - low) // 2
    curr = cost(mid)
    if cost(mid - 1) < curr:
        high = mid
    elif curr > cost(mid + 1):
        low = mid
    else:
        low = mid
        high = mid

result = cost(low)
print("Result: {}".format(result))

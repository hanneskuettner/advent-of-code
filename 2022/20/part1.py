input = open('input.txt', 'r').read().strip()

numbers = [int(d) for d in input.splitlines()]

def mix(numbers):
    with_indices = [(n, i) for i, n in enumerate(numbers)]
    for i, n in enumerate(numbers):
        idx = with_indices.index((n, i))
        with_indices.pop(idx)
        new_idx = (idx + n) % len(with_indices)
        if new_idx == 0:
            with_indices.append((n, i))
        else:
            with_indices.insert(new_idx, (n, i))
    
    return [n for n, _ in with_indices]

mixed = mix(numbers)
zero_index = mixed.index(0)
result = sum(mixed[(zero_index + offset) % len(mixed)] for offset in [1000, 2000, 3000])
print(f"Result: {result}")
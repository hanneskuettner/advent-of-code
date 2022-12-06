input = open('input.txt', 'r').read().strip()

result = next(idx for idx in range(14, len(input)) if len(set(input[idx-14:idx])) == 14)
print(f"Result: {result}")

input = open('input.txt', 'r').read().strip()

result = next(idx for idx in range(4, len(input)) if len(set(input[idx-4:idx])) == 4)
print(f"Result: {result}")

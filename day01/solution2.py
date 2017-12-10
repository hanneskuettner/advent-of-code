number = str(open('input.txt').read()).rstrip()
step = len(number) // 2
print(sum([int(l) for idx, l in enumerate(number) if l == number[(idx+step) % len(number)]]))
number = str(open('input.txt').read()).rstrip()
print(sum([int(l) for idx, l in enumerate(number) if l == number[(idx+1) % len(number)]]))
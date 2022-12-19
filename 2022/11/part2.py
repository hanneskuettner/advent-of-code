import math

input = open('input.txt', 'r').read().strip()

monkeys = [b.splitlines() for b in input.split('\n\n')]
monkeys = [(
        [int(i) for i in l[1][18:].split(',')],
        l[2].split('=')[1],
        int(l[3].split()[-1]),
        int(l[4].split()[-1]),
        int(l[5].split()[-1])
    ) for l in monkeys] 

divider = math.prod([test for _, _, test, *_ in monkeys], start=1)

inspect_count = [0] * len(monkeys)
for _ in range(10000):
    for monkey, (items, op, test, monkey_true, monkey_false) in enumerate(monkeys):
        while items:
            level = items.pop(0)
            level = eval(op, dict(old=level))
            if level % test == 0:
                monkeys[monkey_true][0].append(level % divider)
            else:
                monkeys[monkey_false][0].append(level)
            inspect_count[monkey] += 1


print(inspect_count)

inspect_count = sorted(inspect_count)
result = inspect_count[-1] * inspect_count[-2]
print(f"Result: {result}")
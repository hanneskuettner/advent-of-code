import numpy as np

instructions = open('input.txt', 'r').read().strip().splitlines()

cycle = 0
x = 1
action_queue = []

crt = np.zeros((6, 40))

def add(v):
    global x
    x += v

while instructions:
    if not action_queue:
        instr = instructions.pop(0)
        match instr.split():
            case ['noop']:
                action_queue.append(None)
            case ['addx', v]:
                action_queue.append(None)
                action_queue.append(lambda: add(int(v)))
    
    row = cycle // 40
    col = cycle % 40
    if col - 1 <= x and x <= col + 1:
        crt[row, col] = 1
    
    action = action_queue.pop(0)
    if action:
        action()
        
    cycle += 1

def print_crt():
    for row in range(6):
        for col in range(40):
            if crt[row, col]:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    

print_crt()
instructions = open('input.txt', 'r').read().strip().splitlines()

signal_strength = 0
x = 1
action_queue = []

def add(v):
    global x
    x += v

for cycle in range(1, 222):
    if not action_queue:
        instr = instructions.pop(0)
        match instr.split():
            case ['noop']:
                action_queue.append(None)
            case ['addx', v]:
                action_queue.append(None)
                action_queue.append(lambda: add(int(v)))
    
    if (cycle - 20) % 40 == 0:
        signal_strength += cycle * x
    
    action = action_queue.pop(0)
    if action:
        action()
    
    

result = signal_strength
print(f"Result: {result}")
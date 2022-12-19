import numpy as np

input = open('input.txt', 'r').read().strip()

board = np.zeros((10000, 7))

# create shapes (but invert y) since we flip the board
shapes = [np.array(l) for l in [
    [[1, 1, 1, 1]],
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [1, 1, 1]][::-1],
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]]
]]

shape_indices = [np.array([(i, j) for j in range(shape.shape[1]) for i in range(shape.shape[0]) if shape[i, j]]) for shape in shapes]

current_max = 0
current_shape = 0
current_jet = 0

# index with (shape_idx, jet_idx, distances to pieces in colum) -> blocks dropped
index = {}
rock_heights = {}

rock_limit = 1000000000000
rock = 1
after_cycle_height = 0
cycle_found = False
while rock <= rock_limit:
    # spawn
    shape = shapes[current_shape]
    col = 2
    row = current_max + 3
    
    indices = np.copy(shape_indices[current_shape])
    indices[:, 0] += row
    indices[:, 1] += col
    
    # calculate "hash" for cycle detection before new rock is placed
    hash = (current_shape, current_jet,) + tuple(board[:row, j][::-1].argmax() for j in range(7))
    
    current_shape = (current_shape + 1) % len(shapes)
    
    while True:
        jet = input[current_jet]
        current_jet = (current_jet + 1) % len(input)
        
        board[tuple(indices.T)] = 0
        
        if jet == '>':
            # move right
            indices[:, 1] += 1
            if np.any(indices[:, 1] >= board.shape[1]) or np.any(board[tuple(indices.T)] == 1):
                # undo move
                indices[:, 1] -= 1
        else:
            # move left
            indices[:, 1] -= 1
            if np.any(indices[:, 1] < 0) or np.any(board[tuple(indices.T)] == 1):
                # undo move
                indices[:, 1] += 1
            
        # try move down (up actually)
        indices[:, 0] -= 1
        
        if np.any(indices[:, 0] < 0) or np.any(board[tuple(indices.T)] == 1):
            # backtrack and place shape
            indices[:, 0] += 1
            board[tuple(indices.T)] = 1
            current_max = max(current_max, np.max(indices[:, 0]) + 1)
            break
        
        board[tuple(indices.T)] = 2
    
    # detect cycle
    if not cycle_found and hash in index:
        # now do the math to figure out the height after the cycle
        old_max, old_rock = index[hash]
        cycle_length = rock - old_rock
        cycle_height = current_max - old_max
        full_repeats = rock_limit // cycle_length
        missing_repeats = rock_limit - (full_repeats - 2) * cycle_length - rock
        
        after_cycle_height =  current_max + (full_repeats - 2) * cycle_height
        missing_height = rock_heights[old_rock + missing_repeats] - old_max
        print(f"Result: {after_cycle_height + missing_height}")
        break
    
    index[hash] = (current_max, rock)
    rock_heights[rock] = current_max
    rock += 1

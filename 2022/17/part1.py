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

def print_board():
    discovered_first = False
    for row in range(1, board.shape[0] + 1):
        if not discovered_first and np.all(board[-row, :] == 0):
            continue
        discovered_first = True
        print('|', end='')
        for col in range(7):
            if board[-row, col] == 1:
                print('#', end='')
            elif board[-row, col] == 2:
                print('@', end='')
            else:
                print('.', end='')
        print('|')
    print('+-------+')

for _ in range(2022):
    # spawn
    shape = shapes[current_shape]
    col = 2
    row = current_max + 3
    
    indices = np.copy(shape_indices[current_shape])
    indices[:, 0] += row
    indices[:, 1] += col
    
    # print(f"shape {_}")
    
    # print(indices)
    
    
    # board[tuple(indices.T)] = 2
    # print_board()
    # board[tuple(indices.T)] = 0
    
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
            # print(current_max)
            break
        
        board[tuple(indices.T)] = 2
        
        # print_board()
        
        
    current_shape = (current_shape + 1) % len(shapes)

result = current_max
print(f"Result: {result}")
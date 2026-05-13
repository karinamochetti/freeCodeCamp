def create_board(dimensions):
    rows = dimensions[0]
    cols = dimensions[1]

    board = []
    for r in range(rows):
        board.append([])
        for c in range(cols):
            board[r].append("X" if (r + c) % 2 == 0 else "O")

    return board

print(create_board([3, 3]))
print(create_board([6, 1]))
print(create_board([2, 10]))
print(create_board([5, 4]))

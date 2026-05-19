def tic_tac_toe(board):

    for i in range(3):
        # check horizontal
        if board[i][0] == board[i][1] == board[i][2]:
            return f"{board[i][0]} wins"
        # check vertical
        if board[0][i] == board[1][i] == board[2][i]:
            return f"{board[0][i]} wins"

    # check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return f"{board[1][1]} wins"
    if board[0][2] == board[1][1] == board[2][0]:
        return f"{board[1][1]} wins"
    
    return "Draw"

print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
print(tic_tac_toe([["O", "O", "X"], ["X", "O", "X"], ["O", "X", "X"]]))
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "O"], ["O", "O", "X"]]))
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))

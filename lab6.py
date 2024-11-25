import math
# Initialize board
board = [[' ' for _ in range(3)] for _ in range(3)]
# Display board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if board is full
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True
# Check for winner
def check_winner(board):
    # Rows, columns, and diagonals
    lines = board + [[board[i][j] for i in range(3)] for j in range(3)] + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    if ['X'] * 3 in lines:
        return 'X'
    elif ['O'] * 3 in lines:
        return 'O'
    return None
# MiniMax function
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1  # AI wins
    elif winner == 'O':
        return -1  # Human wins
    elif is_board_full(board):
        return 0  # Tie

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
# Find best move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
# Main game loop
def play_game():
    while True:
        print_board(board)
        if check_winner(board) or is_board_full(board):
            break

        # Human turn
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Cell already taken, try again.")
            continue

        # Check for winner after human move
        if check_winner(board) or is_board_full(board):
            break

        # AI turn
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'
            print("AI played at:", move)

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")

# Start the game
play_game()

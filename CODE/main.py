import math

# Initialize board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(b[i] == player for i in pos) for pos in win_positions)

# Check draw
def is_draw(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, True)
                b[i] = " "
                best = min(score, best)
        return best

# Find best move for AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print("Positions are 0 to 8\n")

    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except:
            print("Invalid input! Enter number 0-8.")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = "O"
        print("AI chooses:", ai_move)
        print_board()

        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run game
play_game()

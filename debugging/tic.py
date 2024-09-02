#!/usr/bin/python3

def print_board(board):
    """
    Print the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0
    total_moves = 9

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be between 0 and 2. Try again.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                moves += 1
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                elif moves >= total_moves:
                    print_board(board)
                    print("It's a draw!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()


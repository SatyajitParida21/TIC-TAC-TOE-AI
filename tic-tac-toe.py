import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell== player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False





def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):


    if is_winner(board, 'O'):
        return 10 - depth
    
    if is_winner(board, 'X'):
        return depth - 10
    

    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] ='O'

            eval= minimax(board, depth + 1, False, alpha, beta)
            board[r][c]= ' '
            max_eval= max(max_eval, eval)
            alpha= max(alpha, eval)

            if beta <=   alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (r, c) in get_available_moves(board):
            board[r][c]= 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[r][c] =' '
            min_eval= min (min_eval, eval)
            beta= min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val= -math.inf
    move =None
    for (r, c) in get_available_moves(board):
        board[r][c] ='O'
        move_val= minimax(board, 0, False, -math.inf, math.inf)
        board[r][c] =' '
        if move_val > best_val:
            best_val= move_val
            move= (r, c)
    return move

def play_tic_tac_toe():
    board = [[" " for _ in  range(3)] for _ in range(3)]
    while True:
        print_board(board)
        if is_winner(board, 'O'):
            print("Satya You Lose . AI wins!")
            break
        if is_winner(board,  'X'):
            print("Satyajit you won!")
            break
        if is_full(board):
            print(" Neither Ai or Satyajit Win. It's a draw!")
            break

        row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
        if board[row][col] ==" ":
            board[row][col] ='X'
        else:
            print("Invalid move. Try again.")
            continue

        if not is_full(board) and not is_winner (board, 'X'):
            ai_move = best_move(board)
            if ai_move:
                board[ai_move[0]][ai_move[1]]= 'O'

if __name__ == "__main__":
    play_tic_tac_toe()

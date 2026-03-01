def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == "Q":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True

def solve_nq(board, col, n):
    if col >= n:
        print_board(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            res = solve_nq(board, col + 1, n) or res
            board[i][col] = "."
    return res

def n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    if not solve_nq(board, 0, n):
        print("No solution exists")

if __name__ == "__main__":
    n = int(input("Enter value of N: "))
    n_queens(n)
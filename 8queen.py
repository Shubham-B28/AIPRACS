n = 8
board = [[0 for i in range(n)] for j in range(n)]


def printing(board):
    temp = []
    for row in board:
        idx = 0
        print(row)
        for j in row:
            idx += 1
            if j == 1:
                temp.append(idx)
    print()
    print(temp)


def isSafe(row, col):
    if 1 in board[row]:
        return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def eight_queen(col):
    if col == n:
        printing(board)
        return True
    for row in range(n):
        if isSafe(row, col):
            board[row][col] = 1
            if eight_queen(col+1) == False:
                board[row][col] = 0
    return False


eight_queen(0)

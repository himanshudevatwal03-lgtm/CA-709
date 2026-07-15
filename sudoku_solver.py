def solveSudoku(board):

    def isValid(row, col, num):
        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check 3x3 box
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if isValid(i, j, num):
                            board[i][j] = num

                            if backtrack():
                                return True

                            board[i][j] = '.'

                    return False

        return True

    backtrack()


# Example
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(board)

for row in board:
    print(row)

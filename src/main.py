def solve_sudoku(board):
    lenboard = boardtolen(board)
    sizeboard = size(board)
    for i in range(lenboard):
        table = set()
        accu = 0

        for j in range(lenboard):
            if board[i][j] == 0:
                return False

            table.add(board[i][j])
            accu += board[i][j]

        if not (accu == sizeboard and len(table) == lenboard):
            return False

# columns
    for i in range(lenboard):
        table = set()
        accu = 0

        for j in range(lenboard):
            if board[j][i] == 0:
                return False

            table.add(board[j][i])
            accu += board[j][i]

        if not (accu == sizeboard and len(table) == lenboard):
            return False

# sub-squares
    for i in range(0, lenboard, 3):
        for j in range(0, lenboard, 3):
            table = set()
            accu = 0

            for xx in range(3):
                for yy in range(3):
                    x = i + xx
                    y = j + yy

                    if board[x][y] == 0:
                        return False

                    table.add(board[x][y])
                    accu += board[x][y]

            if not (accu == sizeboard and len(table) == lenboard):
                return False

    return True
def size(args):
    accu = 0
    for i in range (args):
        accu+=i
    return accu

def boardtolen(board):
    return len(board)

def validate_sudoku(board):
    if(len(board) not in range(1,9)):
        raise Exception("not 9x9, cell with values not in the range 1~9")
    else :
        solve_sudoku(board)

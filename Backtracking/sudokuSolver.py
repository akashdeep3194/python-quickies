"""
Sudoku Solver
Send Feedback
Given a 9*9 sudoku board, in which some entries are filled and others are 0 (0 indicates that the cell is empty),
you need to find out whether the Sudoku puzzle can be solved or not i.e. return true or false.
Input Format :
9 Lines where ith line contains ith row elements separated by space
Output Format :
 true or false
Sample Input :
9 0 0 0 2 0 7 5 0
6 0 0 0 5 0 0 4 0
0 2 0 4 0 0 0 1 0
2 0 8 0 0 0 0 0 0
0 7 0 5 0 9 0 6 0
0 0 0 0 0 0 4 0 1
0 1 0 0 0 5 0 8 0
0 9 0 0 7 0 0 0 4
0 8 2 0 4 0 0 0 6
Sample Output :
true
"""
import print_pretty_array


def canBePlacedHere(x, y, num, dp_cell, dp_row, dp_col):
    cell_xs = (x // 3)
    cell_ys = (y // 3)
    cell_index = 3 * cell_xs + cell_ys

    cell_list = dp_cell[cell_index]

    if cell_list.get(num, 0) != 0:
        return False
    if dp_row[x].get(num, 0) != 0:
        return False
    if dp_col[y].get(num, 0) != 0:
        return False
    return True


def SudokuSolver(board, dp_row, dp_col, dp_cell, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            else:
                for k in range(1, n + 1):
                    if canBePlacedHere(i, j, k, dp_cell, dp_row, dp_col):
                        cell = 3 * (i // 3) + (j // 3)
                        board[i][j] = k
                        dp_cell[cell][k] = 1
                        dp_row[i][k] = 1
                        dp_col[j][k] = 1
                        if SudokuSolver(board, dp_row, dp_col, dp_cell, n):
                            return True
                        else:
                            board[i][j] = 0
                            dp_cell[cell][k] = 0
                            dp_row[i][k] = 0
                            dp_col[j][k] = 0
                return False
    else:
        return True

    pass


def solveSudoku(board):
    n = len(board[0])

    dp_cell = [dict() for i in range(n)]
    dp_row = [dict() for i in range(n)]
    dp_col = [dict() for i in range(n)]

    for cell in range(0, n):
        rs = 3 * (cell // 3)
        cs = 3 * (cell % 3)
        re = rs + 2
        ce = cs + 2
        for r in range(rs, re + 1):
            for c in range(cs, ce + 1):
                if board[r][c] == 0:
                    continue
                dp_cell[cell][board[r][c]] = 1
                dp_row[r][board[r][c]] = 1
                dp_col[c][board[r][c]] = 1
    solvable = SudokuSolver(board, dp_row, dp_col, dp_cell, n)
    return solvable

    # Implement Your Code Here
    pass


board = [[int(ele) for ele in input().split()] for i in range(9)]

ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
# print_pretty_array.print2d(board)

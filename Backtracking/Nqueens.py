"""N-Queens
Send Feedback
You are given N, and for a given N x N chessboard,
find a way to place N queens such that no queen can attack any other queen on the chess board.
A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens.
You have to print all such configurations.
Input Format :
Line 1 : Integer N
Output Format :
One Line for every board configuration.
Every line will have N*N board elements printed row wise and are separated by space
Note : Don't print anything if there isn't any valid configuration.
Constraints :
1<=N<=10
Sample Input 1:
4
Sample Output 1 :
0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0
0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0
"""


def canbeplacedhere(x, y, solution):
    rcount = x
    i = x
    for r in solution:
        if rcount <= 0:
            break
        if r[y] == 1:
            return False
        rcount -= 1
    i = x
    j = y
    while j < n and i >= 0:
        if solution[i][j] == 1:
            return False
        j += 1
        i -= 1
    i = x
    j = y
    while j >= 0 and i >= 0:
        if solution[i][j] == 1:
            return False
        j -= 1
        i -= 1
    return True


def nQueenHelper(x, y, n, solution):
    if x == n:
        for r in solution:
            for ele in r:
                print(ele, end=" ")
        print()

    for i in range(n): # check if queen can be placed in each column of row x
        if canbeplacedhere(x, i, solution):
            solution[x][i] = 1
            nQueenHelper(x + 1, 0, n, solution)
            solution[x][i] = 0
    return


def nQueen(n):
    solution = [[0 for i in range(n)] for i in range(n)]
    nQueenHelper(0, 0, n, solution)
    pass


n = int(input())
nQueen(n)

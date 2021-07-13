from sys import stdin


def wavePrint(mat, nRows, mCols):
    i = j = 0
    count = nRows * mCols
    k = 0
    while j < mCols:
        i = 0
        while i < nRows:
            print(mat[i][j], end=" ")
            k += 1
            i += 1
        j = j + 1
        i = i-1
        if k >= count:
            break
        while i >= 0:
            print(mat[i][j], end=" ")
            k += 1
            i -= 1
        if k >= count:
            break
        j+=1


# Your code goes here


# Taking Iput Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1

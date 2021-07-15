from sys import stdin

"""
'''
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here


























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0 :
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
"""
import sys

'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''


def findLargest(arr, nRows, mCols):
    max_i = max_i_r = 0
    max_c = max_num_r = -2147483648
    max_num_c = [0 for _ in range(mCols)]

    for i in range(nRows):
        sumr = 0
        for j in range(mCols):
            max_num_c[j] = max_num_c[j] + arr[i][j]
            sumr += arr[i][j]
        if sumr > max_num_r:
            max_num_r = sumr
            max_i_r = i
    for i in range(mCols):
        if max_c < max_num_c[i]:
            max_c = max_num_c[i]
            max_i = i
    if max_c > max_num_r:
        print("column", max_i, max_c)
    else:
        print("row", max_i_r, max_num_r)


# Your code goes here


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for _ in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1

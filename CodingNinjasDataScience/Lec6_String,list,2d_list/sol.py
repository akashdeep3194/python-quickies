import sys
from sys import stdin
sys.setrecursionlimit(10**6)

def isPalindrome(string):
    if len(string)<1:
        return True
    if string[0] != string[-1]:
        return False
    sa = isPalindrome(string[1:-1])
    if sa:
        return True
    return False


# Your code goes here


# main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans:
    print('true')
else:
    print('false')

#################################################
from sys import stdin


def printSubstrings(string):
    n = len(string)
    for i in range(n):
        for j in range(i+1, n + 1):
            print(string[i:j])
    return


# Your ciode goes here


# main
string = stdin.readline().strip();
printSubstrings(string)
##################################################
from sys import stdin

def swapAlternate(arr, n) :
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    #Your code goes here



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1
#####################################################
from sys import stdin


def arrayEquilibriumIndex(arr, n):
    sum = 0
    i = -1
    for i in range(n):
        sum = sum + arr[i]
    rightsum = leftsum = 0
    for i in range(n):
        rightsum = sum - arr[i] - leftsum
        if rightsum == leftsum:
            break
        leftsum += arr[i]
    else:
        i=-1
    return i
    # Your code goes here


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1
#############################################################
from sys import stdin


def rowWiseSum(mat, nRows, mCols):
    for r in mat:
        sum = 0
        for c in r:
            sum += c
        print(sum,end = " ")
    return


# Your code goes here


# Taking Input Using Fast I/O
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
    rowWiseSum(mat, nRows, mCols)
    print()

    t -= 1
##########################################################
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
#####################################################
import sys
from sys import stdin

sys.setrecursionlimit(10 ** 6)


def removeConsecutiveDuplicates(string):
    ans = ""
    if len(string) == 0:
        return string
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            pass
        else:
            ans += string[i]
    ans += string[-1]
    return ans

    # if len(string) <= 1:
    #     return string
    # sa = removeConsecutiveDuplicates(string[1:])
    # if string[0] == sa[0]:
    #     return sa
    # else:
    #     return string[0] + sa
    #


# Your code goes here


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
###############################################
from sys import stdin


def reverseEachWord(string):
    word = ""
    ans = ""
    for i in range(len(string)):
        if string[i]==" ":
            word = word[::-1]
            ans+=word+" "
            word=""
        else:
            word += string[i]
    ans += word[::-1]
    return ans

# Your code goes here


# main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
##############################################
from sys import stdin


def highestOccuringChar(string):
    maxcount = 0
    dictionary = dict()
    for char in string:
        count =  dictionary.get(char,0) + 1
        dictionary[char] = count
        if count>maxcount:
            maxcount = count

    for char in string:
        if dictionary[char] == maxcount:
            maxchar = char
            break
    return maxchar



# Your code goes here


# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
#############################################################
from sys import stdin


def arrange(arr, n):
    k = (n-1) // 2
    num = 1
    for i in range(k+1):
        arr[i] = num
        if i != n-i-1:
            arr[n-i-1] = num + 1
        num += 2
    # Your code goes here


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    n = int(stdin.readline().strip())
    arr = n * [0]
    arrange(arr, n)
    printList(arr, n)
    t -= 1
##################################################
"""
Leaders in array
Send Feedback
Given an integer array A of size n. Find and print all the leaders present in the input array. An array element A[i]
is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
Print all the leader elements separated by space and in the same order they are present in the input array.
Input Format :
Line 1 : Integer n, size of array
Line 2 : Array A elements (separated by space)
Output Format :
 leaders of array (separated by space)
Constraints :
1 <= n <= 10^6
Sample Input 1 :
6
3 12 34 2 0 -1
Sample Output 1 :
34 2 0 -1
Sample Input 2 :
5
13 17 5 4 6
Sample Output 2 :
17 6"""
import sys


def LeadersInArray(arr):
    maxr = [sys.maxsize * -1]
    maxnum = -1 * sys.maxsize
    for i in range(len(arr) - 2, -1, -1):
        if arr[i + 1] > maxnum:
            maxnum = arr[i + 1]
        maxr.append(maxnum)
    maxr = maxr[::-1]
    i = 0
    leader = []
    for ele in arr:
        if ele >= maxr[i]:
            leader.append(ele)
        i += 1
    return leader


n = int(input())

arr = list(map(int, sys.stdin.readline().strip().split()))

leader = LeadersInArray(arr)
for ele in leader:
    print(ele,end=" ")
##################################################
"""Maximise the sum
Send Feedback
Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return
the maximum sum.
That is, we can switch from one array to another array only at common elements.
If no intersection element is present, we need to take sum of all elements from the array with greater sum.
Input Format :
 Line 1 : An integer M i.e. size of first array
 Line 2 : M integers which are elements of first array, separated by spaces
 Line 3 : An integer N i.e. size of second array
 Line 4 : N integers which are elements of second array, separated by spaces
Output Format :
Maximum sum value
Constraints :
1 <= M, N <= 10^6
Sample Input :
6
1 5 10 15 20 25
5
2 4 5 9 15
Sample Output :
81
Explanation :
We start from array 2 and take sum till 5 (sum = 11). Then we'll switch to array at element 10 and take till 15.
So sum = 36. Now, no elements left in array after 15, so we'll continue in array 1. Hence sum is 81
"""
import sys


def Maximise_the_sum(arr1, arr2, m, n):
    i = j = 0
    suma = 0
    sumb = 0
    while i < m and j < n:
        if arr1[i] == arr2[j]:
            suma += arr1[i]
            sumb += arr2[j]
            suma = sumb = max(suma, sumb)
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            suma += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sumb += arr2[j]
            j += 1
    while i < m:
        suma += arr1[i]
        i += 1
    while j < n:
        sumb += arr2[j]
        j += 1
    return max(suma, sumb)


m = int(input())
arr1 = list(map(int, sys.stdin.readline().strip().split()))
n = int(input())
arr2 = list(map(int, sys.stdin.readline().strip().split()))

print(Maximise_the_sum(arr1,arr2,m,n))

#######################################################
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
###############################
"""
Print Spiral
Send Feedback
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)
 Mind that every element will be printed only once.
Refer to the Image:
Spiral path of a matrix

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.
Output format :
For each test case, print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
Sample Input 1:
1
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Sample Input 2:
2
3 3
1 2 3
4 5 6
7 8 9
3 1
10
20
30
Sample Output 2:
1 2 3 6 9 8 7 4 5
10 20 30
"""
import sys
from sys import stdin

sys.setrecursionlimit(10 ** 6)


def spiralPrint_Helper(mat, nsi, nei, msi, mei):
    for j in range(msi, mei + 1):
        print(mat[nsi][j], end=" ")
    for i in range(nsi + 1, nei + 1):
        if mei > msi:
            print(mat[i][mei], end=" ")
    for j in range(mei - 1, msi, -1):
        if mei > msi:
            print(mat[nei][j], end=" ")
    for i in range(nei, nsi, -1):
        if nei > nsi:
            print(mat[i][msi], end=" ")

    msi = msi + 1
    nsi = nsi + 1
    mei = mei - 1
    nei = nei - 1

    if msi > mei or nsi > nei:
        return

    spiralPrint_Helper(mat, nsi, nei, msi, mei)


def spiralPrint(mat, nRows, mCols):
    spiralPrint_Helper(mat, 0, nRows - 1, 0, mCols - 1)


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
###########################

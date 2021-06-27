"""Return subset of an array
Send Feedback
Given an integer array (of length n), find and return all the subsets of input array.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain
same as in the input array.
Note : The order of subsets are not important.
Input format :

Line 1 : Size of array

Line 2 : Array elements (separated by space)

Sample Input:
3
15 20 12
Sample Output:
[] (this just represents an empty array, don't worry about the square brackets)
12
20
20 12
15
15 12
15 20
15 20 12 """
import copy
import sys


def subsetsOfArray(arr):
    if len(arr) == 0:
        return [[]]

    sa = subsetsOfArray(arr[1:])

    tmp = copy.deepcopy(sa)
    for ele in tmp:
        ele.insert(0, arr[0])
    sa.extend(tmp)
    return sa


n = int(input())

array = list(map(int, sys.stdin.readline().strip().split()))
print(array)
c = subsetsOfArray(array)
print(c)
for row in c:
    for e in row:
        print(e, end=" ")
    print()

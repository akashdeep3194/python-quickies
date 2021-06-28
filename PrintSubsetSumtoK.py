"""Print Subset Sum to K
Send Feedback
Given an array A and an integer K, print all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array.
But the order of elements should remain same as in the input array.
Note : The order of subsets are not important. Just print them in different lines.
Input format :
Line 1 : Size of input array
Line 2 : Array elements separated by space
Line 3 : K
Sample Input:
9
5 12 3 17 1 18 15 3 17
6
Sample Output:
3 3
5 1
"""
import copy
import sys


def subsetSumToK(arr, k, ans=[]):
    if len(arr) == 0:
        if k == 0:
            for ele in ans:
                print(ele,end=" ")
            print()
        return
    ans2 = ans[:]

    # if arr[0] == k:
    ans.append(arr[0])
    subsetSumToK(arr[1:], k, ans2)
    subsetSumToK(arr[1:], k - arr[0], ans)


n = int(input())
subsetSumToK(list(map(int, sys.stdin.readline().strip().split())), int(input()))



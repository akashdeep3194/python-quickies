""""
Return subsets sum to K
Send Feedback
Given an array A of size n and an integer K, return all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain
same as in the input array.
Note : The order of subsets are not important.
Input format :
Line 1 : Integer n, Size of input array
Line 2 : Array elements separated by space
Line 3 : K
Constraints :
1 <= n <= 20
Sample Input :
9
5 12 3 17 1 18 15 3 17
6
Sample Output :
3 3
5 1
"""
import sys


def subsetSumtoK(arr, k):
    if len(arr) == 0:
        return []
    ans = []
    sa1 = subsetSumtoK(arr[1:], k - arr[0])
    sa2 = subsetSumtoK(arr[1:], k)
    tmp = []
    tmp2 = []
    if len(sa1) > 0:
        for l in sa1:
            tmp2.append(arr[0])
            tmp2.extend(l)
            tmp.append(tmp2)
            tmp2 = []
        ans.extend(tmp)
    if len(sa2) > 0:
        ans.extend(sa2)
    if arr[0] == k:
        x = [arr[0]]
        ans.append(x)
    return ans


n = int(input())

answer = subsetSumtoK(list(map(int, sys.stdin.readline().strip().split())), int(input()))

for row in answer:
    for ele in row:
        print(ele, end = " ")
    print()




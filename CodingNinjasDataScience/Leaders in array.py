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

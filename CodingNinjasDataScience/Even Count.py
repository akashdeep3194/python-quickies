"""
Even Count
Send Feedback
You are provided with an integer array where each number is present either odd number of times or even number of times.
You have to find and return the number which is present even number of times.
If multiple numbers are present even number of times, then return that number which occurs first among these numbers in
the given array. If no such number exists, then return -1.
Note : You may take extra space but solve this problem in O(n) time.
Input Format:
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format:
Array element occurring even no. of times
Constraints :
1 <= N <= 10^5
Sample Input:
6
2 5 3 5 3 4
Sample Output:
5
"""


def evenCount(arr):
    dictionary = dict()
    for ele in arr:
        dictionary[ele] = dictionary.get(ele, 0) + 1
    for ele in arr:
        if dictionary[ele] % 2 == 0:
            return ele
    pass


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(evenCount(arr))

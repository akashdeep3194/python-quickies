from sys import stdin


def maxfreq(arr):
    # Write your code here
    maxf = 0
    maxnum = -1
    dictionary = dict()
    for ele in arr:
        x = dictionary.get(ele,0)+1
        dictionary[ele] = x
        if maxf<x:
            maxnum = ele
            maxf = x

    for ele in arr:
        if dictionary[ele] == maxf:
            return ele
    pass


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(maxfreq(arr))
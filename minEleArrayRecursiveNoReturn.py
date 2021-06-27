import sys


def minEleArr(arr, minans=sys.maxsize):
    if len(arr) == 1:
        print(min(arr[0], minans))
        return
    minans = min(arr[0], minans)
    minEleArr(arr[1:], minans)


array = list(map(int, sys.stdin.readline().strip().split()))
minEleArr(array)

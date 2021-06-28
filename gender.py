import sys


def gender(n, k):
    if n == 1:
        return "Male"
    if gender(n - 1, int((k + 1) / 2)) == "Male":
        if k % 2 == 0:
            return "Female"
        else:
            return "Male"
    else:
        if k % 2 == 0:
            return "Male"
        else:
            return "Female"


t = int(input())
while t > 0:
    arr = list(map(int, sys.stdin.readline().strip().split()))
    x = arr[0]
    y = arr[1]
    print(gender(x, y))
    t -= 1

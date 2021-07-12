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

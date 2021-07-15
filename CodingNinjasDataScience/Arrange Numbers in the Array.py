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

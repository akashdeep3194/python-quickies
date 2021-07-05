import sys


def mergeSort(arr) -> None:
    n = len(arr)
    if n == 1:
        return
    mid = n // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    mergeSort(arr1)
    mergeSort(arr2)

    i = j = 0

    l1 = len(arr1)
    l2 = len(arr2)

    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            arr[i + j] = arr1[i]
            i += 1
        else:
            arr[i + j] = arr2[j]
            j += 1
    while j < l2:
        arr[i + j] = arr2[j]
        j += 1
    while i < l1:
        arr[i + j] = arr1[i]
        i += 1
    return arr


array = list(map(int, sys.stdin.readline().strip().split()))
mergeSort(array)
print(array)

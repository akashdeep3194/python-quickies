def find_pivot_index(arr, z, si, ei):
    if len(arr) == 0:
        return -1
    i = (si + ei) // 2
    if si >= len(arr):
        return 0
    if len(arr) == 1:
        return 0
    if arr[i] < arr[i - 1]:
        return i
    elif arr[i] > z:
        pi = find_pivot_index(arr, z, i + 1, ei)
    else:
        pi = find_pivot_index(arr, z, si, i - 1)
    return pi


def binarySearch(arr, ele, si, ei):
    if ei < si:
        return -1
    i = (si + ei) // 2
    if arr[i] == ele:
        return i
    elif arr[i] > ele:
        sa1 = binarySearch(arr, ele, si, ei - 1)
    else:
        sa1 = binarySearch(arr, ele, i + 1, ei)
    return sa1


def find_indexofele(arr, pi, ele):
    arr1 = arr[:pi]
    arr2 = arr[pi:]

    ans1 = binarySearch(arr1, ele, 0, len(arr1) - 1)
    ans2 = binarySearch(arr2, ele, 0, len(arr2) - 1)

    if ans1 == -1 and ans2 == -1:
        return -1
    elif ans1 != -1:
        return ans1
    else:
        return len(arr1) + ans2


def solve(arr,elem):
    if len(arr) == 0:
        return -1
    pivot_index = find_pivot_index(arr, arr[0], 0, len(arr) - 1)
    print(find_indexofele(arr, pivot_index, elem))


arr = [5]
print(solve(arr,6))

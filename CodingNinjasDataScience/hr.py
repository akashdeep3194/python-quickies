def minimumSwaps(arr):
    i = 0
    ctr = 0
    while i < len(arr):
        if arr[i] == i + 1:
            i += 1
        else:
            ctr += 1
            k = arr[i]
            arr[i], arr[k - 1] = arr[k - 1], arr[i]
    return ctr


n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)
print(res)

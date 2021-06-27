import sys


def print_all_subsequnce(arr, si=0, ans=[""]):
    if len(arr) == si + 1:
        # print(arr[si])
        ans.append(arr[si])
        return ans
    ans = print_all_subsequnce(arr, si + 1, ans)
    tmp = []
    for ele in ans:
        x = arr[si] + ele
        # print(x)
        tmp.append(x)
    ans.extend(tmp)
    return ans


array = list(map(str, sys.stdin.readline().strip().split()))
print_all_subsequnce(array)

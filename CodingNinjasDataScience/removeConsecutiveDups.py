import sys
from sys import stdin

sys.setrecursionlimit(10 ** 6)


def removeConsecutiveDuplicates(string):
    ans = ""
    if len(string) == 0:
        return string
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            ans += string[i]
        else:
            pass
    ans += string[-1]
    return ans

    # if len(string) <= 1:
    #     return string
    # sa = removeConsecutiveDuplicates(string[1:])
    # if string[0] == sa[0]:
    #     return sa
    # else:
    #     return string[0] + sa
    #


# Your code goes here


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)

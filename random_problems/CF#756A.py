from math import log10
def solve(n):
    if n&1 == 0:
        return 0
    if (n//10**int(log10(n)))&1 == 0:
        return 1
    else:
        while n>0:
            digit = n%10
            n = n//10
            if digit&1 == 0:
                return 2
    return -1
                



t = int(input())
while t>0:
    n = int(input())
    print(solve(n))
    t-=1

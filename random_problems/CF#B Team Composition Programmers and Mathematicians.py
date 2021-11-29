from math import log10
def solve(a,b):
    return min(min(a,b),(a+b)//4)

t = int(input())
while t>0:
    a,b = (input().strip().split())
    a = int(a)
    b = int(b)
    print(solve(a,b))
    t-=1

from math import log10
import sys
from typing import List

def solve(a:List,b:int):
    if a[0]>a[-1]:
        ele = a[0]
        if ele != max(a):
            return -1        
        a = a[1:]
    else:
        ele = a[-1]
        if ele != max(a):
            return -1                
        a = a[:-1]

    a = a[::-1]

    a.append(ele)
    return a

t = int(input())

while t>0:
    b = int(input())
    a = list(map(int,sys.stdin.readline().strip().split()))
    arr = solve(a,b)
    if type(arr) is list:
        for ele in arr:
            print(ele,end=" ")
    else:
        print(arr)
    t-=1

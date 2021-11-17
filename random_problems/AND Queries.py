from typing import *
from math import log2

def andQueries(arr: List[int], n: int) -> int:
    dc = dict()

    ans = arr[0]

    for ele in arr:
        ans = ele&ans
    return ans

# print(andQueries([1,3,5],3))

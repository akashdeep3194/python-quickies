from typing import *

def count_mm(arr,si,ei):
    si = si-1
    ei = ei-1
    ctr = 0
    if ei-si<2:
        return 0
    for i in range(si+1,ei):
        if arr[i-1]<arr[i]>arr[i+1]:
            ctr+=1
        elif arr[i-1]>arr[i]<arr[i+1]:
            ctr += 1
    return ctr

def process(n: int, q: int, queries: List[List[int]], arr: List[int])-> List[int]:
    k = 0
    while q:
        quer = queries[k]
        if quer[0] == 1:
            arr[quer[1]-1] = quer[2]
            print(arr)
        else:
            print(count_mm(arr,quer[1],quer[2]))
            if count_mm(arr,quer[1],quer[2])&1 == 1:
                return True
            else:
                return False
        
        q-=1
        k += 1
print(process(5,2,[[1,4,0],[2,1,5]],[1,2,3,1,6]))

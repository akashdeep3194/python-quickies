"""
The program takes input a list as space separated values

The function secondMax() takes an array of strings (representing integers) as input and returns the secondMax number
if not present else it returns -1
"""

import sys


def secondMax(arr):
    if len(arr) <= 1:
        return -1
    max_num = sec_max = int(arr[0])
    for ele in arr:
        ele = int(ele)
        if ele > max_num:
            sec_max = max_num
            max_num = ele
        elif sec_max < ele < max_num:
            sec_max = ele
        elif sec_max > ele and sec_max == max_num:
            sec_max = ele
    if sec_max == max_num:
        return -1
    else:
        return sec_max


max_arr = list(sys.stdin.readline().strip().split())
print(secondMax(max_arr))

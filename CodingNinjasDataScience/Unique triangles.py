"""
Unique triangles
Send Feedback
You are given n triangles. You are required to find how many triangles are unique out of given triangles. For each triangle you are given three integers a, b and c (the sides of a triangle).
A triangle is said to be unique if there is no other triangle with same set of sides.
Note : It is always possible to form triangle with given sides.
Input Constraints :
Line 1 : Integer n, the number of triangles
Next n lines : Three integers a,b,c (sides of a triangle).
Output Format :
print single integer, the number of unique triangles.
Constraints :
1 <= n <= 10^4
1 <= a,b,c <= 10^15.
Sample Input :
5
7 6 5
5 7 6
8 2 9
2 3 4
2 4 3
Sample Output :
1
"""
import sys


def uniqueTriangles(arr):
    return len(arr)


t = int(input())
arr = set()
while t > 0:
    array = list(map(int, sys.stdin.readline().strip().split()))
    array = sorted(array)
    array = tuple(array)
    arr.add(array)
    t -= 1

print(uniqueTriangles(arr))

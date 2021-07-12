import sys
from sys import stdin
sys.setrecursionlimit(10**6)

def isPalindrome(string):
    if len(string)<1:
        return True
    sa = isPalindrome(string[1:-1])
    if sa:
        if string[0] == string[-1]:
            return True
    return False


# Your code goes here


# main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans:
    print('true')
else:
    print('false')


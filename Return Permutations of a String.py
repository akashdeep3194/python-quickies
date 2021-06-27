"""Return Permutations of a String
Send Feedback
Given a string, find and return all the possible permutations of the input string.
Note : The order of permutations are not important.
Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba"""


def insertCharInStringAtKthPos(c, s, k):
    return s[0:k] + c + s[k:]


def permutations(string):
    # Implement Your Code Here
    if len(string) == 0:
        return [""]

    sa = permutations(string[1:])
    op = []
    for smallString in sa:
        for i in range(len(smallString) + 1):
            op.append(insertCharInStringAtKthPos(string[0], smallString, i))
    return op

    pass


string = input()
ans = permutations(string)
for s in ans:
    print(s)

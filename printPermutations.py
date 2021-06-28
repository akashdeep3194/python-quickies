"""Given a string, find and print all the possible permutations of the input string.
Note : The order of permutations are not important. Just print them in different lines.
Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba"""


def charAtposK(e, c, i):
    return e[:i] + c + e[i:]


def Printpermutations(arr, ans=[""]):
    if len(arr) == 0:
        for ele in ans:
            print(ele)
        return
    answer = []
    for ele in ans:
        for i in range(len(ele) + 1):
            tmp = charAtposK(ele, arr[0], i)
            answer.append(tmp)
    Printpermutations(arr[1:], answer)

x=input()
Printpermutations(x)

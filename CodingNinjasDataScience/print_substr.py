from sys import stdin


def printSubstrings(string):
    n = len(string)
    for i in range(n):
        for j in range(i+1, n + 1):
            print(string[i:j])
    return


# Your ciode goes here


# main
string = stdin.readline().strip();
printSubstrings(string)

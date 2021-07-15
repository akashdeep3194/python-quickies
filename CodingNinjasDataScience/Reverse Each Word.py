from sys import stdin


def reverseEachWord(string):
    word = ""
    ans = ""
    for i in range(len(string)):
        if string[i]==" ":
            word = word[::-1]
            ans+=word+" "
            word=""
        else:
            word += string[i]
    ans += word[::-1]
    return ans

# Your code goes here


# main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
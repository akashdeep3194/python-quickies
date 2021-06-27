
def getCharsForDigit(n):
    n = int(n)

    if n == 0:
        return [" "]
    elif n == 1:
        return ["1"]
    elif n == 2:
        return ['a', 'b', 'c']
    elif n == 3:
        return ['d', 'e', 'f']
    elif n == 4:
        return ['g', 'h', 'i']
    elif n == 5:
        return ['j', 'k', 'l']
    elif n == 6:
        return ['m', 'n', 'o']
    elif n == 7:
        return ['p', 'q', 'r', 's']
    elif n == 8:
        return ['t', 'u', 'v']
    elif n == 9:
        return ['w', 'x', 'y', 'z']


def keypad(x):
    if len(x) == 0:
        return [""]
    sx = x[1:]
    so = keypad(sx)
    chars = getCharsForDigit(x[0])
    tmp = []
    for char in chars:
        for ele in so:
            tmp.append(char + ele)
    return tmp


# main
x = input()
for ele in keypad(x):
    print(ele)
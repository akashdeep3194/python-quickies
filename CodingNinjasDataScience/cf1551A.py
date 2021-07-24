t = int(input())

while t > 0:
    x = int(input())
    c1 = c2 = x // 3
    mod = x % 3
    if mod == 1:
        c1 += 1
    if mod == 2:
        c2 += 1
    print(c1, c2)
    t -= 1

def fib(n):
    if n<1:
        print("enter > 0")
    if n == 1:
        print(0)
        return

    if n == 2:
        print(0)
        print(1)
        return

    print(0)
    print(1)

    p1 = 0
    p2 = 1

    while n > 2:

        f = p1 + p2
        print(f)

        p1 = p2
        p2 = f

        n -= 1
    return


n = int(input())
fib(n)

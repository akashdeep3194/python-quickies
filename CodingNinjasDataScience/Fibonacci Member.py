def checkMember(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    fib = [1, 1]
    i = 1
    while fib[i] <= n:
        i += 1
        fib.append(fib[i - 1] + fib[i - 2])
        if fib[i] == n:
            return True

    # Implement Your Code Here
    pass


n = int(input())
if checkMember(n):
    print("true")
else:
    print("false")

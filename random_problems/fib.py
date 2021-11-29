def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fib_mem(n,dp=dict()):

    if n == 1 or n == 2:
        return 1
    else:
        if dp.get(n-1,0) != 0:
            x = dp.get(n-1)
        else:
            x = fib_mem(n-1,dp)
            dp[n-1] = x
        if dp.get(n-2,0) != 0:
            y = dp.get(n-2)
        else:
            y = fib_mem(n-2,dp)
            dp[n-2] = y

        return x+y

print(fib_mem(50))

print(fib(40))

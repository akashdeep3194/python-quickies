def fib(n):
    if n == 1:
        return 2
    if n == 2:
        return 8
    x = fib(n - 1)
    y = fib(n - 2)
    return 4 * x +y


n = int(input())

i = 1
x = 0
sum = 0
if n<2:
    print(sum)
while x <= n:
    sum += x
    x = fib(i)
    i += 1
print(sum)

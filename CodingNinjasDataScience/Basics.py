## Read input as specified in the question.
## Print output as specified in the question.
# print(int(input(),2))
def binToDec(n):
    if n == "0":
        return 0, 1
    elif n == "1":
        return 1, 1
    sa, mul = binToDec(n[1:])
    x = int(n[0]) * (2 ** mul) + sa
    return x, mul + 1


print(binToDec(input()))

def convert(s: str, numRows: int) -> str:
    ans = [[] for _ in range(numRows)]
    i = 0
    j = 0
    rev = False
    while i < len(s):
        ans[j].append(s[i])
        i += 1
        if j < numRows-1 and rev == False:
            j += 1
        elif j == 0 and numRows-1>0:
            j+=1
            rev = False
        elif j>0:
            j -= 1
            rev=True

    answer = ""
    for ele in ans:
        for char in ele:
            answer += char

    return answer


print(convert(input(), 4))

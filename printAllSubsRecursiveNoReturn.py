def printAllSubsRecursiveNoReturn(arr, ans=[""]):
    if len(arr) == 0:
        for ele in ans:
            print(ele)
        return
    tmp = []
    for ele in ans:
        tmp.append(ele + arr[0])
    ans.extend(tmp)
    printAllSubsRecursiveNoReturn(arr[1:], ans)


printAllSubsRecursiveNoReturn(input())

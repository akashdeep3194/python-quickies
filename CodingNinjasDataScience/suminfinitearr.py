def sumInRanges(arr, n, queries, q):
    ans = []
    sums = 0
    for ele in arr:
        sums += ele
    for qr in queries:
        l = qr[0]-1
        r = qr[1]-1
        sa = 0

        # if r - l < n:
        #     ll = l % n
        #     rr = r % n
        #     while ll <= rr:
        #         sa += arr[ll]
        #         ll += 1
        #     ans.append(sa)
        #     continue
        k = (r - l + 1) / n
        ki = int(k)
        sa = ki * sums
        if k == ki:
            ans.append(sa)
            continue
        rr = r % n
        ll = l % n
        if rr >= ll:
            for i in range(ll, rr + 1):
                sa += arr[i]
        else:
            for i in range(ll, n):
                sa += arr[i]
            for j in range(rr + 1):
                sa += arr[j]

        ans.append(sa)
    return ans
    # Write your function Here.


print(sumInRanges([5, 2, 6, 9], 4, [[1, 5], [10, 13], [7, 11]], 3))

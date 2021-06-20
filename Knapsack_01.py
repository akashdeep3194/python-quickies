''' 

val is an array containing the value of the items
wt is an array containing the weight of the items
cap is the capacity of the Knapsack

Approach used: Recursion with Memoization

'''


def Knapsack(val, wt, cap):
    l = len(val)
    dp = [dict() for i in range(l + 1)]
    return KnapsackH(val, wt, l, cap, dp)


def KnapsackH(val, wt, l, cap, dp, si=0, sum=0):
    if cap < 0:
        return 0
    if si == l or cap == 0:
        return sum

    nsum = sum + val[si]
    ncap = cap - wt[si]

    if dp[si + 1].get(ncap, -1) != -1:
        sa1 = dp[si + 1][ncap]
    else:
        sa1 = KnapsackH(val, wt, l, ncap, dp, si + 1, nsum)
        dp[si + 1][ncap] = sa1

    if dp[si + 1].get(cap, -1) != -1:
        sa2 = dp[si + 1][cap]
    else:
        sa2 = KnapsackH(val, wt, l, cap, dp, si + 1, sum)
        dp[si + 1][cap] = sa2

    ans = max(sa1, sa2)
    dp[si][cap] = ans
    return ans

class Solution:
    def ispallindrome(self, ss, dp):
        if len(ss) <= 1:
            return True
        if ss[0] == ss[-1]:
            sa = self.ispallindrome(ss[1:-1])
            return sa
        return False

    def longestPalindrome(self, s: str) -> str:
        maxl = 0
        maxs = ""
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
            if maxl < 1:
                maxl = 1
                maxs = s[i:i + 1]

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i+1][i] = 1
                if maxl < 2:
                    maxl = 2
                    maxs = s[i:i + 2]

        i = 2
        j = 0
        while i < len(s):
            while j <= i - 2:
                if s[i] == s[j] and dp[i - 1][j + 1] == 1:
                    dp[i][j] = 1
                    if maxl < i - j + 1:
                        maxl = i - j + 1
                        maxs = s[j:i + 1]
                j += 1
            i += 1
            j = 0
        return maxs


ss = Solution()
arr = input()
print(ss.longestPalindrome(arr))



import sys

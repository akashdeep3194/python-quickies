class Solution:
    def lols(self, ss):
        if len(ss) == 0:
            return 0, ""
        sa = self.lols(ss[1:])
        sal = sa[0]
        x = ss[0]
        dictionary = dict()
        dictionary[x] = 1
        for i in range(1, len(ss)):
            if dictionary.get(ss[i], 0) >= 1:
                if i >= sal:
                    return i, ss[:i]
                else:
                    return sa[0],sa[1]
            dictionary[ss[i]] = dictionary.get(ss[i], 0) + 1
        else:
            return len(ss), ss

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = self.lols(s)
        return ans[0]


sol = Solution()
print(sol.lengthOfLongestSubstring(input()))

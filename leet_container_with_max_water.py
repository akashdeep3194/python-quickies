import sys


class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        while i < j:
            w = (j - i) * (min(height[i], height[j]))

            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -= 1

            ans = max(w, ans)

        return ans


s = Solution()
arr = list(map(int, sys.stdin.readline().strip().split()))
print(s.maxArea(arr))

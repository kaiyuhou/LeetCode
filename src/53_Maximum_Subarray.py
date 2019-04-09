import math

class Solution:
    def maxSubArray(self, nums) -> int:
        ans = -math.inf
        cnt = 0
        for a in nums:
            cnt += a
            ans = max(ans, cnt)
            cnt = max(cnt, 0)
        return ans


s = Solution()
A = [-2,-1,-3]
print(s.maxSubArray(A))
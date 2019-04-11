# class Solution:
#     def maxProfit(self, prices) -> int:
#         dp = {}
#         dp[0, 0] = 0
#         for i, p in enumerate(prices):
#             cur = i + 1
#             dp[cur, cur] = dp[cur - 1, cur - 1] - p
#
#             for j in range(cur):
#                 dp[cur, j] = dp[cur - 1, j]
#                 if j - 1 >= 0:
#                     dp[cur, j] = max(dp[cur - 1, j - 1] - p, dp[cur, j])
#                 if j + 1 <= cur - 1:
#                     dp[cur, j] = max(dp[cur - 1, j + 1] + p, dp[cur, j])
#
#             print(dp)
#
#         return dp[len(prices), 0]
#
# s = Solution()
# A = [7,1,5,3,6,4]
# print(s.maxProfit(A))

# import math
# class Solution:
#     def maxProfit(self, prices) -> int:
#         if len(prices) == 0:
#             return 0
#
#         min_left = []
#         max_right = []
#
#         cur = math.inf
#         for i, p in enumerate(prices):
#             cur = min(cur, p)
#             min_left.append(cur)
#
#         cur = 0
#         for i in range(len(prices) - 1, -1, -1):
#             cur = max(prices[i], cur)
#             max_right.append(cur)
#
#         return max([max_right[len(prices) - i - 1] - min_left[i] for i in range(len(prices))])

class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        buy= prices[0]
        ans = 0
        for p in prices:
            if p < buy:
                buy = p
            ans = max(ans, p - buy)
        return ans


s = Solution()
A = [7,1,5,3,6,4]
# A = [7,6,4,3,1]
# A = []
print(s.maxProfit(A))
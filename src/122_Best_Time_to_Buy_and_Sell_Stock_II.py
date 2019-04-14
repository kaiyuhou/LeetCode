class Solution:
    def maxProfit(self, prices) -> int:
        N = len(prices)
        if N == 0:
            return 0

        dp = {}

        dp[0, 0] = 0
        dp[0, 1] = -prices[0]
        for cur, p in enumerate(prices):
            if cur == 0:
                continue
            dp[cur, 1] = max(dp[cur - 1, 0] - p, dp[cur - 1, 1])
            dp[cur, 0] = max(dp[cur - 1, 0], dp[cur - 1, 1] + p)

        print(dp)
        return dp[N - 1, 0]

s = Solution()
A = [7,6,10,4,3,1]
# A = [1,2,3,4,5]
# A = [7,6,4,3,1]
print(s.maxProfit(A))
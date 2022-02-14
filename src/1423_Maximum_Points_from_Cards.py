class Solution:
    def maxScore(self, cps: List[int], k: int) -> int:
        left_sum = [0]
        for i in range(0, min(len(cps), k + 1)):
            left_sum.append(cps[i] + left_sum[-1])

        right_sum = [0]
        for i in range(len(cps) - 1, max(-1, len(cps) - k - 2), -1):
            right_sum.append(cps[i] + right_sum[-1])

        ans = 0
        for i in range(k + 1):
            ans = max(ans, left_sum[i] + right_sum[k - i])
        return ans


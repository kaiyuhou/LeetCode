from Tree import  *

# class Solution:
# #     def dayOfYear(self, date: str) -> int:
# #         days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #         Y = int(date[:4])
# #         M = int(date[5:7])
# #         D = int(date[8:])
# #         ans = D + sum(days[:M])
# #         if M > 2:
# #             if Y % 400 == 0:
# #                 ans += 1
# #             elif Y % 4 == 0 and Y % 100 != 0:
# #                 ans += 1
# #         return ans
# #
# #
# # s = Solution()
# # date = "2004-03-01"
# # print(s.dayOfYear(date))

# class Solution:
#     def numRollsToTarget(self, d: int, f: int, target: int) -> int:
#
#         import functools
#         @functools.lru_cache(None)
#         def dfs(n_dice, target):
#             if n_dice > target or n_dice * f < target:
#                 return 0
#             if n_dice == 1 and f >= target:
#                 return 1
#             ans = 0
#             for i in range(1, f + 1):
#                 ans += dfs(n_dice - 1, target - i)
#             return ans % 1000000007
#
#         return dfs(d, target)
#
# s = Solution()
# print(s.numRollsToTarget(30, 30, 500))

# class Solution:
#     def maxRepOpt1(self, text: str) -> int:
#         ans = 0
#         N = len(text)
#         for c in range(26):
#             mem = [0 for _ in range(N + 1)]
#             for i in range(N):
#                 if text[i] == chr(97 + c):
#                     mem[i + 1] = mem[i] + 1
#                 else:
#                     mem[i + 1] = mem[i]
#             total_1 = mem[N]
#
#             dp = {}
#             dp[0, 0] = 0
#             dp[0, 1] = 0
#             for i in range(N):
#                 if text[i] == chr(97 + c):
#                     dp[i + 1, 0] = dp[i, 0] + 1
#                     dp[i + 1, 1] = dp[i, 1] + 1
#                 else:
#                     dp[i + 1, 0] = 0
#                     dp[i + 1, 1] = dp[i, 0] + 1
#                 ans = max(ans, min(total_1, dp[i + 1, 1]))
#
#         return ans
#
# s = Solution()
# # text = "ababa"
# # text = "aaabaaa"
# # text = "aaabbaaa"
# # text = "aaaaa"
# text = "abcdef"
# print(s.maxRepOpt1(text))


class MajorityChecker:

    def __init__(self, A):
        B_size = 140
        Max_Num = 20005
        N = len(A)
        N_Block = (N + B_size - 1) // B_size
        dp = {} # cnt of nums

        for n in range(Max_Num):
            dp[0, n] = 0

        for i in range(1, N_Block + 1):
            for n in range(Max_Num):
                dp[i, n] = dp[i - 1, n]
            for j in range(B_size * (i-1), B_size * i):
                dp[i, A[j]] += 1

        com = {}
        for i in range(N_Block + 1):
            for j in range(N_Block + 1):
                com[i, j] = -1

        for i in range(1, N_Block + 1):
            cur = 0
            n_nums = [0 for _ in range(Max_Num)]
            for j in range(B_size * (i-1), N):
                n_nums[A[j]] += 1
                if n_nums[A[j]] > n_nums[cur]:
                    cur = A[j]
                if (j + 1) % B_size == 0:
                    com[i, j // B_size + 1] = cur

        self.dp = dp
        self.com = com
        self.A = A

    def query(self, left: int, right: int, threshold: int) -> int:
        B_size = 140
        Max_Num = 20005
        A = self.A
        N = len(A)
        N_Block = (N + B_size - 1) // B_size

        L = left // B_size + 1
        R = right // B_size + 1

        ans = -1
        if L < R - 1:
            ans = self.com[L + 1][R - 1]


    def query(self, left: int, right: int, threshold: int) -> int:





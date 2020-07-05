from typing import *
from Tree import *

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         ans = []
#         for i in range(n):
#
#             ans.append(nums[i])
#             ans.append(nums[i + n])
#
#         return ans
#
# s = Solution()
# nums = [2,5,1,3,4,7]
# nums = [1,2,3,4,4,3,2,1]
# print(s.shuffle(nums, 4))

# class Solution:
#     def getStrongest(self, A: List[int], k: int) -> List[int]:
#         A.sort()
#         N = len(A)
#         med = A[(N - 1) // 2]
#         B = []
#         for a in A:
#             B.append((abs(a - med), a))
#         B.sort()
#         B.reverse()
#         ans = []
#         for i in range(k):
#             ans.append(B[i][1])
#         return ans
#
# s = Solution()
# arr = [1,2,3,4,5]
# k = 2
# arr = [1,1,3,5,5]
# k = 2
# arr = [6,7,11,7,6,8]
# k = 5
# arr = [6,-3,7,2,11]
# k = 3
# arr = [-7,22,17,3]
# k = 2
# print(s.getStrongest(arr, k))


# class BrowserHistory:
#
#     def __init__(self, homepage: str):
#         self.history = ["None"] * 5005
#         self.cur = 0
#         self.top = 0
#         self.history[0] = homepage
#
#     def visit(self, url: str) -> None:
#         self.cur += 1
#         self.top = self.cur
#         self.history[self.cur] = url
#
#     def back(self, steps: int) -> str:
#         move = min(self.cur, steps)
#         self.cur -= move
#         return self.history[self.cur]
#
#     def forward(self, steps: int) -> str:
#         move = min(steps, self.top - self.cur)
#         self.cur += move
#         return self.history[self.cur]


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        dp = {}

        if houses[0] == 0:
            for i in range(n):
                dp[0, i, 1] = cost[0][i]
        else:
            dp[0, houses[0] - 1, 1] = 0

        for index in range(1, m):
            if houses[index] != 0:
                for color in range(n):
                    for group in range(1, target + 1):
                        if color == houses[index] - 1:
                            if (index - 1, color, group) in dp:
                                cur = dp[index - 1, color, group]
                                if (index, houses[index] - 1, group) not in dp:
                                    dp[index, houses[index] - 1, group] = cur
                                else:
                                    dp[index, houses[index] - 1, group] = min(dp[index, houses[index] - 1, group], cur)
                        else:
                            if (index - 1, color, group - 1) in dp:
                                cur = dp[index - 1, color, group - 1]
                                if (index, houses[index] - 1, group) not in dp:
                                    dp[index, houses[index] - 1, group] = dp[index - 1, color, group - 1]
                                else:
                                    dp[index, houses[index] - 1, group] = min(cur, dp[index, houses[index] - 1, group])
            else:
                for color in range(n):
                    for group in range(1, target + 1):
                        if (index - 1, color, group) in dp:
                            dp[index, color, group] = dp[index - 1, color, group] + cost[index][color]
                        for last_color in range(n):
                            if last_color == color:
                                continue
                            if (index - 1, last_color, group - 1) in dp:
                                cur = dp[index - 1, last_color, group - 1] + cost[index][color]
                                if (index, color, group) not in dp:
                                    dp[index, color, group] = cur
                                else:
                                    dp[index, color, group] = min(cur, dp[index, color, group])

        ans = 99999999
        for color in range(n):
            if (m - 1, color, target) in dp:
                ans = min(ans, dp[m - 1, color, target])
        if ans == 99999999:
            return -1
        return ans


        # import functools
        # @functools.lru_cache(None)
        # def dfs(index, before_group, last_color, before_cost):
        #     # print(index, before_group, last_color, before_cost)
        #     if before_group > target:
        #         return 99999999
        #
        #     if index == m:
        #         if before_group != target:
        #             return 99999999
        #         return before_cost
        #
        #     if houses[index] != 0:
        #         if last_color != houses[index]:
        #             return dfs(index + 1, before_group + 1, houses[index], before_cost)
        #         else:
        #             return dfs(index + 1, before_group, houses[index], before_cost)
        #
        #     if target == before_group:
        #         return dfs(index + 1, before_group, last_color, before_cost + cost[index][last_color - 1])
        #
        #     if last_color != -1:
        #         ans = dfs(index + 1, before_group, last_color, before_cost + cost[index][last_color - 1])
        #     else:
        #         ans = 99999999
        #
        #     for color in range(n):
        #         if color + 1 == last_color:
        #             continue
        #         cur = dfs(index + 1, before_group + 1, color + 1, before_cost + cost[index][color])
        #         ans = min(ans, cur)
        #     return ans
        #
        # ans = dfs(0, 0, -1, 0)
        # if ans == 99999999:
        #     return -1
        # return ans

s = Solution()
houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3

# houses = [0,2,1,2,0]
# cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# m = 5
# n = 2
# target = 3
#
houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[1,10],[10,1],[1,10]]
m = 5
n = 2
target = 5
#
houses = [3,1,2,3]
cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
m = 4
n = 3
target = 3
#
houses = [0,0,0,14,0,0,11,10,0,0,1,14,4,9,10,0,1,0,0,0,0,8,13,0,0,6,0]
cost = [[30,43,25,47,35,4,11,35,23,4,44,49,32,46],[28,46,3,3,30,28,44,39,7,31,21,45,47,19],[35,50,32,1,45,38,33,46,45,32,40,29,39,41],[48,37,16,1,23,4,31,36,7,25,24,41,30,45],[27,25,40,13,32,43,22,44,48,20,1,17,35,8],[23,14,25,31,11,6,16,38,44,30,19,9,4,10],[19,26,21,4,21,16,29,1,36,33,21,24,19,46],[42,33,30,33,6,25,2,37,8,45,2,18,7,44],[37,8,28,4,12,2,4,11,22,46,32,4,45,43],[46,32,29,21,34,17,42,16,47,35,26,34,21,25],[45,24,6,17,8,28,50,34,43,24,19,19,9,34],[7,48,45,3,42,7,13,21,24,11,24,18,2,23],[26,18,14,19,19,3,49,14,3,38,45,22,19,19],[3,32,47,9,5,32,2,49,28,17,25,17,45,2],[19,37,42,42,32,50,42,30,8,32,36,23,34,2],[38,14,22,7,12,11,23,14,22,36,49,7,45,47],[3,2,34,30,12,15,10,42,18,18,18,12,48,26],[22,45,3,34,17,36,2,16,50,48,42,30,12,37],[18,14,3,41,30,2,33,2,7,2,25,14,34,19],[44,5,22,25,26,25,21,36,31,33,23,5,48,48],[40,34,1,38,48,41,6,9,48,1,7,11,45,45],[34,21,10,3,35,27,41,21,3,7,45,24,44,40],[4,34,3,24,50,49,42,45,33,40,49,29,13,19],[30,37,9,14,38,18,34,30,25,27,27,22,37,33],[30,19,8,23,49,32,15,42,17,8,24,37,42,17],[30,21,12,10,2,4,7,4,46,43,39,37,6,8],[20,38,11,38,38,26,12,4,36,9,36,11,20,45]]
m = 27
n = 14
target = 15

houses = [0,0,0,3]
cost = [[2,2,5],[1,5,5],[5,1,2],[5,2,5]]
m = 4
n = 3
target = 3

print(s.minCost(houses, cost, m, n, target))














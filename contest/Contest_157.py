# class Solution:
#     def minCostToMoveChips(self, chips) -> int:
#         odd, even = 0, 0
#         for c in chips:
#             if c % 2 == 0:
#                 odd += 1
#             else:
#                 even += 1
#         return min(odd, even)

# class Solution:
#     def longestSubsequence(self, arr, difference: int) -> int:
#         if difference == 0:
#             import collections
#             C = collections.Counter(arr)
#             ans = 1
#             for k, v in C.items():
#                 ans = max(ans, v)
#             return ans
#
#         dp = {}
#         for a in arr:
#             if a not in dp:
#                 dp[a] = 1
#             if a - difference in dp:
#                 dp[a] = max(dp[a - difference] + 1, dp[a])
#             # if a + difference in dp:
#             #     dp[a] = max(dp[a + difference] + 1, dp[a])
#
#         # print(dp)
#         ans = 1
#         for k, v in dp.items():
#             ans = max(ans, v)
#         return ans
#
# s = Solution()
# arr = [1,5,7,8,5,3,4,2,1]
# print(s.longestSubsequence(arr, 0))

# class Solution:
#     def getMaximumGold(self, grid) -> int:
#         next = [[0, 1], [0, -1], [-1, 0], [1, 0]]
#         N = len(grid)
#         M = len(grid[0])
#
#         ans = 0
#
#         def dfs(px, py):
#             V[px][py] = True
#             cur = 0
#             for nx, ny in next:
#                 x = px + nx
#                 y = py + ny
#                 if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] == 0 or V[x][y]:
#                     continue
#                 cur = max(cur, dfs(x, y))
#             V[px][py] = False
#             return grid[px][py] + cur
#
#         V = [[False for _ in range(M)] for __ in range(N)]
#         for i in range(N):
#             for j in range(M):
#                 if grid[i][j] == 0:
#                     continue
#                 ans = max(ans, dfs(i, j))
#         return ans
#
#
# s = Solution()
# grid = [[0,6,0],[5,8,7],[0,9,0]]
# grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# grid = [[0]]
# print(s.getMaximumGold(grid))

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1]
        T = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]

        for _ in range(n - 1):
            nxt = [0] * 5
            for i in range(5):
                for j in T[i]:
                    nxt[j] += dp[i]
            dp = nxt

        return sum(dp) % 1000000007

s = Solution()
print(s.countVowelPermutation(20000))












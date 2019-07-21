from contest.Tree import *
import collections

# class Solution:
# #     def numEquivDominoPairs(self, dominoes) -> int:
# #         c = collections.Counter()
# #         for d in dominoes:
# #             if d[0] > d[1]:
# #                 c[(d[1], d[0])] += 1
# #             else:
# #                 c[(d[0], d[1])] += 1
# #
# #         ans = 0
# #         for v in c.values():
# #             if v > 1:
# #                 ans +=  (v * (v - 1)) // 2
# #         return ans
# #
# # s = Solution()
# # dominoes = [[1,2],[2,1],[1,2],[5,6], [2,1], [5,6]]
# # print(s.numEquivDominoPairs(dominoes))


# class Solution:
#     def bfs(self, color):
#         N = len(self.ans)
#         V = [set(), set()]
#
#         stack = [(0, 0, color)] # node, deep, color
#         while len(stack) != 0:
#             cur, deep, clr = stack.pop(0)
#             self.ans[cur] = min(deep, self.ans[cur])
#
#             for neighbor in self.edge[clr][cur]:
#                 if (cur, neighbor) in V[clr]: continue
#                 V[clr].add((cur, neighbor))
#                 stack.append((neighbor, deep + 1, 1 - clr))
#
#
#     def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
#         nr = [[] for i in range(n)]
#         nb = [[] for i in range(n)]
#         self.ans = [100000 for i in range(n)]
#         self.edge = [nr, nb]
#         for r in red_edges:
#             nr[r[0]].append(r[1])
#         for b in blue_edges:
#             nb[b[0]].append(b[1])
#         self.bfs(0)
#         self.bfs(1)
#
#         # print(self.edge)
#
#         for i in range(n):
#             if self.ans[i] == 100000:
#                 self.ans[i] = -1
#
#         return self.ans
#
#
# s = Solution()
#
# # n = 3
# # red_edges = [[0,1],[1,2]]
# # blue_edges = []
#
# # n = 3
# # red_edges = [[0,1]]
# # blue_edges = [[2,1]]
#
# # n = 3
# # red_edges = [[1,0]]
# # blue_edges = [[2,1]]
#
# # n = 3
# # red_edges = [[0,1]]
# # blue_edges = [[1,2]]
#
# n = 3
# red_edges = [[0,1],[0,2]]
# blue_edges = [[1,0]]
#
# print(s.shortestAlternatingPaths(n, red_edges, blue_edges))


class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        ans = 0
        N = len(arr1)
        big_big = (0, arr1[0], arr2[0])
        small_small = (0, arr1[0], arr2[0])
        big_small = (0, arr1[0], arr2[0])
        small_big = (0, arr1[0], arr2[0])

        for i in range(1, N):
            a, b = arr1[i], arr2[i]
            ans = max(ans, big_big[1] - a + big_big[2] - b + i - big_big[0])
            ans = max(ans, a - small_small[1] + b - small_small[2] + i - small_small[0])
            ans = max(ans, big_small[1] - a + b - big_small[2] + i - big_small[0])
            ans = max(ans, a - small_big[1] + small_big[2] - b + i - small_big[0])
            if a - big_big[1] + b - big_big[2] + big_big[0] - i > 0: big_big = (i, a, b)
            if small_small[1] - a + small_small[2] - b + small_small[0] - i > 0: small_small = (i, a, b)
            if a - big_small[1] + big_small[2] - b + big_small[0] - i > 0: big_small = (i, a, b)
            if small_big[1] - a + b - small_big[2] + small_big[0] - i > 0: small_big = (i, a, b)

        return ans
#
# s = Solution()
# # arr1 = [1,2,3,4]
# # arr2 = [-1,4,5,6]
# arr1 = [1,-2,-5,0,10]
# arr2 = [0,-2,-1,-7,-4]
#
# print(s.maxAbsValExpr(arr1, arr2))


class Solution:
    def dfs(self, arr):
        if arr in self.mem:
            return self.mem[arr]
        N = len(arr)
        if N == 1:
            self.mem[tuple(arr)] = 0
            return 0

        # print(N, arr)
        ans = 2094967296
        for i in range(1, N):
            left = self.dfs(arr[:i])
            right = self.dfs(arr[i:])
            ans = min(ans, left + right + max(arr[:i]) * max(arr[i:]))

        self.mem[tuple(arr)] = ans
        return ans

    def mctFromLeafValues(self, arr) -> int:
        self.mem = {}
        return self.dfs(tuple(arr))

s = Solution()
# arr = [6,2,4]
arr = [i for i in range(1, 41)]
print(s.mctFromLeafValues(arr))
















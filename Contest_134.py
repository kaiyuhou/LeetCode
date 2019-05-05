from Tree import *

# class Solution:
# #     def numMovesStones(self, a: int, b: int, c: int):
# #         A = [a, b, c]
# #         A.sort()
# #         diff = A[2] - A[0] - 2
# #         max_moves = diff
# #         left = 1 if A[1] - A[0] > 1 else 0
# #         right = 1 if A[2] - A[1] > 1 else 0
# #         min_moves = left + right
# #         if min_moves == 2:
# #             if A[1] - A[0] == 2 or A[2] - A[1] == 2:
# #                 min_moves = 1
# #         return [min_moves, max_moves]
# #
# # s = Solution()
# # # print(s.numMovesStones(1, 3, 6))
# #
# # # print(s.numMovesStones(4, 3, 2))
# # print(s.numMovesStones(3, 5, 1))

# class Solution:
#     def colorBorder(self, grid, r0: int, c0: int, color: int):
#         N = len(grid)
#         M = len(grid[0])
#
#         ans = set()
#         v = set()
#
#         move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#         def is_b(x, y):
#             if x == 0 or y == 0 or x == N - 1 or y == M - 1:
#                 return True
#             for m in move:
#                 if grid[x][y] != grid[x + m[0]][y + m[1]]:
#                     return True
#
#         def check(x, y):
#             if x >= 0 and x < N and y >= 0 and y < M and (x, y) not in v:
#                 return True
#             return False
#
#         def dfs(x, y):
#             v.add((x, y))
#             if is_b(x, y):
#                 ans.add((x,y))
#
#             for m in move:
#                 next_x = x + m[0]
#                 next_y = y + m[1]
#                 if check(next_x, next_y):
#                     if grid[x][y] == grid[next_x][next_y]:
#                         dfs(next_x, next_y)
#
#         dfs(r0, c0)
#         for i in range(N):
#             for j in range(M):
#                 if (i, j) in ans:
#                     grid[i][j] = color
#         return grid
#
# s = Solution()
# # grid = [[1,1],[1,2]]
# # r0 = 0
# # c0 = 0
# # color = 3
# # grid = [[1,2,2],[2,3,2]]
# # # r0 = 0
# # # c0 = 1
# # # color = 3
# grid = [[1,1,1],[1,1,1],[1,1,1]]
# r0 = 1
# c0 = 1
# color = 2
# print(s.colorBorder(grid, r0, c0, color))


# class Solution:
#     def maxUncrossedLines(self, A, B) -> int:
#         # A_num = [[] for _ in range(2001)]
#         B_num = [[] for _ in range(2001)]
#         for i, b in enumerate(B):
#             B_num[b].append(i)
#
#         ans = dict()
#
#         link = []
#         for a in A:
#             if B_num[a] != []:
#                 link.append(B_num[a])
#
#         # print(link)
#
#         # for i, a in enumerate(A):
#         #     A_num[a].append(i)
#
#         #
#         def max_ans(A_start, A_end, B_start, B_end):
#             # print("call", A_start, A_end, B_start, B_end)
#             # if A_end - A_start < 1 or B_end - B_start < 1:
#             #     return 0
#
#             if (A_start, A_end, B_start, B_end) in ans:
#                 return ans[A_start, A_end, B_start, B_end]
#
#             cur_ans = 0
#             for i in range(A_start, A_end):
#                 for cur in link[i]:
#                     if cur >= B_start and cur < B_end:
#                         left_size = min(i - A_start, cur - B_start)
#                         right_size = min(A_end - i - 1, B_end - cur - 1)
#                         if left_size + right_size < cur_ans:
#                             continue
#                         left = 0 if left_size == 0 else max_ans(A_start, i, B_start, cur)
#                         right = 0 if right_size == 0 else max_ans(i + 1, A_end, cur + 1, B_end)
#
#                         cur_ans = max(cur_ans, 1 + left + right)
#
#             ans[A_start, A_end, B_start, B_end] = cur_ans
#             return cur_ans
#         return max_ans(0, len(link), 0, len(B))
#
# s = Solution()
# # A = [1,4,2]
# # B = [1,2,4]
# # A = [2,5,1,2,5]
# # B = [10,5,2,1,5,2]
# # A = [1,3,7,1,7,5]
# # B = [1,9,2,5,1]
# A = [14,16,7,5,1,18,20,11,4,15,15,14,12,8,18,11,8,4,8,4,6,4,4,12,7,12,16,2,7,20,8,19,16,7,5,7,11,10,4,8,18,15,15,20,16,3,10,3,8,12,7,20,7,6,19,1,16,6,17,10,13,1,6,18,7,5,4,14,8,10,6,16,8,5,19,20,2,3,14,17,13,20,3,14,19,1,2,13,7,18,20,11,9,12,12,6,1,8,14,16]
# B = [15,8,18,17,4,10,20,20,13,19,2,11,3,7,7,9,14,11,7,19,8,20,18,16,6,10,10,2,15,4,13,2,11,12,1,16,18,18,1,5,2,6,19,7,11,6,11,15,19,12,8,14,10,7,15,9,14,19,19,7,14,3,14,11,10,16,13,12,5,10,10,8,8,19,3,18,18,4,11,8,1,8,13,5,2,5,10,6,4,1,19,13,13,11,5,16,1,17,9,4]
# print(s.maxUncrossedLines(A, B))



from contest.Tree import *
import collections

# class Solution:
#     def tribonacci(self, n: int) -> int:
#         ans = [0, 1, 1]
#         for i in range(3, n + 1):
#             ans.append(ans[i -1] + ans[i - 2] + ans[i - 3])
#         return ans[n]
#
# s = Solution()
# print(s.tribonacci(25))

# class Solution:
#     def alphabetBoardPath(self, target: str) -> str:
#         ans = []
#         board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
#         B = {}
#         for i, line in enumerate(board):
#             for j, c in enumerate(board[i]):
#                 B[c] = (i, j)
#
#         def path(src, dest):
#             ans = []
#             if src[1] > dest[1]:
#                 ans += ['L'] * (src[1] - dest[1])
#             else:
#                 ans += ['R'] * (dest[1] - src[1])
#
#             if src[0] > dest[0]:
#                 ans += ['U'] * (src[0] - dest[0])
#             else:
#                 ans += ['D'] * (dest[0] - src[0])
#             return ans + ['!']
#
#         cur = (0, 0)
#         for c in target:
#             if cur == (5, 0) and c != 'z':
#                 cur = (4, 0)
#                 ans.append('U')
#             ans += path(cur, B[c])
#             cur = B[c]
#         return ''.join(ans)
#
# s = Solution()
# target = 'zzz'
# print(s.alphabetBoardPath(target))

# class Solution:
#     def largest1BorderedSquare(self, grid) -> int:
#         N = len(grid)
#         M = len(grid[0])
#         sum_row = [[0] for _ in range(N)]    # 012  i to j = [i + 1] - j
#         for i in range(N):
#             for j in range(M):
#                 sum_row[i].append(sum_row[i][j] + grid[i][j])
#         sum_column = [[0 for _ in range(M)] for _ in range(N + 1)]
#         for j in range(M):
#             for i in range(N):
#                 sum_column[i + 1][j] = sum_column[i][j] + grid[i][j]
#
#         ans = 0
#         for i in range(N):
#             for j in range(M):
#                 MAX_LEN = min(N - i, M - j)
#                 for k in range(ans + 1, MAX_LEN + 1):
#                     if sum_row[i][j + k] - sum_row[i][j] == k \
#                             and sum_row[i + k - 1][j + k] - sum_row[i + k - 1][j] == k \
#                             and sum_column[i + k][j] - sum_column[i][j] == k \
#                             and sum_column[i + k][j + k - 1] - sum_column[i][j + k - 1] == k:
#                         ans = max(ans, k)
#         return ans * ans
#
# s = Solution()
# grid = [[1,1,1], [1,1,0]]
# print(s.largest1BorderedSquare(grid))


class Solution:

    def stoneGameII(self, piles) -> int:
        N = len(piles)
        import functools
        @functools.lru_cache(None)
        def dfs(M, index):
            ans = 0
            for X in range(0, min(2 * M, N - index)):
                adver = dfs(max(M, X + 1), index + X + 1)
                cur = sum(piles[index:]) - adver
                ans = max(cur, ans)
            return ans
        return dfs(1, 0)

s = Solution()
piles = [8,9,5,4,5,4,1,1,9,3,1,10,5,9,6,2,7,6,6,9]
print(s.stoneGameII(piles))










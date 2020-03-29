from Tree import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         ans = 0
#         while head:
#             ans = ans * 2 + head.val
#             head = head.next
#         return ans
#
#
# s = Solution()

# class Solution:
#     def sequentialDigits(self, low: int, high: int):
#         cand = []
#         for i in range(2, 10):
#             for start in range(1, 11 - i):
#                 s = ""
#                 for k in range(i):
#                     s += str(start + k)
#                 cand.append(int(s))
#         ans = []
#         for c in cand:
#             if c >= low and c <= high:
#                 ans.append(c)
#         return ans
#
#
# s = Solution()
# print(s.sequentialDigits(1000, 13000))

# class Solution:
#     def maxSideLength(self, mat, threshold: int) -> int:
#         M = len(mat)
#         N = len(mat[0])
#
#         dpx = [[0] * (N + 1) for _ in range(M)]
#         for i in range(M):
#             for j in range(N):
#                 dpx[i][j + 1] = dpx[i][j] + mat[i][j]
#
#         dp = [[0] * (N + 1) for _ in range(M + 1)]
#         for i in range(M):
#             for j in range(N):
#                 dp[i + 1][j + 1] = dp[i][j + 1] + dpx[i][j + 1]
#
#         ans = 0
#         K = min(M, N)
#         # print(dp)
#         # print(dp[3][3], dp[0][0], dp[3][0], dp[0][3])
#         threshold += 1
#         for k in range(0, K):
#             if ans < k:
#                 break
#             p = k + 1
#             for i in range(M - k):
#                 for j in range(N - k):
#                     if dp[i + p][j + p] + dp[i][j] - dp[i + p][j] - dp[i][j + p] < threshold:
#                         ans = p
#                         break
#                 if ans == p:
#                     break
#         return ans
#
# s = Solution()
# mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
# threshold = 4
# mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
# threshold = 1
# mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
# threshold = 6
# mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
#
# print(s.maxSideLength(mat, threshold))

from heapq import *
class Solution:
    def shortestPath(self, G, k: int) -> int:
        M = len(G)
        N = len(G[0])
        dp = [[[-1] * (M * N) for _ in range(N)] for _ in range(M)]


        q = []
        heapify(q)
        heappush(q, (0, G[0][0], 0, 0))
        Next = [[1,0], [-1, 0], [0, -1], [0, 1]]
        while len(q) > 0:
            step, obs, x, y = heappop(q)
            if dp[x][y][step] == -1:
                dp[x][y][step] = obs
            else:
                if obs >= dp[x][y][step]:
                    continue
                else:
                    dp[x][y][step] = obs
            if x == M - 1 and y == N - 1:
                return step
            if step >= M * N:
                break
            for n in Next:
                nx = x + n[0]
                ny = y + n[1]
                if nx < 0 or ny < 0 or nx >= M or ny >= N:
                    continue
                if obs + G[nx][ny] > k:
                    continue
                for i in range(step + 2):
                    if dp[nx][ny][i] != -1 and dp[nx][ny][i] <= obs + G[nx][ny]:
                        break
                else:
                    heappush(q, (step + 1, obs + G[nx][ny], nx, ny))
        return -1
s = Solution()
grid = [[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]]
k = 1
# grid = [[0,1,1],
#  [1,1,1],
#  [1,0,0]]
# k = 1
grid = [[1] * 40] * 40
k = 800
print(s.shortestPath(grid, k))

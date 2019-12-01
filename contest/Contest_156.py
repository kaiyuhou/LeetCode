from Tree import *

# class Solution:
#     def uniqueOccurrences(self, arr) -> bool:
#         import collections
#         C = collections.Counter(arr)
#         M = set()
#         for k, c in C.items():
#             # print(i)
#             if c in M:
#                 return False
#             M.add(c)
#         return True
#
# s = Solution()
# arr = []
# # arr = [1,2]
# print(s.uniqueOccurrences(arr))

# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         N = len(s)
#         ans = 0
#         A = [0 for _ in range(N)]
#         for i in range(N):
#             A[i] = abs(ord(s[i]) - ord(t[i]))
#
#         cnt = 0
#         q = 0
#         for p in range(N):
#             cnt += A[p]
#             if cnt <= maxCost:
#                 ans = max(p - q + 1, ans)
#             while cnt > maxCost:
#                 cnt -= A[q]
#                 q += 1
#         return ans
#
# ss = Solution()
# s = "abcd"
# t = "bcdf"
# cost = 3
# s = "abcd"
# t = "cdef"
# cost = 3
# s = "abcd"
# t = "ffff"
# cost = 0
# print(ss.equalSubstring(s, t, cost))

# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         A = []
#         for c in s:
#             if len(A) == 0:
#                 A.append((c, 1))
#             elif A[-1][0] == c:
#                 A[-1] = (c , A[-1][1] + 1)
#             else:
#                 A.append((c, 1))
#             if A[-1][1] == k:
#                 A.pop()
#
#         ans = ''
#         for c, i in A:
#             ans += c * i
#         return ans
#
# ss = Solution()
# s = "abcd"
# k = 2
# s = "deeedbbcccbdaa"
# k = 3
# s = "pbbcggttciiippooaais"
# k = 2
# s = 'aa'
# k = 2
# print((ss.removeDuplicates(s, k)))

class Solution:
    def minimumMoves(self, grid) -> int:
        N = len(grid)
        V = set()
        A = [((0, 0), (0, 1), 0)]

        while len(A) > 0:
            p0, p1, step = A[0]
            A.pop(0)
            if (p0, p1) in V:
                continue
            V.add((p0, p1))
            V.add((p1, p0))

            if (p0 == (N-1, N-2) and p1 == (N-1, N-1)) or (p1 == (N-1, N-2) and p0 == (N-1, N-1)):
                return step

            x0, y0 = p0
            x1, y1 = p1
            if x0 == x1:
                if y1 + 1 < N and grid[x1][y1 + 1] == 0:
                    A.append((p1, (x1, y1 + 1), step + 1))
                if x1 + 1 < N and grid[x1 + 1][y0] == 0 and grid[x1 + 1][y1] == 0:
                    A.append(((x0 + 1, y0), (x1 + 1, y1), step + 1))
                    A.append((p0, (x0 + 1, y0), step + 1))
            else:
                if x1 + 1 < N and grid[x1 + 1][y0] == 0:
                    A.append((p1, (x1 + 1, y1), step + 1))
                if y1 + 1 < N and grid[x0][y1 + 1] == 0 and grid[x1][y1 + 1] == 0:
                    A.append(((x0, y1 + 1), (x1, y1 + 1), step + 1))
                    A.append((p0, (x0, y1 + 1), step + 1))
        return -1

s = Solution()
grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,1,1,1],
               [1,1,1,0,0,0]]
print(s.minimumMoves(grid))














from Tree import *


# class Solution:
#     def minimumAbsDifference(self, A):
#         A.sort()
#         diff = A[1] - A[0]
#         N = len(A)
#         for i in range(1, N):
#             diff = min(diff, A[i] - A[i - 1])
#         ans = []
#         mem = set()
#         for a in A:
#             if a - diff in mem:
#                 ans.append([a - diff, a])
#             mem.add(a)
#         return ans
#
# s = Solution()
# arr = [4,2,1,3]
# arr = [1,3,6,10,15]
# arr = [3,8,-10,23,19,-4,-14,27]
# print(s.minimumAbsDifference(arr))

# from math import *
# class Solution:
#     def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
#         A = [a, b, c]
#         A.sort()
#         LCM0 = a * b // gcd(a, b)
#         LCM1 = a * c // gcd(a, c)
#         LCM2 = b * c // gcd(b, c)
#         LCM4 = LCM0 * LCM1 // gcd(LCM0, LCM1)
#
#         # print(LCM0, LCM1, LCM2, LCM4)
#
#         left = 1
#         right = 2 * 10 ** 9
#         while left < right:
#             mid = left + (right - left) // 2
#             if mid // a + mid // b + mid // c - mid // LCM0 - mid // LCM1 - mid // LCM2 + mid // LCM4 < n:
#                 left = mid + 1
#             else:
#                 right = mid
#         return right
#
# s = Solution()
#
# n = 1000000000
# a = 2
# b = 217983653
# c = 336916467
# # n = 5
# # a = 2
# # b = 3
# # c = 3
#
# print(s.nthUglyNumber(n,a,b,c))













# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs) -> str:
#         N = len(s)
#         fa = [i for i in range(N)]
#
#         def find(a):
#             # print(a)
#             if fa[a] != a:
#                 fa[a] = find(fa[a])
#             return fa[a]
#
#         def union(a, b):
#             a = find(a)
#             b = find(b)
#             fa[b] = a
#
#         for a, b in pairs:
#             union(a, b)
#
#         ans = [-1] * N
#         mem = {}
#         mem_i = {}
#         for i, c in enumerate(s):
#             # print(i, c)
#             f = find(i)
#             if f not in mem.keys():
#                 mem[f] = [c]
#                 mem_i[f] = [i]
#             else:
#                 mem[f].append(c)
#                 mem_i[f].append(i)
#
#         for k in mem.keys():
#             mem[k].sort()
#             mem_i[k].sort()
#             for i, index in enumerate(mem_i[k]):
#                 ans[index] = mem[k][i]
#         # print(ans)
#         return ''.join(ans)
#
#
# ss = Solution()
# s = "dcab"
# pairs = [[0,3],[1,2]]
# s = "dcab"
# pairs = [[0,3],[1,2],[0,2]]
# s = "cba"
# pairs = [[0,1],[1,2]]
# print(ss.smallestStringWithSwaps(s, pairs))

class Solution:
    def sortItems(self, n: int, m: int, group, beforeItems):
        for i, g in enumerate(group):
            if g == -1:
                group[i] = i + m

        E = [{} for _ in range(n)]
        income = [0] * n

















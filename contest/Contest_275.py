from typing import *
from Tree import *

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv



# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         n = len(nums)
#         t = sum(nums)
#         n2 = [nums[i % n] for i in range(2 * n)]
#         if t < 2:
#             return 0
#         cur = sum(n2[:t])
#         ans = t - cur
#         for i in range(t, 2*n):
#             cur = cur + n2[i] - n2[i - t]
#             ans = min(ans, t - cur)
#         return ans

# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         n = len(matrix)
#         ans = set([i for i in range(1, n + 1)])
#         for i in range(n):
#             cur = set()
#             cur2 = set()
#             for j in range(n):
#                 cur.add(matrix[i][j])
#                 cur2.add(matrix[j][i])
#             if cur != ans:
#                 return False
#             if cur2 != ans:
#                 return False
#         return True

# class Solution:
#     def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
#         def c2n(c):
#             return 2 ** (ord(c) - 96)
#
#         m = {chr(i): c2n(chr(i)) for i in range(97, 123)}
#
#         def w2n(w):
#             ans = 0
#             for c in w:
#                 ans += m[c]
#             return ans
#
#         s_set = set()
#         for s in startWords:
#             s_set.add(w2n(s))
#
#         rnt = 0
#         for t in targetWords:
#             cur = w2n(t)
#             for c in t:
#                 if cur - m[c] in s_set:
#                     rnt += 1
#                     break
#         return rnt
#
# s = Solution()
# startWords = ["ant","act","tack"]
# targetWords = ["tack","act","acti"]
# startWords = ["ab","az"]
# targetWords = ["abc","abcd"]
# print(s.wordCount(startWords, targetWords))





class Solution:
    def earliestFullBloom(self, p: List[int], g: List[int]) -> int:
        pair = []
        n = len(p)
        for i in range(n):
            pair.append((g[i], p[i]))
        pair.sort()
        ans = 0
        for grow, plant in pair:
            if grow > ans:
                ans = grow + plant
            else:
                ans = ans + plant
        return ans







































from Tree import *

from math import *
# class Solution:
#     def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
#         ans = []
#         for i in range(R):
#             for j in range(C):
#                 ans.append((abs(i - r0) + abs(j - c0), [i, j]))
#         ans.sort()
#         rnt = []
#         for _, cell in ans:
#             rnt.append(cell)
#         return rnt
#
# s = Solution()
# print(s.allCellsDistOrder(2, 3, 1, 2))

# class Solution:
#     def twoCitySchedCost(self, costs):
#         diff = []
#         for i, [A, B] in enumerate(costs):
#             diff.append((A - B, i))
#         diff.sort()
#         # print(diff)
#
#         ans = 0
#         N = len(costs)
#         for i in range(N):
#             if i < N // 2:
#                 ans += costs[diff[i][1]][0]
#             else:
#                 ans += costs[diff[i][1]][1]
#         return ans
#
# s = Solution()
# A = [[10,20],[30,200],[400,50],[30,20]]
# # A = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# print(s.twoCitySchedCost(A))

# class Solution:
#     def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
#         pr = [0]
#         N = len(A)
#         for a in A:
#             pr.append(pr[-1] + a)
#
#         ans = 0
#         for i in range(0, N - L + 1):
#             for j in range(0, N - M + 1):
#                 if i == j:
#                     continue
#                 if i < j and i + L > j:
#                     continue
#                 if i > j and j + M > i:
#                     continue
#
#                 ans = max(ans, pr[i + L] - pr[i] + pr[j + M] - pr[j])
#         return ans
#
# s = Solution()
# # A = [0,6,5,2,2,5,1,9,4]
# # L = 1
# # M = 2
# # A = [3,8,1,3,2,1,8,9,0]
# # L = 3
# # M = 2
# A = [2,1,5,6,0,9,5,0,3,8]
# L = 4
# M = 3
# print(s.maxSumTwoNoOverlap(A, L , M))


class TreeNode:
    def __init__(self):
        self.val = 0
        self.node = [None for _ in range(26)]

class StreamChecker:

    def __init__(self, words):
        self.root = TreeNode()
        self.maxn = 0
        self.curs = []
        for w in words:
            cur = self.root
            self.maxn = max(self.maxn, len(w))
            for i in range(len(w) - 1, -1, -1):
                if cur.node[ord(w[i]) - 97] == None:
                    cur.node[ord(w[i]) - 97] = TreeNode()
                cur = cur.node[ord(w[i]) - 97]
                if i == 0:
                    cur.val = 1

    def query(self, letter: str) -> bool:
        self.curs = [letter] + self.curs
        if len(self.curs) > self.maxn:
            self.curs.pop()

        cur = self.root
        for w in self.curs:
            if cur.node[ord(w) - 97] == None:
                return False
            cur = cur.node[ord(w) - 97]
            if cur.val == 1:
                return True
        return False

obj = StreamChecker(["cd","f","kl"])
for a in ['a', 'b', 'c', 'd', 'e', 'f', 'k','l']:
    print(obj.query(a))





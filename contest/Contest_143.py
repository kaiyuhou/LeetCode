from contest.Tree import *

# from math import *
# class Solution:
#     def distributeCandies(self, candies: int, n: int):
#         base = (1 + n) * n // 2
#
#         a = n * n
#         b = 2 * base - a
#         c = -2 * candies
#
#         round = ( - b + sqrt(b * b - 4 * a * c) ) / (2 * a)
#         round = int(round)
#
#         ans = [(i + 1) * round + n * (round - 1) * round // 2 for i in range(n)]
#
#         # print(ans)
#
#         candies -= sum(ans)
#         for i in range(n):
#             ans[i] += round * n + i + 1
#             candies -= round * n + i + 1
#             if candies <= 0:
#                 ans[i] += candies
#                 break
#         return ans
#
# s = Solution()
# # c = 10
# # n = 3
# # c = 7
# # n = 4
# # c = 17
# # n = 4
# c = 60
# n = 4
# print(s.distributeCandies(c, n))

# class Solution:
#     def pathInZigZagTree(self, label: int):
#         if label == 1:
#             return [1]
#
#         else:
#             def get_level(A):
#                 level = 1
#                 cur = 1
#                 while cur < A:
#                     cur += 2**level
#                     level += 1
#                 return level
#
#             level = get_level(label)
#
#             if level % 2 == 0:
#                 order = (2 ** level) - label + 1
#                 father = (2 ** (level - 2) - 1) + (order // 2)
#             else:
#                 order = label - (2 ** (level - 1) - 1) + 1
#                 father = (2 ** (level - 1) - 1) - (order // 2) + 1
#
#             # print(order, father)
#
#             ans = self.pathInZigZagTree(father)
#             return ans + [label]
#
# s = Solution()
# label = 1000000
# print(s.pathInZigZagTree(label))


# class Solution:
#     def parseBoolExpr(self, exp: str) -> bool:
#         # print(exp)
#
#         if exp[0] == 't':
#             return True
#         if exp[0] == 'f':
#             return False
#         if exp[0] == '!':
#             return not self.parseBoolExpr(exp[2:-1])
#         if exp[0] == '&' or exp[0] == '|':
#             ans = []
#             cnt = 0
#             buf = ''
#
#             for i in range(2, len(exp) -1):
#                 if exp[i] == '(':
#                     cnt += 1
#                 if exp[i] == ')':
#                     cnt -= 1
#                 if exp[i] == ',' and cnt == 0:
#                     ans.append(self.parseBoolExpr(buf))
#                     buf = ''
#                     continue
#                 buf += exp[i]
#             ans.append(self.parseBoolExpr(buf))
#             if exp[0] == '&':
#                 if False in ans:
#                     return False
#                 return True
#             else:
#                 if True in ans:
#                     return True
#                 return False
#
# s = Solution()
# # e = "|(&(t,f,t),!(t))"
# e = "&(t,f)"
# print(s.parseBoolExpr(e))


class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        dp = {}
        dp[-1] = 0
        N = len(books)
        for i in range(N):
            dp[i] = dp[i - 1] + books[i][1]
            cnt = books[i][0]
            height = books[i][1]

            for j in range(i - 1, -1, -1):
                cnt += books[j][0]
                if cnt > shelf_width:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], height + dp[j - 1])

        return dp[N - 1]

s = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf = 4
print(s.minHeightShelves(books,shelf))



































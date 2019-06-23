# class Solution:
#     def minIncrementForUnique(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         n = len(A)
#         if n == 1 or n == 0:
#             return 0
#
#         A.sort()
#         last = A[0]
#         wait = []
#         ans = 0
#         for a in A[1:]:
#             if a == last:
#                 wait.append(a)
#             else:
#                 for t in range(last + 1, a):
#                     if len(wait) > 0:
#                         ans += t - wait[0]
#                         wait = wait[1:]
#                     else:
#                         break
#
#             last = a
#
#         # print(wait)
#
#         for t in range(last + 1, 50000):
#             if len(wait) > 0:
#                 # print(t)
#                 # print(wait[0])
#                 ans += t - wait[0]
#                 wait = wait[1:]
#
#         return ans
#
# s = Solution()
# # A = [1,2,2]
# A = [3,2,1,2,1,7]
# print(s.minIncrementForUnique(A))

# class Solution:
#     def validateStackSequences(self, pushed, popped):
#         """
#         :type pushed: List[int]
#         :type popped: List[int]
#         :rtype: bool
#         """
#         s = [-1]
#         i = 0
#         n = len(pushed)
#         for a in popped:
#             if s[-1] == a:
#                 s.pop(-1)
#                 continue
#
#             while i < n and pushed[i] != a:
#                 s.append((pushed[i]))
#                 i += 1
#
#             if i == n:
#                 return False
#             else:
#                 i += 1
#
#         return True

# class Solution:
#
#
#
#     def removeStones(self, stones):
#         """
#         :type stones: List[List[int]]
#         :rtype: int
#         """
#
#         class node:
#             def __init__(self, father):
#                 self.father = father
#
#         x_mem = {}
#         y_mem = {}
#
#         dp = []
#
#         dp_index = 0
#         n = len(stones)
#
#
#         for p in stones:
#             dp_x_i = -1
#             dp_y_i = -1
#             # print(p)
#
#             if p[0] in x_mem.keys():
#                 # print(p[0])
#                 # print(x_mem)
#                 # print(x_mem[p[0]])
#
#                 dp_x_i = dp[x_mem[p[0]]].father
#                 while dp_x_i != dp[dp_x_i].father:
#                     dp_x_i = dp[dp_x_i].father
#
#
#             if p[1] in y_mem.keys():
#                 dp_y_i = dp[y_mem[p[1]]].father
#
#                 while dp_y_i != dp[dp_y_i].father:
#                     dp_y_i = dp[dp_y_i].father
#
#
#             # print(dp_x_i, dp_y_i)
#             # print(x_mem, y_mem)
#
#             if dp_x_i == -1 and dp_y_i == -1:
#
#
#                 new_node = node(dp_index)
#                 dp.append(new_node)
#
#
#                 x_mem[p[0]] = dp_index
#                 y_mem[p[1]] = dp_index
#                 dp_index += 1
#
#             elif dp_x_i == -1:
#                 x_mem[p[0]] = dp_y_i
#
#             elif dp_y_i == -1:
#                 y_mem[p[1]] = dp_x_i
#
#             elif dp_x_i == dp_y_i:
#                 continue
#             else:
#                 dp[dp_y_i].father = dp[dp_x_i].father
#
#         ans = 0
#         father_set = set()
#         for i in range(len(dp)):
#             father = dp[i].father
#             while father != dp[father].father:
#                 father = dp[father].father
#
#             if father not in father_set:
#                 father_set.add(father)
#                 ans += 1
#
#         return n - ans
#
# s = Solution()
# # A = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# # A = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# # A = [[0,0], [1,1]]
# # A = [[0,1],[1,1]]
# # A = [[3,2],[0,0],[3,3],[2,1],[2,3],[2,2],[0,2]]
# A = [[6,9],[1,3],[8,0],[8,9],[5,1],[7,2],[4,0],[1,2],[4,4],[1,5],[5,3],[9,7],[3,2],[0,0],[8,2],[9,3],[0,5],[3,5],[9,9],[3,8],[4,3],[0,2]]
# print(s.removeStones(A))

class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        ans = 0
        tokens.sort()
        n = len(tokens)
        i = 0

        while i < n:
            if P >= tokens[i]:
                ans += 1
                P -= tokens[i]
                i += 1
            elif n - 1 > i and ans > 0:
                P += tokens[n-1] - tokens[i]
                i += 1
                n -= 1
            else:
                break

        return ans

s = Solution()
# tokens = [100]
# P = 50
# tokens = [100,200]
# P = 150
tokens = [100,200,300,400]
P = 200
print(s.bagOfTokensScore(tokens, P))









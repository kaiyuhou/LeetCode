# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# #
# #
# # class Solution:
# #     def isCompleteTree(self, root):
# #         """
# #         :type root: TreeNode
# #         :rtype: bool
# #         """
# #         if root == None:
# #             return True
# #
# #         current_level = [root]
# #         level = 1
# #         is_continue = True
# #
# #         while len(current_level) > 0:
# #
# #             next_level = []
# #             for node in current_level:
# #                 if node.left == None and node.right != None:
# #                     # print("F1")
# #                     return False
# #
# #                 if node.left != None:
# #                     if is_continue == False:
# #                         # print("F3")
# #                         return False
# #                     next_level.append(node.left)
# #
# #                 if node.right != None:
# #                     if is_continue == False:
# #                         # print("F4")
# #                         return False
# #                     next_level.append(node.right)
# #
# #
# #                 if node.left == None or node.right == None:
# #                     is_continue = False
# #
# #             if next_level != [] and len(current_level) != (2 ** (level - 1)):
# #                 # print("F7")
# #                 return False
# #
# #             if next_level == []:
# #                 return True
# #
# #             current_level = list(next_level)
# #             level += 1
# #
# #         return True
#
# class Solution:
#     def cal(self, A, cur):
#
#         for i in range(len(A) - 1):
#             if cur == A[i]:
#                 return i
#
#         return -1
#
#
#     def prisonAfterNDays(self, cells, N):
#         """
#         :type cells: List[int]
#         :type N: int
#         :rtype: List[int]
#         """
#         A = [cells]
#         cur = cells
#         while self.cal(A, cur) == -1:
#             next = [0 for i in range(8)]
#             for i in range(1, 7):
#                 if cur[i - 1] == cur[ i + 1]:
#                     next[i] = 1
#                 else:
#                     next[i] = 0
#             A.append(next)
#             cur = A[-1]
#             if len(A) == N + 1:
#                 return A[N]
#
#         start_day = self.cal(A, cur)
#         end_day = len(A) - 1
#         p = end_day - start_day
#
#         return A[ (N-start_day) % p + start_day ]
#
# s = Solution()
# # n = [0,1,0,1,1,0,0,1]
# # N = 7
# # cells = [1,0,0,1,0,0,1,0]
# # N = 1000000000
# cells = [0,0,0,0,0,0,0,0]
# N = 11111
# print(s.prisonAfterNDays(cells,N))
#

class Solution:
    def get_exo(self, A, a, b):
        for i in range(len(A)):
            if ord(A[i][a]) > ord(A[i][b]):
                return False
        return True

    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n = len(A[0])
        exo = {}
        for a in range(n - 1):
            for b in range(a + 1, n):
                exo[a , b] = self.get_exo(A, a, b)

        dp = {}
        dp[0] = [0]
        for i in range(1, n):
            ans = [i]
            for j in range(i):
                if exo[dp[j][-1], i] == True:
                    if len(dp[j]) + 1 > len(ans):
                        ans = list(dp[j])
                        ans.append(i)
            dp[i] = list(ans)

        rnt = 0
        for i in range(n):
            # print(dp[i])
            rnt = max(rnt, len(dp[i]))
        return n - rnt

s = Solution()
A = ["babca","bbazb"]
# A = ["edcba"]
# A = ["ghi","def","abc"]
print(s.minDeletionSize(A))


# class Solution:
#
#     def find(self, a):
#         father = self.father[a]
#         while father != self.father[father]:
#             father = self.father[father]
#         return father
#
#     def union(self, a, b):
#         father_a = self.find(a)
#         father_b = self.find(b)
#
#         if father_a != father_b:
#             self.father[father_b] = father_a
#
#
#     def regionsBySlashes(self, grid):
#         """
#         :type grid: List[str]
#         :rtype: int
#         """
#         self.uset = {}
#         self.father = {}
#         N = len(grid)
#         for i in range(N):
#             for j in range(N):
#                 for k in range(1, 5):
#                     self.father[(i, j , k)] = (i, j , k)
#
#         for i in range(N):
#             for j in range(N):
#                 if i != 0:
#                     self.union( (i, j, 1), (i - 1, j , 3))
#                 if i != N - 1:
#                     self.union( (i, j, 3), (i + 1, j, 1))
#                 if j != 0:
#                     self.union( (i, j, 2), (i, j-1 , 4))
#                 if j != N - 1:
#                     self.union( (i, j, 4), (i, j + 1,2))
#
#                 if grid[i][j] == ' ':
#                     self.union((i, j, 1), (i, j, 2))
#                     self.union((i, j, 1), (i, j, 3))
#                     self.union((i, j, 1), (i, j, 4))
#
#                 if grid[i][j] == '/':
#                     self.union((i, j, 1), (i, j, 2))
#                     self.union((i, j, 3), (i, j, 4))
#
#                 if grid[i][j] == '\\':
#                     self.union((i, j, 1), (i, j, 4))
#                     self.union((i, j, 2), (i, j, 3))
#
#         father_set = set()
#         for i in range(N):
#             for j in range(N):
#                 for k in range(1, 5):
#                     # print(self.find( (i, j , k)))
#                     father_set.add(self.find( (i, j , k)))
#
#         return len(father_set)
#
#
# s = Solution()
# A = [
#   " /",
#   "/ "
# ]
# print(s.regionsBySlashes(A))














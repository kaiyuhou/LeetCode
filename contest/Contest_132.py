# class Solution:
#     def divisorGame(self, N: int) -> bool:
#         record = [False, False]
#         for i in range(2, 1001):
#             record.append(False)
#             for j in range(1, i):
#                 if i % j == 0 and record[i - j] == False:
#                     record[i] = True
#                     break
#
#         return record[N]
#
# s = Solution()
# N = 4
# print(s.divisorGame(N))

from Tree import *
# from math import *
# #
# # class Solution:
# #     def dfs(self, root, minn, maxn):
# #         if root.left != None:
# #             self.ans = max(abs(root.left.val - minn), self.ans)
# #             self.ans = max(abs(maxn - root.left.val), self.ans)
# #             self.dfs(root.left, min(minn, root.left.val), max(maxn, root.left.val))
# #
# #         if root.right != None:
# #             self.ans = max(abs(root.right.val - minn), self.ans)
# #             self.ans = max(abs(maxn - root.right.val), self.ans)
# #             self.dfs(root.right, min(minn, root.right.val), max(maxn, root.right.val))
# #
# #     def maxAncestorDiff(self, root: TreeNode) -> int:
# #         self.ans = 0
# #         self.dfs(root, root.val, root.val)
# #         return self.ans
# #
# # s = Solution()
# # root = list_to_tree([8,3,10,1,6, None,14, None,None,4,7,13])
# # print(s.maxAncestorDiff(root))


class Solution:
    def longestArithSeqLength(self, A) -> int:
        dp = {}
        for i in range(10001):
            dp[(0, i)] = 1

        for i in range(1, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                if (j, diff) in dp.keys():
                    if (i, diff) in dp.keys():
                        dp[(i, diff)] = max(dp[(i, diff)], dp[(j, diff)] + 1)
                    else:
                        dp[(i, diff)] = dp[(j, diff)] + 1

                else:
                    if (i, diff) not in dp.keys():
                        dp[(i, diff)] = 2
        return dp[max(dp, key=dp.get)]


s = Solution()
A = [1, 1]
# A = [9,4,7,2,10]
# A = [20,1,15,3,10,5,8]
print(s.longestArithSeqLength(A))



# class Solution:
#     def dfs(self, root, D):
#         if self.S == '':
#             return
#
#         cnt = 0
#         while self.S[cnt] == '-':
#             cnt += 1
#
#         if cnt != D:
#             return
#
#         self.S = self.S[D:]
#
#         cur = ''
#         while self.S != "" and self.S[0] != '-':
#             cur += self.S[0]
#             self.S = self.S[1:]
#
#         root.left = TreeNode(int(cur))
#         self.dfs(root.left, D + 1)
#
#         if self.S == '':
#             return
#
#         cnt = 0
#         while self.S[cnt] == '-':
#             cnt += 1
#
#         if cnt != D:
#             return
#         self.S = self.S[D:]
#
#         cur = ''
#         while self.S != "" and self.S[0] != '-':
#             cur += self.S[0]
#             self.S = self.S[1:]
#
#         root.right = TreeNode(int(cur))
#         self.dfs(root.right, D + 1)
#
#     def recoverFromPreorder(self, S: str) -> TreeNode:
#         if S.find('-') == -1:
#             return TreeNode(int(S))
#
#         self.S = S
#         cur = ''
#         while self.S[0] != '-':
#             cur += self.S[0]
#             self.S = self.S[1:]
#
#         root = TreeNode(int(cur))
#
#         self.dfs(root, 1)
#         return root
#
# s = Solution()
# A = "12-32--3--4-5--6--7"
# print(s.recoverFromPreorder(A))



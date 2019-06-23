# class Solution:
#     def largestSumAfterKNegations(self, A, K: int) -> int:
#         N = len(A)
#         ans = 0
#         n0, np, nn = 0, [], []
#         for a in A:
#             if a == 0:
#                 n0 += 1
#             if a > 0:
#                 np.append(a)
#             if a < 0:
#                 nn.append(a)
#
#         np.sort()
#         nn.sort()
#         if n0 > 0:
#             if len(nn) <= K:
#                 return sum(np) - sum(nn)
#             else:
#                 ans = sum(np)
#                 for a in nn:
#                     if K > 0:
#                         ans += -a
#                     else:
#                         ans += a
#                     K -= 1
#                 return ans
#
#         if len(nn) <= K:
#             ans = sum(np) - sum(nn)
#             if (K - len(nn)) % 2 == 0:
#                 return ans
#             if nn == []:
#                 return ans -  2 * min(np)
#             else:
#                 return ans - 2 * min(min(np), 0- max(nn))
#
#         ans = sum(np)
#         for a in nn:
#             if K > 0:
#                 ans += -a
#             else:
#                 ans += a
#             K -= 1
#         return ans
#
#
# s = Solution()
# A = [5,6,9,-3,3]
# K = 2
# print(s.largestSumAfterKNegations(A, K))

# class Solution:
#     def clumsy(self, N: int) -> int:
#         d, m = divmod(N, 4)
#         ans = 0
#         flag = 1
#         for _ in range(d):
#             ans += flag * (N * (N - 1) // (N - 2) + flag * (N - 3))
#             if flag == 1:
#                 flag = -1
#             N -= 4
#         if m == 3:
#             ans += flag * (N * (N - 1) // (N - 2))
#         if m == 2:
#             ans += flag * (N * (N - 1))
#         if m == 1:
#             ans += flag * (N)
#
#         return ans
#
# s = Solution()
# A = 1
# print(s.clumsy(A))

# class Solution:
#     def check(self, A, B, n):
#         ans = 0
#         for i in range(len(A)):
#             if A[i] == n:
#                 continue
#             elif B[i] == n:
#                 ans += 1
#             else:
#                 return -1
#         return ans
#
#     def minDominoRotations(self, A, B) -> int:
#         ans = 20000
#         flag = -1
#         for i in range(1, 7):
#             t = self.check(A, B, i)
#             if t != -1:
#                 flag = 0
#                 ans = min(ans, t)
#
#         for i in range(1, 7):
#             t = self.check(B, A, i)
#             if t != -1:
#                 flag = 0
#                 ans = min(ans, t)
#
#         if flag == -1:
#             return -1
#         return ans
#
# s = Solution()
# A = [3,5,1,2,3]
# B = [3,6,3,3,4]
# print(s.minDominoRotations(A, B))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        root = None
        if len(preorder) == 0:
            return root

        val = preorder[0]
        root = TreeNode(val)
        left_list, right_list = [], []
        for a in preorder:
            if a < val:
                left_list.append(a)
            if a > val:
                right_list.append(a)

        root.left = self.bstFromPreorder(left_list)
        root.right = self.bstFromPreorder(right_list)
        return root






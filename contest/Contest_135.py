from Tree import *

# class Solution:
#     def isBoomerang(self, p) -> bool:
#         s = set()
#         for a in p:
#             s.add((a[0], a[1]))
#         if len(s) < 3:
#             return False
#
#         return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) !=  (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])
#
#
#
# s = Solution()
# # p = [[1,1],[2,3],[3,2]]
# # p = [[1,1],[2,2],[3,3]]
# p = [[1,1],[1,1],[3,4]]
# print(s.isBoomerang(p))

# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         def dfs(root, sum):
#             if root == None:
#                 return 0
#             pre_sum = sum
#             sum = dfs(root.right, pre_sum)
#             if root.val == 4:
#                 print(sum)
#             sum += root.val
#             root.val = pre_sum + sum
#             sum += dfs(root.left, pre_sum + sum)
#             return sum
#
#         dfs(root, 0)
#         return root
#
# s = Solution()
# A = list_to_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
# print(tree_to_list(s.bstToGst(A)))

import functools
import operator
class Solution:
    def minScoreTriangulation(self, B) -> int:
        mem = {}

        @functools.lru_cache(None)
        def dfs(A):
            N = len(A)
            if N == 3:
                return functools.reduce(operator.mul, A)
            ans = A[-1] * A[0] * A[1] + dfs(A[1:])
            for i in range(2, N - 1):
                ans = min(ans, dfs(A[0:1] + A[i:]) + dfs(A[:i+1]))
            return ans

        return dfs(tuple(B))

s = Solution()
A = [i for i in range(1, 52)]
# A = [1,3,1,4,1,5]
# A = [4,3,4,3,5]
# A = [5,5,1,4,2]
print(s.minScoreTriangulation(A))

# for i in range(N):
#     mem[i, (i + 2) % N] = A[i] * A[(i + 1) % N] * A[(i + 2) % N]
#
# for k in range(3, N + 1):
#     for i in range(N):
#         mem[i, (i + k) % N] = mem[(i - 1) % N, (i + 1) % N] + mem[(i + 1) % N, (i + k) % N]
#         for j in range()
#
#
#         mem[i, (i + k) % N] = min(mem[i % N, (i + 2) % N]  + mem[(i + 2) % N, (i + 2 + k - 1) % N],
#                             mem[(i - 1) % N, (i + 1) % N] + mem[(i + 1) % N, (i + k) % N],
#                             mem[(i - 2) % N, (i) % N] + mem[(i) % N, (i + k - 1) % N])
# ans = mem[0, N - 1]
# for i in range(N):
#     ans = min(ans, mem[i, (i + N - 1) % N])






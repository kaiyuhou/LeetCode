from typing import *
from Tree import *

# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         for i, word in enumerate(sentence.split(' ')):
#             if word.startswith(searchWord):
#                 return i + 1
#         return -1
#
# sentence = "i love eating burger"
# searchWord = "burg"
# sentence = "this problem is an easy problem"
# searchWord = "pro"
# sentence = "i am tired"
# searchWord = "you"
#
# s = Solution()
# print(s.isPrefixOfWord(sentence, searchWord))

# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         cnt = 0
#         ans = 0
#         for i, c in enumerate(s):
#             if c in ['a', 'e', 'i', 'o','u']:
#                 cnt += 1
#             ans = max(ans, cnt)
#             if i >= k - 1:
#                 if s[i - k + 1] in ['a', 'e', 'i', 'o','u']:
#                     cnt -= 1
#         return ans
#
# s = "abciiidef"
# k = 3
# s = "aeiou"
# k = 2
# s = "leetcode"
# k = 3
# s = "rhythms"
# k = 4
# s = "tryhard"
# k = 4
#
# ss = Solution()
# print(ss.maxVowels(s, k))


# class Solution:
#     def pseudoPalindromicPaths (self, root: TreeNode) -> int:
#         def dfs(root, cnt):
#             if root is None:
#                 return 0
#
#             my_cnt = list(cnt)
#             my_cnt[root.val] += 1
#             # print(root.val)
#             #
#             # print(my_cnt)
#
#             if root.left is None and root.right is None:
#
#                 odd = 0
#                 for a in my_cnt:
#                     if a % 2 == 1:
#                         odd += 1
#                 if odd >= 2:
#                     return 0
#                 else:
#                     return 1
#
#             return dfs(root.left, my_cnt) + dfs(root.right, my_cnt)
#
#         my_cnt = [0] * 10
#         return dfs(root, my_cnt)
#
#
# s = Solution()
# root = TreeNode(2)
# root.left = TreeNode(3)
# root.right = TreeNode(1)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(1)
# root.right.right = TreeNode(1)
#
# print(s.pseudoPalindromicPaths(root))

import functools
class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:

        if A[0] > 0:
            A, B = B, A
        flag = True
        for a in A:
            if a >= 0:
                flag = False
        for b in B:
            if b <= 0:
                flag = False
        if flag:
            return max(A) * min(B)

        N = len(A)
        M = len(B)

        dp = {}
        dp[(-1, -1)] = 0
        for i in range(max(N, M)):
            dp[(-1, i)] = 0
            dp[(i, -1)] = 0

        for i in range(N):
            for j in range(M):
                if A[i] * B[j] > 0:
                    dp[(i, j)] = max(A[i] * B[j] + dp[(i - 1, j - 1)], dp[(i - 1, j)], dp[(i, j - 1)])
                else:
                    dp[(i, j)] = max(dp[(i - 1, j - 1)], dp[(i - 1, j)], dp[(i, j - 1)])

        return dp[(N - 1, M - 1)]

nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
nums1 = [3,-2]
nums2 = [2,-6,7]
# nums1 = [9] * 500
# nums2 = [9] * 500
# nums2 = [-1,-1]
# nums1 = [1,1]

s = Solution()

print(s.maxDotProduct(nums1, nums2))














# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         A = str(num)
#         B = ''
#         F = True
#         for a in A:
#             if a == '9' or F is False:
#                 B += a
#             else:
#                 B += '9'
#                 F = False
#         return int(B)
#
# s = Solution()
# print(s.maximum69Number(9999))

# class Solution:
#     def printVertically(self, s: str):
#         words = s.split(' ')
#         N = len(words)
#         M = max(list(map(len, words)))
#         print(N, M)
#         ans = [[' '] * N for _ in range(M)]
#         for i, word in enumerate(words):
#             for j, c in enumerate(word):
#                 ans[j][i] = c
#
#         for i, line in enumerate(ans):
#             for j in range(N - 1, -1, -1):
#                 if line[j] is not ' ':
#                     break
#             ans[i] = ''.join(line[:j + 1])
#         return ans
#
#
#
#
# ss = Solution()
# s = "TO BE OR NOT TO BE"
# s = "HOW ARE YOU"
# s = "CONTEST IS COMING"
# print(ss.printVertically(s))

# from Tree import *
#
# class Solution:
#     def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
#         if root is None:
#             return None
#         root.left = self.removeLeafNodes(root.left, target)
#         root.right = self.removeLeafNodes(root.right, target)
#         if root.left is None and root.right is None and root.val == target:
#             return None
#         return root
#
# root = list_to_tree([1,2,3,2,None,2,4])
# target = 2
# s = Solution()
# print(tree_to_list(s.removeLeafNodes(root, target))

class Solution:
    def minTaps(self, n: int, ranges) -> int:
        mem = []
        dp = [[] for _ in range(n + 1)]
        for i, r in enumerate(ranges):
            for j in range(max(0, i - r), min(n, i + r) + 1):
                dp[j].append((max(0, i - r), i))


        start = n
        ans = []
        while start > 0:
            if len(dp[start]) == 0:
                return -1
            next, select = min(dp[start])
            if next == start:
                return -1
            # print(next, start)
            ans.append(select)
            start = next
        return len(ans)

s = Solution()
n = 5
ranges = [3,4,1,1,0,0]
n = 3
ranges = [0,0,0,0]
n = 7
ranges = [1,2,1,0,2,1,0,1]
n = 8
ranges = [4,0,0,0,0,0,0,0,4]
n = 8
ranges = [4,0,0,0,4,0,0,0,4]
print(s.minTaps(n, ranges))







from Tree import *

# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         ans = []
#         c = 0
#         for s in S:
#             if s == '(':
#                 if c == 0:
#                     c += 1
#                 else:
#                     c += 1
#                     ans.append('(')
#             elif s == ')':
#                 c -= 1
#                 if c != 0:
#                     ans.append(')')
#
#         return "".join(ans)
#
#
# s = Solution()
# A = "()()"
# print(s.removeOuterParentheses(A))

# class Solution:
#     def dfs(self, root, s):
#         if root == None:
#             return
#
#         s = s + str(root.val)
#
#         if root.left == None and root.right == None:
#             self.ans += int(s, 2)
#             self.ans %= 1000000007
#         else:
#             if root.left != None:
#                 self.dfs(root.left, s)
#             if root.right != None:
#                 self.dfs(root.right, s)
#
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         self.ans = 0
#         self.dfs(root, "")
#         return self.ans

# class Solution:
#     def camelMatch(self, queries, pattern: str):
#         ans = []
#         def match(q, p):
#             if len(q) < len(p):
#                 return False
#
#             j = 0
#             for a in p:
#                 if a.islower():
#                     while q[j] != a:
#                         if not q[j].islower():
#                             return False
#                         j += 1
#                         if j >= len(q):
#                             return False
#
#                 else:
#                     while q[j] != a:
#                         if not q[j].islower():
#                             return False
#                         j += 1
#                         if j >= len(q):
#                             return False
#
#                 j += 1
#
#             for i in range(j, len(q)):
#                 if not q[i].islower():
#                     return False
#
#             return True
#
#         for q in queries:
#             ans.append(match(q, pattern))
#
#         return ans
#
# s = Solution()
# q = ["aFooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# p = "aFoBa"
# print(s.camelMatch(q, p))

class Solution:
    def videoStitching(self, clips, T: int) -> int:
        end = 0
        ans = 0
        while end < T:
            max_end = end
            for c in clips:
                if c[0] <= end:
                    max_end = max(max_end, c[1])
            if max_end == end:
                return -1
            end = max_end
            ans += 1
        return ans

s = Solution()
clips = [[0,4],[2,8]]
T = 5
print(s.videoStitching(clips, T))









